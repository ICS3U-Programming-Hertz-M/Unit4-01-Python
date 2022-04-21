#!/usr/bin/env python3

# Created by: Hertz Antonella
# Created on: Arp-19-2022
# This program uses a while loop and ask
# the user how many times they want the program to loop.


def main():
    # this function uses a while loop
    loop_sum = 0
    loop_num = 0
    # Ask the user to enter how many times to repeat
    user_num = input(" Enter how many times to repeat: ")
    print("")
    # check if the user num is a integer
    # calculate the sum from 0 to the user number
    try:
        user_num_as_int = int(user_num)

        if user_num_as_int > 0:

            while loop_num < user_num_as_int:
                loop_num = loop_num + 1
                print("{} time through loop.".format(loop_num))
                loop_sum = loop_sum + loop_num
            print("The sum of the number 0-{} is {}".
                  format(user_num, loop_sum))
        else:
            print("please enter a positive number")
    except Exception:
        print("invalid input")


if __name__ == "__main__":
    main()
