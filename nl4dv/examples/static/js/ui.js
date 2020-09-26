var extractedAttributesDataTable = null;
var extractedTasksDataTable = null;
var myCodeMirror;

function emptyDatasetContainers(){
    $(globalConfig.extractedMetaDataContainer + " table tbody").empty();
}

function emptyQueryResponseContainers(){
    // Output JSON
    $(globalConfig.jsonContainer).empty();

    // VIS
    $(globalConfig.visContainer).empty();

    // VIS Thumbnails
    $(globalConfig.visThumbnailContainer).empty();

    // Debug
    $(globalConfig.executionTimeViz).empty();

    // Tasks
    if(extractedTasksDataTable != null){
        extractedTasksDataTable.clear().draw(false);
    }

    // Attributes
    if(extractedAttributesDataTable != null){
        extractedAttributesDataTable.clear().draw(false);
    }
}

function processDataResponse(response, dataset){
    emptyDatasetContainers();

    // container for Extracted Meta  Data
    $("#datasetUrl").text(dataset);
    $("#columnCount").text(response['columnCount']);
    $("#rowCount").text(response['rowCount']);

    Object.keys(response['summary']).forEach(function(attr){
        var row = document.createElement('tr');

        var cell_attribute = document.createElement('td');
        $(cell_attribute).text(attr);
        $(row).append(cell_attribute);

        var cell_attribute_type = document.createElement('td');
        $(cell_attribute_type).text(response['summary'][attr]['dataType']);
        $(row).append(cell_attribute_type);

        var cell_attribute_aliases = document.createElement('td');
        $(cell_attribute_aliases).text(response['summary'][attr]['aliases']);
        $(row).append(cell_attribute_aliases);

        var cell_unique_items_count = document.createElement('td');
        $(cell_unique_items_count).text(response['summary'][attr]['domain'].length);
        $(row).append(cell_unique_items_count);

        var cell_domain = document.createElement('td');
        $(cell_domain).addClass("text-no-wrap");
        $(cell_domain).text(response['summary'][attr]['domain']);
        $(row).append(cell_domain);

        $(globalConfig.extractedMetaDataContainer + " table tbody").append(row);
    });
}

// Dataset is optional here
function initializeNL4DV(){
    var dataset = $(globalConfig.datasetSelect).val();
    $.post("/init", {"dependency_parser": "corenlp"})
        .done(function (response) {
            configureDatabase(dataset);
        });
}

function configureDatabase(dataset){
    $.post("/setData", {"dataset": dataset})
        .done(function (r1) {
            var attributeTypeChanges = {};
            var ignore_words = [];
            if(dataset == "cars-w-year.csv"){
                attributeTypeChanges = {
                    "Year": "T"
                };
                ignore_words = ['car'];
            }else if(dataset == "cars.csv"){
                ignore_words = ['car'];
            }else if(dataset == "movies-w-year.csv"){
                attributeTypeChanges = {
                    "Release Year": "T"
                };
                ignore_words = ['movie','movies'];
            }else if(dataset == "housing.csv"){
                attributeTypeChanges = {
                    "Year": "T"
                }
                ignore_words = [];
            }else if(dataset == "olympic_medals.csv"){
                attributeTypeChanges = {
                    "Gold Medal": 'Q',
                    "Silver Medal": 'Q',
                    "Bronze Medal": 'Q',
                    "Total Medal": 'Q',
                    "Year": "T"
                }
                ignore_words = [];
            }

            if(attributeTypeChanges != {}){
                $.post("/setAttributeDataType", {"attr_type_obj": JSON.stringify(attributeTypeChanges)})
                    .done(function (r2) {
                        processDataResponse(r2, dataset);
                    });
            }

            if(ignore_words.length > 0){
                $.post("/setIgnoreList", {"ignore_words": JSON.stringify(ignore_words)})
                    .done(function (r3) {
                    });
            }

            if(attributeTypeChanges == {} && ignore_words.length == 0){
                processDataResponse(r1, dataset);
            }

        });
}

$(globalConfig.datasetSelect).change(function() {
    emptyQueryResponseContainers();
    emptyDatasetContainers();
    var dataset = $(this).val();
    configureDatabase(dataset);
});

