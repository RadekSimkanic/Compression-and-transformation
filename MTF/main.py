import time
import cProfile
import pstats

class Stack:
    """
    Only ASCII
    """
    def __init__(self):
        self.stack = range(0, 127)

    def getIndex(self, char):
        if type(char) is not int:
            char = ord(char) # char to int

        virtual_char = 127 - char

        index = self.stack.index(virtual_char)
        del self.stack[index]
        self.stack.append(virtual_char)

        return 127 - index

    def getChar(self, index):
        index = 127 - index

        char = self.stack[index]
        del self.stack[index]
        self.stack.append(char)

        return chr(127 - char)


class MTF:
    def __init__(self, data = ""):
        self.data = data

    def encode(self):
        if type(self.data) is not str:
            raise TypeError, "The initialisation data type must be a string or list"

        s = Stack()
        encoded_list = []
        for char in self.data:
            i = s.getIndex(char)
            encoded_list.append(i)
        return encoded_list


    def decode(self):
        if type(self.data) is not list:
            raise TypeError, "The initialisation data type must be a list"

        s = Stack()
        decoded_list = []
        for i in self.data:
            char = s.getChar(i)
            decoded_list.append(char)
        return "".join(decoded_list)


def demo(expand):
    #s = "aaabbcca"
    s = "The French authorities say they have ended the search for bodies at the site where a Germanwings co-pilot is said to have crashed his aircraft in the French Alps, killing all 150 people on board. Identification of the victims will continue with analysis of the DNA found and debris will carry on being removed. Meanwhile reports said the European Commission took issue with Germany's aviation authority before the crash."
    s *= expand
    print "Length string: %i"%len(s)

    # simple profile
    t1 = time.time()
    mtf = MTF(s)
    encode = mtf.encode()
    print encode

    t2 = time.time()
    mtf = MTF(encode)
    print mtf.decode()
    t3 = time.time()

    print "#1 encoding: %f  decoding: %f complet: %f"%(t2 - t1, t3 - t2, t3 - t1)


if __name__ == "__main__":
    # cprofile

    cProfile.run('demo(5000)', 'profile')
    p = pstats.Stats('profile')
    p.sort_stats('time').print_stats(10)
