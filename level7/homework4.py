list = [10 , 10.0 , "String" , True]
print(list)

choice = input("Which one do you want to remove?: ")

if choice == "10":
    list.remove(10)
    print(list)
elif choice == "10.0":
    list.remove(10.0)
    print(list)
elif choice == "String":
    list.remove("String")
    print(list)
elif choice == "True":
    list.remove(True)
    print(list)
else:
    print("Invalid Choice")
