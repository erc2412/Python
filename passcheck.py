#------------FILES--------------

inputfile = "name.txt"
outputfile = "name.txt"
opepass = "name"
twopass = "name2"
myfile1 = open(inputfile, mode='r', encoding="latin-1")
myfile2 = open(outputfile, mode="w", encoding="latin-1")

for num,line in enumerate(myfile1, 1):
    if opepass in line:
     print("Line N: " + str(num) + " : " + line.strip())
     myfile2.write("Find password : " + line)
    elif twopass in line:
        print("Line N: " + str(num) + " : " + line.strip())
        myfile2.write("Find password : " + line)


