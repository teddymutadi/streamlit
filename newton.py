import streamlit as st

# Judul Aplikasi
st.title("🌍 Aplikasi IPA - Hukum Newton II")
st.write("Mari kita hitung **Gaya (F = m × a)** dengan mudah menggunakan Streamlit.")

# Input dari pengguna
massa = st.number_input("Masukkan Massa (kg)", min_value=0.0, step=0.5)
percepatan = st.number_input("Masukkan Percepatan (m/s²)", min_value=0.0, step=0.5)

# Tombol hitung
if st.button("Hitung Gaya"):
    if massa > 0 and percepatan > 0:
        gaya = massa * percepatan
        st.success(f"👉 Gaya yang dihasilkan adalah **{gaya} Newton (N)**")

        # Customisasi st.balloons() dengan pesan tambahan
        st.balloons()
        st.markdown(
            """
            <div style='text-align: center; font-size: 20px; color: green;'>
                🎉 Selamat! Perhitungan berhasil dilakukan 🎉
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("⚠️ Mohon masukkan nilai massa dan percepatan lebih dari 0.")

# Informasi tambahan
with st.expander("📘 Penjelasan IPA"):
    st.write("""
    - **Massa (m)** adalah jumlah materi dalam benda, satuannya kilogram (kg).  
    - **Percepatan (a)** adalah perubahan kecepatan tiap satuan waktu, satuannya m/s².  
    - **Gaya (F)** adalah hasil kali massa dan percepatan, satuannya Newton (N).  

    Rumus:  
    \[
    F = m * a
    \]
    """)
