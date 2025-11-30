input_a=10
intput_b=0

try:
    c=input_a/intput_b # Risky
    print(c)
except ZeroDivisionError:
    print("Denominator can not be Zero")