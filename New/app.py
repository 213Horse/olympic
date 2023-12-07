from flask import  Flask, request, render_template, jsonify
import os, json

def root_dir():
    """ Returns root director for this project """
    return os.path.dirname(os.path.realpath(__file__ + '/..'))

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods = ['GET','POST'])
def search_data():
    if request.method == 'POST':
        querry = request.form.get('querry').lower()
        search_chude = []
        chude_timduoc = {}

        with open("{}/database/chude.json".format(root_dir()), 'r') as file:
            chude = json.load(file)
        with open("{}/database/demuc.json".format(root_dir()), 'r') as file:
            demuc = json.load(file)

        for topic in chude:
            if querry in topic['Text'].lower():
                search_chude.append(topic)
        if search_chude:
            for chude in search_chude:
                results = []
                for item in demuc:
                    if chude['Value'] == item['ChuDe']:
                        results.append(item)
                chude_timduoc[chude['Text']] = results
        else:
            for item in demuc:
                if querry in item['Text'].lower():
                    for topic in chude:
                        if topic['Value'] == item['ChuDe']:
                  
                            chude_timduoc[topic['Text']] = item
        return jsonify(chude_timduoc) 

    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True,port=8888)