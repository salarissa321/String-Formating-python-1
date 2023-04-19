

#------------
#--- Strrings Formating-----
#--------------------

name= "salar"
age= 36
rank = 10


print("My Name is : " + name) # My Name is : salar
print("My Name is : " + name + "and my Age is :" + age) # TypeError: can only concatenate str (not "int") to str

print("My Name is %s" % "salar") # My Name is salar
print("My Name is %s and my Age is : %d" % (name,age) ) #My Name is salar and my Age is : 36
print("My Name is %s and my Age is : %d and my rank is : %f " % (name,age, rank) ) # My Name is salar and my Age is : 36 and my rank is : 10.000000

# %s => String
# %d => Integer
# %f => float

n= "Salar"
l="python"
y=20

print("My Name is %s and i am %s developer with %d Years Exp" % (n,l,y)) # My Name is Salar and i am python developer with 20 Years Exp

# control Floating Point Number
myNumber = 9
print("my Number is: %d" % myNumber) # my Number is: 9
print("my Number is: %f" % myNumber) # my Number is: 9.000000
print("my Number is: %.2f" % myNumber) # my Number is: 9.00

# Truncate String
myLongString ="Hello guys how are you what are you doing now"
print("Message is %.5s" % myLongString) # Message is Hello
