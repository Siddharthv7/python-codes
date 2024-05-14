import random

class AIAssistant:
    def __init__(self):
        self.greetings = ["Hello!", "Hi there!", "Hey, how can I help you?"]
        self.goodbyes = ["Goodbye!", "See you later!", "Farewell!"]
    
    def greet(self):
        return random.choice(self.greetings)
    
    def say_goodbye(self):
        return random.choice(self.goodbyes)

class MathAI:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero!"

def main():
    ai_assistant = AIAssistant()
    math_ai = MathAI()
    
    print(ai_assistant.greet())
    while True:
        user_input = input("Type 'exit' to quit or ask a math question: ")
        
        if user_input.lower() == 'exit':
            print(ai_assistant.say_goodbye())
            break
        
        try:
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input. Please provide a valid math question.")
                continue
            
            num1 = float(parts[0])
            num2 = float(parts[2])
            operator = parts[1]
            
            if operator == '+':
                result = math_ai.add(num1, num2)
            elif operator == '-':
                result = math_ai.subtract(num1, num2)
            elif operator == '*':
                result = math_ai.multiply(num1, num2)
            elif operator == '/':
                result = math_ai.divide(num1, num2)
            else:
                print("Unsupported operator. Please use +, -, *, or /.")
                continue
            
            print("Result:", result)
        except ValueError:
            print("Invalid input. Please provide valid numbers.")
        
if __name__ == "__main__":
    main()
