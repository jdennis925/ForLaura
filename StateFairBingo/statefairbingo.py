import re
import random


findables = []
with open("findables.txt", "r") as fp:
    for line in fp:
        print(line)
        line = line.strip()
        findables.append(line)
        


outfile = open("randomfindables.txt", "w")


count = 1
while count <= 25:
    if(count == 13):
        outfile.write("ENTER THE STATE FAIR!")
    else:
        index = random.randint(0, len(findables) - 1)
        outfile.write(findables[index])
    if(count > 1 and count % 5 == 0):
        outfile.write("\n")
    else:
        outfile.write("\t")
        
    del findables[index]
    count += 1

outfile.close()
