from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.get('/')
def index():
    products = [
        {"name": "PlayStation 5", "description": "Play Station 5 | 825gb", "price": 550, "image": "static/images/image1.jpg"},
        {"name": "PlayStation 4 Pro", "description": "PlayStation 4 Pro | 1TB", "price": 500, "image": "static/images/image2.webp"},
        {"name": "Xbox Series X", "description": "XBox X | 1TB", "price": 400, "image": "static/images/image3.jpg"},
        {"name": "Xbox Series S", "description": "Xbox Series S | White | 512GB", "price": 270, "image": "static/images/image4.webp"},
        {"name": "Nintendo Switch Oled", "description": "Nintendo Switch Oled | White | 64GB", "price": 500, "image": "static/images/image5.avif"},
        {"name": "PlayStation 5 Slim Digital Edition", "description": "PS 5 Slim | 1Tb", "price": 60, "image": "static/images/image6.webp"},
        # {"name": "Leo14kris", "description": "Best console ever", "price": 1488, "image": "pass"}
    ]
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
