import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6 import QtCore


class MapWindow(QMainWindow):

    def setupUi(self, BAXI):
        BAXI.setObjectName("BAXI")
        BAXI.resize(360, 640)
        BAXI.setMinimumSize(QtCore.QSize(360, 640))
        BAXI.setMaximumSize(QtCore.QSize(360, 640))

        self.setWindowTitle("Google Maps Example")
        self.setGeometry(0, 0, 360, 640)
        self.setMinimumSize(QtCore.QSize(360, 640))
        self.setMaximumSize(QtCore.QSize(360, 640))

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Create a QWebEngineView to display Google Maps
        self.webview = QWebEngineView()
        layout.addWidget(self.webview)

        # Load the map centered on a specific location
        self.load_map(34.79236691747345, 48.48875557706634)

    def load_map(self, lat, lon):
        # Load the URL of Google Maps centered on the specified location
        url = f"https://www.google.com/maps/@{lat},{lon},15.5z?entry=ttu"
        self.webview.setUrl(QUrl(url))
