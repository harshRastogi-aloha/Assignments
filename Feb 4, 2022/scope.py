

PI = 3.14 #Global Variable
r = 5 #Global variable

#Calculating Area of circle
def areacircle(r):
	area = PI *r*r
	return area

def areaSmallCircle(R):
	global r #We have to use 'global' keyword to modify the value of Globally defined variable.
	r= R
	area = PI*R*R   #variable "area" has only function level scope or local scope. So we can declare it here too.
	return area    

def paracircle(r):
	parameter = 2*PI*r
	return parameter

areaCircle = areacircle(r) #passing Radius as parameter
parameterCircle = paracircle(r)
AreaCircle = areaSmallCircle(3)


print("Area of Circle is:",areaCircle, "\n"+ "Parameter of circle is: ",parameterCircle)

print("Area of Smaller Circle is: ",AreaCircle)







