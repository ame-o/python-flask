from flask import Flask, render_template  # added render_template!

app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")  








# import statements, maybe some other routes
@app.route('/users', methods=["POST"])
def process_form():
    print(request.form)
    print(request.form["name"])
    print(request.form["email"])
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)