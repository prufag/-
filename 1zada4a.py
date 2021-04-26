a=int(input())
i=0
b=1
while i<a:
	i=i+1
	if b==1:
		print("I hate ",end="")
		if i==a:
			print("it ",end="")
		else:
			print("that ",end="")
		b=0
		continue
	if b==0:
		print("I love ",end="")
		if i==a:
			print("it ",end="")
		else:
			print("that ",end="")
		b=1
		continue
