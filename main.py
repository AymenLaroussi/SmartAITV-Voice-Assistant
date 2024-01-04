import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget


class SmartTVBuilder(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initializing the workspace for crafting an alternative Smart TV solution
        self.tab_widget = QTabWidget()  # Container for managing various functional modules
        self.setCentralWidget(self.tab_widget)
        self.setWindowTitle("Personal Smart TV")  # Title of the workspace
        self.setWindowIcon(QIcon('assets/icon.png'))  # Icon symbolizing the workspace
        self.create_Browser_tab("https://youtube.com/")  # Starting with a browser tab for initial exploration

    # Method to create the Browser tab for systematic research and development
    def create_Browser_tab(self, url):
        browser = QWebEngineView()  # Component for web interface and exploration
        browser.page().profile().setHttpUserAgent(
            "Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/90.0.4430.212 Large Screen Safari/534.24 GoogleTV/092754")
        browser.load(QUrl(url))  # Loading the provided URL for exploration
        browser.urlChanged.connect(self.track_URL)  # Monitoring the digital pathways
        browser.page().fullScreenRequested.connect(self.enable_fullscreen)  # Activating immersive mode
        self.tab_widget.addTab(browser, "Experimental Browser")  # Integrating the browser for investigation
        self.tab_widget.tabBar().hide()  # Hiding tabs for workspace organization

    # Method to track and document the digital pathways explored
    def track_URL(self, url):
        print("Current Path :", url.toString())  # Recording the pathways for analysis

    # Method to enable full-screen mode for focused experimentation and observation
    def enable_fullscreen(self, request):
        request.accept()  # Accepting the request for an expanded view


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_icon = QIcon('assets/icon.png')  # Symbolizing the workspace for professional representation
    smart_tv = SmartTVBuilder()  # Building a customized Smart TV solution
    smart_tv.show()  # Displaying the workspace for solution development
    sys.exit(app.exec_())  # Managing the event loop for continuous development
