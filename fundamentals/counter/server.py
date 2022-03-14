from flask import Flask, render_template, request, redirect, session
# redirect and session are the new ones

app = Flask(__name__)
app.secret_key = 'kzxcv1b23b6'  # set a secret key for security purposes


@app.route('/')
def index():
    if 'session_count' in session:
        print('key exists!')
        session['session_count'] += 1
        sum = session['session_count']
        return render_template("index.html",count=sum)
    else:
        count = session['session_count'] = 1
        print("key 'count' does NOT exist")
        return render_template("index.html",count=count)

#========================================
#click/count button
#========================================

@app.route('/a', methods=['POST'])
def counter():
    # session['session_count'] += 1
    return redirect("/")
#========================================
#Session Reset
#========================================
    
@app.route('/destroy_session', methods=['POST'])
def clear():
    session.clear()		# clears all keys
    # session.pop('count')		# clears a specific key
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
