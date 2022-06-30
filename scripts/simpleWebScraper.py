import requests                 
from bs4 import BeautifulSoup   
import time                     

def main() :
    print("------------------")

    choice = displayMenu()
    
    while choice != 4 :

        if choice == 1 :            
            url = input("Enter the site to request: ")
            r = pingSite(url)
            print("HTTP status code: ", r)
            
            time.sleep(3)
            choice = displayMenu()
            
        if choice == 2 :
            subChoice = displaySubmenu()
            if subChoice == 1 :
                # scrape wikipedia
                wikiUrl = createWikiUrl()
                r = requests.get(wikiUrl)
                soup = scrape(r)
                writeToFile(soup, "mw-body")

                time.sleep(3)
                choice = displayMenu()
                
            elif subChoice == 2 :
                # scrape darklyrics
                darkUrl = createDarkUrl()
                r = requests.get(darkUrl)
                soup = scrape(r)
                writeToFile(soup, "lyrics")

                time.sleep(3)
                choice = displayMenu()

        if choice == 3 :
            url = input("Enter the site to scrape from: ")
            r = requests.get(url)
            soup = scrape(r)

            scrapeUniqueSite(soup)

            time.sleep(3)
            choice = displayMenu()

        if choice == 4 :
            break

def displayMenu() :
    print("------------------")
    print("1) Ping a web address")
    print("2) Scrape from suggested site")
    print("3) Scrape from different site")
    print("4) Exit")
    print("------------------")

    choice = int(input("Enter your selection: "))
    return choice

def displaySubmenu() :
    print()
    print("List of suggested sites")
    print("-----------------------")
    print("1) Wikipedia.org")
    print("2) Darklyrics.com")
    print("-----------------------")

    subChoice = int(input("Enter your selection: "))
    return subChoice

def pingSite(url) :
    # Send hit request and force utf-8 encoding.
    r = requests.get(url)
    if r.encoding != 'utf-8' :
        r.encoding = 'utf-8'
    return r

def createDarkUrl() :
    band = input("Enter the band's lyrics to scrape: ")
    album = input("Enter the album to scrape: ")
    
    # Get rid of spaces and make lowercase for later.
    band = band.replace(" ", "").lower()
    album = album.replace(" ", "").lower()

    # The finalized url. Fits the formattign of darklyrics headers.
    appendedUrl = "http://www.darklyrics.com/lyrics/" + band + "/" + album + ".html#1"
    return appendedUrl

def createWikiUrl() :
    article = input("Enter the article to scrape : ")
    article = article.replace(" ", "_").capitalize()

    appendedUrl = 'https://en.wikipedia.org/wiki/' + article
    return appendedUrl

def scrape(r) :
    # Create Beautiful Soup object containing all HTML.
    soup = BeautifulSoup(r.content, "lxml")
    return soup   

def writeToFile(soup, class__) :
    fileTitle = input("Enter the file name to write to: ")
    # Again, force utf-8 encoding or the file cannot be written to correctly.
    file = open(fileTitle, "w", encoding="utf-8")

    for div in soup.find_all('div', class_=class__) :
        file.write(div.text)
          
    print("Writing...")
    time.sleep(1)
    print("All done!")

    # Close the file.
    file.close()

def scrapeUniqueSite(soup) :
    fileTitle = input("Enter the file name to write to: ")
    # Again, force utf-8 encoding or the file cannot be written to correctly.
    file = open(fileTitle, "w", encoding="utf-8")

    class__ = input("Enter the tag or class to scrape: ")

    for div in soup.find_all('div', class_=class__) :
        file.write(div.text)
          
    print("Writing...")
    time.sleep(1)
    print("All done!")

    # Close the file.
    file.close()
  
if __name__ == '__main__' : 
    main()
