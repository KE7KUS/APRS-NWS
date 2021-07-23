# APRS-NWS
The US National Weather Service provides a standardized real-time repository of severe weather alerts in the Atom XML format.  The amateur radio APRS Working Group has published a specification which defines a National Weather Service bulletin format as a way to distribute severe weather alerts over the APRS data network.  This code is designed to bring these two specifications together with the end goal of creating standardized text-based severe weather warnings on the APRS network.

## US National Weather Service Bulletin Info
The US National Weather Service regularly publishes weather alerts in the Atom format:  https://alerts.weather.gov/
Technical notes about the CAP (Common Alerting Protocol) and Atom syndication format are also available at the above link.

## APRS Specification
The APRS Working Group's original specification for APRS messages is available here:  http://www.aprs.org/doc/APRS101.PDF
Addendum 1.1 to the original specification was approved by the APRS Working Group in 2004:  http://www.aprs.org/aprs11.html
Addendum 1.2 to the original specification consists of proposals yet to be adopted the the Working Group but have been implemented to varying degrees in some hardware, as well as some client/server software:  http://www.aprs.org/aprs12.html

The original APRSv1.01 specification provided for a specific NWS Bulletin format derived from the standard APRS bulletin.  Of note, the NWS Bulletin format consisted of a bulletin addressed to `NWS-xxxxx` where the `xxxxx` was intended to identify the type of weather bulletin.  Also of note, the original specification declined to specify bulletin text length as part of the message standard.

## APRS-NWS Weather Bulletin Format
In an effort to improve usability of the original NWS Bulletin format while honoring the limited bandwidth available on conventional RF channels, an improved NWS Bulletin format was needed for this project.  Considerations for the format improvement included:

* Bulletin format should make targeted bulletin reception by end-users a simple process using existing message/bulletin filters present in hardware/software implementations of the APRS specification, while preventing unintentional/irritating saturation during periods of intense/widespread weather activity
* Bulletin format should allow an average recipient to quickly determine basic alert information (type of alert, location, level of hazard, begin & end times, etc.) by simply reading the received text
* Bulletins should conform to General Bulletin length standards as identified in the APRSv1.01 specification to ensure that existing hardware/software properly displays the alert without truncation

