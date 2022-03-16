from flask import Flask, render_template, request, redirect, session
# redirect and session are the new ones
app = Flask(__name__)
app.secret_key = "ca56dsf56aS3asf1"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process',methods =['POST'])
def process_form():
    for key in request.form:
        session['name'] = request.form['name'] 
        session['location'] = request.form['location'] 
        session['fave language'] = request.form['fave language'] 
        session['comments'] = request.form['comments'] 
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("result.html",name=session['name'], location=session['location'],fave=session['fave language'], comments=session['comments'])




if __name__ == "__main__":
    app.run(debug=True)