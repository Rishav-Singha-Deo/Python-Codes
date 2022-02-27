def walker(n):
	if n==0:
		return 1
	elif n<0:
		return 0
	else:
		return walker(n-3)+walker(n-2)+walker(n-1)
n=int(input("Enter a distance : "))
print("There are",walker(n),"ways the robot can cross",n,"meters.")