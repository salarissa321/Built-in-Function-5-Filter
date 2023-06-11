


#-------------------------------------------------
#-------- Built in Function 5 => Filter ------
#-------------------------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function on Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Funtion
# [4] Filter Out All Elements For Which The Function Return True
# [5] The function Need To Return Boolean Value
#--------------------------

# Example 1


def checkNumber(num) :
    if num > 10 :
        return num
    
myNumbers = [1,19,10,20,100,5]

myResult = filter(checkNumber ,myNumbers )

for number in myResult :
    print(number) # 19 , 20 , 100

print("#" * 50) # ##################################################

# Example 2


def checkName(name) :
    return name.startswith("O")
    
myTexts = ["Salar" , "Raman" , "Gamel" , "Shergo" , "Osman" , "Omar"]

myReturnedDate = filter(checkName , myTexts )

for person in myReturnedDate :
    print(person) # Osman , Omar

print("#" * 50) # ##################################################

# Example 3


# def checkName(name) :
#     return name.startswith("O")

# one way
    
myNames = ["Salar" , "Raman" , "Gamel" , "Shergo" , "Osman" , "Omar" , "Ahmad" , "Anas"]

myReturnedNames = filter(lambda name : name.startswith("A") , myNames )

for p in myReturnedNames :
    print(p) # Ahmad , Anas

print("#" * 50) # ##################################################

# second way

# def checkName(name) :
#     return name.startswith("O")

myNames = ["Salar" , "Raman" , "Gamel" , "Shergo" , "Osman" , "Omar" , "Ahmad" , "Anas"]


for p in filter(lambda name : name.startswith("A") , myNames ) :
    print(p) # Ahmad , Anas




