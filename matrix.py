from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    matrix1 = [[1, 2, 3], [4, 5, 6]]
    matrix2 = [[7, 8], [9, 10], [11, 12]]
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    # Check if matrices can be multiplied
    if cols1 != rows2:
        return "Matrices cannot be multiplied."

    # Create a result matrix filled with zeros
    result = [[0] * cols2 for _ in range(rows1)]
    # Multiply matrices
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    # Convert result to string
    result_string = ""
    for row in result:
        result_string += " ".join(str(element) for element in row)
        result_string += "\n"
    return result_string


if __name__ == '__main__':
      app.run(host='127.0.0.1', port=8080, debug=True)
