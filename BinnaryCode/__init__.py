import math

def strBinToInt(str):
    return int(str, 2)

def strOctToInt(str):
    return int(str, 8)

def strHexToInt (str):
    return int(str, 16)

def intToBinStr(number):
    return bin(number)

def intToOctStr(number):
    return oct(number)

def intToHexStr(number):
    return hex(number)

def length(number): #lengthIntegerInBinary
    return 0 if number == 0 else int(len(bin(number)[2:]))
    #return 0 if number == 0 else int(math.log(number, 2))+1 # Fast, but sometimes bad value

def getFirstBits(number, first = 1):
    shift = length(number) - first
    if shift < 0:
        raise ValueError, "Parameter 'first' must be less than binary length of number"
    return number >> shift

def getLastBits(number, last = 1):
    if last < 1:
        raise ValueError, "Parameter 'last' must be greater than 0"
    mask = (2**last) - 1
    return number & mask

def getValueInPosition(number, position, reverse = False):
    if reverse:
        mask = 1 << (length(number) - 1)
        mask >>= position - 1
        return int((number & mask) > 0)
    return (number >> (position -1) ) & 1

def cutFirst(number, first = 1):
    return number & ( ( 1 << (length(number) - first) )-1)

def cutLast(number, last = 1):
    return number >> last

def resplitBinaryCodes(lst, new_size):
    """
    Re split list to new list with the equally large blocks/items
    This is good for splitting list of reverse binary fibonacci numbers (1100, 11010, 11, ...)
    Example:
        input (binary) list: [110010, 101, 1100, 1]
        new_size: 5
        output (binary) list: [11001, 01011, 10010] - last zero is padding
        real representation output: [11001, 1011, 10010]
    :param lst: list for re split
    :param new_size: block sizes
    :return: list with new block sizes
    """
    first = True
    result = []

    previous_part = 0
    part_size = 0
    for number in lst:
        if part_size:
            size = part_size + length(number)
            if size == new_size:
                previous_part <<= length(number)
                previous_part += number
                result.append(previous_part)
                previous_part = 0
                part_size = 0
            elif size > new_size:
                previous_part <<= length(number)
                previous_part += number
                part_size += length(number)
                while part_size > new_size:
                    virtual_size = new_size - (part_size - length(previous_part))
                    if virtual_size > 0:
                        result.append(getFirstBits(previous_part, virtual_size))
                        previous_part = cutFirst(previous_part, virtual_size)
                    else:
                        if first:
                            first = False
                        result.append(0)
                    part_size -= new_size
            else:
                previous_part <<= length(number)
                previous_part += number
                part_size += length(number)
            continue

        if length(number) == new_size:
            result.append(number)
            continue

        if length(number) < new_size:
            previous_part = number
            part_size = length(number)
            continue

        previous_part = number
        part_size = length(number)
        while part_size > new_size:
            virtual_size = new_size - (part_size - length(previous_part))
            if virtual_size > 0:
                result.append(getFirstBits(previous_part, virtual_size))
                previous_part = cutFirst(previous_part, virtual_size)
            else:
                if first:
                    first = False
                result.append(0)
            part_size -= new_size

    # padding zeros
    if part_size:
        previous_part <<= new_size - part_size
        result.append(previous_part)

    return result

#global variable for caching
actual_fibonacci_numbers = [
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946,
    17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578,
    5702887, 9227465, 14930352, 24157817, 39088169
]
def encodeFibonacci(number, string_output = False):
    fibonacci_numbers = actual_fibonacci_numbers

    if number < 1:
        return  0

    output_bin = 1
    generate_next = True

    i = 0
    for n in fibonacci_numbers:
        if n > number:
            generate_next = False
            break
        i += 1

    while generate_next:
        fib = sum(fibonacci_numbers[-2:])
        fibonacci_numbers.append(fib)
        if fib > number:
            break
        i += 1

    for fib in reversed(fibonacci_numbers[0:i]):
        output_bin = output_bin << 1
        if number >= fib:
            output_bin += 1
            number -= fib

    if string_output:
        return intToBinStr(output_bin)
    return output_bin

def decodeFibonacci(binary, string_input = False):
    if string_input:
        binary = strBinToInt(binary)
    fib_list = [1, 1]
    number = 0
    was_one = False
    mask = 1

    while binary > mask:
        if binary & mask > 0:
            if was_one:
                break
            number += fib_list[-1]
            was_one = True
        else:
            was_one = False
        fib_list.append(sum(fib_list[-2:]))
        mask <<= 1
    return number

def encodeBcd(number, string_output = False):
    binary = 0

    for i in str(number):
        binary <<= 4
        binary += int(i)
    return binary

def decodeBcd(binary, string_input = False):
    if string_input:
        binary = strBinToInt(binary)

    if binary < 9:
        return binary

    number_list = []
    mask = 0b1111
    run = True
    i = 0
    while run:
        if binary < mask:
            run = False
        number_list.append(str(int((binary&mask) >> (i * 4))))
        mask <<= 4
        i += 1
    number_list = reversed(number_list)
    number = "".join(number_list)

    if string_input:
        return number

    return int(number)
