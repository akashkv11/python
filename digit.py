n = int(input('Enter n : '))
sum=0
while(n>0):
	sum=int(sum+n%10)
	n=n/10
print(sum)

