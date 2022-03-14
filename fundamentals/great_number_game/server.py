from flask import Flask, render_template, request, redirect, session
# redirect and session are the new ones

app = Flask(__name__)
app.secret_key = 'lkdaslfa14583'  # set a secret key for security purposes

#====================
# Root Route
#====================

@app.route('/')
def index():
    return render_template("index.html")

#====================
# Process form
#====================
@app.route('/number', methods=["POST"])
def process():
    return redirect('/')

    
if __name__ == "__main__":
    app.run(debug=True)