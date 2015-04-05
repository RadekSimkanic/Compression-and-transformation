import time
import cProfile
import pstats

class RLE:
    def __init__(self, data = ""):
        self.data = data

    def compress(self):
        if type(self.data) is not str:
            raise TypeError, "The initialisation data type must be a string"

        compressed_data = []

        tmp_char = None
        count = 0
        for char in self.data:
            if tmp_char is None:
                tmp_char = char
                count = 1
                continue
            if tmp_char == char:
                count += 1
            else:
                compressed_data.append((tmp_char, count))
                count = 1
                tmp_char = char
        compressed_data.append((tmp_char, count))


        return compressed_data


    def decompress(self):
        if type(self.data) is not list:
            raise TypeError, "The initialisation data type must be a list, not %s"%str(type(self.data))

        decoded_list = []
        for item in self.data:
            decoded_list.append(str(item[0]) * item[1])
        return "".join(decoded_list)


def demo(expand):
    s = "aaabbcca"
    s *= expand
    print "Length string: %i"%len(s)

    # simple profile
    t1 = time.time()
    rle = RLE(s)
    compress = rle.compress()
    print compress

    t2 = time.time()
    rle = RLE(compress)
    print rle.decompress()
    t3 = time.time()

    print "#1 encoding: %f  decoding: %f complet: %f"%(t2 - t1, t3 - t2, t3 - t1)


if __name__ == "__main__":
    # cprofile

    cProfile.run('demo(5000)', 'profile')
    p = pstats.Stats('profile')
    p.sort_stats('time').print_stats(10)
