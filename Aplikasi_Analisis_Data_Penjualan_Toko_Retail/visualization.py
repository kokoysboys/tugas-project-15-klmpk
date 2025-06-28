import matplotlib.pyplot as plt
from collections import defaultdict

def plot_best_selling_products(data, save_path):
    count = defaultdict(int)
    for item in data:
        count[item['nama_produk']] += item['jumlah']
    labels = list(count.keys())
    values = list(count.values())

    plt.figure(figsize=(8,5))
    plt.bar(labels, values, color='skyblue')
    plt.xlabel("Produk")
    plt.ylabel("Jumlah Terjual")
    plt.title("Produk Terlaris")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_category_distribution(data):
    count = defaultdict(int)
    for item in data:
        count[item['kategori']] += 1
    labels = list(count.keys())
    values = list(count.values())

    plt.figure(figsize=(6,6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Distribusi Transaksi per Kategori")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
