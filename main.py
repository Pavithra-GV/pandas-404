# app.py
from flask import Flask, request, jsonify
from PIL import Image
import io
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

model = load_model('model_name')

# Define class labels
class_labels = ['Healthy', 'Disease']

def predict_crop_disease(image):
    img = image.resize((224, 224))  
    img = np.asarray(img) / 255.0  
    img = np.expand_dims(img, axis=0)  
    
    predictions = model.predict(img)
    
    predicted_class_index = np.argmax(predictions)
    predicted_class_label = class_labels[predicted_class_index]
    
    return predicted_class_label

@app.route('/api/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'})

    image = request.files['image']
    image_bytes = io.BytesIO(image.read())
    img = Image.open(image_bytes)

    # Predict crop disease
    result = predict_crop_disease(img)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
