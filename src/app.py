from flask import Flask
app = Flask(__name__)

@app.route('/',methods=["GET"])
def main():
    return "Welcome to the App!"

@app.route('/health',methods=["GET"])
def health():
    return "App is running"

if __name__=="__main__":
    app.run(debug=True)
