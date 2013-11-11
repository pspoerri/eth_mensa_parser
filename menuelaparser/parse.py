#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Pascal Spörri'

from bs4 import BeautifulSoup
table_day_lut = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
]

# Scans for date in header and returns lut for a mapping
def compute_dates(soup):
    header = soup.find('h2').find(text=True)
    import re
    m = re.match(".+\s(\d{1,2}\.\d{1,2}\.\d{4})", header).group(1)
    from datetime import timedelta
    from dateutil import parser
    date = parser.parse(m)
    dates = {}
    for day in table_day_lut:
        dates[day] = date
        date += timedelta(days=1)

    return dates

# Parse menu from the table
def parse_menu(soup_table):
    rows = soup_table.findAll('tr')
    mensa = str(rows[0].find('td').find(text=True))
    menu = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': [],
    }

    # Assuming the first row shows the weekdays
    for tr in rows[2::]:
        cols = tr.findAll('td')
        menu_type = cols[0].find(text=True)
        dayidx = 0
        # Also assuming the first day is a Monday :)
        for td in cols[2::]:
            day_menu = ' '.join(td.find_all(text=True))
            menu[table_day_lut[dayidx]].append((menu_type, day_menu))
            dayidx += 1
    return mensa, menu

def parse(html):
    soup = BeautifulSoup(html)
    date_lut = compute_dates(soup)
    soup_tables = soup.find_all('table')

    from menu import Menu, MenuEntry

    menu_noon = None
    menu_evening = None
    for tbl in soup_tables:
        (mensa, menu) = parse_menu(tbl)
        entries = []
        for day, daily_menues in menu.iteritems():
            date = date_lut[day]
            for menue in daily_menues:
                entries.append(MenuEntry(date, menue[0], menue[1]))
        if menu_noon == None:
            menu_noon = entries
        elif menu_evening == None:
            menu_evening = entries
        else:
            break
            # Ignore the rest
    return menu_noon, menu_evening
