#!/usr/bin/python3

# APRS NWS Feedparser
# January 2021
# Released under GPLv3

import datetime, requests, os
import lxml.etree as et
from io import BytesIO

# TODO: Process CAP polygons and publish as APRS area items (p. 60 in APRS v1.01 specification)
# TODO: Break out CAP dictionaries and individual state zone dictionaries into separate files and include with import (makes the system modular for other to contribute).
# TODO: Interactive query routine to enable user to send query via APRS and have reply if any NWS alerts
    # - Connect to APRS-IS via TCP on 14580
    # - Search data stream for TOCALL '?NWSALT'
    # - Parse msg text for zone/county code and compare to list of existing alerts
    # - Return alert(s) if found else return None

newsfeed = ('https://alerts.weather.gov/cap/nm.php?x=0')
ns = {"atom":"http://www.w3.org/2005/Atom", "cap":"urn:oasis:names:tc:emergency:cap:1.1", "ha":"http://www.alerting.net/namespace/index_1.0"}

r = requests.get(newsfeed)
b = BytesIO(r.content)
t = et.parse(b)
root = t.getroot()

def xpGetEntryId(entry_no, default='N/A'):
    """Get feed entry ID using XPath."""
    path = 'atom:entry[' + str(entry_no) + ']/atom:id/text()'
    i = t.xpath(path, namespaces=ns)
    print('Entry ID: ' + str(i))
    return i if entry_no else default

def xpGetEntryPubTime(entry_no, default='N/A'):
    """Get feed entry published time using XPath."""
    path = 'atom:entry[' + str(entry_no) + ']/atom:published/text()'
    i = t.xpath(path, namespaces=ns)
    return i if entry_no else default

def xpGetEntryUpdTime(entry_no, default='N/A'):
    """Get feed entry update time using XPath."""
    path = 'atom:entry[' + str(entry_no) + ']/atom:updated/text()'
    i = t.xpath(path, namespaces=ns)
    return i if entry_no else default

def xpGetEntryEvtType(entry_no, default='N/A'):
    """Get feed entry event type using XPath."""
    path = 'atom:entry[' + str(entry_no) +']/cap:event/text()'
    i = t.xpath(path, namespaces=ns)
    return i if entry_no else default

def xpGetEntryEvtEffective(entry_no, default='N/A'):
    """Get feed entry event effective DTG using XPath."""
    path = 'atom:entry[' + str(entry_no) + ']/cap:effective/text()'
    i = t.xpath(path, namespaces=ns)
    return i if entry_no else default

def xpGetEntryEvtExpires(entry_no, default='N/A'):
    """Get feed entry event expires DTG using XPath."""
    path = 'atom:entry[' + str(entry_no) + ']/cap:expires/text()'
    i = t.xpath(path, namespaces=ns)
    return i if entry_no else default

def xpGetEntryEvtStatus(entry_no, default='N/A'):
    """Get feed entry event status using XPath."""
    path = 'atom:entry[' + str(entry_no) + ']/cap:status/text()'
    i = t.xpath(path, namespaces=ns)
    return i if entry_no else default

def xpGetEntryEvtMsgType(entry_no, default='N/A'):
    """Get feed entry event message type using XPath."""
    path = 'atom:entry[' + str(entry_no) + ']/cap:msgType/text()'
    i = t.xpath(path, namespaces=ns)
    return i if entry_no else default

def xpGetEntryEvtCategory(entry_no, default='N/A'):
    """Get feed entry event message category using XPath."""
    path = 'atom:entry[' + str(entry_no) + ']/cap:category/text()'
    i = t.xpath(path, namespaces=ns)
    return i if entry_no else default

def xpGetEntryEvtUrgency(entry_no, default='N/A'):
    """Get feed entry event urgency using XPath."""
    path = 'atom:entry[' + str(entry_no) + ']/cap:urgency/text()'
    i = t.xpath(path, namespaces=ns)
    return i if entry_no else default

