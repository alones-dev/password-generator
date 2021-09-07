import random

caracters = ["a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s", "d", "f", "g", "h", "j", "k", "l", "m", "w", "x", "c", "v", "b", "n", "A", "Z", "E", "R", "T", "Y", "U", "I", "O", "P", "Q", "S", "D", "F", "G", "H", "J", "K", "L", "M", "W", "X", "C", "V", "B", "N", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def generate_password(amount):
    count = 0
    lstAlt = []
    while count < amount:
        count = count + 1
        lstAlt.append(caracters[random.randrange(len(caracters))])

    if count >= amount:
        strAlt = "".join(lstAlt)

    return strAlt

print(generate_password(32))


#     /\ | _ ._  _  _
#    /--\|(_)| |(/__>