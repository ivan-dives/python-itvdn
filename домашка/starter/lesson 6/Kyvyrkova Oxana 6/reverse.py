

str = input("Enter any text here: _  ")


while str != ''.join(reversed(str)):
   print("Try again _ ")
   str1 = input()
   if str1 == ''.join(reversed(str1)):
       print("It is polindrom")
       break



if str == ''.join(reversed(str)):
    print("It is polindrom")
#
# sliced method


text = input("Enter any text here: _  ")


while text != text[::-1]:
   print("Try again _ ")
   str1 = input()
   if str1 == str1[::-1]:
       print("It is polindrom")
       break
if text == text[::-1]:
    print("It is polindrom")

