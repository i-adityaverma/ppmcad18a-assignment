from flask import Flask, jsonify
app = Flask(__name__)

votes = {}


@app.route('/',methods=["GET"])
def main():
    return "Welcome to the App!"

@app.route('/health',methods=["GET"])
def health():
    return "App is running"

@app.route('/vote/<string:name>')
def vote(name):
    candidate = name.lower()
    votes[candidate] = votes.get(candidate, 0) + 1
    return {"msg": f"Vote recorded for {candidate}", "votes": votes[candidate]}

@app.route('/results',methods=["GET"])
def results():
    return votes

if __name__=="__main__":
    app.run(debug=True)
