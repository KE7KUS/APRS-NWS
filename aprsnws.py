#!/usr/bin/python3

# APRS-NWS
# Copyright 2021, Kurt Kochendarfer (KE7KUS)

# ===GNU Public License v3===
# This file is part of APRS-NWS.

# APRS-NWS is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License 
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# APRS-NWS is distributed in the hope that it will be useful,but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with APRS-NWS.  If not, see <https://www.gnu.org/licenses/>.

#-----IMPORTS-----#
import time, datetime, requests, os, sys
import lxml.etree as et
from io import BytesIO
import nm, cap

# TODO: Automate import/install of dependency libraries via pip

#-----GLOBALS-----#
LOCALE = ('nm')
t = None

#TODO: Modify getAlerts to handle multiple locales

def getAlerts(locale):
    """Gets alerts for the locale designated at XMLHandler class instatiation."""
    try:
        newsfeed = ('https://alerts.weather.gov/cap/' + str(locale) + '.php?x=0')
        r = requests.get(newsfeed)
        b = BytesIO(r.content)
        t = et.parse(b)
        root = t.getroot()
        return t
    
    except Exception as ex:
        print(f'getAlerts Exception: {ex}')

#-----CLASSES-----#
class XMLHandler:
    """Methods for extracting alert data from the NWS ATOM feed."""

    def __init__(self):
        """Initializes XML handler to parse imported XML (normally from an instance of the webHandler class). 
        
        Namespaces are unique to the XML file being parsed and are defined in the self.ns variable.  Even if only using a default namespace, that namespace MUST be defined and used in path construction for lxml to parse the XML file.  See <https://lxml.de/xpathxslt.html> for more details."""
        
        self.ns = {"atom":"http://www.w3.org/2005/Atom",
                   "cap":"urn:oasis:names:tc:emergency:cap:1.1",
                   "ha":"http://www.alerting.net/namespace/index_1.0"
                  }
            
    def getEntryId(self, enum, default='N/A'):
        """Get feed entry ID number."""
        self.enum = enum
        
        try:
            self.path = 'atom:entry[' + str(self.enum) + ']/atom:id/text()'
            self.i = getAlerts(LOCALE).xpath(self.path, namespaces=self.ns)
            return self.i if self.enum else default
        
        except Exception as ex:
            print(f'getEntryId Exception: {ex}')
    
    def getEntryPublishedTime(self, enum, default='N/A'):
        """Get feed entry time published."""
        self.enum = enum
        
        try:
            self.path = 'atom:entry[' + str(self.enum) + ']/atom:published/text()'
            self.i = getAlerts(LOCALE).xpath(self.path, namespaces=self.ns)
            return self.i if self.enum else default
        
        except Exception as ex:
            print(f'getEntryPublishedTime Exception: {ex}')
    
    def getEntryUpdatedTime(self, enum, default='N/A'):
        """Get feed entry time updated."""
        self.enum = enum
        
        try:
            self.path = 'atom:entry[' + str(self.enum) + ']/atom:updated/text()'
            self.i = getAlerts(LOCALE).xpath(self.path, namespaces = self.ns)
            return self.i if self.enum else default
        
        except Exception as ex:
            print(f'getEntryUpdatedTime Exception: {ex}')
    
    def getEntryEventType(self, enum, default='N/A'):
        """Get feed entry event type."""
        self.enum = enum
        
        try:
            self.path = 'atom:entry[' + str(self.enum) + ']/cap:event/text()'
            self.i = getAlerts(LOCALE).xpath(self.path, namespaces = self.ns)
            return self.i if self.enum else default
        
        except Exception as ex:
            print(f'getEntryEventType Exception: {ex}')
    
    def getEntryEventEffective(self, enum, default='N/A'):
        """Get feed entry event effective DTG."""
        self.enum = enum
        
        try:
            self.path = 'atom:entry[' + str(self.enum) + ']/cap:effective/text()'
            self.i = getAlerts(LOCALE).xpath(self.path, namespaces = self.ns)
            return self.i if self.enum else default
        
        except Exception as ex:
            print(f'getEntryEventEffective Exception: {ex}')
    
    def getEntryEventExpires(self, enum, default='N/A'):
        """Get feed entry event expires DTG."""
        self.enum = enum
        
        try:
            self.path = 'atom:entry[' + str(self.enum) + ']/cap:expires/text()'
            self.i = getAlerts(LOCALE).xpath(self.path, namespaces = self.ns)
            return self.i if self.enum else default
        
        except Exception as ex:
            print(f'getEntryEventExpires Exception: {ex}')
    
    def getEntryEventStatus(self, enum, default='N/A'):
        """Get feed entry event status."""
        self.enum = enum
        
        try:
            self.path = 'atom:entry[' + str(self.enum) + ']/cap:status/text()'
            self.i = getAlerts(LOCALE).xpath(self.path, namespaces = self.ns)
            return self.i if self.enum else default
        
        except Exception as ex:
            print(f'getEntryEventStatus Exception: {ex}')
    
    def getEntryEventMessageType(self, enum, default='N/A'):
        """Get feed entry event message type."""
        self.enum = enum
        
        try:
            self.path = 'atom:entry[' + str(self.enum) + ']/cap:msgType/text()'
            self.i = getAlerts(LOCALE).xpath(self.path, namespaces = self.ns)
            return self.i if self.enum else default
        
        except Exception as ex:
            print(f'getEntryEventMessageType Exception: {ex}')
    
    def getEntryEventCategory(self, enum, default='N/A'):
        """Get feed entry event category."""
        self.enum = enum
        
        try:
            self.path = 'atom:entry[' + str(self.enum) + ']/cap:category/text()'
            self.i = getAlerts(LOCALE).xpath(self.path, namespaces = self.ns)
            return self.i if self.enum else default
        
        except Exception as ex:
            print(f'getEntryEventCategory Exception: {ex}')
    
    def getEntryEventUrgency(self, enum, default='N/A'):
        """Get feed entry event urgency."""
        self.enum = enum
        
        try:           
            self.path = 'atom:entry[' + str(self.enum) + ']/cap:urgency/text()'
            self.i = getAlerts(LOCALE).xpath(self.path, namespaces = self.ns)
            return self.i if self.enum else default
        
        except Exception as ex:
            print(f'getEntryEventUrgency Exception: {ex}')
    
    def getEntryEventSeverity(self, enum, default='N/A'):
        """Get feed entry event severity."""
        self.enum = enum
        
        try:
            self.path = 'atom:entry[' + str(self.enum) + ']/cap:severity/text()'
            self.i = getAlerts(LOCALE).xpath(self.path, namespaces = self.ns)
            return self.i if self.enum else default
        
        except Exception as ex:
            print(f'getEntryEventSeverity Exception: {ex}')
    
    def getEntryEventCertainty(self, enum, default='N/A'):
        """Get feed entry event severity."""
        self.enum = enum
        
        try:
            self.path = 'atom:entry[' + str(self.enum) + ']/cap:certainty/text()'
            self.i = getAlerts(LOCALE).xpath(self.path, namespaces = self.ns)
            return self.i if self.enum else default
        
        except Exception as ex:
            print(f'getEntryEventCertainty Exception: {ex}')
    
    def getEntryEventPolygon(self, enum, default='N/A'):
        """Get feed entry event polygon.  Returns a string of lat/lon in the format (-)DD.DD (-)DDD.DD,(-)DD.DD (-)DDD.DD (i.e. lat/lon are comma-separated...lat/lon pairs are space-separated.)"""
        self.enum = enum
        
        try:
            self.path = 'atom:entry[' + str(self.enum) + ']/cap:polygon/text()'
            self.i = getAlerts(LOCALE).xpath(self.path, namespaces = self.ns)
            return self.i if self.enum else default
        
        except Exception as ex:
            print(f'getEntryEventPolygon Exception: {ex}')
    
    def getEntryEventAreaDescription(self, enum, default='N/A'):
        """Get feed entry event area description.  Returns a string of semi-colon separated standardized area descriptions."""
        self.enum = enum
        
        try:
            self.path = 'atom:entry[' + str(self.enum) + ']/cap:areaDesc/text()'
            self.i = getAlerts(LOCALE).xpath(self.path, namespaces = self.ns)
            return self.i if self.enum else default
        
        except Exception as ex:
            print(f'getEntryEventAreaDescription Exception: {ex}')
    
    def getEntryEventGeocodeValue(self, enum, default='N/A'):
        """Get CAP geocode area values for individual warning/alerts areas.  Uses NWS-standardized zone/county descriptors.  """
        self.enum = enum
        
        try:
            self.path = 'atom:entry[' + str(self.enum) + ']/cap:geocode/atom:value[2]/text()'
            self.i = getAlerts(LOCALE).xpath(self.path, namespaces = self.ns)
            return self.i if self.enum else default
        
        except Exception as ex:
            print(f'getEntryEventGeocodeValue Exception: {ex}')
    
