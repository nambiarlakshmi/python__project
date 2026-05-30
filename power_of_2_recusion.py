def power_of_2(n):
    if(n<=0):
        return False
    if(n==1):
        return True
    if(n%2==0):
        return power_of_2(n/2)
    return False
if(power_of_2(4)):
    print("Power of 2")
else:
    print("Not power of 2")

