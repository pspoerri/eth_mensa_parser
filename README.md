ETH Mensa Parser
================

ETH Mensa Parser for forum.vis.ethz.ch that integrates into mensa.py.

The parser currently parses the mensa websites available under the following url:
    
    http://www.gastro.ethz.ch/menuela_overview?viewType=weekly&facility={facility}&language={language}

hence the submodule is named menuelaparser.

An alternative would be to reuse the RSS feeds made available for the ETH App:

    http://glyph.ethz.ch/eth-ws/mensas/detail?ids=
    http://glyph.ethz.ch/eth-ws/mensas

The support for said RSS feeds remains unclear and the author was too lazy to parse said websites.
