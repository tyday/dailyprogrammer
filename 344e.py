"""Daily programmer 344 
Baum-Sweet sequence

convert number into binary
search binary for odd occurences of 0
i.e. 0, 000, 00000

How to determine if length of characters are odd or even
-it has to be he end of the string. Either the end of total string
- or end of last occurence.
So, do check on last run through. Or on change of 0 to 1
if end of string and 0 then find out if run of 0s is odd.
if char is 1, then check if there was a run

"""
import re
def is_odd(numb):
    if numb % 2 != 0:
        return True
    else:
        return False

def streak_list(eval_string):
    return_dict = {}
    if eval_string == 1:
        return_dict[eval_string] = 1
        return return_dict
    else:
        for item in eval_string:
            if item in return_dict:
                return_dict[item] += 1
            else:
                return_dict[item] = 1
        return return_dict

def streak_list2(eval_string):
    return_dict = {}
    last_char = "" # the character from the previous run
    streak_numb = 1 #count of various streaks
    
    for item in eval_string:
        if item == last_char:
            label = 'Streak_' +str(streak_numb - 1)
            listy = return_dict[label]
            listy[1] += 1
            return_dict[label] = listy
        else:
            label = 'Streak_' + str(streak_numb)
            return_dict[label] = [item, 1]
            last_char = item
            streak_numb += 1

    return return_dict



bin_list = []
for i in range (1,21):
    print(str(i), "{0:b}".format(i))
    bin_list.append("{0:b}".format(i))
print(bin_list)
for item in bin_list:
    odd = "no odd"
    a = streak_list2(item)
    for c,b in a.items():
        if b[0] == '0' and is_odd(b[1]):
            odd = "has odd"
    print (item, odd)

# attempt at using re to find the pattern. Can't figure it out
for item in bin_list:
    zeros_list =[]
    zeros = '0'
    hasodd = 'none'
    for i in range(1,len(str(item))+1,2):
        zeros = '0' * i
        zeros_list.append(zeros)
    for zero in zeros_list:
        a = re.compile(zero)
        b = a.match(item)
        if b:
            hasodd = 'does'
    print (item,hasodd)