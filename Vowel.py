sent = str(input("enter the sentence por favor "))
string = sent.lower()
print (string)
counter = 0
list = ["a","e","i","o","u"]
for char in string:
    if char in list:
        counter = counter + 1
print("vowels = ", counter) 