import requests
from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup

FONT = ("Verdana", 18, "normal")
foundLinks = set()  
totalLinks = 0

def make_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def crawler(url):
    global totalLinks
    target_url = target_entry.get()
    link = make_request(url)
    for link in link.find_all('a'):
        found_link = link.get('href')
        if found_link:
            if "#" in found_link:
                found_link = found_link.split("#")[0]
            if target_url in found_link and found_link not in foundLinks:
                foundLinks.add(found_link)
                totalLinks += 1
                crawler(found_link)
 
    if totalLinks == len(foundLinks):
        with open("Results.txt", "a") as data_file:
            for link in foundLinks:
                data_file.write(link + '\n')
        messagebox.showinfo("Bilgi", f"{totalLinks} link found. All links are saved to 'Results.txt' file.")

root = Tk()
root.title("Web Crawler")
root.minsize(width=300, height=350)

target_label = Label(text="Enter your target url", font=FONT)
target_label.pack()

target_entry = Entry(width=45)
target_entry.pack()

result_button = Button(text="Search", width=20, command=lambda: crawler(target_entry.get()))
result_button.pack()

root.mainloop()
