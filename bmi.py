def calculate_bmi(height,weight):
    print("Height = "+str(height))
    print("Weight = "+str(weight))

    bmi=weight/height**2
    print("BMI = ", bmi)
    if bmi < 18.5:
        print("You are under weight")
        return(-1)
    elif bmi <= 25:
        print("You are normal weight")
        return(0)
    else:
        print("You are over weight")
        return(1)

calculate_bmi(weight=57,height=1.73)

