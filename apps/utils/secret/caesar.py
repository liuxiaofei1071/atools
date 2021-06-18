

def caesar(msg:str, mode='encrypt', offset=4):
    """
    Caesar algorithm
    :param msg: string info
    :param mode: encrypt/decrypt
    :param offset: The offset default 4, common between 1 and 26
    :return: encrypt/decrypt string result
    """
    if mode == 'decrypt':
        offset = -offset

    result = ''
    for item in msg:
        if item.isalpha():
            _ascii = ord(item)
            _ascii += offset
            if item.isupper():
                if _ascii > ord('Z'):
                    _ascii -= 26
                elif _ascii < ord('A'):
                    _ascii += 26
            elif item.islower():
                if _ascii > ord('z'):
                    _ascii -= 26
                elif _ascii < ord('a'):
                    _ascii += 26
            result += chr(_ascii)
        else:
            result += item
    return result


# ascii_a = ord('a')
# ascii_z = ord('z')
#
# ascii_A = ord('A')
# ascii_Z = ord('Z')
#
# print(ascii_a, 'a')
# print(ascii_z, 'z')
# print(ascii_A, 'A')
# print(ascii_Z, 'Z')
# print(ascii_z - ascii_a)

if __name__ == '__main__':
    print([chr(i) for i in range(97, 123)])
    print([chr(i) for i in range(65, 91)])

    ret = caesar('zz@1!ASz', mode='decrypt', offset=0)
    print(ret)
