import os

# this is not a good way to do this
def swap(a,b):
    aName = os.join("pong",f"img{a}.png")
    bName = os.join("pong",f"img{b}.png")
    tempName = os.join("pong","temp.png")

    os.rename(aName,tempName)
    os.rename(bName, aName)
    os.rename(tempName, bName)


    