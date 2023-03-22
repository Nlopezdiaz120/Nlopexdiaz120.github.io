from flask import Flask, request, render_template
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu', methods=['POST'])
def menu():
    name = request.form['name']
    group = request.form['group']
    menu_items = [
        ('Manzana', 10),
        ('Plátano', 5),
        ('Naranja', 8),
        ('Pera', 12),
        ('Mango', 15),
        ('Piña', 20),
        ('Sandía', 25),
        ('Melón', 18),
        ('Papaya', 22),
        ('Limón', 6)
    ]
    return render_template('menu.html', name=name, group=group, menu_items=menu_items)

@app.route('/order_confirmation', methods=['POST'])
def order_confirmation():
    item = request.form['item']
    price = request.form['price']
    qr = qrcode.QRCode(version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=4)
    qr.add_data(f'Item: {item}, Price: {price}')
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    img.save("qr_code.png")
    
    return render_template('order_confirmation.html', item=item, price=price)

if __name__ == '__main__':
    app.run()