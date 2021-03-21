import webbrowser
import random as rand
import time
import os
import sys


def CreateNewTab(url):
    webbrowser.register('chrome',
    None,
    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)
def CreateRandomtabs(tabstocreate):
    for tabnum in range(tabstocreate):
        time.sleep(2)
        websites=["www.google.com", "www.youtube.com", "stackoverflow.com", "github.com"]
        websitechoosed = "http://" + rand.choice(websites)
        CreateNewTab(websitechoosed)
while True:
    tabstocreate=input("How many tabs you want to create? (Every tab 2 second):")
    CreateRandomtabs(int(tabstocreate))
