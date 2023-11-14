import argparse
import urllib.request
import yaml

#with open('yamlExportFile.yaml', 'w') as stream:
#   document = yaml.dump({'level0': range(50)}, stream,width=50,indent=5)

parser = argparse.ArgumentParser(description='Crawler')
parser.add_argument('--url', type=str, help='URL to crawler')
parser.add_argument('--depth', type=int, help='Depth of the crawler')
arguments = parser.parse_args()

links = [set(arguments.url)]

for layer in range(arguments.depth):
    links.append(set())
    for link in links[layer]:
        web_handler = urllib.request.urlopen(url=link)
        HTML_code = web_handler.read().decode("utf8")
        last_found = 0
        while HTML_code.find('href="', last_found) != -1:
            href_place = HTML_code.find('href="', last_found) + 6
            link = ""
            while HTML_code[href_place] != '"':
                link += HTML_code[href_place]
                href_place += 1
            links[layer+1].add(link)
            last_found = HTML_code.find('href="', last_found) + 7

