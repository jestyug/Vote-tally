from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.secret_key = 'dev-secret-key'

RESULTS = [{
    'name': 'Lubega_Medard_Sseggona',
    'post': 'Memmber of parliament',
    'area': 'Busiro East Constituency',
    'totalresult': 37729
}, {
    'name': 'Sempala kigozi',
    'post': 'Memmber of parliament',
    'area': 'Busiro East Constituency',
    'totalresult': 34345
}, {
    'name': 'Haji Abdul Kiyimba',
    'post': 'Memmber of parliament',
    'area': 'Busiro East Constituency',
    'totalresult': 8989
}]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('sys_login.html')


@app.route('/navii')
def navii():
    return render_template('navii.html')


@app.route('/entries')
def entries():
    return render_template('entry_frm.html')


@app.route('/constituency')
def constituency():
    return render_template('constituencies.html')


@app.route('/parish')
def parish():
    return render_template('parish.html')


@app.route('/subcounty')
def subcounty():
    return render_template('subcounty.html')


@app.route('/candidates')
def candidates():
    return render_template('candidates.html')


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/linkcandpost')
def linkcandpost():
    return render_template('linkcandidatetopost.html')


@app.route('/pollingstation')
def pollingstation():
    return render_template('pollingstation.html')


@app.route('/results')
def results():
    return render_template('results.html', resultsdata=RESULTS)


@app.route('/results2')
def results2():
    return render_template('display2.html', resultsdata=RESULTS)


@app.route('/displayresults')
def displayresults():
    return render_template('displayresults.html')


@app.route('/resultsapi')
def resultsapi():
    return jsonify(RESULTS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
