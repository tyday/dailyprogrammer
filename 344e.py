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
print('100112235',streak_list('100112235'))
print('100112235',streak_list2('100112235'))
print('1001100035',streak_list2('1001100035'))
# i=1
# for elem in bin_list:
#     i = 0   #reset index and streak length to 0
#     j = 0
#     streak = False  # set streak to false
#     while i < len(elem):
#         i += 1
#         if elem[i-1] == 0:  # if element is zero add 1 to j and make sure streak is true
#             streak = True
#             j += 1
#                             # I want to set an else here, but I need to wait to evaluate
#         elif j % 2 != 0:
            
#         if i = len(elem) and streak = True:
#             if j % 2 != 0:
#                 print('Elem:', elem, '1','Count:', j)
#     print('Elem:', elem, 'Count:', j)
