from flask import Flask, render_template, request, redirect, session
#redirect and session are the new ones

app = Flask(__name__)
app.secret_key = 'kzxcv1b23b6' # set a secret key for security purposes


@app.route('/')
def index():
    return render_template("index.html")

#index redirects to users
#method is post because it intakes the input info from index
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')
#session['session key name'] = request.form ['key name']

#redirect from /users sends it to /show

# adding this method
@app.route('/show')
def show_user():
    return render_template('show.html')
#show html now has the ability to call on the stored properties from /users
#by using {{session['session key name']}} directly in the rendered template of show html



if __name__ == "__main__":
    app.run(debug=True)

