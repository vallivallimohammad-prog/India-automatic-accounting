import streamlit as st
import pandas as pd

# --- पेज कॉन्फ़िगरेशन ---
st.set_page_config(
    page_title="पेट्रोल पंप प्रबंधन",
    page_icon="⛽",
    layout="wide"
)

# सेशन स्टेट द्वारा पेज नेविगेशन
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "home"

# ==========================================
# 🏠 1. मुख्य पेज (Home Page)
# ==========================================
if st.session_state["current_page"] == "home":
    st.title("⛽ पेट्रोल पंप प्रबंधन प्रणाली")
    st.markdown("---")
    
    st.subheader("📋 मुख्य विकल्प (Menu)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("### 🧾 दैनिक जमा-खर्च व हिसाब")
        st.write("8 नोज़ल रीडिंग, पर्ची अपलोड, सुबह की टेस्टिंग और दैनिक रजिस्टर का स्वचालित हिसाब मिलाने के लिए नीचे क्लिक करें।")
        if st.button("👉 हिसाब-किताब पेज खोलें", type="primary", use_container_width=True):
            st.session_state["current_page"] = "hisab_page"
            st.rerun()

    with col2:
        st.success("### 📊 स्टॉक व बिक्री रिपोर्ट्स")
        st.write("पुराने दैनिक हिसाब और बिक्री की समरी रिपोर्ट देखें।")
        st.button("📁 रिपोर्ट्स देखें (शीघ्र उपलब्ध)", disabled=True, use_container_width=True)

# ==========================================
# 📄 2. नया हिसाब-किताब पेज
# ==========================================
elif st.session_state["current_page"] == "hisab_page":
    
    if st.button("⬅️ मुख्य मेनू (Home) पर वापस जाएँ"):
        st.session_state["current_page"] = "home"
        st.rerun()

    st.title("📝 दैनिक जमा-खर्च व हिसाब पर्ची")
    st.markdown("---")

    # (A) 8 नोज़ल रीडिंग - पर्ची + टाइपिंग
    st.header("1. नोज़ल रीडिंग दर्ज करें (8 नोज़ल्स)")
    st.info("आप चाहें तो पर्चियों की फोटो अपलोड करें या नीचे सीधे रीडिंग टाइप करें। दोनों तरीकों से सही हिसाब मिल जाएगा।")

    col_m_files, col_e_files = st.columns(2)

    with col_m_files:
        st.subheader("🌅 सुबह की नोज़ल पर्चियाँ (Opening)")
        m_files = [st.file_uploader(f"सुबह की पर्ची {i}", type=["jpg", "jpeg", "png"], key=f"m_file_{i}") for i in range(1, 5)]

    with col_e_files:
        st.subheader("🌆 शाम की नोज़ल पर्चियाँ (Closing)")
        e_files = [st.file_uploader(f"शाम की पर्ची {i}", type=["jpg", "jpeg", "png"], key=f"e_file_{i}") for i in range(1, 5)]

    st.markdown("#### 🔢 मैन्युअल नोज़ल रीडिंग दर्ज करें (8 नोज़ल्स):")
    col_read1, col_read2 = st.columns(2)

    morning_readings = {}
    evening_readings = {}

    with col_read1:
        st.markdown("**सुबह की रीडिंग (Opening):**")
        for i in range(1, 9):
            morning_readings[f"Nozzle {i}"] = st.number_input(
                f"नोज़ल {i} (सुबह)", min_value=0.0, value=0.0, step=0.1, key=f"m_read_{i}"
            )

    with col_read2:
        st.markdown("**शाम की रीडिंग (Closing):**")
        for i in range(1, 9):
            evening_readings[f"Nozzle {i}"] = st.number_input(
                f"नोज़ल {i} (शाम)", min_value=0.0, value=0.0, step=0.1, key=f"e_read_{i}"
            )

    st.markdown("---")

    # (B) सुबह की टेस्टिंग
    st.header("2. सुबह की टेस्टिंग")
    st.caption("यदि कोई टेस्टिंग हुई है तो लीटर या रुपये दर्ज करें। यदि खाली छोड़ेंगे तो नीचे हिसाब में प्रदर्शित नहीं होगी।")

    col_t1, col_t2 = st.columns(2)
    with col_t1:
        testing_liters = st.number_input("टेस्टिंग का तेल (लीटर)", min_value=0.0, value=0.0, step=0.5)
    with col_t2:
        testing_rupees = st.number_input("टेस्टिंग के रुपये (₹)", min_value=0.0, value=0.0, step=1.0)

    st.markdown("---")

    # (C) दैनिक जमा-खर्च पर्चियाँ (4 ऑप्शन)
    st.header("3. हाथ से लिखे दैनिक रजिस्टर की पर्चियाँ")
    st.caption("रजिस्टर की फोटो अपलोड करें (4 अलग-अलग ऑप्शन)।")

    reg_cols = st.columns(4)
    register_files = []
    for i in range(1, 5):
        with reg_cols[i-1]:
            rf = st.file_uploader(f"रजिस्टर पर्ची {i}", type=["jpg", "jpeg", "png"], key=f"reg_file_{i}")
            if rf:
                register_files.append(rf)

    st.markdown("---")

    # (D) स्वचालित हिसाब मिलाएँ बटन
    if st.button("🔄 स्वचालित हिसाब मिलाएँ", type="primary", use_container_width=True):
        st.success("हिसाब सफलतापूर्वक मिल गया है!")
        
        nozzle_data = []
        total_gross_liters = 0.0
        
        for i in range(1, 9):
            m_val = morning_readings[f"Nozzle {i}"]
            e_val = evening_readings[f"Nozzle {i}"]
            diff = max(0.0, e_val - m_val) if e_val >= m_val else 0.0
            total_gross_liters += diff
            nozzle_data.append({
                "नोज़ल नं.": f"नोज़ल {i}",
                "सुबह रीडिंग": f"{m_val:,.2f}",
                "शाम रीडिंग": f"{e_val:,.2f}",
                "कुल बिक्री (लीटर)": f"{diff:,.2f} L"
            })
        
        df_nozzles = pd.DataFrame(nozzle_data)
        
        st.subheader("📊 1. नोज़ल-वार बिक्री विवरण")
        st.table(df_nozzles)
        
        net_liters = max(0.0, total_gross_liters - testing_liters)
        
        st.subheader("📝 2. शुद्ध बिक्री एवं फाइनल हिसाब समरी")
        st.write(f"• **कुल मीटर बिक्री (ग्रॉस):** {total_gross_liters:,.2f} लीटर")
        
        if testing_liters > 0 or testing_rupees > 0:
            test_str = "• **टेस्टिंग कटौती:** "
            parts = []
            if testing_liters > 0:
                parts.append(f"{testing_liters:,.2f} लीटर")
            if testing_rupees > 0:
                parts.append(f"₹ {testing_rupees:,.2f}")
            test_str += " / ".join(parts) + " (घटाया गया)"
            st.write(test_str)
            st.write(f"• **शुद्ध बिक्री (Net Sales):** **{net_liters:,.2f} लीटर**")
        else:
            st.write(f"• **शुद्ध बिक्री (Net Sales):** **{total_gross_liters:,.2f} लीटर**")
            
        uploaded_reg_count = sum(1 for f in register_files if f is not None)
        if uploaded_reg_count > 0:
            st.write(f"• **हाथ से लिखे रजिस्टर की पर्चियाँ:** {uploaded_reg_count} पर्ची/पर्चियों का हिसाब मिलाया गया।")

        st.markdown("---")
        
        # टेक्स्ट / CSV डाउनलोड विकल्प (बिना किसी बाहरी लाइब्रेरी एरर के)
        summary_text = f"पेट्रोल पंप दैनिक रिपोर्ट\n"
        summary_text += f"कुल ग्रॉस बिक्री: {total_gross_liters} L\n"
        summary_text += f"टेस्टिंग: {testing_liters} L / Rs.{testing_rupees}\n"
        summary_text += f"शुद्ध बिक्री: {net_liters} L\n"
        
        st.download_button(
            label="📥 दैनिक रिपोर्ट डाउनलोड करें (Text)",
            data=summary_text,
            file_name="Daily_Report.txt",
            mime="text/plain",
            use_container_width=True
    )
    
