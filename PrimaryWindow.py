"""
Alex Kouyoumjian

Online Web Broser Project

Goal: Create an easy-to-use web browser

Features:
- Input which web engine you'd like to use by entering URl or keyword (if applicable).
- Home button
- Forward and back buttons
- Refresh button
- Shortcuts

"""

import sys
from PyQt5.QtWidgets import * ## to generate UI in Qt
from PyQt5.QtWebEngineWidgets import *  ## for the web browser engine
from PyQt5.QtCore import * ## for setting URL


## class for the primary window of browser.
class PrimaryWindow(QMainWindow):



    def __init__(self):

        ## determines what web engine to use
        print("Enter the URL (ending in .com) of the search engine you would like to use (not case sensitive)."
              "\n Enter keyword if applicable.")

        your_search = input()

        super(PrimaryWindow, self).__init__()
        self.showMaximized() ## expands the window size
        self.browser = QWebEngineView() ## for viewing and interacting with web pages
        self.browser.setUrl(QUrl(your_search))
        self.setCentralWidget(self.browser)


        ## checking if input matches keyword.
        if your_search.lower() == 'google':
            self.browser.setUrl(QUrl("http://google.com"))
        if your_search.lower() == "bing":
            self.browser.setUrl(QUrl("https://www.bing.com"))
        if (your_search.lower() == "yahoo") | (your_search.lower() == "yahoo!"):
            self.browser.setUrl(QUrl("https://search.yahoo.com"))
        if your_search.lower() == "baidu":
            self.browser.setUrl(QUrl("https://www.baidu.com"))

        ##elif your_search.lower().last_n(your_search, 4) != ".com":
         ##   raise Exception("invalid url")


        ## Navigation Bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        ## Back and Forward Button
        back_button = QAction("Go Back", self)
        back_button.triggered.connect(self.browser.back)
        forward_button = QAction("Go Forward", self)
        forward_button.triggered.connect(self.browser.forward)

        ## Home Button
        home_button = QAction("Home", self)
        home_button.triggered.connect(self.nav_home)

        ## Refresh Button
        refresh_button = QAction("Refresh", self)
        refresh_button.triggered.connect(self.browser.reload)

        ## Youtube Shortcut Button
        youtube_shortcut = QAction("YouTube", self)
        youtube_shortcut.triggered.connect(self.nav_yt)

        ## Twitter Shortcut Button
        twitter_shortcut = QAction("Twitter", self)
        twitter_shortcut.triggered.connect(self.nav_twitter)

        ## Espn Shortcut Button
        espn_shortcut = QAction("ESPN", self)
        espn_shortcut.triggered.connect(self.nav_espn)

        ## add buttons to navbar
        navbar.addAction(back_button)
        navbar.addAction(forward_button)
        navbar.addAction(home_button)
        navbar.addAction(refresh_button)
        navbar.addAction(youtube_shortcut)
        navbar.addAction(twitter_shortcut)
        navbar.addAction(espn_shortcut)



        ## add url type in bar functionality at top of web browser.
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.nav_url)
        navbar.addWidget(self.url_bar)

    def nav_url(self):  ## navigates to home page
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    def nav_home(self): ## navigates to home page
        self.browser.setUrl(QUrl("http://google.com"))
    def nav_espn(self): ## navigates to home page
        self.browser.setUrl(QUrl("https://www.espn.com/"))
    def nav_yt(self): ## navigates to home page
        self.browser.setUrl(QUrl("https://www.youtube.com/"))
    def nav_twitter(self): ## navigates to home page
        self.browser.setUrl(QUrl("https://www.twitter.com/home"))



app = QApplication(sys.argv)
QApplication.setApplicationName("Web Browser")
window = PrimaryWindow()
app.exec_()

