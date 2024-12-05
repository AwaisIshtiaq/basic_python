a = input("Enter a tabel Number : ")


try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:
    print("Some unknow values")



b = [1,2,3]

try:
    print(f"second element of list is {b[2]} ")

    print(f"Third element of list is {b[3]}")

except IndexError:
    print("Index is out of range")




def divide_numbers():
    try:
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
    
        result = num1 / num2
    except ValueError:
        print("Error: Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print(f"The result of {num1} divided by {num2} is {result}.")
    finally:
        print("Execution completed.")

divide_numbers()
