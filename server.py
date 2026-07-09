"""
Server module for the Emotion Detection application.
Handles routing, processing user input, and formatting API responses.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def text_detector():
    """
    Route that receives an input text from the frontend, analyzes its emotions 
    using the emotion_detector package, and returns a formatted string.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    
    response = emotion_detector(text_to_analyze)
    
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    
    output_string = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    
    return output_string

@app.route("/")
def render_index_page():
    """
    Route that serves the main HTML interface of the application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)