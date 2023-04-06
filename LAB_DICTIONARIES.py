
phone_book = {"Amal":"0568323222" ,"Mohammed":"0522222232","Khadijah":"0532335983","Abdullah":"0545341144",
"Rawan":"0545534556","Faisal":"0560664566","Layla":"0567917077"}

phone_number = input ("What is the phone number? ")
if not phone_number.isdigit ():
    print ("This is invalid number, use only numbers.") 
elif len (phone_number) < 10 or len (phone_number) > 10:
    print ("This is invalid number")
elif not phone_number in phone_book:
    print ("Sorry, the number is not found") 
else:
    print ("the owner of the number is: ", phone_book [phone_number])


a = [5, 0, 34, 9, 0, 13, 8]
temp = []
zeros = []

for i in range(len(a)):
    if a[i] !=0:
        temp.append(a[i])
    else:
        zeros.append(a[i])
sorted(a, key=lambda x: not x)
print(temp+zeros)
