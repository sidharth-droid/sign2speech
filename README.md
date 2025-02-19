# Sign Language Recognition and Speech Synthesis

This project is developed as part of the 8th-semester submission for college. The system captures images of Indian Sign Language (ISL) hand gestures, processes them, and predicts the corresponding letter using a machine learning model. The output is displayed as text and converted into speech for better accessibility.
## Project Workflow

1. **Data Collection:** Capture images of hand gestures.
2. **Data Preprocessing & Feature Extraction:** Process the collected images to extract features.
3. **Model Training:** Train a machine learning model on the extracted features.
4. **Sign Detection & Prediction:** Use the trained model to recognize ASL gestures in real-time.

## Files and Usage

### 1. `data_collection.py`

- Purpose: Captures images of ASL hand gestures using a webcam.
- Usage: Run this script to collect images for training the model.
- Output: Saves collected images in the `./data` directory, organized by sign class.

### 2. `preprocess_dataset.py`

- Purpose: Processes collected images to extract key features and stores them in a serialized format.
- Usage: Run this after data collection to preprocess images.
- Output: Saves processed data in `data.pickle`.

### 3. `train_model.py`

- Purpose: Trains a Random Forest model using the preprocessed dataset.
- Usage: Run this after preprocessing to train the model.
- Output: Saves the trained model in `model.p`.

### 4. `sign_detection.py`

- Purpose: Uses the trained model to recognize ASL hand gestures in real-time via webcam.
- Usage: Run this script to make predictions based on live hand gestures.
- Output: Displays the recognized sign on the screen in real-time.

## How to Use

### **Step 1: Install Dependencies**

Ensure you have the required dependencies installed. Run the following command:

```bash
pip install opencv-python mediapipe numpy scikit-learn pickle-mixin
```

### **Step 2: Collect Data**

Run the data collection script to capture hand gesture images:

```bash
python data_collection.py
```

### **Step 3: Preprocess Data**

After collecting data, preprocess it using:

```bash
python preprocess_dataset.py
```

### **Step 4: Train the Model**

Train the machine learning model with:

```bash
python train_model.py
```

### **Step 5: Run Real-Time Prediction**

Finally, test the model in real-time by running:

```bash
python sign_detection.py
```

## Future Enhancements

- **Speech Feature:** Convert recognized signs into spoken words.
- **Web/Mobile Interface:** Develop a web or mobile application for accessibility.
- **Reverse Translation:** Allow users to input text and display corresponding ASL gestures.


