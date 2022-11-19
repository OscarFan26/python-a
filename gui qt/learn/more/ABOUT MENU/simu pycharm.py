# encoding: utf-8 #
"""
==========
File Name:              simu pycharm
Author:                 Oscar Fan
Date:                   2022/1/28
requirements:           PyQt6
==========
"""
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QMenu
from PyQt6.QtGui import QAction


class Main(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		menubar = self.menuBar()
		# filemenu = menubar.addMenu('File')
		# impMenu = QMenu('Import', self)
		#
		# impAct = QAction('>>> Import Anything you want <<<', self)
		# impMenu.addAction(impAct)
		#
		# newAct = QAction('New', self)
		# # 在文件中添加newAct和impMenu
		# filemenu.addAction(newAct)
		# filemenu.addMenu(impMenu)

		# Next part the code will be a little bit crazy!

		# ------ Main Menu: File ------
		MainMenu_File = menubar.addMenu('File')
		# All Submenus/Actions which belong to Main Menu: File
		# Actions come first!
		File_NewProject = QAction('New Project... ', self)
		File_New = QAction('New... ', self)
		File_NewScratchFile = QAction('New Scratch File ', self)
		File_Open = QAction('Open... ', self)
		File_SaveAs = QAction('Save As... ', self)
		File_AttachProject = QAction('Attach Project... ', self)
		File_CloseProject = QAction('Close Project', self)
		File_RenameProject = QAction('Rename Project', self)
		File_Settings = QAction('Settings... ', self)
		File_SaveAll = QAction('Save All', self)
		File_ReloadAllFromDisk = QAction('Reload All from Disk ', self)
		File_RepairIDE = QAction('Repair IDE... ', self)
		File_InvalidateCashes = QAction('Invalidate Cashes...\t', self)
		File_RestartIDE = QAction('Restart IDE... ', self)
		File_SaveFileAsTemplate = QAction('Save File As Template... ', self)
		File_Print = QAction('Print... ', self)
		File_PowerSaveMode = QAction('Power Save Mode', self)
		File_Exit = QAction('Exit', self)
		# End
		# Then is Submenus!
		File_OpenRecent = QMenu('Open Recent', self)
		File_FileProperties = QMenu('File Properties', self)
		File_LocalHistory = QMenu('Local History', self)
		File_ManageIDESettings = QMenu('Manage IDE Settings', self)
		File_NewProjectsSetup = QMenu('New Project Setup', self)
		File_Export = QMenu('Export', self)
		# End
		# Then add all actions/submenus into the main menu: File
		MainMenu_File.addAction(File_NewProject)
		MainMenu_File.addAction(File_New)
		MainMenu_File.addAction(File_NewScratchFile)
		MainMenu_File.addAction(File_Open)
		MainMenu_File.addAction(File_SaveAs)
		MainMenu_File.addAction(File_AttachProject)
		MainMenu_File.addMenu(File_OpenRecent)
		MainMenu_File.addAction(File_CloseProject)
		MainMenu_File.addAction(File_RenameProject)
		MainMenu_File.addAction(File_Settings)
		MainMenu_File.addMenu(File_FileProperties)
		MainMenu_File.addMenu(File_LocalHistory)
		MainMenu_File.addAction(File_SaveAll)
		MainMenu_File.addAction(File_ReloadAllFromDisk)
		MainMenu_File.addAction(File_RepairIDE)
		MainMenu_File.addAction(File_InvalidateCashes)
		MainMenu_File.addAction(File_RestartIDE)
		MainMenu_File.addMenu(File_ManageIDESettings)
		MainMenu_File.addMenu(File_NewProjectsSetup)
		MainMenu_File.addAction(File_SaveFileAsTemplate)
		MainMenu_File.addMenu(File_Export)
		MainMenu_File.addAction(File_Print)
		MainMenu_File.addAction(File_PowerSaveMode)
		MainMenu_File.addAction(File_Exit)
		# Add Complete. Next one: All Submenu's Submenus
		# <--- Open Recent -->
		# * Actions
		File_OpenRecent_None = QAction('(None)', self)
		# * No Submenus
		# Add them into the Open Recent
		File_OpenRecent.addAction(File_OpenRecent_None)
		# ---> END <---
		# <--- File Properties --->
		File_FileProperties_FileEncoding = QAction('File Encoding', self)
		File_FileProperties_RemoveBOM = QAction('Remove BOM', self)
		File_FileProperties_AddBOM = QAction('Add BOM', self)
		File_FileProperties_AssociateWithFileType = QAction(
			'Associate with File Type... ', self)
		File_FileProperties_MakeFileReadOnly = QAction('Make File Read-Only',
		                                               self)
		# * Submenus
		File_FileProperties_LineSeparators = QMenu('Line Separators', self)
		# Add them to File Properties
		File_FileProperties.addAction(File_FileProperties_FileEncoding)
		File_FileProperties.addAction(File_FileProperties_RemoveBOM)
		File_FileProperties.addAction(File_FileProperties_AddBOM)
		File_FileProperties.addAction(File_FileProperties_AssociateWithFileType)
		File_FileProperties.addAction(File_FileProperties_MakeFileReadOnly)
		File_FileProperties.addMenu(File_FileProperties_LineSeparators)
		# TODO: WARNING THIS ONE HAS 3 SUBMENU'S SUBMENUS!!!
		# ---> END <---
		# <--- Local History --->

		File_LocalHistory_ShowHistory = QAction('Show History', self)
		File_LocalHistory_ShowHisttoryForSelection = QAction(
			'Show History for Selection', self)
		File_LocalHistory_PutLabel = QAction('Put Label')
		#  * No Submenus
		# Add them to Local History
		File_LocalHistory.addAction(File_LocalHistory_ShowHistory)
		File_LocalHistory.addAction(File_LocalHistory_ShowHisttoryForSelection)
		File_LocalHistory.addAction(File_LocalHistory_PutLabel)
		# ---> END <---
		# <---Manage IDE Settings  --->
		File_ManageIDESettings_ImportSettings = QAction('Import Settings... ',
		                                                self)
		File_ManageIDESettings_ExportSettings = QAction('Export Settings... ',
		                                                self)
		File_ManageIDESettings_RestoreDefaultSettings = QAction(
			'Restore Default Settings', self)
		File_ManageIDESettings_SettingsRepository = QAction(
			'Settings Repository... ', self)
		File_ManageIDESettings_SyncWithSettingsRepository = QAction(
			'Sync with Settings '
			'Repository', self)
		File_ManageIDESettings_SyncSettingsToJetbrainsAccount = QAction(
			'Sync Settings to Jetbrains'
			'Account', self)
		# * No Submenus
		# Add them to Manage IDE Settings
		File_ManageIDESettings.addAction(File_ManageIDESettings_ImportSettings)
		File_ManageIDESettings.addAction(File_ManageIDESettings_ExportSettings)
		File_ManageIDESettings.addAction(
			File_ManageIDESettings_RestoreDefaultSettings)
		File_ManageIDESettings.addAction(
			File_ManageIDESettings_SettingsRepository)
		File_ManageIDESettings.addAction(
			File_ManageIDESettings_SyncWithSettingsRepository)
		File_ManageIDESettings.addAction(
			File_ManageIDESettings_SyncSettingsToJetbrainsAccount)
		#  --- > END <---
		# <--- New Projects Setup --->
		File_NewProjectsSetup_SettingsForNewProjects = QAction(
			'Settings for New Project... ', self)
		File_NewProjectsSetup_RunConfigurationTemplates = QAction(
			'Run Configuration '
			'Templates... ', self)
		# * No Submenus
		#  Add them to New Projects Setup
		File_NewProjectsSetup.addAction(
			File_NewProjectsSetup_SettingsForNewProjects)
		File_NewProjectsSetup.addAction(
			File_NewProjectsSetup_RunConfigurationTemplates)
		# ---> END <---
		# <--- Export --->

		# End All
		self.setGeometry(300, 100, 850, 550)
		self.setWindowTitle('                             '
		                    '                             '
		                    '              '
		                    'Pycharm - C:/Users/Oscar Fan/Desktop/Pythons')
		self.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	m = Main()
	sys.exit(app.exec())
