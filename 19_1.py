#

L = [chr(x) for x in range (97,123)]
print(L)


for j in L:
    f = open(j + ".txt", "w")
    f.write("i am " + j + " file ")

f.close()