def getMySum(* arg):
    sum=""
    for a in arg:
        sum=sum+a
    return sum


output1=getMySum("One","Two")
print("Sum of Three Number :: ",output1)

output2=getMySum("One","Two","Three")
print("Sum of Three Number :: ",output2)