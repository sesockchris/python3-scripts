## Written by Christopher Sesock
## on March 12th, 2020
##

totallist = []

def main() :

    try :

        with open("../assets/elements.txt", "r") as openfile :
            for line in openfile :
                for word in line.split() :
                    totallist.append(word)

        elementlist = totallist[0::5]
        symbollist = totallist[1::5]
        zlist = totallist[2::5]
        atomicweightlist = totallist[3::5]
        clist = totallist[4::5]

        openfile.close()

        element = str(input("Enter the element for information: "))
        element = element.capitalize()
        for count in range(0, len(elementlist)) :
            if elementlist[count] == element :
                print("------------------------")
                print("Element: " + element)
                print("Atomic Name: " + symbollist[count])
                print("Protons: " + zlist[count])
                print("Atomic Weight: " + atomicweightlist[count])
                print("Electrons: " + clist[count])
                print("------------------------")
        element = str(input("Enter the element for information: "))
        

    except FileNotFoundError :

        print("File not found.")

if __name__ == '__main__' : 
    main()                    
