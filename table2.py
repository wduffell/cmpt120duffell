# table 2

def main():
    temp = "{:d} {:5b} {:5o} {:5x}"
    for i in range(1,21):
        print(temp.format(i,i,i,i))

main()
