#################################################################################################
##3DFRAMEWORK - Developed by Richard Jones
#
##PACKAGE:      3DFRAMEWORK
##SUB-MODULE:   FILECONTROL 
#
##VERSION:       1.0
##
##NOTES:  Classes, functions to display Errors in neatly formulated ways 
#################################################################################################


#################################################################################################
##IMPORTS 

import maya.cmds as cmds


#################################################################################################
##CLASSES, FUNCTIONS AND DATA



#################################################################################################
##CLASSES, FUNCTIONS AND DATA

class Report():
	"""Class to display a neatly layed out error message"""
	def __init__(self, message, eTitle = "A Minor Complaint by 3DFramework"):
		self.name = "ImporterFileInfo"

		if (cmds.window(self.name, q=1, exists=1)): cmds.deleteUI(self.name)
		self.eWindow = cmds.window(self.name, title=eTitle, sizeable = False, resizeToFitChildren = True)
		form = cmds.columnLayout()
		cmds.messageLine()
		cmds.scrollField( editable=False, wordWrap=True, text=message, height = 67, width = 400 )
		cmds.messageLine()	
		cmds.button("close", label = "Close", width = 400, command = self.closeUI)
		cmds.window(self.eWindow, e=1)
		cmds.showWindow(self.eWindow)
		cmds.setFocus("close")
	
	def closeUI(self, *args):
		cmds.deleteUI(self.name)