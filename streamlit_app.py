import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

# Fungsi untuk membuat gambar undangan
def generate_invitation(template_path, names, date, location):
    # Membuka template gambar
    template = Image.open(template_path)
    draw = ImageDraw.Draw(template)

    # Menentukan font
    font_path = "arial.ttf"  # Sesuaikan dengan path font yang ada di sistem Anda
    try:
        font_title = ImageFont.truetype(font_path, 40)
        font_body = ImageFont.truetype(font_path, 30)
    except:
        st.error("Font tidak ditemukan! Harap pastikan font tersedia.")
        return template

    # Menambahkan teks ke undangan
    text_color = (255, 255, 255)  # Warna teks putih

    # Menambahkan nama pengantin
    draw.text((100, 200), f"Undangan Pernikahan", fill=text_color, font=font_title)
    draw.text((100, 300), f"{names}", fill=text_color, font=font_body)

    # Menambahkan tanggal dan lokasi
    draw.text((100, 400), f"Tanggal: {date}", fill=text_color, font=font_body)
    draw.text((100, 500), f"Lokasi: {location}", fill=text_color, font=font_body)

    return template

# Streamlit UI
st.title("Aplikasi Undangan Pernikahan Online")

# Input dari pengguna
names = st.text_input("Masukkan Nama Pengantin", "Contoh: Aziz & Meylaini")
date = st.date_input("Pilih Tanggal Pernikahan")
location = st.text_input("Masukkan Lokasi Pernikahan", "Contoh: Gedung Serba Guna, Jakarta")

# Pilihan template
st.subheader("Pilih Template Latar Belakang")
template_options = {
    "Template 1": "template1.jpg",
    "Template 2": "template2.jpg",
    "Template 3": "template3.jpg",
}
selected_template = st.selectbox("Pilih Template", list(template_options.keys()))
template_path = template_options[selected_template]

# Tombol untuk membuat undangan
if st.button("Buat Undangan"):
    # Periksa apakah file template ada
    if not os.path.exists(template_path):
        st.error("Template tidak ditemukan! Harap periksa kembali file template.")
    else:
        # Generate undangan
        invitation = generate_invitation(template_path, names, date.strftime('%d %B %Y'), location)

        # Tampilkan undangan
        st.image(invitation, caption="Undangan Pernikahan Anda", use_column_width=True)

        # Unduh undangan
        invitation_path = "undangan_pernikahan.png"
        invitation.save(invitation_path)
        with open(invitation_path, "rb") as file:
            st.download_button("Unduh Undangan", file, file_name="undangan_pernikahan.png", mime="image/png")
