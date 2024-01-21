''' Executing this function initiates the application to detect
    emotion based on entered text. The application is deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#initialize app
app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def run_emotion_detector():
    ''' This code receives the text from the HTML interface and
        runs emotion analysis over it using emotion_detector()
        function. The output returned a dictionary showing the result.
    '''
    text = request.args.get('textToAnalyze')
    response = emotion_detector(text)

    if response['dominant_emotion'] is None:
        response_text = "Invalid Input! Please try again."
    else:
        response_text = f"For the given statement, the system response is 'anger': \
                        {response['anger']}, 'disgust': {response['disgust']}, \
                        'fear': {response['fear']}, 'joy': {response['joy']}, \
                        'sadness': {response['sadness']}. The dominant emotion is \
                        {response['dominant_emotion']}."

    return response_text


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
