#################################################################################################
##3DFRAMEWORK - Developed by Richard Jones
#
##PACKAGE:      3DFRAMEWORK
##SUB-MODULE:   SYSTEM
#
##VERSION:      1.0
##
##NOTES: 
#################################################################################################


#################################################################################################
##IMPORTS

import sys
from pymel.all import *
import pymel.core as pm
import os
import xml.etree.ElementTree as xml


import fileControl
import errorControl as tDError

#################################################################################################
##CLASSES, FUNCTIONS AND DATA


class Check():
	"""Class with a series of functions to check aspects of our setup"""
	def getEnvironment(self):
		"""Function to print out all the paths that are associated with Maya system setup"""
		sysPaths = sys.path
		
		print "\nsys.paths are:"
		for sysPath in sysPaths:
			print sysPath


class User():
	"""A Class to carry all the user information in a nice neat object, using Excel XML data Approach"""	
	#Methods
	def __init__(self, xmlUserData):
		"""Function to strip out user data into a neat object"""
		self.uForename = xmlUserData.find("Forename").text
		self.uSurname = xmlUserData.find("Surname").text
		self.uName = self.uForename + self.uSurname
		self.uID = xmlUserData.find("ID").text
		self.uCourse = xmlUserData.find("Course").text
		self.uYear = xmlUserData.find("Year").text
		self.uStatus = xmlUserData.find("Status").text

	def getForename(self):
		"""Function to return the username"""
		return self.uForename

	def getSurname(self):
		"""Function to return the username"""
		return self.uSurname
	
	def getName(self):
		"""Function to return the username"""
		return self.uName
	
	def getID(self):
		"""Function to return ID"""
		return self.uID
		
	def getStatus(self):
		"""Function to return Status"""
		return self.uStatus

	def getYear(self):
		"""Function to return Status"""
		return self.uYear

	def getCourse(self):
		"""Function to return Course"""
		return self.uCourse


class EngineInfo():
	"""A Class to strip out all major information regarding the setup of the company"""
	companyXML = None
	
	userInfo = []
	
	def __init__(self):
		"""Function to setup and strip out company info"""
		self.findCompanyXML()
		#Now generate the User Info
		self.generateUserInfo()
	
	def findCompanyXML(self):
		"""Function to look through script and python paths to find the TDFramework.xml document"""
		#Collect paths
		pathsTotal = [] #Crete empty path variable that we can add stuff to later if we like

		#Add in all the system paths to, to check them	
		pathsTotal += sys.path
		
		#Now check to see if the file exists! 
		for path in pathsTotal:
			fullPath = path + "/SVFX/SVFX_Structure.xml"
			pathTest = fileControl.FileMan(fullPath)
			if pathTest.exists():
				pathFound = True
				self.companyXML = fileControl.XMLMan()
				self.companyXML.setLoad(pathTest.getFile())
				return self.companyXML

	def getCompanyName(self):
		"""Function to return the company name as a string"""
		if self.companyXML != None:
			compData = self.companyXML.findBranch("Company_Name")
			return (compData[0].get("Name"))

	def generateUserInfo(self):
		"""Function return information on all users using the Excel XML data Approach"""
		if self.companyXML != None:
			self.userInfo = []
			userDataPath = self.getEnginePath("UserData")
			userDataXML = fileControl.XMLMan()
			userDataXML.setLoad(userDataPath)
			userData = userDataXML.findBranch("User")
			for u in userData:
				uData = User(u)
				self.userInfo.append(uData)
			return self.userInfo

	
	def getUserInfo(self):
		"""Function to return collected user data"""
		if len(self.userInfo) == 0:
			print "TError: There are no users, or the user data has not been generated properly"
		return self.userInfo



	def getUserNames(self):
		"""Function to return a list of user names"""
		if self.companyXML != None:
			usernames = []
			userData = self.companyXML.findBranch("User")
			for user in userData:
				usernames.append(user.get("Name"))
			return usernames
	
	def getUserFromName(self, userName):
		"""A function to return the total user info from the given string name"""
		reqUser = None
		for u in self.userInfo:
			if u.getName() == userName:
				reqUser = u
		return reqUser
	
	def getCurrentUser(self):
		"""A function to return all the user info for the current user - return User Object"""
		cUserName = os.environ.get("USERNAME")
		reqUser = None
		for u in self.userInfo:
			if u.getID() == cUserName:
				reqUser = u
		return reqUser
		
		
	def getEnginePath(self, pathName):
		"""Function to grab the details of specific System Paths"""
		if self.companyXML != None:
			engineRoot = self.companyXML.findBranch("EngineRoom")
			enginePath = self.companyXML.findBranch(pathName)
			return (engineRoot[0].get("Path") + "/" + enginePath[0].get("Path"))
	
	def getProjectPath(self):
		"""Function to return the project path"""
		currentProjectPath = pm.workspace.path
		return currentProjectPath



class ToolHelp():
	hName = ""
	version = ""
	instruction = ""
	patchRelease = ""
	videoFile = None

	def __init__(self,toolName):
		engineInfo = EngineInfo()
		helpFolder = engineInfo.getEnginePath("ToolHelp")
		
		helpXML= fileControl.XMLMan()
		helpXML.setLoad(helpFolder + "/tool_Help.xml")
		helpXMLBranch = helpXML.findBranch(toolName)
		#Now dig out the tool tree that we are interested in
		self.hName = helpXMLBranch.attrib.get("Name")
		self.version = helpXMLBranch.attrib.get("Version")
		self.patchRelease = helpXMLBranch.attrib.get("PatchRelease")
		self.instruction = helpXMLBranch.attrib.get("Instruction")
		##Now Find Video File
		self.videoFile = fileControl.FileMan(helpFolder + "/" + toolName + ".mov")
		
	def getName(self):
		return self.hName
	
	def getVersion(self):
		return self.version
	
	def getInstruction(self):
		return self.instruction
	
	def getPatchRelease(self):
		return self.patchRelease

	def playVideo(self):
		if videoFile.exists():
			tDError.Report("Here is a lovely video file, Look I am playing")
		else:
			tDError.Report("Well this is a pickle. There does not seem to be a video")

""" XML READING ERROR CORRECT"""