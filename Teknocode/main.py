# main.py
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from mydesign import Ui_MyPage 
from detect import analyze_faces  
from gps import accident_gps 

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MyPage()
        self.ui.setupUi(self)
        
        self.ui.nesne.clicked.connect(self.start_analysis)
        self.ui.konum.clicked.connect(self.konum_analysis)
        self.ui.cikis.clicked.connect(self.exit_application)

    def start_analysis(self):
        analyze_faces()

    def konum_analysis(self):
        accident_gps(self)

    def exit_application(self):
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
