unit=int(input("Enter unit: "))
if(unit<=50):
    cost=unit*0.5
elif(unit>50 and unit<101):
    cost=50*0.5+(unit-50)*1
elif(unit>100 and unit<251):
    cost=50*0.5+100*1+(unit-100)*1.5
elif(unit>250 and unit<501):
    cost=50*0.5+100*1+250*1.5+(unit-250)*2
else:
    cost=50*0.5+100*1+250*1.5+500*2+(unit-500)*3
print("Bill amount is ",cost)
