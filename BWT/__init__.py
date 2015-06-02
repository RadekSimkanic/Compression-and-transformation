import time
import cProfile
import pstats



class RotationString:
    def __init__(self, str, position):
        self.position = 0
        self.begin_position = position
        self.length = len(str)
        self.str = str

        if self.length <= position:
            raise IndexError, "The start index (%d) is out of range."%self.begin_position

    def __iter__(self):
        return self

    def next(self):
        if self.position >= self.length:
            self.position = 0
            raise StopIteration

        i = self.position + self.begin_position
        if i >= self.length:
            i -= self.length

        self.position += 1
        return self.str[i]

    def __str__(self):
        #return  "".join(self) # very slow
        return "".join((self.str[ self.begin_position : ], self.str[ : self.begin_position]))

    def __getitem__(self, key):
        if key >= self.length:
            raise IndexError, "The index (%d) is out of range."%key

        i = key + self.begin_position
        if i >= self.length:
            i -= self.length

        return self.str[i]

    def __lt__(self, other):
        first_str = str(self)
        second_str = str(other)
        return first_str < second_str

    def __cmp__(self, other):# not required
        if self < other:
            return self
        return other

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, str(self))

    def getLastChar(self):
        if self.length <= 1:
            return self.str

        if self.begin_position == 0:
            return self.str[ self.length - 1 ]

        if self.begin_position >= self.length - 1:
            return self.str[ self.length - 2 ]

        return self.str[ self.begin_position - 1 ]

    def getPosition(self):
        return self.begin_position

class ListRotationString:
    def __init__(self, str):
        self.position = 0
        self.length = len(str)
        self.str = str

    def __iter__(self):
        return self

    def next(self):
        if self.position == self.length:
            raise StopIteration
        else:
            s = RotationString(self.str, self.position)
            self.position += 1
            #return str(s)
            return s

class Indexer:
    def __init__(self, l):
        self.list = l
        self.jumper = []#linker(l, False, True)

        self.linker()

    def getPosition(self, item, count):
        #if item not in self.list: # make slower code
        #    raise IndexError, "The index (%s) is not exist."%item

        i = self.list.index(item)

        for counter in xrange(1, len(self.list)):
            if count == counter:
                return i
            i = self.jumper[i]


    def linker(self):
        self.jumper = [-1] * len(self.list)
        positions = {}
        i = 0
        for char in self.list:
            if char in positions:
                tmp_position = positions[char]
                self.jumper[tmp_position] = i
            positions[char] = i
            i += 1

class BWT:
    def __init__(self, str):
        if type(str) != type(""):
            raise TypeError, "The type must be a string"
        self.str = str

    def encode(self):
        vectors_of_string = ListRotationString(self.str) # for using less memory
        sorted_vectors = sorted(vectors_of_string)

        synchronization_index = 0
        for vector in sorted_vectors:
            if vector.getPosition() == 0:
                break
            synchronization_index += 1

        encode_string = "".join(map(lambda x: x.getLastChar(), sorted_vectors))
        return (synchronization_index, encode_string )

    def decode(self, synchronization_index):
        sorted_str = sorted(self.str)
        encoded_str = list(self.str)
        decoded_data = []

        #counter = linker(encoded_str, True, False)
        counter = self.counter(encoded_str)
        indexer = Indexer(sorted_str)

        char = encoded_str[synchronization_index]
        decoded_data.append(char)
        count = counter[synchronization_index]

        for i in xrange(0, len(self.str)-1):
            index = indexer.getPosition(char, count)
            char = encoded_str[index]
            count = counter[index]
            decoded_data.append(char)

        decoded_data = "".join( reversed(decoded_data) )

        return decoded_data

    def counter(self, lst):
        tmp_counter = {}
        count = []
        for char in lst:
            c = tmp_counter.get(char, 0) + 1
            tmp_counter[char] = c
            count.append(c)
        return count

################################################# Own alphabet #########################################################


class RotationList:
    def __init__(self, list_of_data, position):
        self.position = 0
        self.begin_position = position
        self.length = len(list_of_data)
        self.list_of_data = list_of_data

        if self.length <= position:
            raise IndexError, "The start index (%d) is out of range."%self.begin_position

    def __iter__(self):
        return self

    def next(self):
        if self.position >= self.length:
            self.position = 0
            raise StopIteration

        i = self.position + self.begin_position
        if i >= self.length:
            i -= self.length

        self.position += 1
        return self.list_of_data[i]

    def __getitem__(self, key):
        if key >= self.length:
            raise IndexError, "The index (%d) is out of range."%key

        i = key + self.begin_position
        if i >= self.length:
            i -= self.length

        return self.list_of_data[i]

    def __lt__(self, other):
        return list(self) < list(other)


    def __cmp__(self, other):# not required
        if list(self) < list(other):
            return self
        return other

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, str(self))

    def getLastItem(self):
        if self.length <= 1:
            return self.list_of_data

        if self.begin_position == 0:
            return self.list_of_data[ self.length - 1 ]

        if self.begin_position >= self.length - 1:
            return self.list_of_data[ self.length - 2 ]

        return self.list_of_data[ self.begin_position - 1 ]

    def getPosition(self):
        return self.begin_position

