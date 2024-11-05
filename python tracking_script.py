import platform
import requests

def menu():
    print("   [+] TRACKING SCRIPT [+]")
    print("=================================")
    print("1. Menampilkan Informasi Perangkat")
    print("2. Menampilkan IP Publik (tidak tersedia di PyCode)")
    print("3. Cari Username (dengan link media sosial saja)")
    print("4. Melihat Informasi Nomor Telepon")
    print("0. Keluar")
    print("=================================")

def show_device_info():
    print("\nInformasi Perangkat:")
    print(f"Sistem Operasi: {platform.system()}")
    print(f"Versi OS: {platform.version()}")
    print(f"Prosesor: {platform.processor()}")
    print(f"Nama Perangkat: {platform.node()}")
    print(f"Versi: 1.1Beta")

def find_username():
    username = input("Masukkan username yang ingin dicari: ")
    platforms = {
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "X (Twitter)": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
    }

    print(f"\nLink profil untuk username '{username}':")
    for platform_name, url in platforms.items():
        print(f"{platform_name}: {url}")

def get_phone_info(phone_number):
    api_key = "386e33ea187d85de8dae9d8f2c412dce"  # API key Anda
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}"
    
    try:
        response = requests.get(url)
        data = response.json()
        if data.get('valid'):
            print("\nInformasi Nomor Telepon:")
            print(f"Nomor: {data['number']}")
            print(f"Internasional: {data['international_format']}")
            print(f"Negara: {data['country_name']}")
            print(f"Jenis: {data['line_type']}")
        else:
            print("Nomor telepon tidak valid.")
    except Exception as e:
        print("Terjadi kesalahan saat memanggil API:", str(e))

def phone_info():
    phone_number = input("Masukkan nomor telepon (tanpa spasi atau tanda): ")
    get_phone_info(phone_number)

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Pilih Opsi: ")
        
        if choice == "1":
            show_device_info()
        elif choice == "2":
            print("Fitur menampilkan IP publik tidak tersedia di PyCode.")
        elif choice == "3":
            find_username()
        elif choice == "4":
            phone_info()
        elif choice == "0":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

        input("\nTekan Enter untuk kembali ke menu...")