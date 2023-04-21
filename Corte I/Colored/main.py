from colored import *

name ="Marvel"

for i in range(len(name)):
    if(i%2==0):
        print(fg(1) + name[i] + attr("reset") , end="")
    else:
        print(fg(4) + name[i] + attr("reset"), end="")
print("\n")

for i in range(10):
    for j in range(i):
        print(bg(j),fg(i) , i ,attr("reset"),end="")
    print("")