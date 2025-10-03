from liquid import Environment, CachingFileSystemLoader
from lxml import etree
import html5lib
import shutil

def generateIndex(env, name, file, title):
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

# Load data
#with open("data/buf_projects.json") as f:
#    buf_projects = json.load(f)


env = Environment(loader=CachingFileSystemLoader("templates"))

generateIndex(env, "index", file="index.html", title="Fabien Micallef")
generateIndex(env, "portfolio-details", file="portfolio-enwaii.html", title="Enwaii")
generateIndex(env, "portfolio-details", file="portfolio-hold-the-world.html", title="Hold The World")
generateIndex(env, "portfolio-details", file="portfolio-vrsatile.html", title="VRsatile")
generateIndex(env, "portfolio-details", file="portfolio-pioneering.html", title="Pioneering Reality Capture")
generateIndex(env, "portfolio-details", file="portfolio-immersive.html", title="Immersive projects")
generateIndex(env, "portfolio-details", file="portfolio-commercials.html", title="Commercials")
