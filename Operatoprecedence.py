#OperatorPrecednce
Name= input("What's your name.")
Age= input("What's your Age.")

if Name== "Srikara" or Name== "Sreshta":
    print("Hello")
else:
    print("GETTT OUTTTTT")


#DivisibleNumbers
Numerator= int(input("Enter numerator: "))
Denominator= int(input("Enter denominator: "))

if Numerator%Denominator==0:
    print("Numerator is divisble by denominator")
else:
    print("Numerator is NOT divisible by denominator")

#MeanValues
mean1=38

wrong_number=36

correct_number=56

total_number=40

#sum of 40 numbers

sum=mean1*total_number

print("The sum of 40 numbers:",sum)

#correct sum of these numbers

SUM2=sum-(wrong_number)+(correct_number)

print("CORRECTED SUM",SUM2)

#the correct mean

mean2=SUM2/total_number

print(mean2)

#AverageSpeed

A= int(input("Enter value: "))
B= int(input("Enter value: "))
C= int(input("Enter value: "))

Avg= A+B+C/3
print("Avg =", Avg)

if Avg > A and Avg > B and Avg > C:
    print()