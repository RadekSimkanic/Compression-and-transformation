import time
import cProfile
import pstats
import math

# https://en.wikipedia.org/wiki/Discrete_cosine_transform

# 1D
class DCT:
    def __init__(self, data = ""):
        self.data = data

    def encodeDct1(self, integers_output = True):
        if type(self.data) is not list:
            raise TypeError, "The initialisation data type must be a list"

        if len(self.data) < 2:
            raise TypeError, "The list must contains minimal 2 items."

        encoded_list = []

        N = len(self.data)

        for k in xrange(0, N):
            c = 0
            for n in xrange(1, N - 1):
                c += self.data[n] * math.cos((math.pi / (N - 1)) * k * n )
            c += 0.5 * (self.data[0] + (-1)**k * self.data[N - 1])
            if integers_output:
                encoded_list.append(int(round(c, 0)))
            else:
                encoded_list.append(c)

        return encoded_list


    def decodeDct1(self, integers_output = True):
        if type(self.data) is not list:
            raise TypeError, "The initialisation data type must be a list"

        N = len(self.data)
        if integers_output:
            f = lambda x: int(round(x * 2.0 / (N-1), 0))
        else:
            f = lambda x: x * 2.0 / (N-1)

        return map(f, self.encodeDct1(False))

    def encodeDct2(self, integers_output = True):
        if type(self.data) is not list:
            raise TypeError, "The initialisation data type must be a list"

        encoded_list = []

        N = len(self.data)

        for k in xrange(0, N):
            c = 0
            for n in xrange(0, N):
                c += self.data[n] * math.cos((math.pi / N) * k * (n + 0.5) )
            if integers_output:
                encoded_list.append(int(round(c, 0)))
            else:
                encoded_list.append(c)

        return encoded_list


    def decodeDct2(self, integers_output = True):
        if type(self.data) is not list:
            raise TypeError, "The initialisation data type must be a list"

        N = len(self.data)
        if integers_output:
            f = lambda x: int(round(x * 2.0 / N, 0))
        else:
            f = lambda x: x * 2.0 / N

        return map(f, self.encodeDct3(False))

    def encodeDct3(self, integers_output = True):
        if type(self.data) is not list:
            raise TypeError, "The initialisation data type must be a list"

        decoded_list = []
        N = len(self.data)
        for k in xrange(0, N):
            c = 0
            for n in xrange(1, N):
                c += self.data[n] * math.cos((math.pi / N) * n * (k + 0.5) )
            c += 0.5 * self.data[0]
            if integers_output:
                decoded_list.append(int(round(c, 0)))
            else:
                decoded_list.append(c)

        return decoded_list

    def decodeDct3(self, integers_output = True):
        if type(self.data) is not list:
            raise TypeError, "The initialisation data type must be a list"

        N = len(self.data)

        if integers_output:
            f = lambda x: int(round(x * 2.0 / N, 0))
        else:
            f = lambda x: x * 2.0 / N

        return map(f, self.encodeDct2(False))


    def encodeDct4(self, integers_output = True):
        if type(self.data) is not list:
            raise TypeError, "The initialisation data type must be a list"

        decoded_list = []
        N = len(self.data)
        for k in xrange(0, N):
            c = 0
            for n in xrange(0, N):
                c += self.data[n] * math.cos((math.pi / N) * (n + 0.5) * (k + 0.5) )
            if integers_output:
                decoded_list.append(int(round(c, 0)))
            else:
                decoded_list.append(c)

        return decoded_list

    def decodeDct4(self, integers_output = True):
        if type(self.data) is not list:
            raise TypeError, "The initialisation data type must be a list"

        N = len(self.data)


        if integers_output:
            f = lambda x: int(round(x * 2.0 / N, 0))
        else:
            f = lambda x: x * 2.0 / N

        return map(f, self.encodeDct4(False))


    def encode(self):
        return self.encodeDct2()

    def decode(self):
        return self.decodeDct2()



def demo(expand):
    d = [1, 2, 34, 56, 8, 87, 68, 78, 7, 43, 2, 32, 4]

    print "Length list: %i"%len(d)
    print  d
    # simple profile
    t1 = time.time()
    dct = DCT(d)
    encode = dct.encodeDct2(False)
    print encode

    t2 = time.time()
    dct = DCT(encode)
    print dct.decodeDct2()
    t3 = time.time()

    print "#1 encoding: %f  decoding: %f complet: %f"%(t2 - t1, t3 - t2, t3 - t1)


if __name__ == "__main__":
    # cprofile

    cProfile.run('demo(5000)', 'profile')
    p = pstats.Stats('profile')
    p.sort_stats('time').print_stats(10)
