import argparse
import urllib.parse
import urllib.request
import yaml

parser = argparse.ArgumentParser(description='Crawler')
parser.add_argument('--url', type=str, help='URL to crawl')
parser.add_argument('--depth', type=int, help='Depth of the crawler')
arguments = parser.parse_args()

links = [set()]
links[0].add(arguments.url)

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

                # Construct absolute URL from relative URL
                absolute_link = urllib.parse.urljoin(cLink, link)

                links[layer + 1].add(absolute_link)
                last_found = href_end + 1
        except Exception as e:
            print(f"Error processing URL {cLink}: {str(e)}")

# Convert sets to lists for YAML serialization
links_list = [list(link_set) for link_set in links]

# Save links to YAML file
with open('yamlExportFile.yaml', 'w') as stream:
    yaml.dump(links_list, stream, default_flow_style=False)
