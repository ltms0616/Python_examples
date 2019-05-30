import sys

def main():
    write_start()
    read_fp = open("country_data.txt", "r")
    write_fp = open("country_data.html", "a")
    count = 0
    line = read_fp.readline()
    while line:
        if count == 0:
            color = "lightgreen"
        elif count % 2:
            color = "white"
        else:
            color = "lightyellow"
        write_lines(write_fp, line, color)
        line = read_fp.readline()
        count += 1
    read_fp.close()
    write_fp.close()
    write_end()

def write_start():
    with open("country_data.html", "w") as fp:
        fp.write("<table border=1>")

def write_lines(fp, line, color):
    fields = extract_fields(line)
    fp.write("<tr bgcolor={}>".format(color))
    for field in fields:
        if not field:
            fp.write("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                fp.write("<td>{:d}</td>".format(round(x)))
            except ValueError:
                field = field.title()
                fp.write("<td>{}</td>".format(field))
    fp.write("</tr>")

def extract_fields(line):
    fields=[]
    quote = None
    field = ""
    for x in line:
        if x in "\"'":
            if quote is None:
                quote = x
            elif quote == x:
                quote = None
            else:
                field += x
        elif quote is None and x == ",":
            fields.append(field)
            field=""
        else:
            field += x
    if field:
        fields.append(field)
    return fields

#def escape_html():

def write_end():
    with open("country_data.html", "a") as fp:
        fp.write("</table>")

main()

