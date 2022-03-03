#!/usr/bin/env python3

# Created by Devin Jhu
# Created on March 2022
# The curcumference calculator

import constants


def main():
    # this function calculates curcumference

    # input
    radius = int(input("enter radius (mm): "))

    # process
    circumference = constants.TAU * radius

    # output
    print("circumference is {} mm².".format(circumference))
    print("\nDone")


if __name__ == "__main__":
    main()
