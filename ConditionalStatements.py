A= 250
B= 225

if (A>B):
    print(A,"is greater than", B)
else:
     print(A,"is less than", B)


#CalculatingProfit
costprice =int(input("enter the cp: "))

sellingprice =int(input("enter the sp: "))

if(sellingprice>costprice):

   print("profit")

   pt=sellingprice-costprice
   print(pt)

else :
   print("HAHHAHAHAHHAHAHAH LOL NO PROFIT")

 

#OddOrEven
Number = input("Enter a number:")

Calulate = Number%2
if Calulate==0:
    print(Number, "is even")
else:
    print(Number, "is odd")