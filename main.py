from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'dev-secret-key'


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
    return render_template('results.html')


@app.route('/displayresults')
def displayresults():
    return render_template('displayresults.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
