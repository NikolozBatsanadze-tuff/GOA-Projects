age = int(input("whats your age?: "))
heart_beat = int(input("whats your heart beat?: "))

if age < 30 and heart_beat < 140:
    print("you can workout more")
elif age >= 30 and heart_beat > 170:
    print("you need to rest")
else:
    print("heart beat is normal")    



