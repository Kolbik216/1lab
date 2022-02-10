import cmath

a=float(input("Число a "))
b=float(input("Число b "))
c=float(input("Число c "))

print("Наше уравнение имеет вид: ",f"{a}*x^2+{b}*x+{c}")
disc = (b**2) - (4*a*c)
if disc>0 :
	x1 = (-b-cmath.sqrt(disc))/(2*a)
	x2 = (-b+cmath.sqrt(disc))/(2*a)
	print("x1=",x1,"\nx2=",x2)
elif disc == 0 :
	x1= -b/(2*a)
	print("Ответ x=",x1)
else:
	print("Корней нет")
