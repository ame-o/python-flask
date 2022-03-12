from flask import Flask  
app = Flask(name)    



@app.route('/')          
def hello_world():
    return 'Hello World!'  




@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/say/<name>')
def sayname(name):
    return 'hello, ' + name


@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"

    return output


if name=="main":   
    app.run(debug=True)    

