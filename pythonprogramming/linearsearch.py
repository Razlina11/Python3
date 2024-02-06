def linearsearch(list,ele):
    for i in range(len(list)):
        if(list[i]==ele):
            print("Element at the position",i)
            i+=1
            return
a=[2,3,4,5,6]
linearsearch(a,2)
