#!/usr/bin/env python3

## @package doxygit
# This is an example package demonstrating Doxygen
#
# Written for the CS tutorial
#
# @author Jens Dede <jd@comnets.uni-bremen.de>
# @date 2018-05-25 Initial commit
#
# @copyright GNU General Public License v3.0

from human import Human

## A class representing a teacher derived from the human class
class Teacher(Human):

    ## The default constructor
    # @param age    Age of the teacher
    # @param name   The name of the teacher
    def __init__(self, age=0, name=None):
        Human.__init__(self, age, name)

if __name__ == "__main__":
    print("Testing", __file__)
    t = Teacher()
    print(t)