def xpGetEntryEvtSeverity(entry_no, default='N/A'):
    """Get feed entry event severity using XPath."""
    path = 'atom:entry[' + str(entry_no) + ']/cap:severity/text()'
    i = t.xpath(path, namespaces=ns)
    return i if entry_no else default

def xpGetEntryEvtCertainty(entry_no, default='N/A'):
    """Get feed entry event certainty using XPath."""
    path = 'atom:entry[' + str(entry_no) + ']/cap:certainty/text()'
    i = t.xpath(path, namespaces=ns)
    return i if entry_no else default

def xpGetEntryEvtPolygon(entry_no, default='N/A'):
    """Get feed entry polygon data using XPath.  Returns a string of lat/lon in the format (-)MM.MM,(-)MMM.MM (-)MM.MM,(-)MMM.MM (i.e. lat/lon are comma-separated...lat/lon pairs space-separated."""
    path = 'atom:entry[' + str(entry_no) + ']/cap:polygon/text()'
    i = t.xpath(path, namespaces=ns)
    return i if entry_no else default
    # Example item:  'cap_polygon': '38.1,-105.51 38.05,-105.67 38.2,-105.73 38.28,-105.52 38.1,-105.51'

def xpGetEntryEvtAreaDesc(entry_no, default='N/A'):
    """Get feed entry event area text description using XPath.  Returns a string of standardized area descriptions which a semi-colon separated."""
    path = 'atom:entry[' + str(entry_no) + ']/cap:areaDesc/text()'
    i = t.xpath(path, namespaces=ns)
    return i if entry_no else default

def xpGetCAPGeocodeValue(entry_no, default='N/A'):
    """Get CAP geocode area values for individual warning/alert areas.  Uses NWS-standard zone or county descriptors. May return a space-separated string of zones/counties."""
    path = 'atom:entry[' + str(entry_no) + ']/cap:geocode/atom:value[2]/text()'
    i = t.xpath(path, namespaces=ns)
    return i if entry_no else default

def makeToCall(geocode):
    """Make 9-character NWSXXXXXX to-call for weather alert message where XXXXXX is a standardized NWS county or zone identifier."""

    if len(geocode) <= 6:
        tocall = 'NWS'+ geocode
    else:
        tocall = geocode.split(' ')        
    return tocall

