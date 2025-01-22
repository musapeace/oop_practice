# Program to handle ZeroDivisionError

class ZeroDivisionError(Exception):
    def __init__(self, message="Cannot divide by zero"):
        self.message = message
        super().__init__(self.message)

def division_of_2_numbers():
    try:
        # Taking two numbers as input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Performing division and check for zero
        if num2 == 0:
            raise ZeroDivisionError
        result = num1 / num2
        print(f"The result of division is: {result}")
    
    except ZeroDivisionError as e:
        print(e.message)
    except ValueError:
        print("Please enter valid numeric inputs.")

# Running  the function
division_of_2_numbers()
