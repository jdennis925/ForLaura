import re

infile = open("unsortedtable.txt", "r")
outfile = open("outfile.txt", "w")

while(True):
    x = infile.readline()
    x = x.strip()
    x= re.sub('\'', '', x)
    splits = re.split(r'\t+', x)
    y = '{{\'Symbol\':\'{0}\', \'Name\':\'{1}\', \'origin\':\'{2}\',\'mass\':\'{3}\'}},\n'.format(splits[0],splits[1],splits[2],splits[3])
    outfile.writelines(y)