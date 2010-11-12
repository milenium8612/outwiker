#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Tue Mar 23 21:59:58 2010

import gettext
import platform
import os

import wx

from core.config import GeneralConfig, getConfigPath
import core.system


class OutWiker(wx.App):
	def __init__(self, *args, **kwds):
		wx.App.__init__ (self, *args, **kwds)


	def __initLocale (self):
		language = self.config.languageOption.value

		langdir = os.path.join (core.system.getCurrentDir(), u'locale')
		try:
			lang = gettext.translation(u'outwiker', langdir, languages=[language])
		except IOError:
			lang = gettext.translation(u'outwiker', langdir, languages=["en"])
			wx.MessageBox (u"Can't load language: %s" % language, u"Error", wx.ICON_ERROR | wx.OK) 

		lang.install(unicode=1)

	
	def getConfig (self):
		return self.config


	def OnInit(self):
		self._configFileName = getConfigPath (u".outwiker", u"outwiker.ini")
		self.config = GeneralConfig (self._configFileName)
		self.__initLocale()

		from gui.MainWindow import MainWindow
		wx.InitAllImageHandlers()
		mainWnd = MainWindow(None, -1, "")
		self.SetTopWindow(mainWnd)
		mainWnd.Show()
		return 1

# end of class OutWiker

if __name__ == "__main__":
	#print sys.argv[0]
	outwiker = OutWiker(0)
	outwiker.MainLoop()
