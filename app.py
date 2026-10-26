import streamlit as st

from PIL import Image

st.set_page_config(page_title="AI Lab PPE Detection System")

st.title("AI Lab PPE Detection System")

st.subheader("ระบบตรวจสอบอุปกรณ์ป้องกันในห้องแล็บ")

st.write("อัปโหลดภาพเพื่อตรวจสอบอุปกรณ์ PPE")

uploaded_file = st.file_uploader(

    "เลือกรูปภาพ",

    type=["jpg", "jpeg", "png"]

)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="ภาพที่อัปโหลด")

    st.info(

        "อัปโหลดภาพสำเร็จ "

        "ขณะนี้ยังไม่ได้เชื่อมต่อโมเดล AI ตรวจจับจริง"

    )

st.write("รายการอุปกรณ์ที่ต้องการตรวจสอบ")

st.write("1. เสื้อกาวน์ (Lab Coat)")

st.write("2. แว่นตานิรภัย (Safety Goggles)")

st.write("3. หน้ากาก (Face Mask)")

st.write("4. ถุงมือ (Gloves)")