def getMyDivision(a,b):
    c=0
    try:
        c=a/b
    except:
        print("Error Occured")
    return c


output1=getMyDivision(a=10,b=2)
print(output1)

output2=getMyDivision(a=10,b=0)
print(output2)