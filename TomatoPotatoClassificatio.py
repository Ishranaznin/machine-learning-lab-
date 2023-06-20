import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import joblib

# Path to folder containing images to train the SVM
image_folder = 'D:/8th semister/machine learning/tomato-potato-dataset/image'

# Function to extract features from the image
def extract_features(image_path):
    image = Image.open(image_path)
    image = image.resize((224, 224))  # Resize the image to a fixed size
    image_array = np.array(image)
    flattened_image = image_array.flatten()  # Flatten the image into a 1D array
    return flattened_image

def load_data(image_folder):
    images = []
    labels = []
    class_names = []
    class_mapping = {}  # Mapping between class labels and indices
    # Traverse the image folder
    for root, dirs, files in os.walk(image_folder):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(root, file)
                label = file.split("_")[0]
                if label not in class_mapping:
                    class_mapping[label] = len(class_mapping)
                    class_names.append(label)
                images.append(extract_features(image_path))
                labels.append(class_mapping[label])
    return np.array(images), np.array(labels), class_names


def train_svm(images, labels):
    scaler = StandardScaler()
    scaled_images = scaler.fit_transform(images)  # Scale the image features
    X_train, X_test, y_train, y_test = train_test_split(scaled_images, labels, test_size=0.2, random_state=42)
    classifier = svm.SVC(kernel='linear')
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)
    return classifier, scaler

def classify_image(image_path, classifier, scaler, class_names):
        image_features = extract_features(image_path)
        scaled_features = scaler.transform([image_features])  # Scale the image features
        predicted_class_index = classifier.predict(scaled_features)[0]
        predicted_label = class_names[predicted_class_index]
        return predicted_label

images, labels, class_names = load_data(image_folder)
classifier, scaler = train_svm(images, labels)

def classify_button_click():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select Image File")
    if file_path:
        predicted_label = classify_image(file_path, classifier, scaler, class_names)
        result_label.config(text=f"Predicted Class: {predicted_label}")
    else:
        messagebox.showwarning("Image Classification", "No file selected.")

# Create the GUI window
window = tk.Tk()
window.title("Image Classification")
window.geometry("300x150")

# Create a classify button
classify_button = tk.Button(window, text="Classify Image", command=classify_button_click)
classify_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text=" ")
result_label.pack()

# Run the GUI event loop
window.mainloop()
