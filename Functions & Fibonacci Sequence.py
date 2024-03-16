# Defining generate_fibonacci_sequence function
def generate_fibonacci_sequence(n):

# Initializing the first two terms of the Fibonacci sequence
    fibonacci_sequence = [0, 1]

# Generating the Fibonacci sequence up to the nth term using for loop
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence[:n]

# Defining the main function
def main():

# Implementing error handling code to check if the user input is an integer(n) or not
    while True:
        try:

# Prompting the user to input the number of terms(n)
         n = int(input("Enter the number of terms(n) for the Fibonacci sequence: "))

# Exit the loop if the input(n) is an integer            
         break  

# If the input(n) is not an integer, display an error message that the user should input a valid integer(n)
        except ValueError:
            print("Please enter a positive integer!")

# Checking the condition if n is less than or equal to 0 
    if n <= 0:

# If n is less than or equal 0, ask the user to enter a positive integer
        print("Please enter a positive integer.")
        return
    
# Generating Fibonacci sequence
    fibonacci_sequence = generate_fibonacci_sequence(n)

# Printing the generated Fibonacci sequence
    print("Fibonacci sequence up to the", n, "term(s):", fibonacci_sequence)

# Calling the main function 
if __name__ == "__main__":
    main()