products = []

print("პროდუქტების სია:")

print("1.პროდუქტის დამატება")
print("2.პროდუქტის წაშლა")
print("3.პროდუქტის რაოდენობის გაგება")

choice = input("1,2 თუ 3?: ")

if choice == "1":
    add = input("რას დაამატებთ?: ")
    products.append(add)
    print(products)
elif choice == "2":
    remove = input("რას წაშლით?: ")
    if remove in products:
     products.remove(remove)
    else:
       print("This is not in the list")
elif choice == "3":
    print(len(products))
else:
   print("Invalid choice")


