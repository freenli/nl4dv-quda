function execute(){
    var table = document.getElementById('debugTable');
    var data;
    var current_dataset = "";
    var dict = Object();
    var queryList = [];
	$.ajax({
	    type: "GET",
	    url: "assets/queries/debugger_batch_queries.txt?version="+Math.random(),
	    dataType: "text",
	    success: function(data)
	    {
            var rows = data.split("\n");
            for (var i = 1; i < rows.length; i++) {
                var attributeList = [];
                var taskList = [];

                var cells = rows[i].split("\t");

                if (cells.length > 1) {
                    var dataset = cells[0];
                    var alias = cells[1];
                    var query = cells[2];
                    queryList.push(query);

                    // Set data ONLY if you detect a different dataset
                    if(current_dataset != dataset){
                        current_dataset = dataset;
                        configureDatabase(dataset); // Now synchronous
                    }

                    var attributeList = [];
                    var taskList = [];
                    var visObj;

                    var new_row = table.insertRow(-1);

                    // Dataset
                    var cell = new_row.insertCell(-1);
                    cell.innerHTML = dataset;

                    // Query
                    var cell = new_row.insertCell(-1);
                    cell.innerHTML = query;

                    $.ajax("/analyze_query", {type: 'POST', data: {"query": query}, async:false})
                        .done(function (response_string) {
                            var response = JSON.parse(response_string);

                            // container for Extracted Attributes
                            var attributeMap = response['attributeMap'];
                            Object.keys(attributeMap).forEach(function(attr){
                                attributeList.push(attributeMap[attr]);
                            });

                            // container for Extracted Tasks
                            var tasksObjectList = response['taskMap'];
                            Object.keys(tasksObjectList).forEach(function(task){
                                tasksObjectList[task].forEach(function(taskObj){
                                    taskList.push(taskObj);
                                });
                            });

                            // Visualization
                            visObj = response['visList'];
                    });

                    dict[queryList.length] = visObj;

                    // visualization
                    var new_cell = new_row.insertCell(0);
                    var vizContainer = document.createElement('div');
                    $(vizContainer).addClass("vizContainer");
                    visObj.forEach(function(visSpec) {
                        if(JSON.stringify(visSpec['encoding']) != "{}"){
                            var div = document.createElement('div');
                            $(div).width(270);
                            $(div).height(270);
                            $(div).addClass("text-center overflow display-inline");
                            if(visObj != null){
                                visObj["width"] = 200;
                                visObj["height"] = 200;
                                vegaEmbed(div, visSpec["vlSpec"], vegaOptMode);
                            }
                            $(vizContainer).append(div);

                            var div = document.createElement('div');
                            total = visSpec['score'];
                            score_list = visSpec['scoreObj'];
                            content = '<br/>';
                            content += "<table class='table table-bordered table-condensed'>";
                            content += '<tr><th>Score</th><th>By&nbsp;Attribute</th><th>By&nbsp;Task</th><th>By&nbsp;Vis</th></tr>';
                            content += '<tr>' +
                                    '<td>' + Math.round(total) + '</td>' +
                                    '<td>' + Math.round(score_list['by_attributes'],2) + '</td>' +
                                    '<td>' + Math.round(score_list['by_task'],2) + '</td>' +
                                    '<td>' + Math.round(score_list['by_vis'],2) + '</td>' +
                                '</tr>';
                            content += "</table>";
                            content += "<hr>";
                            $(div).append(content);
                            $(vizContainer).append(div);

                        }
                    });
                    new_cell.appendChild(vizContainer);
                    new_row.appendChild(new_cell);

                    // attributes
                    new_cell = new_row.insertCell(0);
                    var content = "<div class='table-responsive'><table class='table table-bordered table-condensed'>"
                    content += '<tr><th>Name</th><th>Query Phrase</th><th>Metric</th><th>Reference Type</th><th>Is Ambiguous</th><th>Meta</th></tr>';
                    for(var t = 0; t < attributeList.length; t++){
                        content += '<tr>' +
                                        '<td>' + attributeList[t]['name'] + '</td>' +
                                        '<td>' + attributeList[t]['queryPhrase'] + '</td>' +
                                        '<td>' + attributeList[t]['metric'] + '</td>' +
                                        '<td>' + attributeList[t]['inferenceType'] + '</td>' +
                                        '<td>' + attributeList[t]['isAmbiguous'] + '</td>' +
                                        '<td>' + JSON.stringify(attributeList[t]['meta']) + '</td>' +
                                    '</tr>';
                    }
                    content += "</table></div>";
                    $(new_cell).append(content);
                    new_row.appendChild(new_cell);

                    // tasks
                    new_cell = new_row.insertCell(0);
                    var content = "<div class='table-responsive'><table class='table table-bordered table-condensed'>"
                    content += '<tr><th>Task</th><th>Operator</th><th>Value</th><th>Attribute</th><th>Inference Type</th><th>Is Attribute Ambiguous</th><th>Is Value Ambiguous</th><th>Query Phrase</th><th>Meta</th></tr>';
                    for(var t = 0; t < taskList.length; t++){
                        content += '<tr>' +
                                        '<td>' + taskList[t]['task'] + '</td>' +
                                        '<td>' + (taskList[t]['operator'] === null ? '' : taskList[t]['operator']) + '</td>' +
                                        '<td>' + (taskList[t]['values'] === null ? '' : taskList[t]['values']) + '</td>' +
                                        '<td>' + taskList[t]['attributes'] + '</td>' +
                                        '<td>' + taskList[t]['inferenceType'] + '</td>' +
                                        '<td>' + taskList[t]['isAttrAmbiguous'] + '</td>' +
                                        '<td>' + taskList[t]['isValueAmbiguous'] + '</td>' +
                                        '<td>' + taskList[t]['queryPhrase'] + '</td>' +
                                        '<td>' + JSON.stringify(taskList[t]['meta']) + '</td>' +
                                    '</tr>';
                    }
                    content += "</table></div>";
                    $(new_cell).append(content);
                    new_row.appendChild(new_cell);
                }
            }
        }
    });
}


function initNL4DV(dependency_parser) {
    $.post("/init", {"dependency_parser": dependency_parser})
        .done(function (response) {
           // All OK
        });
}

function configureDatabase(dataset){
    $.ajax("/setData", {type: 'POST', data: {"dataset": dataset}, async:false})
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
                $.post("/setAttributeDataType", {"attr_type_obj": JSON.stringify(attributeTypeChanges), async:false})
                    .done(function (r2) {
                    });
            }

            if(ignore_words.length > 0){
                $.post("/setIgnoreList", {"ignore_words": JSON.stringify(ignore_words), async:false})
                    .done(function (r3) {
                    });
            }
        });
}

$(document).ready(function() {
    initNL4DV("corenlp");
});