class ListRotation:
    def __init__(self, data):
        self.position = 0
        self.length = len(data)
        self.list = data

    def __iter__(self):
        return self

    def next(self):
        if self.position == self.length:
            raise StopIteration
        else:
            s = RotationList(self.list, self.position)
            self.position += 1
            return s

class BWTOwnAlphabet:
    def __init__(self, inline_list_of_data, own_alphabet, is_transformed_number_data = False):
        if isinstance(inline_list_of_data, list) and isinstance(inline_list_of_data, tuple):
            print str(type(inline_list_of_data))
            raise TypeError, "The type must be a list or tuple"
        if isinstance(own_alphabet, list) and isinstance(own_alphabet, tuple):
            raise TypeError, "The type must be a list or tuple"

        self.alphabet = own_alphabet

        if is_transformed_number_data:
            self.inline_number_list_of_data = inline_list_of_data
        else:
            self.data = inline_list_of_data
            self.inline_number_list_of_data = self._transformDataToNumbers()

    def _transformDataToNumbers(self):
        inline_number_list_of_data = map(
            lambda x: self.alphabet.index(x),
            self.data
        )

        return inline_number_list_of_data

    def _transformDataFromNumbers(self, inline_number_list_of_data):
        inline_data = map(
            lambda x: self.alphabet[x],
            inline_number_list_of_data
        )

        return inline_data

    def encode(self, numbers_output = False):
        vectors_of_data = ListRotation(self.inline_number_list_of_data) # for using less memory
        sorted_vectors = sorted(vectors_of_data)

        synchronization_index = 0
        for vector in sorted_vectors:
            if vector.getPosition() == 0:
                break
            synchronization_index += 1

        encode_data = map(lambda x: x.getLastItem(), sorted_vectors)

        if numbers_output is False:
            encode_data = self._transformDataFromNumbers(encode_data)

        return (synchronization_index, encode_data )

    def decode(self, synchronization_index, numbers_output = False):
        sorted_data = sorted(self.inline_number_list_of_data)
        encoded_data = list(self.inline_number_list_of_data)
        decoded_data = []

        counter = self.counter(encoded_data)
        indexer = Indexer(sorted_data)

        char = encoded_data[synchronization_index]
        decoded_data.append(char)
        count = counter[synchronization_index]

        for i in xrange(0, len(self.inline_number_list_of_data)-1):
            index = indexer.getPosition(char, count)
            char = encoded_data[index]
            count = counter[index]
            decoded_data.append(char)

        decoded_data = reversed(decoded_data)

        if numbers_output is False:
            decoded_data = self._transformDataFromNumbers(decoded_data)

        return decoded_data

    def counter(self, lst):
        tmp_counter = {}
        count = []
        for char in lst:
            c = tmp_counter.get(char, 0) + 1
            tmp_counter[char] = c
            count.append(c)
        return count

def demo(expand):
    s = "The French authorities say they have ended the search for bodies at the site where a Germanwings co-pilot is said to have crashed his aircraft in the French Alps, killing all 150 people on board. Identification of the victims will continue with analysis of the DNA found and debris will carry on being removed. Meanwhile reports said the European Commission took issue with Germany's aviation authority before the crash."
    s *= expand
    print "Length string: %i"%len(s)

    # simple profile
    t1 = time.time()
    bwt = BWT(s)
    encode = bwt.encode()
    print encode

    t2 = time.time()
    bwt = BWT(encode[1])
    print bwt.decode(encode[0])
    t3 = time.time()

    print "#1 encoding: %f  decoding: %f complet: %f"%(t2 - t1, t3 - t2, t3 - t1)

    #own alphabet
    data = ["h", "e", "l", "l", "o", 1, 2, 3, 3, 3, 2, 1, 3, 1, 2, 2, 1, 3, 3, 1, 1, 3, 1, 3, 1, "B", "O", "O", "O", "O", "O", "O", "O", "O", "O", "M", "BLAH", "BLAH", "BLAH"]
    alphabet = ["e", "h", "l", "o", 1, 2, 3, "B", "O", "M", "BLAH"]
    t1 = time.time()
    bwt2 = BWTOwnAlphabet(data, alphabet)
    encode = bwt2.encode()
    print encode

    t2 = time.time()
    bwt2 = BWTOwnAlphabet(encode[1], alphabet)
    print bwt2.decode(encode[0])
    t3 = time.time()

    print "#2 encoding: %f  decoding: %f complet: %f"%(t2 - t1, t3 - t2, t3 - t1)

if __name__ == "__main__":
    # cprofile
    cProfile.run('demo(1)', 'profile')
    p = pstats.Stats('profile')
    p.sort_stats('time').print_stats(10)