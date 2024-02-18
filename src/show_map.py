# import io
# import sys
# from PyQt6.QtWidgets import QApplication
# from PyQt6.QtWidgets import QMainWindow
# from PyQt6.QtWidgets import QFileDialog
# from PyQt6.QtWidgets import QVBoxLayout
# from PyQt6.QtWidgets import QWidget
# from PyQt6.QtWidgets import QHBoxLayout
#
# from PyQt6.QtWebEngineWidgets import QWebEngineView
# import folium
#
#
# class MyApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("map")
#         self.window_width, self.window_height = 360, 640
#         self.setMinimumSize(self.window_width, self.window_height)
#
#         layout = QVBoxLayout()
#         self.setLayout(layout)
#
#         coordinate = (34.79681370911893, 48.507035740072375)
#         m = folium.Map(
#
#             title="Hamedan",
#             zoom_start=13,
#             Location=(34.79681370911893, 48.507035740072375)
#         )
#         data = io.BytesIO()
#         m.save(data, close_file=False)
#
#         webView = QWebEngineView()
#         webView.setHtml(data.getvalue().decode())
#         layout.addWidget(webView)
#
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myApp = MyApp()
#     myApp.show()
#     sys.exit(app.exec())




import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView


class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Google Maps Example")
        self.setGeometry(100, 100, 800, 600)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec())

