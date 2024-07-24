import sys 
import webbrowser

URLS = {
    "work" : ['https://www.chatgpt.com','https://www.office.com'],
    "personal_life" :["https://www.instagram.com","https://www.youtube.com"],
    "projects" : ["https://www.chatgpt.com","https://www.stackoverflow.com"]
}

def openwebpage(urls):
    for url in urls:
        webbrowser.open(url)
#openwebpage(urls["personal life"])

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in URLS:
        print('sorry, the available sets are : ')
        for name in URLS.keys():
            print(name) 
        sys.exit(1)       
    setname = sys.argv[1]
    url = URLS[setname]
    openwebpage(url)