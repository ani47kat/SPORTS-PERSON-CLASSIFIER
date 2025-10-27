from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "✅ Flask server is running! Use POST /classify_image to classify images."

@app.route('/classify_image', methods=['POST'])
def classify_image():
    try:
        if 'image_data' not in request.form:
            return jsonify({'error': 'No image data received'}), 400

        image_data = request.form['image_data']
        result = util.classify_image(image_data, None)

        # Convert numpy arrays to lists for JSON serialization
        for item in result:
            if hasattr(item.get('class_probability'), 'tolist'):
                item['class_probability'] = item['class_probability'].tolist()

        return jsonify(result)

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    print("🚀 Flask server started at: http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)

