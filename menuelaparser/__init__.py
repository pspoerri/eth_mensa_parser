#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Pascal Spörri'

from parse import parse
from menu import MenuEntry, Menu, Mensa

mensa_url = "http://www.gastro.ethz.ch/menuela_overview?viewType=weekly&facility={facility}&language={language}"

# Alternative feeds provided for the mensa app
# http://glyph.ethz.ch/eth-ws/mensas/detail?ids=
# http://glyph.ethz.ch/eth-ws/mensas


def get_mensa(id, lang="DE"):
    import urllib

    html =  urllib.urlopen(mensa_url.format(facility=id, language=lang))
    menu_noon, menu_evening = parse(html)
    return Mensa(id, menu_noon, menu_evening)