def makeZoneText(zone, default='N/A'):
    """Convert zone/area of forecast to standardized 15-character human-readable text string for the relevant zone/area."""
    
    zt = {'NMZ027':'GUADALUPE MTNS ','NMZ028':'EDDY CTY PLAINS','NMZ029':'N LEA COUNTY   ','NMZ033':'CENTRAL LEA CTY','NMZ034':'S LEA CTY      ','NMZ101':'NW PLATEAU     ','NMZ102':'N CENTRAL MTNS ','NMZ103':'NE HIGHLANDS   ','NMZ104':'NE PLAINS      ','NMZ105':'NW HIGHLANDS   ','NMZ106':'M RIO GRANDE VY','NMZ107':'SAN+MAN MTNS   ','NMZ108':'E CENTRAL PLNS ','NMZ109':'WC HIGHLANDS   ','NMZ110':'SW MOUNTAINS   ','NMZ111':'SW DESERTS     ','NMZ112':'S CEN LOWLANDS ','NMZ113':'CAP & SAC MTNS ','NMZ116':'SAC FH+GUAD MTS','NMZ117':'CHAVEZ PLAINS  ','NMZ118':'EDDY PLAINS    ','NMZ119':'LEA            ','NMZ201':'NW PLATEAU     ','NMZ202':'CHUSKA MTNS    ','NMZ203':'FAR NW HILANDS ','NMZ204':'NW HIGHLANDS   ','NMZ205':'WC PLATEAU     ','NMZ206':'WC MOUNTAINS   ','NMZ207':'WC HIGHLANDS   ','NMZ208':'SW MOUNTAINS   ','NMZ209':'SF RIVER VLY   ','NMZ210':'TUSAS MTN+CHAMA','NMZ211':'JEMEZ MTNS     ','NMZ212':'GLORIETA MESA  ','NMZ213':'N SAN DE CRISTO','NMZ214':'S SAN DE CRISTO','NMZ215':'E SAN DE CRISTO','NMZ216':'U RIO GRANDE VY','NMZ217':'ESPANOLA VLY   ','NMZ218':'SANTA FE METRO ','NMZ219':'ABQ METRO      ','NMZ220':'L RIO GRANDE VY','NMZ221':'SAN+MAN MTNS   ','NMZ222':'ESTANCIA VLY   ','NMZ223':'CEN HIGHLANDS  ','NMZ224':'S CEN HIGHLANDS','NMZ225':'U TULAROSA VLY ','NMZ226':'S CEN MOUNTAINS','NMZ227':'JB MESAS+RATON ','NMZ228':'FAR NE HILANDS ','NMZ229':'NE HIGHLANDS   ','NMZ230':'UNION CTY      ','NMZ231':'HARDING CTY    ','NMZ232':'E SAN MIGUEL CY','NMZ233':'GUADALUPE CTY  ','NMZ234':'QUAY CTY       ','NMZ235':'CURRY CTY      ','NMZ236':'ROOSEVELT CTY  ','NMZ237':'DE BACA CTY    ','NMZ238':'CHAVES CTY PLNS','NMZ239':'E LINCOLN CTY  ','NMZ240':'SW CHAVES CTY  ','NMZ241':'SAN AG PLAINS  ','NMZ401':'U GILA RVR VLY ','NMZ402':'BLACK RANGE    ','NMZ403':'MIMBRES VLY    ','NMZ404':'L GILA RVR VLY ','NMZ405':'LO BOOTHEEL    ','NMZ406':'UPLAND BOOTHEEL','NMZ407':'MIMBRES BASIN  ','NMZ408':'E BLK RNG FTHLS','NMZ409':'SIERRA CTY LAKE','NMZ410':'N DONA ANA CTY ','NMZ411':'S DONA ANA CTY ','NMZ412':'C TULA BASIN   ','NMZ413':'S TULA BASIN   ','NMZ414':'W SAC MTNS<7500','NMZ415':'SAC MTNS>7500  ','NMZ416':'E SAC MTNS<7500','NMZ417':'OTERO MESA     ','NMC001':'BERNALILLO CTY ','NMC003':'CATRON CTY     ','NMC005':'CHAVES CTY     ','NMC006':'CIBOLA CTY     ','NMC007':'COLFAX CTY     ','NMC009':'CURRY CTY      ','NMC011':'DE BACA CTY    ','NMC013':'DONA ANA CTY   ','NMC015':'EDDY CTY       ','NMC017':'GRANT CTY      ','NMC019':'GUADALUPE CTY  ','NMC021':'HARDING CTY    ','NMC023':'HIDALGO CTY    ','NMC025':'LEA CTY        ','NMC027':'LINCOLN CTY    ','NMC028':'LOS ALAMOS CTY ','NMC029':'LUNA CTY       ','NMC031':'MCKINLEY CTY   ','NMC033':'MORA CTY       ','NMC035':'OTERO CTY      ','NMC037':'QUAY CTY       ','NMC039':'RIO ARRIBA CTY ','NMC041':'ROOSEVELT CTY  ','NMC043':'SANDOVAL CTY   ','NMC045':'SAN JUAN CTY   ','NMC047':'SAN MIGUEL CTY ','NMC049':'SANTA FE CTY   ','NMC051':'SIERRA CTY     ','NMC053':'SOCORRO CTY    ','NMC055':'TAOS CTY       ','NMC057':'TORRANCE CTY   ','NMC059':'UNION CTY      ','NMC061':'VALENCIA CTY   '}

    return zt[zone] if zone else default

