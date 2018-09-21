#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 14, 2018 5:03:01 PM$"

def spam1():

    def spam2():

        def spam3():
            z = " even" + y
            print("In spam3, locals are {}".format(locals())) # nonlocals are added to local scope automatically; cannot update without declaring with nonlocal keyword
            return z

        y = " more " + x # y must exist before spam3 is called
        y += spam3()
        print("In spam2, locals are {}".format(locals()))
        return y

    x = "spam" # x must exist before spam2 is called
    x += spam2()
    print("In spam1, locals are {}".format(locals()))
    return x

print(spam1())