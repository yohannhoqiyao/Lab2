

def display_main_menu():
    print("Enter some numbers seperated by commas (e.g. 5, 67, 32)")

def get_user_input():
    stringuser = input()
    spli = stringuser.split(",")
    for i in range(len(spli)):
        spli[i] = float(spli[i])
    return spli

def calc_average_temperature(splist):
    return sum(splist)/len(splist)

def calc_min_max_temperature(splist):
    return min(splist), max(splist)
    

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    x = get_user_input()
    print(x)
    print(calc_average_temperature(x))
    print(calc_min_max_temperature(x))


if __name__ == "__main__":
    main()