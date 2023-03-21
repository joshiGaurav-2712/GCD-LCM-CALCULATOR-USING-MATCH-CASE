#LCM:It is the least number that is div by two  or more numbers
#HCF:It is the Highest number that can div two or more nos

def lcm(a,b):
    maxn=max(a,b)

    while True:
        if maxn%a==0 and maxn%b==0:
            break
        maxn+=1
    print(f"LCM of {a} and {b} is {maxn}")  
def gcd(a,b):
    minn=min(a,b)
    for i in range(1,minn+1):
        if a%i==0 and b%i==0:
            hcf=i
    print(f"HCF of {a} and {b} is {hcf}") 
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))    

x=input("Enter your choice (LCM/HCF/Both):").upper() 
match x:
    case _ if x=="LCM":
              lcm(a,b)
    case _ if x=="HCF": 
              gcd(a,b)  
    case _ if x=="BOTH":
              lcm(a,b)
              gcd(a,b)

    case _:   
              print("Invalid input")