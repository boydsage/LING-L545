VOcount = 0
OVcount = 0

# import sys to read standard in file
import sys

# set up while loop to read file line by line, when line empty loop stops
line = sys.stdin.readline()
while line:

# if line starts with # continue
    if line[0] == '#':
        line = sys.stdin.readline()
        continue

# if the line doesn't have 9 tabs continue
    tabs = 0
    for char in line[:]:
        if char == '\t':
            tabs += 1

    if tabs < 9:
        line = sys.stdin.readline()
        continue

# split the line into a list on the tab character and put into list called row
    row = line.split('\t')

# if first column is "." continue
    if row[0].count('.') > 0:
        line = sys.stdin.readline()
        continue

# call token id, 0 item in row list and convert to int
    try:
        token = int(row[0])
    except:
        line = sys.stdin.readline()
        pass

# call dependency relation, 7 item in row list
    dependRelat = row[7]

# call the head, 6 item in row list and convert to int
    try:
        head = int(row[6])
    except:
        line = sys.stdin.readline()                                             
        pass
        
# if dependency relation is obj and if the token is less than head, then OVcount increases by one
    if (dependRelat == 'obj') and (token < head):
        OVcount += 1

# if dependency relation is obj and if the token is greater than head, the VOcount increases by one
    if (dependRelat == 'obj') and (token > head):
        VOcount += 1

# read next line
    line = sys.stdin.readline()


# compute and print x and y
print('x = ', OVcount/(VOcount + OVcount))
print('y = ', VOcount/(VOcount + OVcount))
