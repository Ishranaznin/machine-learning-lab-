import tkinter as tk

def calculate_edit_distance():
    #exercised executed
    string1 = entry1.get()
    string2 = entry2.get()
    distance = edit_distance(string1, string2)
    result.config(text="Edit Distance: " + str(distance))

def edit_distance(string1, string2):
    m = len(string1)
    n = len(string2)
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    return dp[m][n]

root = tk.Tk()
root.title("Edit Distance Calculator")

label1 = tk.Label(root, text="Enter first string:")
entry1 = tk.Entry(root)
label2 = tk.Label(root, text="Enter second string:")
entry2 = tk.Entry(root)
calculate_button = tk.Button(root, text="Calculate", command=calculate_edit_distance)
result = tk.Label(root, text="")

label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
calculate_button.pack()
result.pack()

root.mainloop()
