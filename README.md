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
```
      ----------------------------------------------------------------------------------------------------------------------------------------------------------
Item  | : | ADDRESS | : | ZONETEXT | {sp} | * | EVENT TYPE | * | TYPE | {sp} | SEV | - | CER | - | URG | {sp} | CATG | {sp} | EVT START | - | EVT END | { | ID |
       ---------------------------------------------------------------------------------------------------------------------------------------------------------
Bytes | 1 |    9    | 1 |    15    |   1  | 1 |     10     | 1 |   4  |   1  |  3  | 1 |  3  | 1 |  3  |   1  |   4  |   1  |      7    | 1 |    7    | 1 | 5  |
      ----------------------------------------------------------------------------------------------------------------------------------------------------------
```
The fields above are specified as follows:

* Single byte ASCII characters in the above template are literals and `{sp}` denotes a space.
