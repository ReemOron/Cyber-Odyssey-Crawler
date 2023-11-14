import argparse
import urllib.request
import yaml

#with open('yamlExportFile.yaml', 'w') as stream:
#   document = yaml.dump({'level0': range(50)}, stream,width=50,indent=5)

parser = argparse.ArgumentParser(description='Crawler')
parser.add_argument('--url', type=str, help='URL to crawler')
arguments = parser.parse_args()

links = set()

web_handler = urllib.request.urlopen(url=arguments.url)
HTML_code = web_handler.read().decode("utf8")

last_found = 0
while HTML_code.find('href="', last_found) != -1:
    href_place = HTML_code.find('href="', last_found) + 6
    link = ""
    while HTML_code[href_place] != '"':
        link += HTML_code[href_place]
        href_place += 1
    links.add(link)
    last_found = HTML_code.find('href="', last_found) + 7

print(links)
