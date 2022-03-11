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



@app.route('/35/<int:hello>')
def tell(hello):
    return 'hello ' * hello

@app.route('/80/<int:bye>')
def tell(bye):
    return 'bye ' * bye

@app.route('/99/<int:dogs>')
def tell(dogs):
    return 'dogs' ' * dogs



if name=="main":   
    app.run(debug=True)    

