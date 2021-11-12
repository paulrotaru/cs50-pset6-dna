import csv
import sys
import random

def main():

    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    #convert sequences files in lists
    with open(sys.argv[2], "r") as sequence:
        seq = sequence.read()


    #convert cvs file in dictionar
    datadna = []
    with open (sys.argv[1]) as f:
        reader = csv.DictReader(f)
        for row in reader:
            datadna.append(row)


    #returns the maximum number of times that the STR repeats
    #iterate through sequence to find STR
    #when find STR counting repeats
    #when new maximum of consecutive repeats reached, switch count_max
    count_max = []

    for i in range(1, len(reader.fieldnames)):
        seq_str = reader.fieldnames[i]
        count_max.append(0)
     #iterate through sequence to find STR
        for j in range(len(seq)):
            countstr = 0
            if seq[j:(j + len(seq_str))] == seq_str:
                k = 0
    #when find STR counting repeats
                while seq[(j + k):(j + k + len(seq_str))] == seq_str:
                    countstr = countstr + 1
                    k = k + len(seq_str)
     #when new maximum of consecutive repeats reached, switch count_max
                if countstr > count_max[i - 1]:
                    count_max[i - 1] = countstr

    #check if the STR maximum nr of consecutive repeats match the dictionary
    #if find matches, print name, else print No match
    for i in range(len(datadna)):
        match = 0
        for j in range(1, len(reader.fieldnames)):
            if int(count_max[j - 1]) == int(datadna[i][reader.fieldnames[j]]):
                match = match + 1
            if match == (len(reader.fieldnames) - 1):
                print(datadna[i]["name"])
                exit(0)

    print("No match")


if __name__ == "__main__":
    main()