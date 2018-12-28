# -*- coding: UTF-8 -*-
import os
import sys
import time
import webbrowser
from urllib import urlencode
from urlparse import parse_qsl

import xbmc
import xbmcplugin
from xbmcgui import ListItem


def buildUrl(url):
    return sys.argv[0] + '?' + urlencode({'url': url})


def callBrowser(url):
    if url:
        if xbmc.getCondVisibility('system.platform.android'):
            xbmc.executebuiltin('StartAndroidActivity(,android.intent.action.VIEW,,%s)' % url)
        else:
            webbrowser.open(url)


HANDLE = int(sys.argv[1])
xbmcplugin.setContent(HANDLE, 'files')

params = {key: value for key, value in parse_qsl(sys.argv[2][1:])}

if 'url' in params:
    callBrowser(params['url'])
    xbmc.executebuiltin('Container.Update(%s,replace)' % sys.argv[0])
else:    
    dirItems = (
        (buildUrl('https://olpair.com/pair'), ListItem('[B]Openload[/B] (https://openload.co)'), True),
        (buildUrl('https://vev.io/pair'), ListItem('[B]Vev-io[/B] (https://vev.io)'), True),
        (buildUrl('https://streamango.com/pair'), ListItem('[B]Streamango[/B] (https://streamango.com)'), True),
        (buildUrl('https://streamcherry.com/pair'), ListItem('[B]Streamcherry[/B] (https://streamcherry.com)'), True),
        (buildUrl('https://vidup.io/pair'), ListItem('[B]Vidup-io[/B] (https://vidup.io)'), True)
        #(buildUrl('https://vshare.eu/pair'), ListItem('[B]vShare[/B]'), True)
        #(buildUrl('https://www.flashx.tv/?op=login&redirect=https://www.flashx.tv/pairing.php'), ListItem('[B]FlashX[/B]'), True)
    )
    xbmcplugin.addDirectoryItems(HANDLE, dirItems)
xbmcplugin.endOfDirectory(int(sys.argv[1]))