After integrating the above considerations, the following format was devised:
Item | : | ADDRESS | : | ZONETEXT | {sp} | \* | EVENT TYPE | \* | TYPE | {sp} | SEV | - | CER | - | URG | {sp} | CATG | {sp} | EVT START | - | EVT END | { | ID |
-----|---|---------|---|----------|------|----|------------|----|------|------|-----|---|-----|---|-----|------|------|------|-----------|---|---------|---|----|
Bytes| 1 |    9    | 1 |    15    |   1  |  1 |     10     |  1 |  4   |   1  |  3  | 1 |  3  | 1 |  3  |   1  |   4  |   1  |     7     | 1 |     7   | 1 |  5

The fields above are specified as follows.  Single byte ASCII characters in the above template are literals and `{sp}` denotes a space:

*ADDRESS*: The bulletin address per the APRS specification.  The original APRS specification's `NWS-xxxxx` format has been replaced with the six-character CAP geocode UGC zone value derived from the NWS weather alert feed format.  The zones pertinent to each US state can be found at the NWS weather alert website listed above.  Examples of valid zones include `NMC035` (Otero County) or `NMZ414` (West Slopes Sacramento Mountains Below 7500 Feet).

The address was changed from the APRS specification to prevent flooding end-user devices/software with alerts which are irrelevant to that user's local area.  Many APRS devices/software come configured to receive weather bulletins using the `NWS*` message/bulletin filter.  To prevent flooding those devices, end users can simply change their group message/bulletin filters to identify the specific zones for which they prefer to receive text-based weather alerts.  Other alert packets will be passed by digipeaters based on the APRS transmit path, but only packets matching end-point device filters will be displayed to the user.

*ZONETEXT*: This 15-character text is created by matching the NWS-assigned text label for the zone/county from the ADDRESS field to a Python dictionary key pairing that standard label with a **user-created** 15-character abbreviation for that zone text label.  The abbreviated label should be human-readable.  Eventually, stand-alone dictionary files for all 50 states will be created, and operators will be able to pull in a dictionary for a specific state using the Python import function.

*EVENT TYPE*: This value is another Python dictionary lookup which matches the NWS/CAP standard types of weather alerting events with **user-created** 10-character abbreviations.  This process has already been accomplished and captured in the `aprsnws.py` file using CAP1.1 standards.

*TYPE*: This value is another Python dictionary lookup matching the CAP standard message type data.  See the CAP documentation at the NWS site for details.

*SEV*: This value is another Python dictionary lookup matching the CAP standard weather severity assessment.  See the CAP documentation at the NWS site for details.

*CER*: This value is another Python dictionary lookup matching the CAP standard weather certainty assessment.  See the CAP documentation at the NWS site for details.

*URG*: This value is another Python dictionary lookup matching the CAP standard alert urgency assessment.  See the CAP documentation at the NWS site for details.

*CATG*: This value is another Python dictionary lookup matching the CAP standard alert category.  See the CAP documentation at the NWS site for details.

*EVT START and EVT END*: These values are date/time pairs indicating the beginning and end of the alert forecast period.  Date/times are in the format DD/HHMM.

*ID*: Each bulletin is sent with an appended 5-character message ID per the APRS specification.  Normally, ID's are used by client software to formulate a message ACK return message; however, bulletins/group messages should not be ACK'ed.  The ID is included as many client devices/software prevent the display of duplicate messages by matching incoming message ID's with already received message ID's.  The ID in this program is generated by using the Python `hash()` function.  Once a weather bulletin is fully assembled, the string is run through the `hash()` function and the last 5 characters of the hash string are sliced to form the message ID.  The `hash()` function will return the same hash every time a message is run through the function *as long as the aprsnws.py script has not been stopped and restarted.*  If the script is stopped and restarted, or if two different instances of the script are pushing packets into the same RF coverage area, end users may receive multiple copies of the same message due to two different message ID's being generated by two different instances of the software.

## APRX Integration ##
This program was designed to produce output to *stdout* to factilitate compatibility with the Kenneth Finnegan (W6KWF) fork of APRX: https://thelifeofkenneth.com/aprx/
This program uses the `<beacon>` *exec* method outlined in Kenneth's APRX manual, where APRX will read and send each line written to *stdout* as an APRS packet. Creating a `<beacon>` section in the APRX config file which uses the *exec* function pointed at *aprxfeeder.py* will cause APRX to run *aprxfeeder.py* at the configured beacon interval and beacon any weather alerts output to *stdout*.  Note: there is no packet validation process in APRX when reading from *stdout*, so incorrectly formed packets produced by APRS-NWS will be transmitted without further checking.

To have this software work correctly, the sysop must first start an instance of *aprsnws.py* running in the background:

`./aprsnws.py &`

Once *aprsnws.py* is running in the background, it will generate a new */tmp/wxalerts.txt* file at the interval specified in the main program *while True* loop.  When creating the `<beacon>` section in */etc/aprx.conf*, for best performance ensure the weather alert beacon section is set to a relatively short cycle time (i.e. 5 minutes).  Each time *aprx* runs a beacon cycle, *aprxfeeder.py* will open/read the */tmp/wxalerts.py* file and push the first line of the file to *stdout*, then strip that line out of the file.  With a short cycle time, this process will transmit all alerts in the file one at a time in 5 minute intervals.  The transmit interval may need to be adjusted in the *aprx.conf* file depending on how may alerts appear in the systop alert area.

## Beacon PATH Considerations ##
> With great power comes great responsibility.       --*Uncle Ben*

When transmitting these packets, it is **strongly** recommended that sysops utilize the **SSn-N** paradigm wherever local digipeaters are configured to do so.  If local digipeaters do not implement the SSn-N paradigm, sysops should limit the number of hops to a number appropriate to cover no further than their state border.  In most cases, this can be accomplished using a path of **WIDE2-2**.

Sysops desiring to implement APRS-NWS on a digipeater should carefully search http://aprs.fi for packets already being generated by an instance of APRS-NWS for their state.  Search for **SSZ*** or **SSC*** where *SS* is the US Postal Service two-letter abbreviation for your state.  If another instance of APRS-NWS is already operating in your state, coordination with the sysop will likely be required to implement APRS-NWS from two different systems in the same state (see the *ID* section above for the why...)

## Dependencies ##
This program depends on the following Python libraries:  lxml, requests, io, datetime, and os.  Depending on your Python installation, missing libraries can be installed using `pip3 install` plus the missing package names.  Also, on Linux machines the program may require the installation of `libxslt-dev` package using your distribution package manager. 
