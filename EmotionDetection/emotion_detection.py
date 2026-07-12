import json
import requests

def emotion_detector(text_to_analyze):
    # Prepare input data
    url = 'https://sn-watson-emotion.labs.skills.network/' \
    'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    # API call to the Watson NLP Library
    response = requests.post(url, json = input_json, headers = headers, timeout = 5)
    json_response = json.loads(response.text)
    emotions = json_response['emotionPredictions'][0]['emotion']

    # Find the strongest emotion
    dominant_emotion = ('', 0)
    for emotion, score in emotions.items():
        _, max_score = dominant_emotion
        if score > max_score:
            dominant_emotion = (emotion, score)

    # Prepare final response object
    final_response = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion[0]
    }

    return final_response
