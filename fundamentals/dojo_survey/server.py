from flask import Flask, render_template, request, redirect, session
# redirect and session are the new ones
app = Flask(__name__)
app.secret_key = "ca56dsf56aS3asf1"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process')
def process_form():
    session['']
    return redirect('/result')



if __name__ == "__main__":
    app.run(debug=True)