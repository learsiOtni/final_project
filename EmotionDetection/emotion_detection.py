''' This is a document string
'''
import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input_json, headers = headers, timeout=1.5)

    formatted_response = json.loads(response.text)

    if response.status_code == 400:
        emotions = {
            'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = ''
        dominant_emotion_score = 0
        for emotion, score in emotions.items():
            if score > dominant_emotion_score:
                dominant_emotion_score = score
                dominant_emotion = emotion

        emotions["dominant_emotion"] = dominant_emotion

    return emotions