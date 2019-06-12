import sys
import datetime
import xml.sax.saxutils

COPYRIGHT_TEMPLATE = "Copyright (c) {0} {1}. All right reserved"
STYLESHEET_TEMPLATE = ('<link rel="stylesheet" type="text/css"'
                       'media="all" href="{0}"/>\n')

HTML_TEMPLATE = """<?xml version="1.0"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" \
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<title>{title}</title>
<!-- {copyright} -->
<meta name="Description" content="{description}" />
<meta name="Keywords" content="{keywords}" />
<meta name="content-type" content="text/html; charset=utf-8" />
{stylesheet}\
</head>
<body>

</body>
</html>
"""

class CancelledError(Exception): pass

def main():
    information = dict(name=None, year=datetime.date.today().year,
                       filename=None, title=None, description=None,
                       keywords=None, stylesheet=None)
    while True:
        try:
            print("Make Html Skeleton")
            populate_information(information)
            make_html_skeleton(**information)
        except CancelledError:
            print("Canceled")
        if(get_string("\nCreate another (y/n)?", default="y").lower()
            not in {"y", "yes"}):
            break

