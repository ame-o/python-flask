from flask import Flask, render_template  # added render_template!

app = Flask(__name__)



@app.route('/')
def index():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template("index.html",num1=8, num2=8)  

# import statements, maybe some other routes

@app.route('/4')
def by_four(color1 ="black", color2="red"):
    return render_template("index.html",num1=8,num2=4,color1=color1, color2=color2)

@app.route('/<int:num1>/<int:num2>')
def by_xy(num1,num2):
    return render_template("index.html",num1=num1,num2=num2,color1 ="black", color2="red") 


if __name__=="__main__":
    app.run(debug=True)