function runNL4DV(query){
    $.post("/analyze_query", {"query": query})
        .done(function (response_string) {
            var response = JSON.parse(response_string);
            emptyQueryResponseContainers();

            // Output JSON
            var div = document.createElement('div');
            var tree = jsonTree.create(response, div);
            tree.expand(function(node) {
                return true;
            });
            $(globalConfig.jsonContainer).append(div);

            // container for Input query
            $(globalConfig.inputQueryContainer).text(response['query']);

            // container for Extracted Attributes
            var attributeMap = response['attributeMap'];
            Object.keys(attributeMap).forEach(function(attr){
                var word = attributeMap[attr]['queryPhrase']
                var type = attributeMap[attr]['metric'];
                var relevance = attributeMap[attr]['matchScore'];
                var meta = attributeMap[attr]['meta'];
                extractedAttributesDataTable.row.add([attr, word, type, relevance, JSON.stringify(meta)]).draw(false);
            });

            // container for Extracted Tasks
            var tasksObjectList = response['taskMap'];
            Object.keys(tasksObjectList).forEach(function(task){
                tasksObjectList[task].forEach(function(taskObj){

                    var operator = taskObj['operator'];
                    var values = taskObj['values'];
                    var attribute = taskObj['attributes'];
                    var queryPhrase = taskObj['queryPhrase'];
                    if(queryPhrase){
                        queryPhrase = queryPhrase.toString()
                    }
                    if(values){
                        values = values.toString()
                    }
                    extractedTasksDataTable.row.add([task, operator, values, attribute, queryPhrase, "1"]).draw(false);

                });
            });

            for(var i=0; i<response['visList'].length; i++){

                var obj = response['visList'][i];
                if(JSON.stringify(obj['encoding']) != "{}"){

                    // container for Vis
                    if(i == 0){
                        // Main Viz
                        obj["vlSpec"]['width'] = globalConfig.vegaMainChartSize.width;
                        obj["vlSpec"]['height'] = globalConfig.vegaMainChartSize.height;
                        vegaEmbed(document.getElementById("outputVisContainer"), obj["vlSpec"], vegaOptMode);

                        // container for Data
                        $("#inputContainer").empty();
                        myCodeMirror = CodeMirror(document.getElementById("inputContainer"), {
                          value: JSON.stringify(obj["vlSpec"], null, 2),
                          lineNumbers: true,
                          matchBrackets: true,
                          autoCloseBrackets: true,
                          mode: "application/ld+json",
                          lineWrapping: true
                        });
                    }

                    var objclone = JSON.parse(JSON.stringify(obj));

                    var thumbnail = document.createElement("div");
                    thumbnail.id = "visThumbnail-" + i.toString()
                    if(i != 0){
                        thumbnail.className = "thumbnail";
                    }else{
                        thumbnail.className = "thumbnail thumbnail-active";
                    }
                    thumbnail.addEventListener("click", function() {
                        $(this).parent().find(".thumbnail").removeClass("thumbnail-active");
                        $(this).addClass("thumbnail-active");
                        var index = parseInt(this.id.split("-")[1]);
                        var obj = response['visList'][index];

                        // Update main Vis
                        $("#outputVisContainer").empty();
                        obj["vlSpec"]['width'] = globalConfig.vegaMainChartSize.width;
                        obj["vlSpec"]['height'] = globalConfig.vegaMainChartSize.height;
                        vegaEmbed(document.getElementById("outputVisContainer"), obj["vlSpec"], vegaOptMode);

                        // Update CodeMirror
                        $("#inputContainer").empty();
                        myCodeMirror = CodeMirror(document.getElementById("inputContainer"), {
                          value: JSON.stringify(obj["vlSpec"], null, 2),
                          lineNumbers: true,
                          matchBrackets: true,
                          autoCloseBrackets: true,
                          mode: "application/ld+json",
                          lineWrapping: true
                        });
                    });

                    objclone["vlSpec"]['width'] = globalConfig.vegaThumbnailSize.width;
                    objclone["vlSpec"]['height'] = globalConfig.vegaThumbnailSize.height;
                    vegaEmbed(thumbnail, objclone["vlSpec"], vegaOptMode);

                    $(globalConfig.visThumbnailContainer).append(thumbnail);
                }

            }
    });
}

$(globalConfig.vegaSpecBtn).on("click",function(evt){
    var spec = myCodeMirror.getValue();
    $("#outputVisContainer").empty();
    $(globalConfig.visThumbnailContainer).empty();
    spec['width'] = globalConfig.vegaMainChartSize.width;
    spec['height'] = globalConfig.vegaMainChartSize.height;
    vegaEmbed(document.getElementById("outputVisContainer"), JSON.parse(spec), vegaOptMode);
});

$(globalConfig.queryBtn).on("click",function(evt){
    var query = $(globalConfig.queryInput).val();
    runNL4DV(query);
});

$(document).ready(function() {
    var parentWidth = $("#outputVisContainer").parent().width();
    var parentHeight = $("#outputVisContainer").parent().height();
//    globalConfig.vegaMainChartSize.width = parentWidth * 0.70;
//    globalConfig.vegaMainChartSize.height = parentHeight - 400;

    globalConfig.vegaMainChartSize.width = 400;
    globalConfig.vegaMainChartSize.height = 400;

    extractedAttributesDataTable = $(globalConfig.extractedAttributesContainer).DataTable(globalConfig.attributeDataTablesOptions);
    extractedTasksDataTable = $(globalConfig.extractedTasksContainer).DataTable(globalConfig.taskDataTablesOptions);
    initializeNL4DV();

    myCodeMirror = CodeMirror(document.getElementById("inputContainer"), {
      value: "",
      lineNumbers: true,
      matchBrackets: true,
      autoCloseBrackets: true,
      mode: "application/ld+json",
      lineWrapping: true
    });
});

