import sys

def write_start(htmlfile):
    htmlfile.write("<table border='1'>")

def write_end(htmlfile):
    htmlfile.write("</table>")
def escape_html(data):
    data = data.replace("&", "&amp;")
    data = data.replace("<", "&lt;")
    data = data.replace(">", "&gt;")
    return data

def write_fields(file, fields, color, maxwidth):
    file.write("<tr bgcolor='{0}'>".format(color))
    for field in fields:
        if not field:
            file.write("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                data = float(number)
                file.write("<td align='right'>{0:d}</td>".format(round(data)))
            except ValueError:
                field = field.title()
                field = field.replace(" AND ", " and ")
                if len(field) < maxwidth:
                    field = escape_html(field)
                else:
                    field = "{0}...".format(escape_html(field[0:maxwidth]))
                file.write("<td>{0}</td>".format(field))
    file.write("</tr>\n")
def extract_fields(line):
    field=""
    fields = []
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:
                quote = c
            elif quote == c:
                quote = None
            else:
                field += c
        elif quote is None and c == ",":
            fields.append(field)
            field = ""
        else:
            field += c
    if field:
        fields.append(field)
    return fields
def main():
    if len(sys.argv)>1:
        if sys.argv[1] in ("-h", "--help"):
            print("usage: {0} [csvfile] [htmlfile]".format(sys.argv[0]))
        elif sys.argv[1].lower().endswith(".csv"):
            infile = sys.argv[1]
        else:
            print("wrong input")
            print("usage: {0} [csvfile] [htmlfile]".format(sys.argv[0]))

        if len(sys.argv) > 2:
            if sys.argv[2].lower().endswith(".html"):
                outfile = sys.argv[2]
            else:
                outfile = "data.html"
    else:
        print("usage: {0} [csvfile] [htmlfile]".format(sys.argv[0]))

    csvfile = open(infile)
    htmlfile = open(outfile, 'a')
    write_start(htmlfile)
    count = 0
    maxwidth = 100
    while True:
        line = csvfile.readline()
        if not line:
            break
        if count == 0:
            color = "lightgreen"
        elif count%2:
            color = "white"
        else:
            color = "lightyellow"
        fields = extract_fields(line)
        write_fields(htmlfile, fields, color, maxwidth)
        count+=1
    write_end(htmlfile)
    csvfile.close()
    htmlfile.close()

main()