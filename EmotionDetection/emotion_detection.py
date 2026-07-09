import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects the emotion of the given.

    Args:
        text_to_analyze (str): The input text for emotion detection.

    Returns:
        str: The response text from the emotion detection.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"Grpc-Metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_data = { "raw_document": { "text": text_to_analyze } }
    
    try:
        response = requests.post(url, headers=headers, json=input_data)
        
        response.raise_for_status() 
        
        formatted_response = json.loads(response.text)

        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)

        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }

        dominant_emotion = max(emotions, key=emotions.get)

        new_output_format = {
            'anger' : anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion' : dominant_emotion
        }

        return new_output_format

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }