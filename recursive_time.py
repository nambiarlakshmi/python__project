def fac(n):
    if(n==1 or n==0):
        return 1
    return n*fac(n-1)

print("The time complexity of the function fac is O(n) because there is no looping.")

def print1to10(n):
    if(n>10):
        return
    print(n)
    print1to10(n+1)

print("The time complexity of the function print1to10 is O(n) because there is no looping.")