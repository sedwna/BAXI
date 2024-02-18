import io
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QHBoxLayout

from PyQt6.QtWebEngineWidgets import QWebEngineView
import folium


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("map")
        self.window_width, self.window_height = 360, 640
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        coordinate = (34.791782835906865, 48.48797546205399)
        m = folium.Map(

            title="Hamedan",
            zoom_start=13,
            Location=coordinate
        )
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet('''
    QWidget{
    font-size: 35px;
    }
    
    
    ''')
    myApp = MyApp()
    myApp.show()

    sys.exit(app.exec())
