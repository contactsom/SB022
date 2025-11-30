def getMyDivision(a,b):
    c=0
    try:
        print("Statement-1")
        c=a/b
        print("Statement-2")
    except:
        print("Statement-3")
        print("Error Occured")
        print("Statement-4")
    return c

#output1=getMyDivision(a=10,b=2)
#print(output1)

output2=getMyDivision(a=10,b=0)
print(output2)