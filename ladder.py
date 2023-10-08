def my_steps(n):
    #N has to be greater than or equal to 1, and less than or equal to 25
    if n<1 or n>25:
        raise ValueError("N is not in the range from 1 to 25")

    upOne=1
    upTwo=1

    for(i) in range (n-1):
        temp = upOne
        upOne=  upOne + upTwo
        upTwo = temp

    return upOne