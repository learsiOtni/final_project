''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' Documented doc string
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']

    text = ''
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    for emotion, score in response.items():
        if emotion == 'joy':
            text += f"'{emotion}': {score} and "
            continue
        if emotion == 'sadness':
            text += f"'{emotion}': {score}"
            continue
        if emotion == 'dominant_emotion':
            continue
        text += f"'{emotion}': {score}, "

    first_sentence = f"For the given statement, the system response is {text}. "
    second_sentence = f"The dominant emotion is {dominant_emotion}."
    return first_sentence + second_sentence

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
