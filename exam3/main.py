
start = input("Boshlash uchun birni bosing: ")

while start == "1":
    num = int(input("Birinchi sonni kiriting: "))
    num2 = int(input("Ikkinchi sonni kiriting: "))
    num3 = input("Amalni kiriting: ")

    if num3 == "+":
         print(num + num2)
         start == 0
    if num3 == "-":
        print(num - num2)  
        start == 0   
    if num3 == "*":
        print(num * num2)
        start == 0
    if num3 == "/":
        print(num / num2)
        start == 0
    start = input("Davom etish uchun birni bosing: ")
    















