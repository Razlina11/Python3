import numpy as np
def funcone():
    x=int(input("Enter the starting point"))
    y=int(input("Ending point:"))
    number=int(input("Enter the number of value to be printed:"))
    return x,y,number
def functwo():
    r=int(input("Enter the number of Rows"))
    c=int(input("Enter the number of columns"))
    return r,c


while True:
    print("1.Create a sequence with linspace function\n2.Create a n-dimensional array using Random Function\n3.Create a n-dimensional Arrays of Zeroes\n4.Create a n-dimensional Array of ones\n5.Create a n-dimensional Array using fill function\n6.exit")
    n=int(input("Enter your Choice:"))
    if not n<1 and n>5:
        if n==1:
            x,y,number=funcone()
            l=np.linspace(x,y,number)
            print("Generated Sequence",l)
        if n==2:
            r,c=functwo()
            r=np.random.random((r,c))
            print("Random Sequence:",r)
        if n==3:
            r,c=functwo()
            z=np.zeros((r,c),dtype='int')
            print("Zero array",z)
        if n==4:
            r,c=functwo()
            o=np.ones((r,c),dtype='int')
            print("One-D Array",o)
        if n==5:
            r,c=functwo()
            s=np.full((r,c),6)
            print("Scalar Matrix",s)
    elif n==6:
        break
    else:
        print("Please enter 1-6")
