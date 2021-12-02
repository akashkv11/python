n=int(input("Enter the number:"))
f=0
i=2
while(i<=n/2):
    if(n%i==0):
        f=f+1
    i=i+1
    
if(f!=0):
    print("Number is not prime")
elif(f==0):
    print("Number is  prime")
    
    
        
    
