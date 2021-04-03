#4




def main():
    
    namesFile = open("names.txt", "r")
    line = namesFile.readline()
    numberOfLines = 0

    while line != " ":
        numberOfLines = numberOfLines + 1
        line = namesFile.readline()

    print("the file has ", numberOfLines, "lines")


   

main()

