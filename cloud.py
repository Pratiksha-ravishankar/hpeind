from flask import Flask
import os
app=Flask(__name__)
@app.route("/")
def home():
    return "Hello Flask"
if __name__=="__main__":
    port=os.environ("PORT",5000)
    app.run(debug=False, host="0,0,0,0", port=port)