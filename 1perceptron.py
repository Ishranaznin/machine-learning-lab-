import numpy as np
class Perceptron:
    def __init__(self, inputs, labels):
        self.inputs = inputs
        self.labels = labels
        self.weights = np.random.uniform(-1, 1, (3,))
        self.bias = np.random.uniform(-1, 1)     
    def activation_function(self, x):
        if x >= 0:
            return 1
        else:
            return 0
    def train(self, epochs):
        for epoch in range(epochs):
            for i in range(len(self.inputs)):               
                prediction = self.predict(self.inputs[i])               
                error = self.labels[i] - prediction              
                self.weights += error * self.inputs[i]
                print(self.weights)
                self.bias += error

    def predict(self, inputs):
        dot_product = np.dot(inputs, self.weights) + self.bias
        
        prediction = self.activation_function(dot_product)
        
        return prediction

# Define input patterns
inputs = np.array([[1, 1, -1],  [1, -1, -1]])

# Define corresponding labels (1 for apples and -1 for oranges)
labels = np.array([1,-1])

# Initialize the perceptron network
perceptron = Perceptron(inputs, labels)

# Train the network
perceptron.train(100)

# Test the network with some inputs
test_inputs = np.array([[1, 1, 1], [1, -1, 1], [1, -1, -1]])
for inputs in test_inputs:
    prediction = perceptron.predict(inputs)
    if prediction==1:
        print(f"Input:{inputs} Prediction: Apple")  
    else:
        print(f"Input:{inputs} Prediction: Orange")
    
import tkinter as tk

# Define a function to handle the button click event
def button_click():
    # Get the input array from the entry widget
    input_str = input_entry.get()
    input_arr = [int(x.strip()) for x in input_str.split(",")]
    
    # Display the input array in the label widget
    output_label.config(text=f"Input array: {input_arr}")
    prediction = perceptron.predict(input_arr)
    if prediction==1:
        print(f"Input: {input_arr}, Prediction: Apple")
        output_label.config(text=f"Output: Prediction: Apple")
    else:
        print(f"Input: {input_arr}, Prediction: Orange")
        output_label.config(text=f"Output: Prediction: Orange")
# Create the GUI
root = tk.Tk()
root.title('Array Input')

# Create a label for the input entry widget
input_label = tk.Label(root, text='Enter the array (comma-separated):')
input_label.pack()

# Create an entry widget for the input array
input_entry = tk.Entry(root)
input_entry.pack()

# Create a button to display the input array
display_button = tk.Button(root, text='Display', command=button_click)
display_button.pack()

# Create a label for the output
output_label = tk.Label(root, text='')
output_label.pack()

root.mainloop()
