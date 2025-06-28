import os
from data_handler import (
    load_data,
    calculate_total_revenue,
    get_best_selling_product,
    get_transaction_count_by_category,
)
from visualization import plot_best_selling_products, plot_category_distribution

def main():
    try:
        # Load data dari file CSV
        data = load_data("data/penjualan.csv")

        # Hitung total pendapatan
        total_revenue = calculate_total_revenue(data)

        # Cari produk terlaris
        best_seller = get_best_selling_product(data)

        # Hitung jumlah transaksi berdasarkan kategori
        category_counts = get_transaction_count_by_category(data)

        # Tampilkan hasil analisis
        print(f"Total Pendapatan: Rp{total_revenue:,}")
        print(f"Produk Terlaris: {best_seller}")
        print("Jumlah Transaksi per Kategori:")
        for category, count in category_counts.items():
            print(f" - {category}: {count} transaksi")

        # Pastikan folder 'img' ada sebelum menyimpan grafik
        os.makedirs("img", exist_ok=True)

        # Buat dan simpan grafik
        plot_best_selling_products(data, "img/grafik1.png")
        plot_category_distribution(data)

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
