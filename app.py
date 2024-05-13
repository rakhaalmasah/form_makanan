from flask import Flask, render_template, request

app = Flask(__name__)

menu_makanan = [
    {'nomor': 1, 'teks': 'Pecel Lele', 'harga': 15000, "jumlah" : 0},
    {'nomor': 2, 'teks': 'Nasi Bandeng', 'harga': 20000, "jumlah" : 0},
    {'nomor': 3, 'teks': 'Orak Arik Ayam', 'harga': 17500, "jumlah" : 0},
    {'nomor': 4, 'teks': 'Omlete Mie', 'harga': 20000, "jumlah" : 0},
    {'nomor': 5, 'teks': 'Es Teh', 'harga': 5000, "jumlah" : 0},
    {'nomor': 6, 'teks': 'Es Jeruk', 'harga': 7500, "jumlah" : 0},
]

judul_tabel = [
    {'teks': 'No.'},
    {'teks': 'Nama Makanan'},
    {'teks': 'Harga'},
    {'teks': 'Qty'},
    {'teks': 'Jumlah'},
]

@app.context_processor
def inject_navbar():
    for menu in menu_makanan:
        menu['harga_formatted'] = 'Rp. {:,}'.format(menu['harga'])
        menu['jumlah_formatted'] = 'Rp. {:,}'.format(menu['jumlah'])
    return dict(menu_makanan=menu_makanan, judul_tabel=judul_tabel)

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        for menu in menu_makanan:
            menu['qty'] = 0
            menu['jumlah'] = 0
        total_harga = 'Rp. 0'
    return render_template('index.html', total_harga=total_harga)

@app.route('/', methods=['POST'])
def post_index():
    total_harga = 0
    qty_values = request.form.getlist('qty')
    for i, menu in enumerate(menu_makanan):
        try:
            menu['qty'] = int(qty_values[i])
            menu['jumlah'] = menu['qty'] * menu['harga']
            total_harga += menu['jumlah']
        except ValueError:
            menu['qty'] = 0
            menu['jumlah'] = 0
    total_harga = 'Rp. {:,}'.format(total_harga)
    for menu in menu_makanan:
        menu['jumlah_formatted'] = 'Rp. {:,}'.format(menu['jumlah'])
    return render_template('index.html', total_harga=total_harga)

if __name__ == '__main__':
    app.run(debug=True)
