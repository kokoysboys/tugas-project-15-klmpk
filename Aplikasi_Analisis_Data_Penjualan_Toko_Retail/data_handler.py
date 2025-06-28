import csv
from collections import defaultdict

def load_data(filepath):
    data = []
    try:
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['jumlah'] = int(row['jumlah'])
                row['harga'] = int(row['harga'])
                data.append(row)
        return data
    except FileNotFoundError:
        raise Exception("File tidak ditemukan.")
    except ValueError:
        raise Exception("Format data salah.")

def calculate_total_revenue(data):
    return sum(item['jumlah'] * item['harga'] for item in data)

def get_best_selling_product(data):
    produk_count = defaultdict(int)
    for item in data:
        produk_count[item['nama_produk']] += item['jumlah']
    return max(produk_count, key=produk_count.get)

def get_transaction_count_by_category(data):
    kategori_count = defaultdict(int)
    for item in data:
        kategori_count[item['kategori']] += 1
    return kategori_count
