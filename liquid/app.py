from liquid import Environment, CachingFileSystemLoader
from lxml import etree
import html5lib
import shutil

def generateIndex(env, name, title, file):
    # Render your Liquid template
    template = env.get_template(name + ".liquid")
    raw_html = template.render(title=title)

    # Parse and beautify the HTML -> TODO at the end to fix everything
    #document = html5lib.parse(raw_html, treebuilder="lxml", namespaceHTMLElements=False)
    #pretty_html = etree.tostring(document, pretty_print=True, encoding="unicode")

    file_path_generated = "generated/" + file
    with open(file_path_generated, "w") as f:
        #f.write(pretty_html)    
        f.write(raw_html)
    
    #Copy file directly
    shutil.copy(file_path_generated, "../alquanti")

env = Environment(loader=CachingFileSystemLoader("templates"))

generateIndex(env, "index", title="Fabien Micallef", file="index.html")
generateIndex(env, "portfolio-details", title="Enwaii", file="portfolio-enwaii.html")
generateIndex(env, "portfolio-details", title="Hold The World", file="portfolio-hold-the-world.html")
generateIndex(env, "portfolio-details", title="VRsatile", file="portfolio-vrsatile.html")
generateIndex(env, "portfolio-details", title="Pioneering Reality Capture", file="portfolio-pioneering.html")