def makeEventType(event, default='N/A'):
    """Convert NWS forecast event type text to an abbreviated 10-character human-readable format using a Python dictionary lookup."""

    et = {'911 Telephone Outage':'911TEL OUT','Administrative Message':'ADMIN MSG','Air Quality Alert':'ARQUAL ALT','Air Stagnation Advisory':'ARSTAG ADV','Ashfall Advisory':'ASHFALL ADV','Ashfall Warning':'ASHFALL WRN','Avalanche Warning':'AVLNCH WRN','Avalanche Watch':'AVLNCH WCH','Beach Hazards Statement':'BCHHAZ STM','Blizzard Warning':'BLZZRD WRN','Blizzard Watch':'BLZZRD WCH','Blowing Dust Advisory':'BLWDST ADV','Blowing Snow Advisory':'BLWSNO ADV','Brisk Wind Advisory':'BSKWND ADV','Child Abduction Emergency':'!AMBERALT!','Civil Danger Warning':'CIVDAN WRN','Civil Emergency Message':'CIVEMR MSG','Coastal Flood Advisory':'CSTFLD ADV','Coastal Flood Statement':'CSTFLD STM','Coastal Flood Warning':'CSTFLD WRN','Coastal Flood Watch':'CSTFLD WCH','Dense Fog Advisory':'DNSFOG ADV','Dense Smoke Advisory':'DNSMOK ADV','Dust Storm Warning':'DSTORM WRN','Earthquake Warning':'ERTHQK WRN','Evacuation Immediate':'EVACUATE  ','Excessive Heat Warning':'EXHEAT WRN','Excessive Heat Watch':'EXHEAT WCH','Extreme Cold Warning':'EXCOLD WRN','Extreme Cold Watch':'EXCOLD WCH','Extreme Fire Danger':'EXFIRE DGR','Extreme Wind Warning':'EXWIND WRN','Fire Warning':'FIRE WARN ','Fire Weather Watch':'FIREWX WCH','Flash Flood Statement':'FLSHFD STM','Flash Flood Warning':'FLSHFD WRN','Flash Flood Watch':'FLSHFD WCH','Flood Advisory':'FLOOD ADV ','Flood Statement':'FLOOD STMT','Flood Warning':'FLOOD WARN','Flood Watch':'FLOOD WTCH','Freeze Warning':'FREEZE WRN','Freeze Watch':'FREEZE WCH','Freezing Drizzle Advisory':'FRZDRZ ADV','Freezing Fog Advisory':'FRZFOG ADV','Freezing Rain Advisory':'FRZRN ADV ','Freezing Spray Advisory':'FRZSPR ADV','Frost Advisory':'FROST ADV ','Gale Warning':'GALE WARN ','Gale Watch':'GALE WATCH','Hard Freeze Warning':'HRDFRZ WRN','Hard Freeze Watch':'HRDFRZ WCH','Hazardous Materials Warning':'HAZMAT WRN','Hazardous Seas Warning':'HAZSEA WRN','Hazardous Seas Watch':'HAZSEA WCH','Hazardous Weather Outlook':'HAZWX OTLK','Heat Advisory':'HEAT ADVSY','Heavy Freezing Spray Warning':'FRZSPR WRN','Heavy Freezing Spray Watch':'FRZSPR WCH','Heavy Snow Warning':'HVYSNO WRN','High Surf Advisory':'HISURF ADV','High Surf Warning':'HISURF WRN','High Wind Warning':'HIWIND WRN','High Wind Watch':'HIWIND WCH','Hurricane Force Wind Warning':'HURWND WRN','Hurricane Force Wind Watch':'HURWND WCH','Hurricane Statement':'HURRCN STM','Hurricane Warning':'HURRCN WRN','Hurricane Watch':'HURRCN WCH','Hurricane Wind Warning':'HURWND WRN','Hurricane Wind Watch':'HURWND WCH','Hydrologic Advisory':'HYDRO ADV ','Hydrologic Outlook':'HYDRO OTLK','Ice Storm Warning':'ICESTM WRN','Lake Effect Snow Advisory':'LAKSNO ADV','Lake Effect Snow and Blowing Snow Advisory':'LAKSNO ADV','Lake Effect Snow Warning':'LAKSNO WRN','Lake Effect Snow Watch':'LAKSNO WCH','Lakeshore Flood Advisory':'LAKFLD ADV','Lakeshore Flood Statement':'LAKFLD STM','Lakeshore Flood Warning':'LAKFLD WRN','Lakeshore Flood Watch':'LAKFLD WCH','Lake Wind Advisory':'LAKWND ADV','Law Enforcement Warning':'LAWENF WRN','Local Area Emergency':'LOCAL EMR','Low Water Advisory':'LOWH2O ADV','Marine Weather Statement':'MARWX STMT','Nuclear Power Plant Warning':'NUKPLT WRN','Radiological Hazard Warning':'RADHAZ WRN','Red Flag Warning':'REDFLG WRN','Rip Current Statement':'RIPCUR STM','Severe Thunderstorm Warning':'SVTSTM WRN','Severe Thunderstorm Watch':'SVTSTM WCH','Severe Weather Statement':'SVRWX STMT','Shelter In Place Warning':'SHLTIP WRN','Sleet Advisory':'SLEET ADV ','Sleet Warning':'SLEET WRN ','Small Craft Advisory':'SMCRFT ADV','Snow Advisory':'SNOW ADV  ','Snow and Blowing Snow Advisory':'BLWSNO ADV','Special Marine Warning':'SPCMAR WRN','Special Weather Statement':'SPECWX STM','Storm Warning':'STORM WARN','Storm Watch':'STORM WTCH','Test':'TEST  TEST','Tornado Warning':'TORNDO WRN','Tornado Watch':'TORNDO WCH','Tropical Storm Warning':'TPCSTM WRN','Tropical Storm Watch':'TPCSTM WCH','Tropical Storm Wind Warning':'TPCWND WRN','Tropical Storm Wind Watch':'TPCWND WCH','Tsunami Advisory':'TSUNMI ADV','Tsunami Warning':'TSUNMI WRN','Tsunami Watch':'TSUNMI WCH','Typhoon Statement':'TYPHUN STM','Typhoon Warning':'TYPHUN WRN','Typhoon Watch':'TYPHUN WCH','Volcano Warning':'VOLCNO WRN','Wind Advisory':'WIND ADVSY','Wind Chill Advisory':'WNDCHL ADV','Wind Chill Warning':'WNDCHL WRN','Wind Chill Watch':'WNDCHL WCH','Winter Storm Warning':'WTRSTM WRN','Winter Storm Watch':'WTRSTM WCH','Winter Weather Advisory':'WNTRWX ADV'}
    return et[event[0]] if event else default

