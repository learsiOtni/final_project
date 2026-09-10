from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = ''
    result_in_text = ''

    for emotion, score in response.items():
        if emotion == 'joy':
            result_in_text += f"'{emotion}': {score} and "
            continue
        elif emotion == 'sadness':
            result_in_text += f"'{emotion}': {score}"
            continue
        elif emotion == 'dominant_emotion':
            dominant_emotion = score
            continue
        
        result_in_text += f"'{emotion}': {score}, "

    return f"For the given statement, the system response is {result_in_text}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)