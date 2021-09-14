import random

caracters = ["a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s", "d", "f", "g", "h", "j", "k", "l", "m", "w", "x", "c", "v", "b", "n", "A", "Z", "E", "R", "T", "Y", "U", "I", "O", "P", "Q", "S", "D", "F", "G", "H", "J", "K", "L", "M", "W", "X", "C", "V", "B", "N", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "é", "è", "?", "!", "$", "*"]

def generate_password(amount):
    '''
    This function allows you to randomly generate a password with a chosen number of characters.
    :type:
        amount -> int
    
    :return:
        str
    
    :example:
        generate_password(32)
        >>> VvVOS52DpqQDGn1BUQjB87q5vkiY8NNo
    '''
    assert type(amount) == int, "You must use an integer"
    count = 0
    lstAlt = []
    while count < amount:
        count = count + 1
        lstAlt.append(caracters[random.randrange(len(caracters))])

    if count >= amount:
        strAlt = "".join(lstAlt)

    return strAlt


#     /\ | _ ._  _  _
#    /--\|(_)| |(/__>
