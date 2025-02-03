import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    request_object = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, headers=header, json=request_object)
    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    elif response.status_code == 400:
        emotion_scores = {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None}
        dominant_emotion = None

    return { 
        **emotion_scores, 
        "dominant_emotion": dominant_emotion
    }
