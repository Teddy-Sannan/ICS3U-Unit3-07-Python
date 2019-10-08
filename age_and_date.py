#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: October 2019
# This lets the user guess a number


def main():
    while True:
        try:
            age = int(input("Please enter your age: "))

            if age >= 25 and age <= 40:
                print()
                print("You can date my grandchild")

            else:
                print()
                print("You cannot date my grandchild")

        except ValueError:
            print()
            print("Invalid Input")
            print()
            continue

        else:
            break


if __name__ == "__main__":
    main()
