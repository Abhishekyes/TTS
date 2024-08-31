from text_to_speech.exception import TTSException
from flask_cors import CORS, cross_origin
from flask import Flask,render_template,request
from text_to_speech.component.get_accent import get_accent_message,get_accent_tld
from text_to_speech.component.texttospeech import TTSapplication
import sys
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG
)

    
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET','POST'])
@cross_origin()
def home():
    try: 
        accent_list = get_accent_message()
        return render_template('index.html', accent_list=accent_list)
    except Exception as e:
        raise TTSException(e, sys)

@app.route("/predict", methods=['GET','POST'])
@cross_origin()
def predict():
    try:
        if request.method == 'POST':
            data = request.json['data']
            accent_input = request.json['accent']
            accent = get_accent_tld(accent_input)
            print(accent)
            result = TTSapplication().text2speech(data, accent)
            return {"data": result.decode("utf-8")}
    except Exception as e:
        raise TTSException(e, sys)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=False)