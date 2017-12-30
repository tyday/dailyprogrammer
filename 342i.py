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

def encode_string(word): # word is a 4 byte/ 32 bit length
    ascii_list = [ord(x) for x in word] #convert word into a list of ascii values
    byte_string = ''
    # convert ascii values to binary... ensure length is in multiples of 4(8 is a byte)
    for x in ascii_list:
        byte = "{0:b}".format(x)
        while len(byte) % 4 != 0:
            byte = '0' + byte
        byte_string += byte
    # Convert the 32 bit binary string to integer
    converted = int(byte_string,2)
    converted_list = []
    #divide it into 4 numbers
    x = converted
    print(x)
    # Repeatedly divide by 85 keeping the remainder until result is less than 85
    # This gives us the base number for the encoding
    while x != 0: 
        x,converted = divmod(x,85)
        converted_list.append(converted)
    converted_list.reverse()
    converted_string = ''
    #Add 33 to each number. Then convert to ascii character
    for i in converted_list:
        i = i + 33
        converted_string += chr(i)
    print(ascii_list)
    print(converted_list)
    print(converted_string)
    print(byte_string)

    

#encode_string('hello world')
encode_string('sure')