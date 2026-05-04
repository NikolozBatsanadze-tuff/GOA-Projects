points = int(input("How many points do you have?: "))

if points >=90:
    print("You got a A")
elif points >= 80  and points<90:
    print("you got a B")
elif points < 80 and points >=70:
    print("You got a C")
elif points < 70:
    print("You got a C-")