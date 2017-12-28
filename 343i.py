""" 343i https://www.reddit.com/r/dailyprogrammer/comments/7i1ib1/20171206_challenge_343_intermediate_mozarts/
create a composition using randomly added measures
"""
import random
def load_compostition(filename):
    """
    Read contents of file. Assume file contents are space separated
    note beat duration
    F# 23 1
    G 23 .5
    """
    notelist = []
    with open(filename) as f:
        read_data = f.readlines()
        for line in read_data:
            linedata = line.split()
            if len(linedata) == 3:
                notelist.append(linedata)
        return notelist

def load_select_list(filename):
    select_list = []
    with open(filename) as f:
        read_data = f.readlines()
        for line in read_data:
            linedata = line.split()
            select_list.append(linedata)
    return select_list

def split_measures(notelist):
    """ Assumes measures are 3 beats long.
    Returns a dictionary of measures 
    and notes in measure
    """
    measure_dict = {}
    for index, note in enumerate(notelist):
        #print(index,note)
        measure = float(note[1]) // 3
        newnote = note
        newnote[1] = float(note[1]) - measure* 3
        measure += 1
        if measure in measure_dict:
            measure_dict[measure].append(newnote)
        else:
            measure_dict[measure] = []
            measure_dict[measure].append(newnote)
    return measure_dict

def create_composition(measure_dict):
    song = "" # will return song in string format
    for i in range(0,16):
        # Get random measure 
        selection = random.randint(1,len(measure_dict))
        print(i, selection)
        #get measure from list
        measure = measure_dict[selection]
        # adjust measure to position in new song
        for note in measure:
            note[1] += i * 3
            #Add measure to song
            song += note[0] + " " + str(note[1]) + " " + note[2] + "\n"
    return song

def create_composition2(measure_dict):
    selectlist = load_select_list('343i_select.txt')
    song = "" # will return song in string format
    j = 0
    for i in selectlist:
        # Get random measure 
        rint = random.randint(0,len(i)-1)
        selection = int(i[rint])
        print(i,rint, selection)
        #get measure from list
        measure = measure_dict[selection]
        # adjust measure to position in new song
        for note in measure:
            note[1] += j * 3
            #Add measure to song
            song += note[0] + " " + str(note[1]) + " " + note[2] + "\n"
        j += 1
    return song


origcomp = load_compostition('343i.txt')
mlist = split_measures(origcomp)
# print(len(mlist))
# for item in mlist:
#     print(mlist[item])
# print(create_composition(mlist))
# print(load_select_list('343i_select.txt'))
print(create_composition2(mlist))
input('press any key to continue')