function autocomplete(inp) {
      /*the autocomplete function takes two arguments,
      the text field element and an array of possible autocompleted values:*/
      var currentFocus;
      var timer;
      /*execute a function when someone writes in the text field:*/
      inp.addEventListener("input", function(e) {
          /*close any already open lists of autocompleted values*/
          closeAllLists();
          clearTimeout(timer);
          let that = this;
          timer = setTimeout(() => {
          var query = $(globalConfig.queryInput).val();
          $.ajax({
              type: "POST",
              url: "/getAutoCompleteQuery",
              data: {"query": query}, 
              beforeSend: function() {
                $body.removeClass("loading");
              },
              success: function(response) {
                let recommendation = response
                activateCommendation(that, recommendation);
              }
          })
          /*
          $.ajax("/getAutoCompleteQuery", {"query": query}, function (response) {
            let recommendation = response
            activateCommendation(that, recommendation);
        })  */       
          }, 1000)
          
      });
      /*execute a function presses a key on the keyboard:*/
      inp.addEventListener("keydown", function(e) {
          var x = document.getElementById(this.id + "autocomplete-list");
          if (x) x = x.getElementsByTagName("div");
          if (e.keyCode == 40) {
            /*If the arrow DOWN key is pressed,
            increase the currentFocus variable:*/
            currentFocus++;
            /*and and make the current item more visible:*/
            addActive(x);
          } else if (e.keyCode == 38) { //up
            /*If the arrow UP key is pressed,
            decrease the currentFocus variable:*/
            currentFocus--;
            /*and and make the current item more visible:*/
            addActive(x);
          } else if (e.keyCode == 13) {
            /*If the ENTER key is pressed, prevent the form from being submitted,*/
            e.preventDefault();
            if (currentFocus > -1) {
              /*and simulate a click on the "active" item:*/
              if (x) x[currentFocus].click();
            }
          }
      });
    
    function activateCommendation(that, recommendation) {
            var a, b, i, val = that.value;
            if (!val) { return false;}
            currentFocus = -1;
            /*create a DIV element that will contain the items (values):*/
            a = document.createElement("DIV");
            a.setAttribute("id", that.id + "autocomplete-list");
            a.setAttribute("class", "autocomplete-items");
            /*append the DIV element as a child of the autocomplete container:*/
            that.parentNode.appendChild(a);
            /*for each item in the array...*/
            for (i = 0; i < recommendation.length; i++) {
        
                /*create a DIV element for each matching element:*/
                b = document.createElement("DIV");
                /*make the matching letters bold:*/
                b.innerText = recommendation[i];
                /*insert a input field that will hold the current array item's value:*/
                // b.innerHTML += "<input type='hidden' value='" + recommendation[i] + "'>";
                /*execute a function when someone clicks on the item value (DIV element):*/
                b.addEventListener("click", function(e) {
                    /*insert the value for the autocomplete text field:*/
                    //console.log(this.childNodes[0].data)
                    inp.value = this.innerText;
                    //inp.value = this.getElementsByTagName("input")[0].value;
                    //inp.value = this.childNodes[0].data
                    /*close the list of autocompleted values,
                    (or any other open lists of autocompleted values:*/
                    closeAllLists();
                });
                a.appendChild(b);
            }
          }
        
          function addActive(x) {
            /*a function to classify an item as "active":*/
            if (!x) return false;
            /*start by removing the "active" class on all items:*/
            removeActive(x);
            if (currentFocus >= x.length) currentFocus = 0;
            if (currentFocus < 0) currentFocus = (x.length - 1);
            /*add class "autocomplete-active":*/
            x[currentFocus].classList.add("autocomplete-active");
          }
          function removeActive(x) {
            /*a function to remove the "active" class from all autocomplete items:*/
            for (var i = 0; i < x.length; i++) {
              x[i].classList.remove("autocomplete-active");
            }
          }
          function closeAllLists(elmnt) {
            /*close all autocomplete lists in the document,
            except the one passed as an argument:*/
            var x = document.getElementsByClassName("autocomplete-items");
            for (var i = 0; i < x.length; i++) {
              if (elmnt != x[i] && elmnt != inp) {
                x[i].parentNode.removeChild(x[i]);
              }
            }
          }
          /*execute a function when someone clicks in the document:*/
          document.addEventListener("click", function (e) {
              closeAllLists(e.target);
          });
        }


 
var countries = ["Afghanistan","Albania","Algeria"];

autocomplete(document.getElementById("queryInput"));


