a=34
b=20
c=15
d=17
e=18
f=21
sum_odd=0
sum_even=0
if a % 2 ==0:
	sum_even=sum_even+a
else:
	sum_odd=sum_odd+a
if b % 2 ==0:
	sum_even=sum_even+b
else:
	sum_odd=sum_odd+b
if c % 2 ==0:
	sum_even=sum_even+c
else:
	sum_odd=sum_odd+c
if d % 2 ==0:
	sum_even=sum_even+d
else:
	sum_odd=sum_odd+d
if e % 2 ==0:
	sum_even=sum_even+e
else:
	sum_odd=sum_odd+e
if f % 2 ==0:
	sum_even=sum_even+f
else:
	sum_odd=sum_odd+f
print("sum of even",sum_even)
print("sum of odd",sum_odd)