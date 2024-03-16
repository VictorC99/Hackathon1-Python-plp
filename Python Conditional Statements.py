# Defining the main function
def main():

# Implementing error handling code to check if the user input is an integer or not
    while True:
        try:

# Prompting the user to enter their age
            age = int(input("Enter your age: "))

# Exit the loop if the input is an integer            
            break  

# If the input is not an integer, display an error message that the use should input a valid integer
        except ValueError:
            print("Please enter a valid age!")

# Checking if the age is greater than or equal to 18
    if age >= 18:

# If the condition is true, that the use is 18 years or older print "You are eligible to vote.😀"
        print("You are eligible to vote.😀")

# If the condition is false, that the use is under 18 years old print "You are not eligible to vote.😔"
    else:
        print("You are not eligible to vote.😔")

# Calling the main function
if __name__ == "__main__":
    main()
