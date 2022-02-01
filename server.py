from flask import Flask,render_template,request,redirect,url_for,session,flash,Response
from datetime import datetime,timedelta
import json
from translate import Translate


app = Flask(__name__)
app.secret_key = "asdkjfbaskdljfouaksdhfklsadhlfhsdlifhsk"
app.permanent_session_lifetime = timedelta(days=5)

@app.route("/translate",methods = ["GET"])
def translate():
    json_data  = request.json 
    text       = json_data["text"]
    target_lan = json_data["target"].lower()
    print(text,target_lan)
    
    translate_object = Translate()
   
    res = translate_object.translate(text,target_lan)
    #print(json.dumps(res))
    return res

if __name__ == "__main__":
    app.run(debug=True)