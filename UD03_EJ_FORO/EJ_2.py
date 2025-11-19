altura = int(input("Introduce la altura de la figura: "))
print("4")
for i in range(1, altura-1):
    print("4",end="")
    print(" "*(i-1),end="")
    print("4")
    
# Base figura
print("4"*altura)