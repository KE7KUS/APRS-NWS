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

def makeEventType(event, default = 'N/A'):
    """Convert NWS forecast event type into 10-byte human-readable event type descriptor.  Dictionary comforms to the CAP v1.1 standard as implemented by the US National Weather Service.  For a list of current event types, see <https://alerts.weather.gov/cap/product_list.txt>."""
    
    et = {'911 Telephone Outage':'911TEL OUT','Administrative Message':'ADMIN MSG','Air Quality Alert':'ARQUAL ALT','Air Stagnation Advisory':'ARSTAG ADV','Ashfall Advisory':'ASHFALL ADV','Ashfall Warning':'ASHFALL WRN','Avalanche Warning':'AVLNCH WRN','Avalanche Watch':'AVLNCH WCH','Beach Hazards Statement':'BCHHAZ STM','Blizzard Warning':'BLZZRD WRN','Blizzard Watch':'BLZZRD WCH','Blowing Dust Advisory':'BLWDST ADV','Blowing Snow Advisory':'BLWSNO ADV','Brisk Wind Advisory':'BSKWND ADV','Child Abduction Emergency':'!AMBERALT!','Civil Danger Warning':'CIVDAN WRN','Civil Emergency Message':'CIVEMR MSG','Coastal Flood Advisory':'CSTFLD ADV','Coastal Flood Statement':'CSTFLD STM','Coastal Flood Warning':'CSTFLD WRN','Coastal Flood Watch':'CSTFLD WCH','Dense Fog Advisory':'DNSFOG ADV','Dense Smoke Advisory':'DNSMOK ADV','Dust Storm Warning':'DSTORM WRN','Earthquake Warning':'ERTHQK WRN','Evacuation Immediate':'EVACUATE  ','Excessive Heat Warning':'EXHEAT WRN','Excessive Heat Watch':'EXHEAT WCH','Extreme Cold Warning':'EXCOLD WRN','Extreme Cold Watch':'EXCOLD WCH','Extreme Fire Danger':'EXFIRE DGR','Extreme Wind Warning':'EXWIND WRN','Fire Warning':'FIRE WARN ','Fire Weather Watch':'FIREWX WCH','Flash Flood Statement':'FLSHFD STM','Flash Flood Warning':'FLSHFD WRN','Flash Flood Watch':'FLSHFD WCH','Flood Advisory':'FLOOD ADV ','Flood Statement':'FLOOD STMT','Flood Warning':'FLOOD WARN','Flood Watch':'FLOOD WTCH','Freeze Warning':'FREEZE WRN','Freeze Watch':'FREEZE WCH','Freezing Drizzle Advisory':'FRZDRZ ADV','Freezing Fog Advisory':'FRZFOG ADV','Freezing Rain Advisory':'FRZRN ADV ','Freezing Spray Advisory':'FRZSPR ADV','Frost Advisory':'FROST ADV ','Gale Warning':'GALE WARN ','Gale Watch':'GALE WATCH','Hard Freeze Warning':'HRDFRZ WRN','Hard Freeze Watch':'HRDFRZ WCH','Hazardous Materials Warning':'HAZMAT WRN','Hazardous Seas Warning':'HAZSEA WRN','Hazardous Seas Watch':'HAZSEA WCH','Hazardous Weather Outlook':'HAZWX OTLK','Heat Advisory':'HEAT ADVSY','Heavy Freezing Spray Warning':'FRZSPR WRN','Heavy Freezing Spray Watch':'FRZSPR WCH','Heavy Snow Warning':'HVYSNO WRN','High Surf Advisory':'HISURF ADV','High Surf Warning':'HISURF WRN','High Wind Warning':'HIWIND WRN','High Wind Watch':'HIWIND WCH','Hurricane Force Wind Warning':'HURWND WRN','Hurricane Force Wind Watch':'HURWND WCH','Hurricane Statement':'HURRCN STM','Hurricane Warning':'HURRCN WRN','Hurricane Watch':'HURRCN WCH','Hurricane Wind Warning':'HURWND WRN','Hurricane Wind Watch':'HURWND WCH','Hydrologic Advisory':'HYDRO ADV ','Hydrologic Outlook':'HYDRO OTLK','Ice Storm Warning':'ICESTM WRN','Lake Effect Snow Advisory':'LAKSNO ADV','Lake Effect Snow and Blowing Snow Advisory':'LAKSNO ADV','Lake Effect Snow Warning':'LAKSNO WRN','Lake Effect Snow Watch':'LAKSNO WCH','Lakeshore Flood Advisory':'LAKFLD ADV','Lakeshore Flood Statement':'LAKFLD STM','Lakeshore Flood Warning':'LAKFLD WRN','Lakeshore Flood Watch':'LAKFLD WCH','Lake Wind Advisory':'LAKWND ADV','Law Enforcement Warning':'LAWENF WRN','Local Area Emergency':'LOCAL EMR','Low Water Advisory':'LOWH2O ADV','Marine Weather Statement':'MARWX STMT','Nuclear Power Plant Warning':'NUKPLT WRN','Radiological Hazard Warning':'RADHAZ WRN','Red Flag Warning':'REDFLG WRN','Rip Current Statement':'RIPCUR STM','Severe Thunderstorm Warning':'SVTSTM WRN','Severe Thunderstorm Watch':'SVTSTM WCH','Severe Weather Statement':'SVRWX STMT','Shelter In Place Warning':'SHLTIP WRN','Sleet Advisory':'SLEET ADV ','Sleet Warning':'SLEET WRN ','Small Craft Advisory':'SMCRFT ADV','Snow Advisory':'SNOW ADV  ','Snow and Blowing Snow Advisory':'BLWSNO ADV','Special Marine Warning':'SPCMAR WRN','Special Weather Statement':'SPECWX STM','Storm Warning':'STORM WARN','Storm Watch':'STORM WTCH','Test':'TEST  TEST','Tornado Warning':'TORNDO WRN','Tornado Watch':'TORNDO WCH','Tropical Storm Warning':'TPCSTM WRN','Tropical Storm Watch':'TPCSTM WCH','Tropical Storm Wind Warning':'TPCWND WRN','Tropical Storm Wind Watch':'TPCWND WCH','Tsunami Advisory':'TSUNMI ADV','Tsunami Warning':'TSUNMI WRN','Tsunami Watch':'TSUNMI WCH','Typhoon Statement':'TYPHUN STM','Typhoon Warning':'TYPHUN WRN','Typhoon Watch':'TYPHUN WCH','Volcano Warning':'VOLCNO WRN','Wind Advisory':'WIND ADVSY','Wind Chill Advisory':'WNDCHL ADV','Wind Chill Warning':'WNDCHL WRN','Wind Chill Watch':'WNDCHL WCH','Winter Storm Warning':'WTRSTM WRN','Winter Storm Watch':'WTRSTM WCH','Winter Weather Advisory':'WNTRWX ADV'}
    return et[event[0]] if event else default

