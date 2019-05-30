import sys

sites={}

for filename in sys.argv[1:]:
    for line in open(filename, encoding="utf8"):
        idx = 0
        while True:
            idx = line.find("http://", idx)
            if idx > -1:
                site=None
                idx += len("http://")
                for j in range(idx, len(line)):
                    if not (line[j].isalnum() or line[j] in ".-/"):
                        site = line[idx:j].lower()
                        print(site)
                        break
                if site and "." in site:
                    sites.setdefault(site, set()).add(filename)
                idx = j
            else:
                break

"""for site,filename in sites.items():
    print("{}:{}".format(site, filename))"""

for site in sorted(sites):
    print("{0} is referred to in:".format(site))
    for filename in sorted(sites[site], key=str.lower):
        print("    {0}".format(filename))