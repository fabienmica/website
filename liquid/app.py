from liquid import Environment, CachingFileSystemLoader
from lxml import etree
import html5lib

env = Environment(loader=CachingFileSystemLoader("templates"))

# Render your Liquid template
template = env.get_template("index.liquid")
raw_html = template.render(name="Fabien", page_title="Home")

# Parse and beautify the HTML -> TODO at the end to fix everything
# document = html5lib.parse(raw_html, treebuilder="lxml", namespaceHTMLElements=False)
# pretty_html = etree.tostring(document, pretty_print=True, encoding="unicode")

with open("output.html", "w") as f:
    #f.write(pretty_html)    
    f.write(raw_html)