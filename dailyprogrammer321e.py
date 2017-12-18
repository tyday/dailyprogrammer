# Locate all repeating numbers in a given number of digits. The size of the number that gets repeated should be more than 1. You may either accept it as a series of digits or as a complete number. I shall explain this with examples: 
# 11325992321982432123259 
# We see that:
# 321 gets repeated 2 times
# 32 gets repeated 4 times
# 21 gets repeated 2 times
# 3259 gets repeated 2 times
# 25 gets repeated 2 times
# 59 gets repeated 2 times
# Or maybe you could have no repeating numbers:
# 1234565943210
# You must consider such a case:
# 9870209870409898
# Notice that 987 repeated itself twice (987, 987) and 98 repeated itself four times (98, 98, 987 and 987). 
# Take a chunk "9999". Note that there are three 99s and two 999s.
# 9999 9999 9999 
# 9999 9999

# Take a string and take all the possible substrings out and add them to a dictionary

def stringshredder(sentence):
    recurring_bits = {}
    for c,d in enumerate(sentence):
        i=0
        j=0
        sentence_part=sentence[c:(len(sentence)-i)]
        for i in range(c,len(sentence)-j):
            sentence_part = sentence[c:(len(sentence)-j)]
            if len(sentence_part)<2:
                #do nothing
                j+=1
            elif sentence_part in recurring_bits:
                recurring_bits[sentence_part]+=1
                j+=1
            else:
                recurring_bits[sentence_part] = 1
                j+=1
    # for parts,numberof in recurring_bits.items():
    #     if numberof > 1:
    #         print(parts,numberof)
    return recurring_bits

test = '124489903108444899' #input('Give me a list of numbers')
#print(stringshredder(test))
dict_one = stringshredder(test)
parts,number = sorted(dict_one.items(), key=lambda x:x[1])
for parts,numberof in dict_one.items():
        if numberof > 1:
            print(parts,numberof)
for parts,numberof in sorted(dict_one.values()):
        if numberof > 1:
            print(parts,numberof)

