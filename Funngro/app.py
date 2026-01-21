from flask import Flask, render_template, Response, request

app = Flask(__name__)

# ✅ HOME PAGE
@app.route("/")
def home():
    full_url = request.url_root.rstrip("/") + "/"
    seo = {
        "title": "Funngro Teen Freelancing | Earn, Learn & Build Portfolio",
        "description": "A Funngro-style teen freelancing platform where students work on real company projects, build skills, earn money and grow early.",
        "keywords": "funngro, teen freelancing, student projects, earn money online, internships for students, portfolio building",
        "canonical": full_url
    }
    return render_template("index.html", seo=seo)


# ✅ CATEGORIES PAGE
@app.route("/categories")
def categories():
    full_url = request.url_root.rstrip("/") + "/categories"
    seo = {
        "title": "Project Categories | Marketing, Design, Development & More",
        "description": "Explore categories like Social Media Marketing, Video Creation, Website Design, Mobile App Development, Content Writing and more.",
        "keywords": "student freelancing categories, teen projects, website design, app development, marketing tasks",
        "canonical": full_url
    }
    return render_template("categories.html", seo=seo)


# ✅ ROBOTS.TXT
@app.route("/robots.txt")
def robots_txt():
    content = f"""User-agent: *
Allow: /
Sitemap: {request.url_root.rstrip('/')}/sitemap.xml
"""
    return Response(content, mimetype="text/plain")


# ✅ SITEMAP.XML
@app.route("/sitemap.xml")
def sitemap_xml():
    root = request.url_root.rstrip("/")
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

  <url>
    <loc>{root}/</loc>
    <priority>1.0</priority>
  </url>

  <url>
    <loc>{root}/categories</loc>
    <priority>0.8</priority>
  </url>

</urlset>
"""
    return Response(xml, mimetype="application/xml")


# ✅ OPTIONAL: LOCAL RUN (NOT REQUIRED FOR VERCEL)
if __name__ == "__main__":
    app.run(debug=True)
