#Parses a table with two columns and outputs both
#to individual text files for easier processing
import os

def parse1st(f):
    with open(f, 'r') as openfile:
        with open("1st.txt", 'w') as builtfile:
            for line in openfile:
                builtfile.write(line.split()[0])
                builtfile.write('\n')

def parse2nd(f):
    with open(f, 'r') as openfile:
        with open("2nd.txt", 'w') as builtfile:
            for line in openfile:
                builtfile.write(line.split()[-1])
                builtfile.write('\n')

def main():
    filename = input("Enter filename to parse: ")
    parse1st(filename)
    parse2nd(filename)
    os.system('pause')

if __name__ == "__main__":
    main()
