from flask import Flask, render_template, request, redirect, session
# redirect and session are the new ones
app = Flask(__name__)
app.secret_key = 'lkdaslfa14583'  # set a secret key for security purposes

import random 	 # import the random module



#====================
# Root Route
#====================

@app.route('/')
def index():
    if "comp_guess" in session:
        print("the correct number is " + str(session["comp_guess"]))
    else:
        session["comp_guess"] = random.randint(1, 100)
    if "comparison" not in session:
        session["comparing"] = "not here??"
    return render_template("index.html", comparison = session['comparing'])

#=======================================
# Process form
#=======================================
@app.route('/number', methods=["POST"])
def process():
    if request.form["guess"] != "":
        your_guess = int(request.form["guess"])
    comp_guess = session['comp_guess']

    if comp_guess > your_guess:
        session["comparing"] = "low"
    elif comp_guess < your_guess:
        session["comparing"] = "high"
    else:
        session["comparing"] = "correct"
    return redirect("/")

#=======================================
# Reset Route
#=======================================
@app.route('/reset')
def reset():
    session.clear()
    return redirect("/")









if __name__ == "__main__":
    app.run(debug=True)