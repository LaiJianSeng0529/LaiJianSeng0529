#Get angle a in triangle
a=int(input("angle a of triangle="))
#Get angle b in triangle
b=int(input("angle b in triangle="))
#Get angle c in triangle
c=int(input("angle c in triangle="))
#Determine the triangle in valid or not
total=a+b+c
#sum of total angle of triangle
print("total angle of triangle=",total)
#triangle is valid
if(total==180):
  print("triangle is valid")
#triangle is invalid  
else:
  print("triangle is invalid")
