import requests 
import json
from tkinter import * # type: ignore
import random

root = Tk()

root.title("Ramdom champion picker")

root.geometry("220x70")

lbl = Label(root, text="Chapion: ...")
lbl1 = Label(root, text="Title : ...")

lbl.grid(column= 1, row=0)
lbl1.grid(column = 1, row=1)

def clicked():
    url = "https://ddragon.leagueoflegends.com/cdn/14.3.1/data/en_US/champion.json"
    page = requests.get(url)
    data = json.loads(page.text)

    champion_list = list(data["data"].keys())

    s = random.randint(0, len(champion_list))


    lbl.configure(text=f"Chapion : {data["data"][champion_list[s]]["id"]}")

    lbl1.configure(text=f"Title : {data["data"][champion_list[s]]["title"]}")

btn = Button(root, text="Random", command=clicked)
btn.grid(column = 2, row = 0)

root.mainloop()