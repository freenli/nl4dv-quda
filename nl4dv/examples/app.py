import sys
sys.path.append("..")
from nl4dv import NL4DV
import os
import json
from flask import Flask, jsonify, request, Blueprint, render_template, abort, send_from_directory
from jinja2 import TemplateNotFound
import csv
import numpy
import tensorflow_hub as hub
from operator import itemgetter
import nl4dv
from vega import VegaLite
import random
import requests

# Import our Example Applications

# Import our Debugging Applications
from debuggers.debugger_single import debugger_single_routes
from debuggers.debugger_batch import debugger_batch_routes
from debuggers.vis_matrix import vis_matrix_routes
from debuggers.test_queries import test_queries_routes

# Initialize the app
app = Flask(__name__)

# Initialize nl4dv variable
nl4dv_instance = None

# Load the Model
embed = hub.load("../../4")

# Initialize table info
table_info = None
table_vec_info = None

@app.route('/init', methods=['POST'])
def init():
    global nl4dv_instance
    if nl4dv_instance is not None:
        return jsonify({"message":"NL4DV already initialized"})

    dependency_parser = request.form['dependency_parser']
    if dependency_parser == "corenlp":
        dependency_parser_config = {'name': 'corenlp','model': os.path.join("../../jars","stanford-english-corenlp-2018-10-05-models.jar"),'parser': os.path.join("../../jars","stanford-parser.jar")}
        nl4dv_instance = NL4DV(dependency_parser_config=dependency_parser_config, verbose=True)

    elif dependency_parser == "spacy":
        dependency_parser_config = {'name': 'spacy','model': 'en_core_web_sm','parser': None}
        nl4dv_instance = NL4DV(dependency_parser_config=dependency_parser_config, verbose=True)

    elif dependency_parser == "corenlp-server":
        dependency_parser_config = {'name': 'corenlp-server','url': 'http://localhost:9000'}
        nl4dv_instance = NL4DV(dependency_parser_config=dependency_parser_config, verbose=True)

    else:
        raise ValueError('Error with Dependency Parser')

    

    return jsonify({"message":"NL4DV Initialized"})


@app.route('/setDependencyParser', methods=['POST'])
def setDependencyParser():
    global nl4dv_instance
    if nl4dv_instance is None:
        return jsonify({"message":"NL4DV NOT initialized"})

    dependency_parser = request.form['dependency_parser']
    if dependency_parser == "corenlp":
        dependency_parser_config = {'name': 'corenlp','model': os.path.join("assets","jars","stanford-english-corenlp-2018-10-05-models.jar"),'parser': os.path.join("assets","jars","stanford-parser.jar")}
        nl4dv_instance.set_dependency_parser(config=dependency_parser_config)

    elif dependency_parser == "spacy":
        dependency_parser_config = {'name': 'spacy','model': 'en_core_web_sm','parser': None}
        nl4dv_instance.set_dependency_parser(config=dependency_parser_config)

    elif dependency_parser == "corenlp-server":
        dependency_parser_config = {'name': 'corenlp-server','url': 'http://localhost:9000'}
        nl4dv_instance.set_dependency_parser(config=dependency_parser_config)
    else:
        raise ValueError('Data not provided')


@app.route('/setData', methods=['POST'])
def setData():
    global nl4dv_instance
    if nl4dv_instance is None:
        return jsonify({"message":"NL4DV NOT initialized"})

    dataset = request.form['dataset']
    if dataset is not None:
        datafile_obj = dataset.rsplit(".")
        nl4dv_instance.data_genie_instance.set_data(data_url=os.path.join("assets", "data", datafile_obj[0] + ".csv"))
        nl4dv_instance.data_genie_instance.set_alias_map(alias_url=os.path.join("assets", "aliases", datafile_obj[0] + ".json"))
        return get_dataset_meta()
    else:
        raise ValueError('Data not provided')

@app.route('/setIgnoreList', methods=['POST'])
def setIgnoreList():
    global nl4dv_instance
    if nl4dv_instance is None:
        return jsonify({"message":"NL4DV NOT initialized"})

    ignore_words = request.form['ignore_words']
    nl4dv_instance.data_genie_instance.set_ignore_words(ignore_words=json.loads(ignore_words))
    return jsonify({'message': 'Ignore List Set successfully'})


