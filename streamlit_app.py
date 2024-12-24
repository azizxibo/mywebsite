import streamlit as st

st.title("Aplikasi Undangan Pernikahan Online")
with st.form("undangan_form"):
    nama = st.text_input("Nama Pengantin")
    tanggal = st.date_input("Tanggal Pernikahan")
    lokasi = st.text_input("Lokasi Pernikahan")
    submit_button = st.form_submit_button("Buat Undangan")

if submit_button:
    st.write(f"**Undangan Pernikahan**")
    st.write(f"Nama: {nama}")
    st.write(f"Tanggal: {tanggal}")
    st.write(f"Lokasi: {lokasi}")
