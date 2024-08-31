"""
This file manages a server that runs emotion detection

Username: SalmonCool
Date: August 30th 2024
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """ Function called when server launches that displays the 'index.html' template """
    return render_template('index.html')

@app.route('/emotionDetector')
def detect():
    """ Calls the emotion_detector function to analyze the text given by the user"""

    #Get text from http request
    text = request.args.get('textToAnalyze','')
    result = emotion_detector(text)

    #Check for 'None' as dominant_emotion
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    #Continue as normal if no None present
    result_text_format = "For the given statement, " \
    "the system response is 'anger': " + str(result['anger']) + "," \
    " 'disgust': " + str(result['disgust']) + "," \
    " 'fear': " + str(result['fear']) + "," \
    " 'joy': " + str(result['joy']) + "," \
    " 'sadness': " + str(result['sadness']) + "," \
    " The dominant emotion is " + str(result['dominant_emotion']) + "."
    return result_text_format

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
