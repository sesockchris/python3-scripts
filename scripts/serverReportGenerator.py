## Script used to generate a report of open ip addresses from a zenmap port scan.
## Used to find open directories.
##

from collections import deque
import re

#global variables
pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
current_server = deque(maxlen=5)

def createServerReport() :
    counter = 0

    file = open("open server report.txt", "w+")
    #name of text file containing ip addresses
    with open("output.txt") as input:
        for line in input:
            if "open" in line or "Open" in line or "OPEN" in line:
                print(*current_server, line, sep='')
                print("----------------------------------------")
                try :
                    for i in range(5) :
                        file.write(current_port[i])
                except :
                    print("could not write to file.")

                current_server.clear()
                counter += 1
            current_server.append(line)
    print(counter, "open ports found.")
    file.close()


if __name__ == "__main__":
    createServerReport()