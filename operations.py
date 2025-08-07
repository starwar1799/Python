#Doing operations
tree1=5
tree2=4
tree3=3
tree4=2
tree5=1
addition=tree1+tree2+tree3+tree4+tree5
average=addition/5

Percentage=average*10
print("The sum of all 5 trees is...", addition)
print("The average of all 5 trees is...", average)

print("The perceentage of all 5 trees is...", Percentage )
#Taking total amount as user input
Amount= int(input("Enter desired withdrawal amount."))
Note_1=Amount//100
Note_2=(Amount%100)//50
Note_3=((Amount%100)%50)//10

print("Notes of 100 Rupees", Note_1)
print("Notes of 50 Rupees", Note_2)
print("Notes of 10 Rupees", Note_3)

#