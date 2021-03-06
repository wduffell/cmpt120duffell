#userfile.py
# program to create a file of usernames in batch mode

def main():
    print("This program creates a file of usernames from a")
    print("file of names")

    #get file names
    infileName = input("What file are the names in?")
    outfileName = input("What file should the usernames go in?")

    #open the file
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    #process each line in the input file
    for line in infile:
        # get the first and last names from line
        first, last = line.split()
        # create a username
        uname = (first[0] + last[:7].lower())
        # write it to the output file
        print(uname, file = outputfile)

    #close both files
    infile.close()
    outfile.clos()

    print("Usernames have been written to", outfileName)

main()