@app.route('/setThresholds', methods=['POST'])
def setThresholds():
    global nl4dv_instance
    if nl4dv_instance is None:
        return jsonify({"message":"NL4DV NOT initialized"})

    thresholds_str = request.form['thresholds']
    try:
        thresholds = json.loads(thresholds_str)
        response = nl4dv_instance.set_thresholds(thresholds)
        return jsonify({'message': 'Thresholds Set successfully'})
    except:
        raise ValueError('Thresholds not a JSON string')


@app.route('/setImportanceScores', methods=['POST'])
def setImportanceScores():
    global nl4dv_instance
    if nl4dv_instance is None:
        return jsonify({"message":"NL4DV NOT initialized"})

    scores_str = request.form['importance_scores']
    try:
        scores = json.loads(scores_str)
        response = nl4dv_instance.set_importance_scores(scores)
        return jsonify({'message': 'Scores Set successfully'})

    except Exception:
        raise ValueError('Importance Scores not a JSON string')


@app.route('/analyze_query', methods=['POST'])
def analyze_query():
    global nl4dv_instance
    if nl4dv_instance is None:
        return jsonify({"message":"NL4DV NOT initialized"})

    query = request.form['query']
    return json.dumps(nl4dv_instance.analyze_query(query, debug=True))


@app.route('/setAttributeDataType', methods=['POST'])
def setAttributeDataType():
    global nl4dv_instance
    if nl4dv_instance is None:
        return jsonify({"message":"NL4DV NOT initialized"})

    attr_type_obj = request.form['attr_type_obj']
    nl4dv_instance.data_genie_instance.set_attribute_datatype(json.loads(attr_type_obj))
    return get_dataset_meta()


# @app.route('/',methods=['GET'])
# def application_homepage():
#     try:
#         return render_template('index.html')
#     except TemplateNotFound:
#         abort(404)

@app.route('/', methods=['GET'])
def application_homepage():
    try:
        return render_template('vleditor.html')
    except TemplateNotFound:
        abort(404)

@app.route('/assets/<path:filename>')
def serveAssets(filename):
    return send_from_directory(os.path.join("assets"), filename, conditional=True)




