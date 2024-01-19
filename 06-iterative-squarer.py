proceed = True

while proceed == True:
    num = int(input ("Enter a number: "))
    if num == 0:
        proceed = False
    
    elif num > 0:
        result = num * num
        print (result)
