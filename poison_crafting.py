def poison():



    # Find original market value
    mvalue = input("What is the market value of the poison \n Value in GP: ")

    # Convert string to int

    mvalue = int(mvalue)

    # change market value to crafting value

    cvalue = .3333333 * mvalue

    difficulty_check = input("What is the DC you would like to use? (base is DC for poison) \n You can voluntarily increase the DC to increase the speed at which you craft \n DC: ")

    difficulty_check = int(difficulty_check)

    roll = input("What did you roll? \n ")

    roll = int(roll)


    top = roll * difficulty_check
    bottom = 10 * cvalue

    number_completed_week = top / bottom
    number_completed_day = number_completed_week / 7

    print(f"You have completed {number_completed_week} of your item this week")
    print(f"You have completed {number_completed_day} of your item today")

    user_continue = input("Would you like to run this again? Y/N\n")
    user_continue = user_continue.upper()
    if (user_continue == 'Y'):
        poison()
    if (user_continue != 'Y'):
        exit
    # print("mvalue: " + str(mvalue))
    # print("cvalue: " + str(cvalue))
    # print("difficulty_check: " + str(difficulty_check))
    # print("roll: " + str(roll))

#while True:
poison()