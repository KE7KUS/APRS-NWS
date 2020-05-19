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
                    
        #A valid CAP message has two major components - 
        #REQUIRED:  alert
        #OPTIONAL:  info (can be more than one info tag)
    
    def message(self, alert, *info):
        self.alert = alert
        self.info = info
            
        #A CAP message alert element has the following sub-elements - 
        #REQUIRED: identifier, sender, sent, status, msgType, scope
        #OPTIONAL: source, restriction, addresses, code, note, references, incidents
    
    def alert(self, identifier, sender, sent, status, msgType, source=None, scope, restriction=None, addresses=None, code=None, note=None, references=None, incidents=None):
        
        self.xmlns = ("urn:oasis:names:tc:emergency:cap:1.1")   #An alert must include the xmlns attribute referencing CAP URN as the namespace
        self.invalid_chars = re.compile('[ ,&<]')               #The characters [space],[comma],[ampersand], and [less than] are invalid characters
        
        if self.invalid_chars.match(identifier) == None:        #Evaluate the alert identifier for invalud character content
            self.identifier = identifier
        else:
            self.identifier = None
            print('Invalid CAP identifier: ' + identifier + ':Value set to None.')
         
        if self.invalid_chars.match(sender) == None:
            self.sender = sender 
        else:
            self.sender = None
            print('Invalid CAP sender: ' + sender + ':Value set to None.')
        
        self.sent = sent
        self.status = status
        self.msgType = msgType
        self.source = source
        self.scope = scope
        self.restriction = restriction 
        self.addresses = addresses
        self.code = code
        self.note = note 
        self.references = references
        self.incidents = incidents
    def info(self):