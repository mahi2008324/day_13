a=int(input("Enter the number : "))
sum_even=0
sum_odd=0
for i in range(a+1):
	if i % 2 == 0:
	   sum_even=sum_even+i
	if i % 2 != 0:
 	   sum_odd=sum_odd+i
	
print("sum of even numbers upto {} is : {}".format(a,sum_even))
print("sum of even numbers upto {} is : {}".format(a,sum_odd))