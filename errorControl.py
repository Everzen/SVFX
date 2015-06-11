#################################################################################################
##3DFRAMEWORK - Developed by Richard Jones
#
##PACKAGE:      SVFX
##SUB-MODULE:   ERROR CONTROL 
#
##VERSION:       1.0
##
##NOTES:  Classes, functions to display Errors in neatly formulated ways 
#################################################################################################


#################################################################################################
##IMPORTS 
from PySide import QtGui, QtCore
import sys
#################################################################################################
##CLASSES, FUNCTIONS AND DATA



#################################################################################################
##CLASSES, FUNCTIONS AND DATA

class Report(QtGui.QWidget):

	def __init__(self, message, eTitle = "A Minor Complaint by the SVFX Team"):
		super(Report, self).__init__()
		topLayout = QtGui.QHBoxLayout() #Finish off with a top level Layout to hold the main splitter
		errorLabel = QtGui.QLabel(message)
		topLayout.addWidget(errorLabel)
		self.setLayout(topLayout)

		self.setGeometry(300, 300, 350, 25)
		self.setWindowTitle(eTitle)    
		self.show()

"""
##TEST CODE TO RUN AS SEPARATE APPLICATION
def main():
	app = QtGui.QApplication(sys.argv)
	badger = Report("This is a shit Error System, This is a shit Error System, This is a shit Error System ,This is a shit Error System, This is a shit Error System, This is a shit Error System, This is a shit Error System ,This is a shit Error System")
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
"""
