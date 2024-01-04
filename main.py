import json
import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtNetwork import QNetworkCookie
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
from dotenv import load_dotenv

# Load variables from .env file into environment
load_dotenv()


class SmartTVBuilder(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initializing the workspace for crafting an alternative Smart TV solution
        self.tab_widget = QTabWidget()  # Container for managing various functional modules
        self.setCentralWidget(self.tab_widget)
        self.setWindowTitle("Personal Smart TV")  # Title of the workspace
        self.setWindowIcon(QIcon('assets/icon.png'))  # Icon symbolizing the workspace
        self.create_YouTube_tab("https://youtube.com/")  # Starting by loading Youtube TV as HomePage
        self.create_Netflix_tab("https://www.netflix.com/")  # Open Netflix in new tab & set cookies

    # Method to create the Browser tab for systematic research and development
    def create_YouTube_tab(self, url):
        browser = QWebEngineView()  # Component for web interface and exploration
        browser.page().profile().setHttpUserAgent(os.getenv("UserAgent"))  # Set Android Smart Useer Agent
        browser.load(QUrl(url))  # Loading the provided URL for exploration
        browser.urlChanged.connect(self.track_URL)  # Monitoring the digital pathways
        browser.page().fullScreenRequested.connect(self.enable_fullscreen)  # Activating immersive mode
        self.tab_widget.addTab(browser, "Experimental Browser")  # Integrating the browser for investigation
        self.tab_widget.tabBar().hide()  # Hiding tabs for workspace organization

    def create_Netflix_tab(self, url):
        web = QWebEngineView()  # Create a new QWebEngineView instance for the browser tab

        # Create a cookie store
        cookie_store = web.page().profile().cookieStore()  # Access the cookie store for the web page
        with open("cookies.json", 'r') as file:
            Netflix_cookies = json.load(file) # Load data from cookies.json file
        # Set each cookie in the cookie store
        for cookie in Netflix_cookies:
            qcookie = QNetworkCookie()  # Create a QNetworkCookie object for each cookie
            qcookie.setDomain(cookie["domain"])  # Set the cookie's domain
            expiration_date = QDateTime.fromSecsSinceEpoch(int(cookie["expirationDate"]))  # Get expiration date
            qcookie.setExpirationDate(expiration_date)  # Set the cookie's expiration date
            qcookie.setHttpOnly(cookie["httpOnly"])  # Set if the cookie is HTTP only
            qcookie.setName(cookie["name"].encode())  # Set the cookie's name
            qcookie.setPath(cookie["path"])  # Set the cookie's path
            qcookie.setSecure(cookie["secure"])  # Set if the cookie is secure
            qcookie.setValue(cookie["value"].encode())  # Set the cookie's value
            cookie_store.setCookie(qcookie, QUrl(url))  # Add the cookie to the cookie store for the URL

        # Load the URL with the set cookies
        web.load(QUrl(url))  # Load the specified URL in the web view
        self.tab_widget.addTab(web, "Netflix")  # Add the web view to the tab widget for Netflix
        self.tab_widget.setStyleSheet("QTabBar::tab { width: 0; margin: -1; padding: 0; border: none; }")

        # Function to print the current URL when the page finishes loading
        def print_current_url():
            current_url = web.url().toString()
            print("🍿 Netflix :", current_url)

        web.loadFinished.connect(print_current_url)  # Connect the signal for page load finished to the function

        # Function to navigate to the Netflix browse page after a delay
        def navigate_to_browse():
            user_agent = os.getenv('user_agent')
            web.page().profile().setHttpUserAgent(user_agent)  # Set a custom user agent for the web page
            web.load(QUrl("https://www.netflix.com/browse"))  # Load the Netflix browse page

        QTimer.singleShot(3000, navigate_to_browse)  # Schedule navigating to the browse page after 3 seconds

    # Method to track and document the digital pathways explored
    def track_URL(self, url):
        print("🎥 YouTube :", url.toString())  # Recording the pathways for analysis

    # Method to enable full-screen mode for focused experimentation and observation
    def enable_fullscreen(self, request):
        request.accept()  # Accepting the request for an expanded view


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_icon = QIcon('assets/icon.png')  # Symbolizing the workspace for professional representation
    smart_tv = SmartTVBuilder()  # Building a customized Smart TV solution
    smart_tv.tab_widget.tabBar().setVisible(True)
    smart_tv.show()  # Displaying the workspace for solution development
    sys.exit(app.exec_())  # Managing the event loop for continuous development
