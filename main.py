import argparse
import urllib.request
import urllib.parse
import yaml

# with open('yamlExportFile.yaml', 'w') as stream:
#   document = yaml.dump({'level0': range(50)}, stream,width=50,indent=5)

parser = argparse.ArgumentParser(description='Crawler')
parser.add_argument('--depth', type=int, help='Depth of the crawler')
parser.add_argument('--regex', type=list[str], help='Regex for the crawler')
parser.add_argument('--url', type=str, help='URL to crawler')
arguments = parser.parse_args()

links = [set()]
visited_links = set()

links[0].add(arguments.url)
visited_links.add(arguments.url)

def valid(url, regex):
    for check in regex:
        if check in url:
            return False
    return True

for layer in range(arguments.depth):
    links.append(set())
    for cLink in links[layer]:
        try:
            web_handler = urllib.request.urlopen(url=cLink)
            HTML_code = web_handler.read().decode("utf8")
            last_found = 0
            while HTML_code.find('href="', last_found) != -1:
                href_start = HTML_code.find('href="', last_found) + 6
                href_end = HTML_code.find('"', href_start)
                link = HTML_code[href_start:href_end]
                link = urllib.parse.urljoin(cLink, link)
                print(link)
                print(valid(link,arguments.regex))
                if link not in visited_links and not valid(link,arguments.regex):
                    links[layer + 1].add(link)
                    visited_links.add(link)
                last_found = HTML_code.find('href="', last_found) + 7
        except Exception as e:
            print(f'Error in {cLink}, {e}')
print(links)
