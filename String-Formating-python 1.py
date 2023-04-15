

#------------
#--- Strrings Formating-----
#--------------------

name= "salar"
age= 36
rank = 10


print("My Name is : " + name)
# print("My Name is : " + name + "and my Age is :" + age)

print("My Name is %s" % "salar")
print("My Name is %s and my Age is : %d" % (name,age) )
print("My Name is %s and my Age is : %d and my rank is : %f " % (name,age, rank) )

# %s => String
# %d => Integer
# %f => float

n= "Salar"
l="python"
y=20

print("My Name is %s and i am %s developer with %d Years Exp" % (n,l,y))

# control Floating Point Number
myNumber = 9
print("my Number is: %d" % myNumber)
print("my Number is: %f" % myNumber)
print("my Number is: %.2f" % myNumber)

# Truncate String
myLongString ="Hello guys how are you what are you doing now"
print("Message is %.5s" % myLongString)
