"""
Alex Kouyoumjian

Online Web Broser Project

Goal: Create an easy-to-use web browser

Features:
- Input which web engine you'd like to use by entering URl or keyword (if applicable).
- Home button
- Forward and back buttons
- Refresh button

"""

import sys
from PyQt5.QtWidgets import * ## to generate UI in Qt
from PyQt5.QtWebEngineWidgets import *  ## for the web browser engine
from PyQt5.QtCore import * ## for setting URL


## class for the primary window of browser.
class PrimaryWindow(QMainWindow):



    def __init__(self):
        super(PrimaryWindow, self).__init__()
        self.showMaximized() ## expands the window size
        self.browser = QWebEngineView() ## for viewing and interacting with web pages
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)

        ## determines what web engine to use

        print("Enter the URL (ending in .com) of the search engine you would like to use? "
          "\n Enter keyword if applicable. ")

        your_search = input()

        ## checking if input matches keyword.
        if your_search.lower() == "google":
            self.browser.setUrl(QUrl("http://google.com"))
        if your_search.lower() == "bing":
            self.browser.setUrl(QUrl("https://www.bing.com"))
        if your_search.lower() == "yahoo":
            self.browser.setUrl(QUrl("https://search.yahoo.com"))
        if your_search.lower() == "baidu":
            self.browser.setUrl(QUrl("https://www.baidu.com"))
        elif your_search.lower().lastN(4) != ".com":
            raise Exception("invalid url")
        else:
            self.browser.setUrl(QUrl(your_search))


app = QApplication(sys.argv)
QApplication.setApplicationName("Web Browser")
window = PrimaryWindow()
app.exec_()

## gets the last n digits of a string
## make static method
def lastN(n):











    '''

    8:36

    '''





