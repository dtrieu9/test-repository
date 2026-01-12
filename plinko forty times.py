import random

def plinko(iterations):
    

    green = 0
    pink = 0
    yellow = 0
    purple = 0


    for i in range(iterations):
        path = ""
        value = 0
        for j in range(1, 10):
            num = random.randint(1, 2)
            if num == 1:
                bounce = "left, "
                value = value - 1
            elif num == 2:
                bounce = "right, "
                value = value + 1
            path += bounce
            
        if value < -6:
            green += 1
            print(path)
            print("Your path leads to the green bin!")
        elif value < 0:
            pink += 1
            print(path)
            print("Your path leads to the green bin!")
        elif value < 6:
            yellow += 1
            print(path)
            print("Your path leads to the green bin!")
        else:
            purple += 1
            print(path)
            print("Your path leads to the green bin!")

    print('\nResults:\nGreen:', green, '\nPink:', pink,'\nYellow:', yellow, '\nPurple:', purple)
    
    return




plinko(40)

