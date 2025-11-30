def getMySum(* arg):
    sum=0
    for a in arg:
        sum=sum+a
    return sum


output0=getMySum(1)
print("Sum of One Number :: ",output0)

output1=getMySum(1,2,3)
print("Sum of Three Number :: ",output1)

output2=getMySum(1,2,3,4)
print("Sum of Four Number :: ",output2)

output3=getMySum(1,2,3,4,5)
print("Sum of Five Number :: ",output3)

output4=getMySum()
print("Sum of No Number :: ",output4)