# -*- coding: utf-8 -*-

from outwiker.gui.baseaction import BaseAction


class SwitchCodeResultAction (BaseAction):
    """
    Переключение между кодом (вики или HTML) и результатом рендеринга
    """
    stringId = u"SwitchCodeResult"

    def __init__(self, application):
        self._application = application

    @property
    def title(self):
        return _(u"Code / Preview")

    @property
    def description(self):
        return _(u"Switch Code <--> Preview for HTML and wiki pages")

    def run(self, params):
        assert self._application.mainWindow is not None
        assert self._application.mainWindow.pagePanel is not None

        self._application.mainWindow.pagePanel.pageView.switchCodeResult()
