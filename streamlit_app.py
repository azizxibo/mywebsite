import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

# Fungsi untuk membuat gambar undangan
def generate_invitation(template_path, names, date, location, font_choice, title_color, body_color, title_size, body_size):
    # Membuka template gambar
    template = Image.open(template_path)
    draw = ImageDraw.Draw(template)

    # Menentukan font
    font_paths = {
        "DanyMeka": "danymekafont.ttf",
        "TwenlyBoa": "twenlyboafont.ttf",
        "CloseFont": "closefont.ttf"
    }

    font_path = font_paths.get(font_choice, font_paths["Custom"])
    try:
        font_title = ImageFont.truetype(font_path, title_size)
        font_body = ImageFont.truetype(font_path, body_size)
    except:
        st.error("Font tidak ditemukan! Harap pastikan font tersedia.")
        return template

    # Menambahkan teks ke undangan
    # Menambahkan nama pengantin
    draw.text((100, 200), f"Undangan Pernikahan", fill=title_color, font=font_title)
    draw.text((100, 300), f"{names}", fill=body_color, font=font_body)

    # Menambahkan tanggal dan lokasi
    draw.text((100, 400), f"Tanggal: {date}", fill=body_color, font=font_body)
    draw.text((100, 500), f"Lokasi: {location}", fill=body_color, font=font_body)

    return template

# Streamlit UI
st.title("Aplikasi Undangan Pernikahan Online")

# Input dari pengguna
names = st.text_input("Masukkan Nama Pengantin", "Contoh: Aziz & Meylaini")
date = st.date_input("Pilih Tanggal Pernikahan")
location = st.text_input("Masukkan Lokasi Pernikahan", "Contoh: Gedung Serba Guna, Jakarta")

# Pilihan font
st.subheader("Pilih Font")
font_options = ["DanyMeka", "TwenlyBoa", "Custom"]
font_choice = st.selectbox("Pilih Font untuk Undangan", font_options)

# Pilihan warna
st.subheader("Pilih Warna Teks")
title_color = st.color_picker("Pilih Warna untuk Judul", "#FFFFFF")
body_color = st.color_picker("Pilih Warna untuk Subjudul", "#FFFFFF")

# Pilihan ukuran font
st.subheader("Pilih Ukuran Font")
title_size = st.slider("Ukuran Font Judul", min_value=20, max_value=100, value=40)
body_size = st.slider("Ukuran Font Subjudul", min_value=20, max_value=100, value=30)

# Pilihan template
st.subheader("Pilih Template Latar Belakang")
template_options = {
    "Template 1": "template1.jpeg",
    "Template 2": "template2.jpeg",
    "Template 3": "template3.jpeg",
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
        invitation = generate_invitation(
            template_path, names, date.strftime('%d %B %Y'), location,
            font_choice, title_color, body_color, title_size, body_size
        )

        # Tampilkan undangan
        st.image(invitation, caption="Undangan Pernikahan Anda", use_column_width=True)

        # Unduh undangan
        invitation_path = "undangan_pernikahan.png"
        invitation.save(invitation_path)
        with open(invitation_path, "rb") as file:
            st.download_button("Unduh Undangan", file, file_name="undangan_pernikahan.png", mime="image/png")
