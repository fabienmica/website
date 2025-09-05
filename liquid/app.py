from liquid import Environment, CachingFileSystemLoader

env = Environment(loader=CachingFileSystemLoader("templates"))
template = env.get_template("index.liquid")

html = template.render(name="Fabien", page_title="Home")
with open("output.html", "w") as f:
    f.write(html)