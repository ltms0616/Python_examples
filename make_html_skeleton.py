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


def populate_information(info):

    try:
        name = get_string("Enter your name (for copyright)", "name", info["name"])
        if not name:
            raise CancelledError()

        year = get_integer("Enter copyright year [{0}]:", "year", info["year"], 2000,
                           datetime.date.today().year+1, True)
        if year == 0:
            raise CancelledError()

        filename = get_string("Enter filename", "filename", info["filename"])
        if not filename:
            raise CancelledError()

        title = get_string("Enter title", "title", info["title"])
        if not title:
            raise CancelledError()

        description = get_string("Enter description", "description", info["description"])
        if not description:
            raise CancelledError()

        while True:
            keyword = get_string("Enter a keyword (optional)", "keyword", info["keyword"])
            if not keyword:
                raise CancelledError()
            else:
                info[keyword].append(keyword)

        stylesheet = get_string("Enter stylesheet filename", "stylesheet", info["stylesheet"])
        if not stylesheet:
            raise CancelledError()

    except CancelledError:
        print("Cancelled")


def get_string(message, name="string", default=None, min_length=0, max_length=80):
    message += ": "if default is None else "[{0}]".format(default)
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if min_length == 0:
                    return ""
                else:
                    raise ValueError("{0} may not be empty".format(name))
            if not (min_length <= len(line) <= max_length):
                raise ValueError("{name} must have at least"
                                 "{min_length} and at most"
                                 "{max_length} characters".format(**locals()))
            return line
        except ValueError as err:
            print("ERROR", err)

def get_integer(message, name="integer", default=None, minimum=0, maximum=100, allow_zero=True):
    message += ": "if default is None else "[{0}]".format(default)
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                else:
                    raise ValueError("{0} may not be empty".format(name))
            if not (minimum <= int(line) <= maximum):
                raise ValueError("{name} must between {minimum} and {maxmum}".format(**locals()))
            return line
        except ValueError as err:
            print("ERROR", err)
