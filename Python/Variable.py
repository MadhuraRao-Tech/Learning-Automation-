name=input("Enter your  Name:--")
age= input("Enter  your Age:--")
# print(age.isdigit())
if age.isdigit():
    if int(age)>=18: #Adult scenario
        print(f"hey {name} you  are  adult")
    else: #minor scenario
        print(f"opps {name} you are not adult")
else: #invalide input
    print("Dont  make  fun !! add  proper age :)")