def cosin_distance(vector1, vector2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return None
    else:
        return dot_product / ((normA * normB) ** 0.5)

#Compute the Interface Table's Attr and Value's Vec
def compute_table_vec(table_info):
    vec_array = []
    for key in table_info:
        dic = {
            'attr': key,
            'values': table_info[key]['domain'],
            'data_type': table_info[key]['dataType'].lower(),
            'attr_vec': '',
            'values_vec': ''
        }
        attr_embedding = embed([key])
        dic['attr_vec'] = (attr_embedding[0].numpy()).tolist()
        values_info = []
        if dic['data_type'] != 'q':
            for value in dic['values']:
                value_embedding = embed([str(value)])
                values_info.append((value_embedding[0].numpy()).tolist())
        dic['values_vec'] = values_info
        vec_array.append(dic)
    return vec_array


def get_dataset_meta():
    global nl4dv_instance
    global table_info
    global table_vec_info
    output = {
        "summary": nl4dv_instance.data_genie_instance.data_attribute_map,
        "rowCount": nl4dv_instance.data_genie_instance.rows,
        "columnCount": len(nl4dv_instance.data_genie_instance.data_attribute_map.keys())
    }
    table_info = output["summary"]
    table_vec_info = compute_table_vec(table_info)
    return jsonify(output)

#Get Top 5 Expert Sentences
def top_five(sen_vec):
    with open('corpusData/corpus_vec.json','r',encoding='utf8')as fp:
        data = json.load(fp)
    result_top_five = []
    for i, item in enumerate(data):
        similarity = cosin_distance(sen_vec, item['sen_vec'])
        if len(result_top_five) < 5:
            dic = {
                'id': i,
                'sentence': item['sentence'],
                'similarity': similarity
            }
            result_top_five.append(dic)
        if len(result_top_five) == 5:
            result_top_five = sorted(result_top_five, key=itemgetter('similarity'))
            if similarity > result_top_five[0]['similarity']:
                result_top_five[0] = {
                    'id': i,
                    'sentence': item['sentence'],
                    'similarity': similarity
                }
    result_top_five = sorted(result_top_five, key=itemgetter('similarity'), reverse=True)
    return result_top_five

#Replace the Attr and Value of Expert Sentences
def value_replace(table_vec_info, sentence_info):
    with open('corpusData/corpus_vec.json','r',encoding='utf8')as fp:
        data = json.load(fp)
    replace_attr = []
    replace_value = []
    sentenceInfo = data[sentence_info['id']]
    sentence = sentenceInfo['sentence']
    sen_attr = sentenceInfo['dataAttribute']
    sen_attr_vec = sentenceInfo['attr_vec']
    sen_values = sentenceInfo['dataValue']
    sen_values_vec = sentenceInfo['value_vec']
    #Replace Attr
    for i, attr in enumerate(sen_attr):
        dic = {
            'attr': '',
            'similarity': -10
        }
        for item in table_vec_info:
            if item['data_type'] == attr[1]:
                similarity = cosin_distance(sen_attr_vec[i], item['attr_vec'])
                if similarity > dic['similarity']:
                    dic['attr'] = item['attr']
                    dic['similarity'] = similarity
        #No matching same type attr
        if dic['attr'] == '':
            for item in table_vec_info:
                similarity = cosin_distance(sen_attr_vec[i], item['attr_vec'])
                if similarity > dic['similarity']:
                    dic['attr'] = item['attr']
                    dic['similarity'] = similarity
        replace_attr.append(dic['attr'])
    #Replace Value
    for i, value in enumerate(sen_values):
        dic = {
            'value': '',
            'similarity': -10
        }
        #Value is q type
        if value[1] == 'q':
            for item in table_vec_info:
                if item['data_type'] == 'q':
                    dic['value'] = random.choice(item['values'])
                    break
            #No q type in table
            if dic['value'] == '':
                dic['value'] = random.randint(1, 1000)
        #Value is o，n，t type
        else:
            for item in table_vec_info:
                if item['data_type'] == value[1]:
                    for j, instance in enumerate(item['values']):
                        similarity = cosin_distance(sen_values_vec[i], item['values_vec'][j])
                        if similarity > dic['similarity']:
                            dic['value'] = instance
                            dic['similarity'] = similarity
            if dic['value'] == '':
                if value[1] == 't':
                    dic['value'] = "2000"
                else:
                    for item in table_vec_info:
                        if item['data_type'] != 'q':
                            for j, instance in enumerate(item['values']):
                                similarity = cosin_distance(sen_values_vec[i], item['values_vec'][j])
                                if similarity > dic['similarity']:
                                    dic['value'] = instance
                                    dic['similarity'] = similarity
        replace_value.append(dic['value'])
    for i, item in enumerate(sen_attr):
        sentence = sentence.replace(str(item[0]), str(replace_attr[i]))
    for i, item in enumerate(sen_values):
        sentence = sentence.replace(str(item[0]), str(replace_value[i]))
    return sentence

#task classification api
@app.route('/get_query_tasks', methods=['POST', 'GET'])
def get_query_tasks():
    query = request.form['query']
    api = "https://freenli.projects.zjvis.org/get_sentences_tasks"
    params = {'sentences': query}
    result = requests.get(api, params = params)
    tasks = json.loads(result.json()['tasks'])
    return jsonify(tasks)


#task classification api for single query
@app.route('/get_sentence_tasks', methods=['POST'])
def get_sentence_tasks():
    query = request.form['query']
    api = "https://freenli.projects.zjvis.org/get_sentences_tasks"
    sentences = json.dumps([str(query)])
    params = {'sentences': sentences}
    result = requests.get(api, params = params)
    tasks = json.loads(result.json()['tasks'])[0]
    return jsonify(tasks)


#task classification api for multiple queries
@app.route('/get_sentences_tasks', methods=['POST'])
def get_sentences_tasks():
    queries = request.form['queries']
    api = "https://freenli.projects.zjvis.org/get_sentences_tasks"
    params = {'sentences': queries}
    result = requests.get(api, params = params)
    tasks = json.loads(result.json()['tasks'])
    return jsonify(tasks)

#Get Top 5 Recommendation
@app.route('/getAutoCompleteQuery', methods=['POST'])
def auto_complete():
    query = request.form['query']
    print('query recommendation')
    embedding = embed([query])
    sen_vec = embedding[0].numpy()
    result = top_five(sen_vec)
    print(result)
    cands = []
    for sen in result:
        returnSen = value_replace(table_vec_info, sen)
        cands.append(returnSen)
    return jsonify(cands)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True, port=80)
