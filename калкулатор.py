def calkulator():  
    print("Изберете операция:")  
    print("1. add")
    print("2. Изваждане")  
    print("3. Умножение")  
    print("4. delete")

    операция = input("Въведете номера на операцията (1/2/3/4): ")  

    if операция in ('1', '2', '3', '4'):  
        num1 = float(input("Въведете първото число: "))  
        num2 = float(input("Въведете второто число: "))  

        if операция == '1':  
            резултат = num1 + num2  
            print(f"Резултатът е: {резултат}")  

        elif операция == '2':  
            резултат = num1 - num2  
            print(f"Резултатът е: {резултат}")  

        elif операция == '3':  
            резултат = num1 * num2  
            print(f"Резултатът е: {резултат}")  

        elif операция == '4':  
            if num2 != 0:  
                резултат = num1 / num2  
                print(f"Резултатът е: {резултат}")  
            else:  
                print("Грешка: Деление на нула не е разрешено.")  
    else:  
        print("Невалидна операция. Моля, опитайте отново.")  

calkulator()

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        result = divide(num1, num2)
        if result == "Error! Division by zero.":
            print(result)
        else:
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input. Please try again.")