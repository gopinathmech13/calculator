num1 =float(input("enter a number : "))

while True: 
    
    para=input("press (+,-,*,/) or press q to quit : ")
    if para!="q" and para!="+" and para!="-" and para!="*" and para!="/":
        print("Invalid input, please try again !!")
        continue

    elif para=="q":
        result=num1
        print("final result = ",result)
        break 
    num2=float(input("enter another number : "))
    if para =="+" :
        #num2=0
        result=num1+num2
        print("result so far = ",result)

        
    elif para =="-" :
        #num2=0
        result=num1-num2
        print("result so far =",result)

    elif para =="*" :
        #num2=1
        result=num1*num2
        print("result so far = ",result)

    elif para =="/" :
        #num2=1
        result=num1/num2
        print("result so far = ",result)

    elif para=="q":
        print("final result = ",result)
        break
    num1=result

