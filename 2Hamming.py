import numpy as np

# Initialize weights and biases
weights = np.array([[-1, 1, -1], [-1, -1, 1]])
biases = np.array([3, 3])

# Define activation function
def activation(x):
    if x >= 0:
        return x
    else:
        return 0
    
def activationForward(x):
         return x
weigh2=np.array([[1,-0.5],[-0.5,1]])
# Define the forward pass
def forward(inputs, weights, biases):
    output = np.dot(weights,inputs) + biases
    return [activationForward(x) for x in output]
   
def recurrent(outputs, weigh2):
    output2 = np.dot(weigh2, outputs)
    return [activation(x) for x in output2]
    

# Define the fruit classification function
def classify_fruit(inputs):
    outputs = forward(inputs, weights, biases)
    outputs2=recurrent(outputs, weigh2)
    if outputs2[0] > outputs2[1]:
        return "Banana"
    else:
        return "Pineapple"

# Define input vectors for fruit
test_input = np.array([1,- 1, 1])
print(f"test {test_input}, {classify_fruit(test_input)}")
# Test the operation of the network


import tkinter as tk

# Define a function to handle the button click event
def button_click():
    # Get the input array from the entry widget
    input_str = input_entry.get()
    input_arr = [int(x.strip()) for x in input_str.split(",")]
    
    # Display the input array in the label widget
    output_label.config(text=f"Input:  { input_arr}, Output:  {classify_fruit( input_arr)}")
    
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
