#input- ნიშნავს მომხმარებლისგან მონაცემის მიღებას(პროგრამა გისვამს კითხვას და შენ პასუხობ)
#გამოკლება - რიცხვებს ერთმანეთს აკლებს
#მიმატება + რიცხვებს ერთმანეთს უმატებს
#გამრავლება * რიცხვებს ერთმანეთთან ამრავლებს
#გაყოფა(ათწილადად) / რიცხვებს ერთმანეთთან ყოფს
#მთელი გაყოფა // რიცხვებს ერთმანეთთან მთელ რიცხვად ყოფს
#ნაშთი % რიცხვებს ერთმანეთთან ყოფს და ნაშთს გვიბრუნებს
#ხარისხი ** რიცხვები ერთმანეთთან ხარისხში აჰყავს
#backend - პროგრამის ნაწილი რომელიც მომხმარებლი ვერ ხედავს.(იგივე სერვერია)
#frontend - პროგრამის ნაწილი რომელსაც მომხმარებლი ხედავს.(ანუ ვიზუალური ნაწილი)

name = input("hello, What is your name? ")
surname = input("your last name? ")
age = input("your age? ")
favorite_number = input("your favorite number? ")
print(name)
print(surname)
print(age)
print(favorite_number)


num1 = input("first number: ")
num2 = input("second number: ")
addition = int(num1) + int(num2)
subsctraction = int(num1) - int(num2)
multiply = int(num1) * int(num2)
divide = int(num1) / int(num2)
ნაშთი = int(num1) % int(num2)
divide2 = int(num1) // int(num2)
power = int(num1) ** int(num2)
print(addition)
print(subsctraction)
print(multiply)
print(divide)
print(ნაშთი)
print(divide2)
print(power)
