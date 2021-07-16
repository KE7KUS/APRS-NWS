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

def makeNMZoneText(zone, default='N/A'):
    """Convert zone/area of forecast to standardized 15-character human-readable text string for the relevant zone/area."""
    
    nmzt = {'NMZ027':'GUADALUPE MTNS ','NMZ028':'EDDY CTY PLAINS','NMZ029':'N LEA COUNTY   ','NMZ033':'CENTRAL LEA CTY','NMZ034':'S LEA CTY      ','NMZ101':'NW PLATEAU     ','NMZ102':'N CENTRAL MTNS ','NMZ103':'NE HIGHLANDS   ','NMZ104':'NE PLAINS      ','NMZ105':'NW HIGHLANDS   ','NMZ106':'M RIO GRANDE VY','NMZ107':'SAN+MAN MTNS   ','NMZ108':'E CENTRAL PLNS ','NMZ109':'WC HIGHLANDS   ','NMZ110':'SW MOUNTAINS   ','NMZ111':'SW DESERTS     ','NMZ112':'S CEN LOWLANDS ','NMZ113':'CAP & SAC MTNS ','NMZ116':'SAC FH+GUAD MTS','NMZ117':'CHAVEZ PLAINS  ','NMZ118':'EDDY PLAINS    ','NMZ119':'LEA            ','NMZ201':'NW PLATEAU     ','NMZ202':'CHUSKA MTNS    ','NMZ203':'FAR NW HILANDS ','NMZ204':'NW HIGHLANDS   ','NMZ205':'WC PLATEAU     ','NMZ206':'WC MOUNTAINS   ','NMZ207':'WC HIGHLANDS   ','NMZ208':'SW MOUNTAINS   ','NMZ209':'SF RIVER VLY   ','NMZ210':'TUSAS MTN+CHAMA','NMZ211':'JEMEZ MTNS     ','NMZ212':'GLORIETA MESA  ','NMZ213':'N SAN DE CRISTO','NMZ214':'S SAN DE CRISTO','NMZ215':'E SAN DE CRISTO','NMZ216':'U RIO GRANDE VY','NMZ217':'ESPANOLA VLY   ','NMZ218':'SANTA FE METRO ','NMZ219':'ABQ METRO      ','NMZ220':'L RIO GRANDE VY','NMZ221':'SAN+MAN MTNS   ','NMZ222':'ESTANCIA VLY   ','NMZ223':'CEN HIGHLANDS  ','NMZ224':'S CEN HIGHLANDS','NMZ225':'U TULAROSA VLY ','NMZ226':'S CEN MOUNTAINS','NMZ227':'JB MESAS+RATON ','NMZ228':'FAR NE HILANDS ','NMZ229':'NE HIGHLANDS   ','NMZ230':'UNION CTY      ','NMZ231':'HARDING CTY    ','NMZ232':'E SAN MIGUEL CY','NMZ233':'GUADALUPE CTY  ','NMZ234':'QUAY CTY       ','NMZ235':'CURRY CTY      ','NMZ236':'ROOSEVELT CTY  ','NMZ237':'DE BACA CTY    ','NMZ238':'CHAVES CTY PLNS','NMZ239':'E LINCOLN CTY  ','NMZ240':'SW CHAVES CTY  ','NMZ241':'SAN AG PLAINS  ','NMZ401':'U GILA RVR VLY ','NMZ402':'BLACK RANGE    ','NMZ403':'MIMBRES VLY    ','NMZ404':'L GILA RVR VLY ','NMZ405':'LO BOOTHEEL    ','NMZ406':'UPLAND BOOTHEEL','NMZ407':'MIMBRES BASIN  ','NMZ408':'E BLK RNG FTHLS','NMZ409':'SIERRA CTY LAKE','NMZ410':'N DONA ANA CTY ','NMZ411':'S DONA ANA CTY ','NMZ412':'C TULA BASIN   ','NMZ413':'S TULA BASIN   ','NMZ414':'W SAC MTNS<7500','NMZ415':'SAC MTNS>7500  ','NMZ416':'E SAC MTNS<7500','NMZ417':'OTERO MESA     ','NMC001':'BERNALILLO CTY ','NMC003':'CATRON CTY     ','NMC005':'CHAVES CTY     ','NMC006':'CIBOLA CTY     ','NMC007':'COLFAX CTY     ','NMC009':'CURRY CTY      ','NMC011':'DE BACA CTY    ','NMC013':'DONA ANA CTY   ','NMC015':'EDDY CTY       ','NMC017':'GRANT CTY      ','NMC019':'GUADALUPE CTY  ','NMC021':'HARDING CTY    ','NMC023':'HIDALGO CTY    ','NMC025':'LEA CTY        ','NMC027':'LINCOLN CTY    ','NMC028':'LOS ALAMOS CTY ','NMC029':'LUNA CTY       ','NMC031':'MCKINLEY CTY   ','NMC033':'MORA CTY       ','NMC035':'OTERO CTY      ','NMC037':'QUAY CTY       ','NMC039':'RIO ARRIBA CTY ','NMC041':'ROOSEVELT CTY  ','NMC043':'SANDOVAL CTY   ','NMC045':'SAN JUAN CTY   ','NMC047':'SAN MIGUEL CTY ','NMC049':'SANTA FE CTY   ','NMC051':'SIERRA CTY     ','NMC053':'SOCORRO CTY    ','NMC055':'TAOS CTY       ','NMC057':'TORRANCE CTY   ','NMC059':'UNION CTY      ','NMC061':'VALENCIA CTY   '}

    return nmzt[zone] if zone else default
