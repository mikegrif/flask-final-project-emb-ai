import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=data, headers=header)
    result = ''
    print('DEBUG: ' + str(json.loads(response.text)))

    if (response.status_code == 200):
        formatted_response = json.loads(response.text)
        emotions = dict(formatted_response['emotionPredictions'][0])
        result = emotions['emotion']

        # find dominant emotion
        key, value = max(result.items(), key = lambda item: float(item[1]))
        result['dominant_emotion'] = key
        return result

    if response.status_code == 400:
        result = {"anger": None, "disgust": None, "fear": None,
              "joy": None, "sadness": None}

        return result

    return result

