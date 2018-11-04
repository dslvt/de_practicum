from PyQt5.QtWidgets import QApplication
import sys

from gui import GUI


app = QApplication([])
gallery = GUI()
gallery.show()
sys.exit(app.exec_())

