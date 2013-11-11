#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Pascal Spörri'

## Compatibility for mensa class
class MenuEntry:
    def __init__(self, date, menu, food):
        self.date, self.menu, self.food = date, menu, food
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, ', '.join('%s=%r' % nvp for nvp in self.__dict__.iteritems()))
class Menu:
    def __init__(self, start_date, end_date, entries):
        self.start_date, self.end_date, self.entries = start_date, end_date, entries
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, ', '.join('%s=%r' % nvp for nvp in self.__dict__.iteritems()))

class Mensa(object):
    def __init__(self, mensaid, noon_menu, evening_menu):
        self.mensaid, self.noon_menu, self.evening_menu = mensaid, noon_menu, evening_menu
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, ', '.join('%s=%r' % nvp for nvp in self.__dict__.iteritems()))
