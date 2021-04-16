def number():
    try:
        number = int(input("Please enter the number: "))
        return number
    except:
        print("Invalid input!")

num = number()