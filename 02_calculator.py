num1 =float(input("enter a number : "))

while True: 
    
    para=input("press (+,-,*,/) or press q to quit : ")
    if para=="q":
        result=num1
        print("final result=",result)
        break
    num2=float(input("enter another number : "))
    if para =="+" :
        #num2=0
        result=num1+num2
        print("result=",result)

        
    elif para =="-" :
        #num2=0
        result=num1-num2
        print("result=",result)

    elif para =="*" :
        #num2=1
        result=num1*num2
        print("result=",result)

    elif para =="/" :
        #num2=1
        result=num1/num2
        print("result=",result)

    else:
        print("printing mistake")
        continue
    num1=result
#print("result=",result)
