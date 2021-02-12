import requests
import validators
from bs4 import BeautifulSoup
from tkinter import messagebox, Tk, Label, Button, Entry, Frame

# ================ GUI Specifications ================ #

root = Tk()
root.title("Tags Collector")

# ================ Centering GUI on launch ================ #
window_width = 500
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2)-(window_width / 2)
y = (screen_height / 2)-(window_height / 2)

root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

##################### FUNCTIONALITIES #####################


def start():
    url = input_url.get()
    validation = validators.url(url)

    if validation == True:
        f = requests.get(url)
        soup = BeautifulSoup(f.text, 'html.parser')
        rawtagsList = []

        for tag in soup.find_all():
            rawtagsList.append(tag.name)

        countTotalTags = {i: rawtagsList.count(i) for i in rawtagsList}
        countBox.insert(0, countTotalTags)

        cleanList = list(dict.fromkeys(rawtagsList))

        for uniqueTag in cleanList:
            boxText.insert(0, uniqueTag + ", ")

    else:
        messagebox.showinfo("WARNING", "Please enter a valid url")


def popup():
    messagebox.showinfo(
        "Credits", "This script can be used/modified/implemented/tested for free. \n\nAuthor: simo54 => https://github.com/simo54")

##################### CREATING WIDGETS #####################


button_start = Button(root, text="Start", padx=10, pady=5, command=start)
button_quit = Button(root, text="Quit", padx=10, pady=5, command=root.quit)
input_url = Entry(root, width=70)
button_credits = Button(root, text="Credits", padx=10, pady=5, command=popup)
boxText = Entry(root, width=70)
countBox = Entry(root, width=70)
labelTagsList = Label(root, text="Tags used")
labelCountTags = Label(root, text="Counting Tags")
labelInfo = Label(root, text="Insert your link below")

##################### DISPLAYING WIDGETS #####################

input_url.grid(column=1, row=1)
button_start.grid(column=2, row=1)

labelTagsList.grid(column=1, row=3, pady=5)
boxText.grid(column=1, row=4)

labelCountTags.grid(column=1, row=7, pady=5)
countBox.grid(column=1, row=8)
button_credits.grid(column=2, row=9)
button_quit.grid(column=2, row=10)


# ================ Runner ================ #

root.mainloop()
