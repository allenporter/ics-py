cal1 = """
BEGIN:VCALENDAR
METHOD:PUBLISH
VERSION:2.0
X-WR-CALNAME:plop
PRODID:-//Apple Inc.//Mac OS X 10.9//EN
X-APPLE-CALENDAR-COLOR:#882F00
X-WR-TIMEZONE:Europe/Brussels
CALSCALE:GREGORIAN
BEGIN:VTIMEZONE
TZID:Europe/Brussels
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
DTSTART:19810329T020000
TZNAME:UTC+2
TZOFFSETTO:+0200
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
DTSTART:19961027T030000
TZNAME:UTC+1
TZOFFSETTO:+0100
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20131024T204716Z
UID:ABBF2903-092F-4202-98B6-F757437A5B28
DTEND;TZID=Europe/Brussels:20131029T113000
TRANSP:OPAQUE
SUMMARY:dfqsdfjqkshflqsjdfhqs fqsfhlqs dfkqsldfkqsdfqsfqsfqsfs
DTSTART;TZID=Europe/Brussels:20131029T103000
DTSTAMP:20131024T204741Z
SEQUENCE:3
DESCRIPTION:Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed 
 vitae facilisis enim. Morbi blandit et lectus venenatis tristique. Donec 
 sit amet egestas lacus. Donec ullamcorper, mi vitae congue dictum, quam 
 dolor luctus augue, id cursus purus justo vel lorem. Ut feugiat enim ips
 um, quis porta nibh ultricies congue. Pellentesque nisl mi, molestie id 
 sem vel, vehicula nullam.
END:VEVENT
END:VCALENDAR
"""

cal2 = """
BEGIN:VCALENDAR
BEGIN:VEVENT
DTEND;TZID=Europe/Berlin:20120608T212500
SUMMARY:Name
DTSTART;TZID=Europe/Berlin:20120608T202500
LOCATION:MUC
SEQUENCE:0
BEGIN:VALARM
TRIGGER:-PT1H
DESCRIPTION:Event reminder
ACTION:DISPLAY
END:VALARM
END:VEVENT
END:VCALENDAR
"""

cal3 = """
BEGIN:VCALENDAR
END:VCALENDAR
"""

cal4 = """BEGIN:VCALENDAR"""

cal5 = """
BEGIN:VCALENDAR
VERSION:2.0
END:VCALENDAR
"""

cal6 = """
DESCRIPTION:a
 b
"""

cal7 = """
BEGIN:VCALENDAR

END:VCALENDAR
"""

cal8 = """
BEGIN:VCALENDAR
\t
END:VCALENDAR
"""

cal9 = """

BEGIN:VCALENDAR
END:VCALENDAR
"""


unfolded_cal2 = [
'BEGIN:VCALENDAR',
'BEGIN:VEVENT',
'DTEND;TZID=Europe/Berlin:20120608T212500',
'SUMMARY:Name',
'DTSTART;TZID=Europe/Berlin:20120608T202500',
'LOCATION:MUC',
'SEQUENCE:0',
'BEGIN:VALARM',
'TRIGGER:-PT1H',
'DESCRIPTION:Event reminder',
'ACTION:DISPLAY',
'END:VALARM',
'END:VEVENT',
'END:VCALENDAR',
]

unfolded_cal1 = [
'BEGIN:VCALENDAR',
'METHOD:PUBLISH',
'VERSION:2.0',
'X-WR-CALNAME:plop',
'PRODID:-//Apple Inc.//Mac OS X 10.9//EN',
'X-APPLE-CALENDAR-COLOR:#882F00',
'X-WR-TIMEZONE:Europe/Brussels',
'CALSCALE:GREGORIAN',
'BEGIN:VTIMEZONE',
'TZID:Europe/Brussels',
'BEGIN:DAYLIGHT',
'TZOFFSETFROM:+0100',
'RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU',
'DTSTART:19810329T020000',
'TZNAME:UTC+2',
'TZOFFSETTO:+0200',
'END:DAYLIGHT',
'BEGIN:STANDARD',
'TZOFFSETFROM:+0200',
'RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU',
'DTSTART:19961027T030000',
'TZNAME:UTC+1',
'TZOFFSETTO:+0100',
'END:STANDARD',
'END:VTIMEZONE',
'BEGIN:VEVENT',
'CREATED:20131024T204716Z',
'UID:ABBF2903-092F-4202-98B6-F757437A5B28',
'DTEND;TZID=Europe/Brussels:20131029T113000',
'TRANSP:OPAQUE',
'SUMMARY:dfqsdfjqkshflqsjdfhqs fqsfhlqs dfkqsldfkqsdfqsfqsfqsfs',
'DTSTART;TZID=Europe/Brussels:20131029T103000',
'DTSTAMP:20131024T204741Z',
'SEQUENCE:3',
'DESCRIPTION:Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae facilisis enim. Morbi blandit et lectus venenatis tristique. Donec sit amet egestas lacus. Donec ullamcorper, mi vitae congue dictum, quam dolor luctus augue, id cursus purus justo vel lorem. Ut feugiat enim ipsum, quis porta nibh ultricies congue. Pellentesque nisl mi, molestie id sem vel, vehicula nullam.',
'END:VEVENT',
'END:VCALENDAR',
]

unfolded_cal6 = ['DESCRIPTION:ab']