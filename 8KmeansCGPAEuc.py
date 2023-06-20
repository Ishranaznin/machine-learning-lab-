import numpy as np
import tkinter as tk

# Create the Tkinter window
window = tk.Tk()
window.title("K-Means Clustering")
window.geometry("400x300")

# Create input fields for number of clusters, cluster center points, and test number
cluster_label = tk.Label(window, text="Number of Clusters:")
cluster_label.pack()
cluster_entry = tk.Entry(window)
cluster_entry.pack()

centers_label = tk.Label(window, text="Cluster Center Points (comma-separated):")
centers_label.pack()
centers_entry = tk.Entry(window)
centers_entry.pack()

test_label = tk.Label(window, text="Test Number:")
test_label.pack()
test_entry = tk.Entry(window)
test_entry.pack()

# Function to run the clustering algorithm and display results
def run_clustering():
    # Get input values from the user
    k = int(cluster_entry.get())
    centroids = np.array([float(x) for x in centers_entry.get().split(",")])
    test_point = float(test_entry.get())

    # Student CGPA
    data = np.array([3.45, 3.78, 2.98, 3.24, 4.0, 3.9])

    def euclidean_distance(x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))

    # Define a function to assign each point to the nearest center
    def assign_to_clusters(points, centers):
        distances = np.abs(points[:, np.newaxis] - centers)
        cluster_assignments = np.argmin(distances, axis=1)
        return cluster_assignments

    def find_clusters(data, centroids):
        clusters = np.zeros(len(data))
        for i in range(len(data)):
            dist = np.zeros(k)
            for j in range(k):
                dist[j] = euclidean_distance(data[i], centroids[j])
            cluster = np.argmin(dist)
            clusters[i] = cluster
        return clusters

    def update_centroids(data, clusters, centroids):
        for i in range(k):
            points = [data[j] for j in range(len(data)) if clusters[j] == i]
            centroids[i] = np.mean(points, axis=0)

    # Repeat until convergence
    while True:
        clusters = find_clusters(data, centroids)
        prev_centroids = centroids
        update_centroids(data, clusters, centroids)
        if np.allclose(prev_centroids, centroids):
            break

    # Display the final clusters
    result_label = tk.Label(window, text="Final Clusters:")
    result_label.pack()
    for i in range(k):
        points = [data[j] for j in range(len(data)) if clusters[j] == i]
        cluster_result = f"Cluster {i + 1}: {points}"
        cluster_result_label = tk.Label(window, text=cluster_result)
        cluster_result_label.pack()

    # Assign the test number to a cluster
    test_assignment = assign_to_clusters(np.array([test_point]), centroids)
    test_result = f"Test point {test_point} belongs to cluster {test_assignment + 1}"
    test_result_label = tk.Label(window, text=test_result)
    test_result_label.pack()

# Create a button to run the clustering algorithm
run_button = tk.Button(window, text="Run Clustering", command=run_clustering)
run_button.pack()

# Run the Tkinter event loop
window.mainloop()
