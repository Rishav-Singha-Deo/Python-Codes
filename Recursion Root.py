def sqroot(l,u,n):
    if l<=u:
        m=(l+u)//2
        if m**2<=n and (m+1)**2>n:
            return m
        elif m**2<n:
            return sqroot(m+1,u,n)
        else:
            return sqroot(l,m-1,n)
    return l
n=int(input("Enter a number : "))
print("The square root is :",sqroot(0,n,n))