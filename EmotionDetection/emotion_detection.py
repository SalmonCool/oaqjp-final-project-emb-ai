import requests
import json

def emotion_detector (text_to_analyze):

    #Get response as text and convert it to json object though 'json.loads' function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json =  { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=headers, json=input_json)
    response_json = json.loads(response.text)

    #We have to peel back a few layers to get at the emotion data we want
    emotion_predictions_list = response_json['emotionPredictions']
    emotion_internal_dict = emotion_predictions_list[0]
    raw_emotions_dict = emotion_internal_dict['emotion']

    #Get value of each emotion from raw_emotions_dict
    anger = raw_emotions_dict['anger']
    disgust = raw_emotions_dict['disgust']
    fear = raw_emotions_dict['fear']
    joy = raw_emotions_dict['joy']
    sadness = raw_emotions_dict['sadness']

    #Get dominant emotion through finding key with highest value
    dominant_emotion = max(raw_emotions_dict, key=lambda k: raw_emotions_dict[k])

    #Return format described by task 3
    return_format = {
    'anger': anger,
    'disgust': disgust,
    'fear': fear,
    'joy': joy,
    'sadness': sadness,
    'dominant_emotion': dominant_emotion
    }
    return return_format
