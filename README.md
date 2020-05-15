# APRS-NWS
The US National Weather Service provides a standardized real-time repository of severe weather alerts in the Atom XML format.  The amateur radio APRS Working Group has published a specification which defines a National Weather Service bulletin format as a way to distribute severe weather alerts over the APRS data network.  This code is designed to bring these two specifications together with the end goal of creating standardized text-based severe weather warnings on the APRS network.

This software provides the following:
* Python classes to validate and handle the CAP v1.1 format used to publish NWS weather alerts
* Python classes to transform NWS weather alerts from the Atom format into valid APRS NWS bulletins
* Python classes to publish valid APRS NWS bulletins to RF, as well as APRS-IS (if desired)
