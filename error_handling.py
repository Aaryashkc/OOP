
while True:
    try:
        age = int(input("Enter your age: "))
        print(age)
        mango= 100/age
        print(mango)

    except ValueError:
        print("Invalid age: Please enter a valid age.")

    except ZeroDivisionError:
        print("Invalid number: you cannot divide by zero")

    else:
        print("Age successfully set!: thanks for your data muheheheheh")
        break
    finally:
        print("Have a good day!")

def sum(num1, num2, num3):
    try:
        return num1 + num2 + num3
    except TypeError as err:
        return f"this has error man{err}"
print(sum(1,2,'3'))


while True:
    try:
        age = int(input("Enter your age1: "))
        man= 10/age
        raise ValueError("hey cut it out")  #this runs no matter what
    except ZeroDivisionError:
        print("Invalid number: you cannot divide by zero")
    else:
        break
    finally:
        print("Have a good day!")

