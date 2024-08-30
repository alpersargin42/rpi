from PyQt5 import QtWidgets
import subprocess

class OptionsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(OptionsDialog, self).__init__(parent)
        self.setWindowTitle("Seçiniz")
        self.setGeometry(100, 100, 300, 150)  # Adjust size and position as needed
        
        # Create layout and buttons
        layout = QtWidgets.QVBoxLayout()
        
        self.object_button = QtWidgets.QPushButton("Object")
        self.traffic_sign_button = QtWidgets.QPushButton("Traffic Sign")
        
        layout.addWidget(self.object_button)
        layout.addWidget(self.traffic_sign_button)
        
        self.setLayout(layout)
        
        # Set the size of the dialog
        self.setGeometry(0, 0, 300, 150)
        self.center()
    def center(self):
        # Get the screen geometry
        screen_geometry = QtWidgets.QDesktopWidget().availableGeometry()
        screen_center = screen_geometry.center()
        
        # Calculate the dialog position
        dialog_geometry = self.frameGeometry()
        dialog_geometry.moveCenter(screen_center)
        
        # Move the dialog to the calculated position
        self.move(dialog_geometry.topLeft())        
        # Connect buttons to their slots
        self.object_button.clicked.connect(self.object_selected)
        self.traffic_sign_button.clicked.connect(self.traffic_sign_selected)

    def object_selected(self):
        # Handle object detection with yolov5s.pt
        print("Object detection selected")
        self.run_detection("yolov5s.pt")
        self.accept()

    def traffic_sign_selected(self):
        # Handle traffic sign detection with best_93.pt
        print("Traffic sign detection selected")
        self.run_detection("best_93.pt")
        self.accept()

    def run_detection(self, weights_file):
        # Command to run detect.py with the specified weights file
        command = [
            "python", "yolov5/detect.py",
            "--weights", f"yolov5/{weights_file}",
            "--source", "0"  # Update this to your actual source
        ]
        subprocess.Popen(command)

def analyze_faces():
    dialog = OptionsDialog()
    dialog.exec_()