def makeAlertType(alert, default = 'N/A'):
    """Convert NWS forecast alert type into 4-byte human-readable alert type descriptor.  Dictionary conforms to the CAP v1.1 standard as implemented by the US National Weather Service.  For a list of current data types, see <https://www.oasis-open.org/committees/download.php/14759/emergency-CAPv1.1.pdf>."""    
    
    at = {'Alert':'ALRT','Update':'UPDT','Cancel':'CANX','Ack':'ACK ','Error':'ERR '}
    return at[alert[0]] if alert else default

def makeSeverity(severity, default = 'N/A'):
    """Convert NWS forecast severity into 3-byte human-readable severity descriptor.  Dictionary conforms to the CAP v1.1 standard as implemented by the US National Weather Service.  For a list of current data types, see <https://www.oasis-open.org/committees/download.php/14759/emergency-CAPv1.1.pdf>."""
    
    sev = {'Extreme':'EXT','Severe':'SEV','Moderate':'MOD','Minor':'MIN','Unknown':'UNK'}
    return sev[severity[0]] if severity else default

def makeCertainty(certainty, default = 'N/A'):
    """Convert NWS forecast certainty into a 3-byte human-readable certainty descriptor.  Dictionary conforms to the CAP v1.1 standard as implemented by the US National Weather Service.  For a list of current data types, see <https://www.oasis-open.org/committees/download.php/14759/emergency-CAPv1.1.pdf>."""
    
    cer = {'Observed':'OBS','Likely':'LIK','Possible':'POS','Unlikely':'ULK','Unknown':'UNK'}
    return cer[certainty[0]] if certainty else default

def makeUrgency(urgency, default = 'N/A'):
    """Convert NWS forecast urgency into 3-byte human-readable urgency descriptor.  Dictionary conforms to the CAP v1.1 standard as implemented by the US National Weather Service.  For a list of current data types, see <https://www.oasis-open.org/committees/download.php/14759/emergency-CAPv1.1.pdf>."""
    
    urg = {'Immediate':'IMM','Expected':'EXP','Future':'FUT','Past':'PST','Unknown':'UNK'}
    return urg[urgency[0]] if urgency else default

def makeCategory(category, default = 'N/A'):
    """Convert NWS forecast category into 4-byte human-readable category descriptor.  Dictionary conforms to the CAP v1.1 standard as implemented by the US National Weather Service.  For a list of current data types, see <https://www.oasis-open.org/committees/download.php/14759/emergency-CAPv1.1.pdf>."""

    cat = {'Geo':'GEO','Met':'MET','Safety':'SFTY','Security':'SECU','Rescue':'RESC','Fire':'FIRE','Health':'HLTH','Env':'ENV','Transport':'TRAN','Infra':'INFR','CBRNE':'CBRN','Other':'OTHR'}
    return cat[category[0]] if category else default

def makeEffectiveStart(dtg):
    """Convert NWS forecast DTG to an abbreviated date/time human-readable format.  Uses the raw NWS feed time format 'YYYY-MM-DDTHH:MM:SSZZZ:ZZ' where ZZZ:ZZ is the UTC time offset in HH:MM and the first character is +/- based on shift from UTC."""
    
    start = dtg[8:10] + '/' + dtg[11:13] + dtg[14:16]
    return start

def makeEffectiveEnd(dtg):
    """Convert NWS forecast DTG to an abbreviated date/time human-readable format.  Uses the raw NWS feed time format 'YYYY-MM-DDTHH:MM:SSZZZ:ZZ' where ZZZ:ZZ is the UTC time offset in HH:MM and the first character is +/- based on shift from UTC."""
    
    end = dtg[8:10] + '/' + dtg[11:13] + dtg[14:16]
    return end