class MsgHandler:
    """Methods for creating properly formatted APRS messages.  See <http://www.aprs.org/doc/APRS101.PDF> for baseline message specifications.  Follow-on specifications changes are documented at <http://www.aprs.org/aprs11.html> and proposed improvements at <http://www.aprs.org/aprs12.html>."""
    
    def __init__(self):
        """Initializes message handler to create APRS-formatted messages.  Default text encoding is UTF-8."""
        self.encoding = 'utf-8'
    
    def makeToCall(self, geocode):
        """Create a 9-byte to-call for weather alert messages using the format XXXXXX___, where XXXXXX is a standardized NWS six-byte alert zone or county identifier, followed by three spaces.  Per the APRS specification, the to-call is a fixed 9-byte address."""
        self.geocode = geocode
        
        try:
            if len(self.geocode) <= 6:
                self.tocall = str(self.geocode + '   ')
            else:
                self.tocall = self.geocode.split(' ')
            return self.tocall
        
        except Exception as ex:
            print(f'makeToCall Exception: {ex}')
    
    def makeWxMsgPacket(self, evttype, atype, severity, certainty, urgency, category, eff_start, eff_end):
        """Create APRS weather alert message."""
        self.evttype = evttype
        self.atype = atype
        self.severity = severity
        self.certainty = certainty
        self.urgency = urgency
        self.category = category
        self.eff_start = eff_start
        self.eff_end = eff_end
        
        try:
            self.msg_pkt = (f'*{self.evttype}* {self.atype} {self.severity}-{self.certainty}-{self.urgency} {self.category} {self.eff_start}-{self.eff_end}')
            if len(self.msg_pkt) <= 78:      # Maximum allowable length of the APRS NWS message minus message ID length is 78 characters.
                return self.msg_pkt
            else:
                print('The message packet is too long...truncating.')
                return self.msg_pkt[:79]
            
        except Exception as ex:
            print(f'makeWxMsgPacket Exception: {ex}')
    
    def appendMsgId(self, msg):
        """Append a valid APRS message ID to a constructed message using the Python hash() function.  NOTE: hash() can only be used on immutable Python objects.  Returns the entire message w/ ID."""
        self.msg = msg
        
        try:
            self.h = str(hash(self.msg))
            self.m_id = self.h[-5:]
            self.t_msg = str(self.msg + '{' + self.m_id)
            return self.t_msg
        
        except Exception as ex:
            print(f'appendMsgId Exception: {ex}')
    