def makeAlertType(alert, default='N/A'):
    """Convert NWS forecast alert type to an abbreviated 4-character human-readable format using a Python dictionary lookup."""

    at = {'Alert':'ALRT','Update':'UPDT','Cancel':'CANX','Ack':'ACK ','Error':'ERR '}
    return at[alert[0]] if alert else default

def makeSeverity(severity, default='N/A'):
    """Convert NWS forecast severity to an abbreviated 3-character human-readable format using a Python dictionary lookup."""

    sev = {'Extreme':'EXT','Severe':'SEV','Moderate':'MOD','Minor':'MIN','Unknown':'UNK'}
    return sev[severity[0]] if severity else default

def makeCertainty(certainty, default='N/A'):
    """Convert NWS forecast certainty to an abbreviated 3-character human-readable format using a Python dictionary lookup."""

    cer = {'Observed':'OBS','Likely':'LIK','Possible':'POS','Unlikely':'ULK','Unknown':'UNK'}
    return cer[certainty[0]] if certainty else default

def makeUrgency(urgency, default='N/A'):
    """Convert NWS forecast urgency to an abbreviated 3-character human-readable format using a Python dictionary lookup."""

    urg = {'Immediate':'IMM','Expected':'EXP','Future':'FUT','Past':'PST','Unknown':'UNK'}
    return urg[urgency[0]] if urgency else default

