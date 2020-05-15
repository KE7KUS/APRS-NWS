#!/usr/bin/python

# NWS APRS Feedparser
# Copyright 2020 Kurt Kochendarfer, KE7KUS

# This file is part of APRS-NWS.
# APRS-NWS is free sofware: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 or the License, or (at your option) any later version.

# APRS-NWS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with APRS-NWS.  If not, see <https://www.gnu.org/licenses>.

from datetime import datetime
import re

class CAP11:
    """Class definition for a CAP v1.1 message - http://www.oasis-open.org/committees/download.php/14759/emergency-CAPv1.1/pdf"""

    def __init__(self):
                    
        #A valid CAP message has four components - 
        #REQUIRED:  alert
        #OPTIONAL:  info, resource, area
    
        def message(self, alert, info=None, resource=None, area=None):
            self.alert = alert
            if self.info is None:
                self.info = ""
            else:
                self.info = info
            if resource is None:
                self.resource = ""
            else:
                self.resource = resource
            if self.area is None:
                self.area = ""
            else:
                self.area = area
                
        #A CAP message alert element has the following sub-elements - 
        #REQUIRED: identifier, sender, sent, status, msgType, scope
        #OPTIONAL: source, restriction, addresses, code, note, references, incidents
    
        def alert(self,identifier,sender,sent,status,msgType,source=None,scope,restriction=None,addresses=None,code=None,note=None,references=None,incidents=None):
            self.xmlns = ("urn:oasis:names:tc:emergency:cap:1.1")   #An alert must include the xmlns attribute referencing CAP URN as the namespace
            self.identifier = identifier
            self.sender = sender
            self.sent = sent
            self.status = status
            self.msgType = msgType
            if self.source is None:
                self.source = ""
            else:
                self.source = source
            self.scope = scope
            if self.restriction is None:
                self.restriction = ""
            else:
                self.restriction = restriction 
            if self.addresses is None:
                self.addresses = ""
            else:
                self.addresses = addresses
            if self.code is None:
                self.code = ""
            else:
                self.code = code
            if self.note is None:
                self.note = ""
            else:
                self.note = note 
            if self.references is None:
                self.references = ""
            else:
                self.references = references
            if self.incidents is None:
                self.incidents = ""
            else:
                self.incidents = incidents