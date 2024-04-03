from flask import Flask, render_template
from dati import dabutrindas

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tests")
def te():
    return render_template("tests.html")

@app.route("/saraksts")
def saraksts():
    saraksts = ["kakis", "katla", "panna"]
    bildes = ["https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Felis_catus-cat_on_snow.jpg/1200px-Felis_catus-cat_on_snow.jpg", "https://arkolat.lv/storage/uploads/global/product_images/image/000/055/684/large/ef387b5ad94e9169c7f220dda11f92da.jpg", "https://ksd-images.lt/display/aikido/store/9e14ae8a2575d2ffabdc0c6476c47f3d.jpg"]
    
    kopejais_saraksts = []
    faila_rindas = dabutrindas()
    for rinda in faila_rindas:
        elements = rinda.split(", ")
        kopejais_saraksts.append(elements)
    
    return render_template("saraksts.html", vardi = saraksts, bildes = bildes)



if __name__ == '__main__':
      app.run(port = 5000)