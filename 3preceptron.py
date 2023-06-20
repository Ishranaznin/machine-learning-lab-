#Here's a Python program that implements the perceptron learning rule for the given training set:
import numpy as np

# define the training set
X = np.array([[1, 0, 1], [0, -1, -1], [-1, -0.5, -1]])
y = np.array([-1, 1, 1])

# initialize the weight vector
w = np.array([1, -1, 0])

# set the learning rate and maximum number of iterations
bias = 0.1
max_iterations = 100

# train the neural network using the perceptron learning rule
for i in range(max_iterations):
    for j in range(len(X)):
        x = X[j]
        y_hat = np.sign(np.dot(w, x))
        error = y[j] - y_hat
        w = w+ error * bias * x
        bias = bias+ bias * error 
    # check for convergence
    if np.all(np.sign(np.dot(X, w)) == y):
        print(f"Converged after {i+1} iterations.")
        break
    else:
        print(f"Did not converge after {max_iterations} iterations.")

print("Final weight vector: ", w)
print("Final bias : ",bias)
# test the network with new input patterns
x_test = np.array([[1, 1, 1], [-1, 0, 1], [0, 1, -1]])
y_test = np.sign(np.dot(x_test, w))
print("Predictions for test set: ", y_test)
import tkinter as tk

# Define a function to handle the button click event
def button_click():
    # Get the input array from the entry widget
    input_str = input_entry.get()
    input_list = input_str.split(';')
    input_arr = np.array([list(map(int, row.split(','))) for row in input_list])  
    # Display the input array in the label widget
    y_test = np.sign(np.dot(input_arr, w))
    output_label.config(text=f"Predictions for test set: { y_test } \n weight : { w}\n bias: {bias}")
    
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