def main():
    """Main program."""
    x = XMLHandler()
    m = MsgHandler()
    
    try:
        if os.path.exists('/tmp/wxalerts.txt'):
            os.remove('/tmp/wxalerts.txt')
            
        entries = int(getAlerts(LOCALE).xpath('count(atom:entry)', namespaces = x.ns))
        print(f'There are currently {entries} entries in the locale ATOM feed.')
        
        e = 1
        while e <= entries:
            zones = x.getEntryEventGeocodeValue(e)
            evttype = x.getEntryEventType(e)
            atype = x.getEntryEventMessageType(e)
            severity = x.getEntryEventSeverity(e)
            certainty = x.getEntryEventCertainty(e)
            urgency = x.getEntryEventUrgency(e)
            category = x.getEntryEventCategory(e)
            evt_start = x.getEntryEventEffective(e)
            evt_end = x.getEntryEventExpires(e)
                        
            #Convert raw data to APRS-formatted data
            f_evttype = cap.makeEventType(evttype)
            f_alt_type = cap.makeAlertType(atype)
            f_severity = cap.makeSeverity(severity)
            f_certainty = cap.makeCertainty(certainty)
            f_urgency = cap.makeUrgency(urgency)
            f_category = cap.makeCategory(category)
            f_evt_start = cap.makeEffectiveStart(evt_start[0])
            f_evt_end = cap.makeEffectiveEnd(evt_end[0])
            
            wxmsg = m.makeWxMsgPacket(f_evttype, f_alt_type, f_severity, f_certainty, f_urgency, f_category, f_evt_start, f_evt_end)
            
            zonelist = zones[0].split(' ')
            for z in zonelist:
                tocall = m.makeToCall(z)
                zonetext = nm.makeNMZoneText(z)    #TODO:  this will have to change when getAlerts is modified for multiple locales
                fullmsg = (f':{tocall}:{zonetext} ' + wxmsg)
                with open('/tmp/wxalerts.txt', 'a') as f:
                    f.writelines(m.appendMsgId(fullmsg) + '\n')
                sys.stdout.write(m.appendMsgId(fullmsg))
            e += 1
            
    except Exception as ex:
        print(f'Main Exception: {ex}')
        pass
        
    time.sleep(1800)
            
if __name__ == '__main__':
    main()