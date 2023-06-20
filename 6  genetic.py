import random
import math
import tkinter as tk
# Define a function to handle the button click event
def button_click():
    # Get the function expression from the entry widget
    function_expression = input_entry.get()

    # define the function to be optimized
    def function_to_optimize(x):
        return ((-x**2)/10)+(3*x)    
    
    # define the search interval
    search_interval = (0, 31)
    # define the genetic algorithm parameters
    population_size = 10
    mutation_rate = 0.1
    generations = int(generations_entry.get())  # Get the number of generations from the entry widget
    
    # define the individual representation and initialization
    def create_individual():
        return random.uniform(search_interval[0], search_interval[1])
    
    # define the fitness function
    def fitness(individual):
        return function_to_optimize(individual)
    
    # define the selection operator
    def selection(population):
        return random.sample(population, 2)
    
    # define the crossover operator
    def crossover(parents):
        return (parents[0] + parents[1]) / 2
    
    # define the mutation operator
    def mutation(individual):
        return individual + random.uniform(-1, 1) * mutation_rate
    
    # initialize the population
    population = [create_individual() for i in range(population_size)]
    
    # iterate over the generations
    for i in range(generations):
        # evaluate the fitness of the population
        fitness_values = [fitness(individual) for individual in population]
        # select the parents for reproduction
        parents = [selection(population) for j in range(population_size // 2)]
        # perform crossover to generate the offspring
        offspring = [crossover(parents[j]) for j in range(population_size // 2)]
        # perform mutation on the offspring
        offspring = [mutation(individual) for individual in offspring]
        # replace the least fit individuals with the offspring
        print([type(p) for p in population])
        print([type(f) for f in fitness_values])
        population = sorted(list(zip(population, fitness_values)), key=lambda x: -x[1])[:population_size // 2]
        population = [individual for individual, fitness in population] + offspring
    
    # print the best solution found
    best_individual = max(population, key=fitness)
    print(f"The maximum value of the function is : { fitness(best_individual)} \n at x = {best_individual}")
    output_label.config(text=f"The maximum value of the function is:\n {fitness(best_individual)}\n at x = { best_individual}")
# Create the GUI
root = tk.Tk()
root.title('Function Input')

# Create a label for the input entry widget
input_label = tk.Label(root, text='Enter a function (use x as variable):')
input_label.pack()

# Create an entry widget for the function input
input_entry = tk.Entry(root)
input_entry.pack()

# Create a label for the generations entry widget
generations_label = tk.Label(root, text='Enter the number of generations:')
generations_label.pack()

# Create an entry widget for the number of generations
generations_entry = tk.Entry(root)
generations_entry.pack()

# Create a button to display the validity of the function
display_button = tk.Button(root, text='Test Function', command=button_click)
display_button.pack()

# Create a label for the output
output_label = tk.Label(root, text='')
output_label.pack()

root.mainloop()
