age = int(input("Please enter your age: "))
card = input("Do you have a student card:").lower()

if card == "yes" or age < 18:
    print("დანაზოგი გაქ!")
elif age >= 60 and card == "No":
    print("პენსიონერის ფასდაკლება გაქვთ!")
else:
    print("ფასდაკლება არ გეკუთვნის")





6