# -*- coding: UTF-8 -*-

from outwiker.gui.baseaction import BaseAction
from .i18n import get_


class ChangePageUIDAction (BaseAction):
    """
    Описание действия
    """
    def __init__ (self, application):
        self._application = application

        global _
        _ = get_()

    stringId = u"ChangeUID_ChangePageUID"


    @property
    def title (self):
        return _(u"Change Page Identifier")


    @property
    def description (self):
        return _(u"Change Page Identifier")


    def run (self, params):
        print "Run!"