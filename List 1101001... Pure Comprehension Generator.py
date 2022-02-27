l=sum([[1]]+[[0 if j<i-1 else 1 for j in range(i)] for i in range(12)],[])
print(l)