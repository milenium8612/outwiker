#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os.path

from basemainwnd import BaseMainWndTest
from core.tree import RootWikiPage, WikiDocument
from pages.text.textpage import TextPageFactory
from core.application import Application
from test.utils import removeWiki
from core.attachment import Attachment


class AttachPanelTest (BaseMainWndTest):
	"""
	Тесты окна со списком прикрепленных файлов
	"""
	def setUp (self):
		BaseMainWndTest.setUp (self)

		self.path = u"../test/testwiki"
		removeWiki (self.path)

		self.wikiroot = WikiDocument.create (self.path)

		TextPageFactory.create (self.wikiroot, u"Страница 1", [])
		TextPageFactory.create (self.wikiroot, u"Страница 2", [])
		TextPageFactory.create (self.wikiroot[u"Страница 2"], u"Страница 3", [])
		TextPageFactory.create (self.wikiroot[u"Страница 2/Страница 3"], u"Страница 4", [])
		TextPageFactory.create (self.wikiroot[u"Страница 1"], u"Страница 5", [])

		self.page = self.wikiroot[u"Страница 2/Страница 3"]

		filesPath = u"../test/samplefiles/"
		self.files = [u"accept.png", u"add.png", u"anchor.png", u"файл с пробелами.tmp", u"dir"]
		self.fullFilesPath = [os.path.join (filesPath, fname) for fname in self.files]


	def tearDown (self):
		BaseMainWndTest.tearDown (self)
		Application.wikiroot = None
		removeWiki (self.path)


	def testEmpty (self):
		self.assertNotEqual (None, self.wnd.attachPanel)
		self.assertNotEqual (None, self.wnd.attachPanel.attachList)
		self.assertNotEqual (None, self.wnd.attachPanel.toolbar)
		self.assertEqual (0, self.wnd.attachPanel.attachList.GetItemCount())


	def testAttach1 (self):
		attach = Attachment (self.page)
		attach.attach (self.fullFilesPath)

		Application.wikiroot = self.wikiroot
		Application.wikiroot.selectedPage = self.page
		self.assertEqual (self.wnd.attachPanel.attachList.GetItemCount(), len (self.fullFilesPath))

		attach.removeAttach ([self.files[0]])
		self.assertEqual (self.wnd.attachPanel.attachList.GetItemCount(), len (self.fullFilesPath) - 1)


	def testAttach2 (self):
		Application.wikiroot = self.wikiroot
		Application.wikiroot.selectedPage = self.page

		attach = Attachment (self.page)
		attach.attach (self.fullFilesPath)

		self.assertEqual (self.wnd.attachPanel.attachList.GetItemCount(), len (self.fullFilesPath))


	def testAttach3 (self):
		Application.wikiroot = self.wikiroot
		Application.wikiroot.selectedPage = self.page

		attach = Attachment (self.page)
		attach.attach (self.fullFilesPath[:1])

		self.assertEqual (self.wnd.attachPanel.attachList.GetItemCount(), 1)
		attach.attach (self.fullFilesPath[1:])

		self.assertEqual (self.wnd.attachPanel.attachList.GetItemCount(), len (self.fullFilesPath))


	def testAttach4 (self):
		attach = Attachment (self.page)
		attach.attach (self.fullFilesPath)

		Application.wikiroot = self.wikiroot
		Application.wikiroot.selectedPage = self.page
		self.assertEqual (self.wnd.attachPanel.attachList.GetItemCount(), len (self.fullFilesPath))

		Application.wikiroot.selectedPage = self.wikiroot[u"Страница 1"]
		self.assertEqual (self.wnd.attachPanel.attachList.GetItemCount(), 0)


	def testAttach5 (self):
		attach = Attachment (self.page)
		attach.attach (self.fullFilesPath)

		Application.wikiroot = self.wikiroot
		Application.wikiroot.selectedPage = self.page
		self.assertEqual (self.wnd.attachPanel.attachList.GetItemCount(), len (self.fullFilesPath))

		Application.wikiroot = None
		self.assertEqual (self.wnd.attachPanel.attachList.GetItemCount(), 0)


	def testAttach6 (self):
		attach = Attachment (self.page)
		attach.attach (self.fullFilesPath)

		Application.wikiroot = self.wikiroot
		Application.wikiroot.selectedPage = self.page
		self.assertEqual (self.wnd.attachPanel.attachList.GetItemCount(), len (self.fullFilesPath))

		Application.wikiroot.selectedPage = None
		self.assertEqual (self.wnd.attachPanel.attachList.GetItemCount(), 0)


	def testAttach7 (self):
		attach = Attachment (self.page)
		attach.attach (self.fullFilesPath)

		self.wikiroot.selectedPage = self.page
		Application.wikiroot = self.wikiroot

		self.assertEqual (self.wnd.attachPanel.attachList.GetItemCount(), len (self.fullFilesPath))

		Application.wikiroot.selectedPage = None
		self.assertEqual (self.wnd.attachPanel.attachList.GetItemCount(), 0)



