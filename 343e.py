""" 12 notes on the chromatic scale
C, C#, D, D#, E, F, F#, G, G#,A, A#, B

A major scale comprises 7 out of the 12 notes on the chromatic scale
0, 2, 4, 5, 7, 9, 11
Do, Re, Me, Fa, So, La, Ti...

"""
major_scale = {'Do':0,'Re':2,'Mi':4,'Fa':5,'So':7,'La':9,'Ti':11}
chromatic_scale = {'C':0, 'C#':1,'D':2,'D#':3, 'E':4, 'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
for item in chromatic_scale:
    print (item, chromatic_scale[item])

print(chromatic_scale)
y = input('Please give note followed by scale position seperated by comma')
ylist = y.split(',')
root_note = ylist[0].strip()
comp_note = ylist[1].strip()
mspos = major_scale[comp_note]
mspos = mspos + chromatic_scale[root_note]
if mspos > 11:
    mspos = mspos % 12
print(chromatic_scale[ylist[0]], mspos)
