__version__ = '1.0'
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

    def stripColors(self, s):
        return re.sub('\^[0-9]{1}', '', s)

    def onEvent(self, event):
        if event.type == b3.events.EVT_CLIENT_AUTH:
            name = str(event.client.name.replace(" ", ""))
            guid = str(event.client.guid)
            if len(name) < 3:
                self.debug("(%s) have short name" %(name))
                event.client.ban("Are you bot dickhead?", keyword="famous_hacker", silent=True)
                return
            elif guid == "NOGUIDWARNINGNOGUIDWARNINGNOGUID":
                self.debug("(%s) have generic guid" %(name))
                event.client.ban("Are you bot motherfucker?", keyword="famous_hacker", silent=True)
                return 
            elif guid == "123456789NoGuid0123456789NoGuid0":
                self.debug("(%s) have generic guid" %(name))
                event.client.ban("Are you bot motherfucker?", keyword="famous_hacker", silent=True)
                return 