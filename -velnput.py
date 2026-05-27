def negative_number(n):
    if n < 0:
        print("Number -ve")
    else:
        print("Number +ve")
        negative_number(int(input("Enter your number : ")))
    
num =  negative_number(int(input("Enter your number : "))) 