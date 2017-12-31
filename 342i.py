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
    buff = 0
    # convert ascii values to binary... ensure length is in multiples of 4(8 is a byte)
    for x in ascii_list:
        if x == 0:
            buff += 1
            byte = '00000000'#"{0:b}".format(x)
            byte_string += byte
        else:
            byte = "{0:b}".format(x)
            while len(byte) % 4 != 0:
                byte = '0' + byte
            byte_string += byte
    # Convert the 32 bit binary string to integer
    converted = int(byte_string,2)
    converted_list = []
    #divide it into 4 numbers
    x = converted
    # print(x)
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
    if buff > 0:
        converted_string = converted_string[:-buff]
    # print(ascii_list)
    # print(converted_list)
    # print(byte_string)
    # print(converted_string)
    return converted_string

def decode_string(word):
    converted_list = []
    word = word[::-1]
    for a,b  in enumerate(word):
        c = -33 + ord(b)
        converted_list.append(c * 85 **a)
    # print(sum(converted_list), converted_list)
    converted = bin(sum(converted_list))
    converted = converted[2:]
    while len(converted) <32: #pad converted with 000s
        converted = '0' + converted
    #divide converted into 4 bytes
    byte_list = []
    while len(converted)>1:
        byte_list.append(converted[:8])
        converted = converted[8:]
    #convert bytelist into ascii
    return_string = ""
    for byte in byte_list:
        letter = int(byte,2)
        letter = chr(letter)
        return_string += letter
    
    # print(byte_list)
    # print(return_string)
    return return_string
        
def encode_graph(paragraph):
    """Receives text string of any length
    divides it into 4 char words and passes
    those off to encode_string
        Returns a string
    """
    word = ""
    if len(paragraph) <= 4:
        while len(paragraph) < 4:
            paragraph += chr(0)#"0" #adds a space to make paragraph 4 units long
        return encode_string(paragraph)
    else:
        word = encode_string(paragraph[:4])
        return word + encode_graph(paragraph[4:])
# encode_string('hello world')
# print(decode_string(r"""+F81(_Lnf5/6[,"""))
# encode_string('sure')
# decode_string('F*2M7')
# encode_string('fire')
# decode_string('Anc9s')
# encode_string('bowl')
# decode_string('@W-I,')
# encode_string('hare')
# decode_string('@rH:%')
# print(r'/mo[')
# encode_string(r'/mo[')
# decode_string('05YW3')
# print('hel+llp')
# print(encode_string('sure'))
spam = 'hell'
print(encode_string(spam))
spam = encode_string(spam)
print(decode_string(spam))
print('\n')
spam = 'Attack at dawn'
jam = 'Mom, send dollars!'
print(encode_graph(spam))
print(encode_graph(jam))
print(encode_graph('.'))
# print(decode_string('6$.3W'))
# print(decode_string('@r!2q'))
# print(decode_string('F<G+&'))
# print(decode_string('GA])g'))
