''' Executing this function initiates the application to detect
    emotion based on entered text. The application is deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#initialize app
app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def process_emotion():
    ''' This code receives the text from the HTML interface and
        runs emotion analysis over it using emotion_detector()
        function. The output returned a dictionary showing the result.
    '''
    text = request.args.get('textToAnalyze')
    response = emotion_detector(text)
    key = 'dominant_emotion'

    if response.get(key, None) is None:
        return 'Invalid text! - please try again.'

    msg = 'For the given statement, the system response is: ' + str(response)
    return msg

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
