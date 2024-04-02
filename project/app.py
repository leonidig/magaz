from flask import Flask, render_template, url_for


app = Flask(__name__)



def get_consoles():
    consoles = [
        {"name": "PlayStation 5", "description": "Play Station 5 | 825gb", "price": 550, "image": "static/images/consoles/image1.jpg"},
        {"name": "PlayStation 4 Pro", "description": "PlayStation 4 Pro | 1TB", "price": 500, "image": "static/images/consoles/image2.webp"},
        {"name": "Xbox Series X", "description": "XBox X | 1TB", "price": 400, "image": "static/images/consoles/image3.jpg"},
        {"name": "Xbox Series S", "description": "Xbox Series S | White | 512GB", "price": 270, "image": "static/images/consoles/image4.webp"},
        {"name": "Nintendo Switch Oled", "description": "Nintendo Switch Oled | White | 64GB", "price": 500, "image": "static/images/consoles/image5.avif"},
        {"name": "PlayStation 5 Slim DE", "description": "PS 5 Slim | 1Tb", "price": 570, "image": "static/images/consoles/image6.webp"},
        {"name": "Xbox Series S", "description": "Xbox Series S | 1Tb | Black", "price": 460, "image": "static/images/consoles/image7.avif"},
        {"name": "Asus ROG Ally Extreme", "description": "Asus ROG Ally Extreme| 512gb | White", "price": 846, "image": "static/images/consoles/image8.avif"},
        {"name": "Nintendo Switch Lite", "description": "Nintendo Switch Lite | 32gb | Gray", "price": 290, "image": "static/images/consoles/image10.jpg"},
        {"name": "Steam Deck", "description": "Steam Deck | Oled | 1TB", "price": 1170, "image": "static/images/consoles/image11.webp"},
    ]
    return consoles


def get_phones():
    phones = [
        {"name": "iPhone 15 Pro Max", "description": "iPhone 15 Pro Max | 256gb | Natural Titanium", "price": 1500, "image": "static/images/phones/image9.webp"},
        {"name": "Xiaomi 14", "description": "Xiaomi 14 | 512gb | Black", "price": 1050, "image": "static/images/phones/image12.avif"},
        {"name": "Poco X6 Pro", "description": "Poco X6 Pro | 512gb | Black", "price": 420, "image": "static/images/phones/image13.avif"},
        {"name": "Samsung Galaxy Fold5", "description": "Samsung Galaxy Fold5 | 512gb | Black", "price": 2000, "image": "static/images/phones/image14.avif"},
        {"name": "OPPO Reno10 Pro", "description": "OPPO Reno10 Pro | 256gb | Silvery Grey", "price": 570, "image": "static/images/phones/image15.avif"},
        {"name": "Samsung Galaxy S24 Ultra", "description": "Samsung Galaxy S24 Ultra | 512gb | Titanium Gray", "price": 1600, "image": "static/images/phones/image16.avif"},
        {"name": "OnePlus 9 Pro ", "description": "OnePlus 9 Pro | 128gb | Morning Mist", "price": 700, "image": "static/images/phones/image17.avif"},
        {"name": "vivo V23e ", "description": "vivo V23e | 128gb | Moonlight Shadow", "price": 250, "image": "static/images/phones/image18.avif"}
    ]
    return phones



@app.get("/")
def main():
    consoles = get_consoles()
    phones = get_phones()
    products = consoles + phones
    return render_template("index.html", products=products)


@app.get("/consoles")
def console():
    consoles = get_consoles()
    return render_template("consoles.html", products=consoles)


@app.get("/phones")
def phone():
    phones = get_phones()
    return render_template("phones.html", products=phones)



if __name__ == '__main__':
    app.run(debug=True)
