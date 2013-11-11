#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Pascal Spörri'

from parse import parse
from menu import MenuEntry, Menu, Mensa

mensa_lut = {
    'mm': 11,
    'cla': 13,
    'etz': 9,
    'hph': 1,
    'cab': 3,
    'ifw': 6,
} 

mensa_url = "http://www.gastro.ethz.ch/menuela_overview?viewType=weekly&facility={facility}&language={language}"

# Alternative feeds provided for the mensa app
# http://glyph.ethz.ch/eth-ws/mensas/detail?ids=
# http://glyph.ethz.ch/eth-ws/mensas

def get_menu(id, lang="DE"):
    import urllib
    html =  urllib.urlopen(mensa_url.format(facility=mensa_lut[id], language=lang))
    return parse(html)
def get_mensa(id, lang="DE"):
    menu_noon, menu_evening = get_menu(id, lang)
    return Mensa(id, menu_noon, menu_evening)