def makeCategory(category, default='N/A'):
    """Convert NWS forecast categordy to an abbreviated 4-character human-readable format using a Python dictionary lookup."""

    cat = {'Geo':'GEO ','Met':'MET ','Safety':'SFTY','Security':'SECU','Rescue':'RESC','Fire':'FIRE','Health':'HLTH','Env':'ENV ','Transport':'TRAN','Infra':'INFR','CBRNE':'CBRN','Other':'OTHR'}
    return cat[category[0]] if category else default

def makeEffStart(dtg):
    """Convert NWS forecast DTG to an abbreviated date/time human-readable format.  Uses the raw NWS feed time format 'YYYY-MM-DDTHH:MM:SSZZZ:ZZ' where ZZZ:ZZ is the UTC time offset in HH:MM and the first character is +/- based on shift from UTC."""

    start = dtg[8:10] + '/' + dtg[11:13] + dtg[14:16]
    return start

def makeEffEnd(dtg):
    """Convert NWS forecast DTG to an abbreviated date/time human-readable format. Uses the raw NWS feed time format 'YYYY-MM-DDTHH:MM:SSZZZ:ZZ' where ZZZ:ZZ is the UTC time offset in HH:MM and the first character is +/- based on shift from UTC."""

    end = dtg[8:10] + '/' + dtg[11:13] + dtg[14:16]
    return end

def makeWxMsgPacket(eventtype, atype, severity, certainty, urgency, category, effective_start, effective_end):
    """Take all gathered parameters and assemble into a valid APRS weather message."""

    msg_pkt = (f'*{eventtype}* {atype} {severity}-{certainty}-{urgency} {category} {effective_start}-{effective_end}')
    if len(msg_pkt) <= 78:      # Maximum allowable length of the APRS NWS message minus message ID length is 78 characters.
        return msg_pkt
    else:
        print('The message packet is too long.')

def appendMsgId(msg):
    """Append a valid APRS message ID to a constructed message using the hash() function.  NOTE: hash() can only be used on immutable Python objects.  Returns the entire message w/ ID."""

    h = str(hash(msg))
    m_id = h[-5:]
    t_msg = str(msg + '{' + m_id)
    return t_msg

if __name__ == '__main__':

    # Clean up the old alerts file so we can add a new one
    if os.path.exists('wxalerts.txt'):
        os.remove('wxalerts.txt')

    entries = t.xpath('count(atom:entry)', namespaces=ns)
    e = 1    
    while e <= entries:
        zones = xpGetCAPGeocodeValue(e) 
        eventtype = xpGetEntryEvtType(e)
        atype = xpGetEntryEvtMsgType(e)
        severity = xpGetEntryEvtSeverity(e)
        certainty = xpGetEntryEvtCertainty(e)
        urgency = xpGetEntryEvtUrgency(e)
        category = xpGetEntryEvtCategory(e)
        evt_start = xpGetEntryEvtEffective(e)
        evt_end = xpGetEntryEvtExpires(e)

        f_evt_type = makeEventType(eventtype)
        f_alt_type = makeAlertType(atype)
        f_severity = makeSeverity(severity)
        f_certainty = makeCertainty(certainty)
        f_urgency = makeUrgency(urgency)
        f_category = makeCategory(category)
        f_evt_start = makeEffStart(evt_start[0])
        f_evt_end = makeEffEnd(evt_end[0])

        wxmsg = makeWxMsgPacket(f_evt_type,f_alt_type,f_severity,f_certainty,f_urgency,f_category,f_evt_start,f_evt_end)

        zonelist = zones[0].split(' ')
        for z in zonelist:
            tocall = str(z) + '   '
            zonetext = makeZoneText(z)
            fullmsg =(f':{tocall}:{zonetext} ' + wxmsg)
            with open('wxalerts.txt', 'a') as f:
                f.writelines(appendMsgId(fullmsg) + '\n')
        e += 1
