import numpy as np
import pandas as pd
import tkinter as tk

# Define the data
data = [(158, 58, 'M'), (158, 59, 'M'), (158, 63, 'M'), (160, 59, 'M'), (160, 60, 'M'), (163, 60, 'M'),
        (163, 61, 'M'), (160, 64, 'L'), (163, 64, 'L'), (165, 61, 'L'), (165, 62, 'L'), (165, 65, 'L'),
        (168, 62, 'L'), (168, 63, 'L'), (168, 66, 'L'), (170, 63, 'L'), (170, 64, 'L'), (170, 68, 'L')]

# Convert data to a dataframe
df = pd.DataFrame(data, columns=['height', 'weight', 'tshirt_size'])

# Define the tkinter window
window = tk.Tk()
window.title("T-Shirt Size Prediction")

# Create input labels and entry widgets
height_label = tk.Label(window, text="Enter height in cms:")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

weight_label = tk.Label(window, text="Enter weight in kgs:")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

k_label = tk.Label(window, text="Enter the value of k:")
k_label.pack()
k_entry = tk.Entry(window)
k_entry.pack()

# Define the button click function
def predict_tshirt_size():
    height = int(height_entry.get())
    weight = int(weight_entry.get())
    k = int(k_entry.get())

    # Define the target observation
    target = np.array([height, weight])

    # Calculate the Euclidean distance
    def euclidean_distance(x, y):
        return np.sqrt(np.sum((x - y) ** 2))

    # Define the KNN algorithm
    def knn(df, target, k):
        distances = []
        for i, row in df.iterrows():
            distance = euclidean_distance(np.array([row['height'], row['weight']]), target)
            distances.append((row['tshirt_size'], distance))
        distances = sorted(distances, key=lambda x: x[1])
        return [x[0] for x in distances[:k]]

    # Predict the T-shirt size
    result = knn(df, target, k)
    predicted_size = max(set(result), key=result.count)
    result_label.config(text="Predicted T-shirt size: " + predicted_size)

# Create a button to trigger the prediction
predict_button = tk.Button(window, text="Predict T-Shirt Size", command=predict_tshirt_size)
predict_button.pack()

# Create a label to display the prediction result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the tkinter event loop
window.mainloop()
