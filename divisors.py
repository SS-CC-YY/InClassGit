def number():
    try:
        number = int(input("Please enter the number: "))
        return number
    except:
        print("Invalid input!")

def check_divisor(dividend,divisor):
    if dividend % divisor == 0:
        return True
    else:
        return False


num = number()
for i in range(num+1):
    if i ==0 :
        continue
    if check_divisor(num,i) == True:
        print(i)
    