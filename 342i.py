""" https://www.reddit.com/r/dailyprogrammer/comments/7gdsy4/20171129_challenge_342_intermediate_ascii85/
code and decode to ASCII85

convert from
text->ascii_>binary(byte)
Concatenate
Retrieve the 32 bit value
Repeatedly divide by 85
Add 33 to each remainder to reveal a new
ASII character:

"""

def encode_string(sentence):
    ascii_list = [ord(x) for x in sentence] #convert sentence into a list of ascii values
    print(ascii_list)
    byte_string = ''
    # convert ascii values to binary... ensure length is in multiples of 4(8 is a byte)
    for x in ascii_list:
        byte = "{0:b}".format(x)
        while len(byte) % 4 != 0:
            byte = '0' + byte
        byte_string += byte
    # Convert the bytestring
    byte_string = int(byte_string)
    newvalue = "{0:d}".format(byte_string)
    #newvalue.encode('hex'), 16
    print(newvalue)

encode_string('hello world')
encode_string('sure')