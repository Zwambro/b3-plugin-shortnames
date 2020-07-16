#
# ################################################################### #
#                                                                     #
#  Shortnames Plugin for BigBrotherBot(B3) (www.bigbrotherbot.com)    #
#  Copyright (c) 2020 Zwambro                                         #
#                                                                     #
#  This program is free software; you can redistribute it and/or      #
#  modify it under the terms of the GNU General Public License        #
#  as published by the Free Software Foundation; either version 2     #
#  of the License, or (at your option) any later version.             #
#                                                                     #
#  This program is distributed in the hope that it will be useful,    #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of     #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the       #
#  GNU General Public License for more details.                       #
#                                                                     #
#  You should have received a copy of the GNU General Public License  #
#  along with this program; if not, write to the Free Software        #
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA      #
#  02110-1301, USA.                                                   #
#                                                                     #
# ################################################################### #
# CHANGELOG:
#  03.11.2020 - v1.0 - Zwambro
#  - first release.
#
#  16/07/2020 - v1.1 - Zwambro
#  - forgot to add ' (thanks to diamante0018 for the report)
#

__version__ = '1.1'
__author__ = 'Zwambro'

import b3
import b3.events
import b3.plugin
from b3 import functions
import re

class ShortnamesPlugin(b3.plugin.Plugin):
    _adminPlugin = False
    requiresConfigFile = False

    def onStartup(self):

        self._adminPlugin = self.console.getPlugin('admin')
        if not self._adminPlugin:
            self.debug('Could not find admin plugin')
            return False
        else:
            self.debug('Plugin loaded normal')
        self.registerEvent(b3.events.EVT_CLIENT_AUTH)
        self.debug('Started')

    def onEvent(self, event):
        if event.type == b3.events.EVT_CLIENT_AUTH:
            name = str(event.client.name.replace(" ", ""))
            if len(name) < 3:
                self.debug("(%s) has short name" %(name))
                event.client.kick("Are you bot?", keyword="short_name")
                return True
            else:
                self.debug('Client has more than 3 characters on his in game name')
                return False