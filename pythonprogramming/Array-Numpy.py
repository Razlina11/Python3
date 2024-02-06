import numpy as np
a=np.array([[1,2],[3,5]])
b=np.array([[2,3],[4,5]])
while True:
    print("Enter 1-9 and See the magic")
    n=int(input("Enter the option number"))
    if not n<1 and not n>8:
        if n==1:
            c=np.add(a,b)
            print("Sum:",c)
        if n==2:
            d=np.subtract(a,b)
            print("Difference:",d)
        if n==3:
            e=np.multiply(a,b)
            print("Multiply:",e)
        if n==4:
            f=np.divide(a,b)
            print("Divide:",f)
        if n==5:
            g=np.dot(a,b)
            print("Dot:",g)
        if n==6:
            h=exp(a)
            i=exp(b)
            print("Exponentiation:",h,i)
        if n==7:
            j=log(a)
            k=log(b)
            print("Logarithm:",j,k)
        if n==8:
            l=log10(a)
            m=log10(b)
            print("Natural Logarithm:",l,m)
    elif n==9:
        break
    else:
        print("Enter 1-9")
