import streamlit as st

# 1. पेज कॉन्फ़िगरेशन
st.set_page_config(page_title="राष्ट्रीय ई-लेखा एवं बही-खाता पोर्टल", layout="wide")

# 2. कस्टम CSS (एक बड़ा सिंगल डिब्बा और अंदर सीधी लाइनें + घूमता 'V' बैज)
st.markdown("""
<style>
    /* 3D घूमता V बैज */
    @keyframes spinV {
        0% { transform: rotateY(0deg); }
        50% { transform: rotateY(180deg); }
        100% { transform: rotateY(360deg); }
    }
    .v-badge {
        display: inline-block;
        width: 26px;
        height: 26px;
        line-height: 26px;
        text-align: center;
        background: linear-gradient(135deg, #0d47a1, #1976d2);
        color: white;
        font-weight: bold;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.25);
        animation: spinV 3s infinite linear;
        font-family: sans-serif;
    }
    
    /* सिंगल मुख्य बॉक्स जिसमें सभी लाइनें होंगी */
    .main-container-box {
        background-color: #ffffff;
        border: 1px solid #d1d5db;
        border-radius: 10px;
        padding: 15px 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }

    /* बटन को बिल्कुल सीधी टेक्स्ट लाइन की तरह दिखाना */
    div.stButton > button {
        width: 100%;
        text-align: left;
        background: none !important;
        border: none !important;
        border-bottom: 1px solid #e2e8f0 !important;
        border-radius: 0px !important;
        padding: 14px 5px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        color: #1e293b !important;
        box-shadow: none !important;
    }
    div.stButton > button:hover {
        color: #1d4ed8 !important;
        background-color: #f8fafc !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. सेशन स्टेट द्वारा वर्तमान पेज ट्रैक करना
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# ==========================================
# 🏠 1. मुख्य होमपेज (HOME SCREEN - सिंगल डिब्बा लेआउट)
# ==========================================
if st.session_state.current_page == "home":
    st.markdown("### 🏛️ राष्ट्रीय ई-लेखा एवं बही-खाता सत्यापन पोर्टल")
    st.caption("भारत सरकार / राज्य डिजिटल सेवा से प्रेरित - स्वचालित बही-खाता प्रणाली")

    # डिस्क्लेमर बॉक्स
    st.warning("""
    ⚠️ **आवश्यक सूचना एवं कानूनी अस्वीकरण (Disclaimer):**  
    यह प्रणाली केवल स्वचालित डिजिटल गणना एवं संदर्भ सहायता हेतु उपलब्ध कराई गई है। हिसाब-किताब में किसी भी प्रकार की भिन्नता होने पर प्रणाली/डेवलपर की कोई ज़िम्मेदारी नहीं होगी।
    """)

    st.markdown("---")

    # 📦 एक सिंगल बड़े बॉक्स के अंदर सभी लाइनें
    st.markdown('<div class="main-container-box">', unsafe_allow_html=True)
    
    # लाइन 1: पेट्रोल पंप
    col_text, col_v = st.columns([0.92, 0.08])
    with col_text:
        if st.button("⛽ पेट्रोल पंप दैनिक लेखा-जोखा एवं नोज़ल रीडिंग मिलान", key="btn_petrol"):
            st.session_state.current_page = "petrol_pump"
            st.rerun()
    with col_v:
        st.markdown('<div style="padding-top: 10px;"><span class="v-badge">V</span></div>', unsafe_allow_html=True)

    # लाइन 2: किराना स्टोर
    col_text, col_v = st.columns([0.92, 0.08])
    with col_text:
        if st.button("🛒 किराना एवं जनरल स्टोर दैनिक बिक्री व बही-खाता", key="btn_kirana"):
            st.session_state.current_page = "kirana"
            st.rerun()
    with col_v:
        st.markdown('<div style="padding-top: 10px;"><span class="v-badge">V</span></div>', unsafe_allow_html=True)

    # लाइन 3: सब्जी व फल मंडी
    col_text, col_v = st.columns([0.92, 0.08])
    with col_text:
        if st.button("🥦 सब्जी एवं फल मंडी दैनिक व्यापार रजिस्टर", key="btn_sabji"):
            st.session_state.current_page = "sabji"
            st.rerun()
    with col_v:
        st.markdown('<div style="padding-top: 10px;"><span class="v-badge">V</span></div>', unsafe_allow_html=True)

    # लाइन 4: हार्डवेयर व स्टील दुकान
    col_text, col_v = st.columns([0.92, 0.08])
    with col_text:
        if st.button("🔩 हार्डवेयर, लोहा एवं स्टील ट्रेडर्स लेजर", key="btn_hardware"):
            st.session_state.current_page = "hardware"
            st.rerun()
    with col_v:
        st.markdown('<div style="padding-top: 10px;"><span class="v-badge">V</span></div>', unsafe_allow_html=True)

    # लाइन 5: मोबाइल व सॉफ्टवेयर दुकान
    col_text, col_v = st.columns([0.92, 0.08])
    with col_text:
        if st.button("📱 मोबाइल, इलेक्ट्रॉनिक्स एवं सॉफ्टवेयर शॉप खाता", key="btn_mobile"):
            st.session_state.current_page = "mobile"
            st.rerun()
    with col_v:
        st.markdown('<div style="padding-top: 10px;"><span class="v-badge">V</span></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# ⛽ 2. पेट्रोल पंप विशेष साइड/पेज (PETROL PUMP PAGE)
# ==========================================
elif st.session_state.current_page == "petrol_pump":
    # ⬅️ बैक बटन
    if st.button("⬅️ मुख्य पृष्ठ (Home) पर वापस जाएं"):
        st.session_state.current_page = "home"
        st.rerun()

    st.markdown("---")
    st.header("⛽ पेट्रोल पंप दैनिक लेखा-जोखा एवं नोज़ल रीडिंग")

    # 1. रीडिंग व दर इनपुट
    st.subheader("📊 1. नोज़ल रीडिंग एवं दर (Rate) दर्ज करें")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        morning_read = st.number_input("सुबह की रीडिंग (Morning Reading):", min_value=0.0, step=0.1)
    with col2:
        evening_read = st.number_input("शाम की रीडिंग (Evening Reading):", min_value=0.0, step=0.1)
    with col3:
        rate = st.number_input("ईंधन की दर / प्रति लीटर रेट (₹):", min_value=0.0, step=0.01)
        
    # ऑटो-कैलकुलेशन (शाम रीडिंग - सुबह रीडिंग = बिका लीटर)
    if evening_read >= morning_read and morning_read > 0:
        total_liters = evening_read - morning_read
        total_sale_amount = total_liters * rate
        st.success(f"✅ **कुल बिका हुआ ईंधन:** {total_liters:.2f} लीटर")
        st.info(f"💰 **कुल बिक्री राशि:** ₹ {total_sale_amount:,.2f}")
    elif evening_read < morning_read and evening_read > 0:
        st.error("⚠️ शाम की रीडिंग सुबह की रीडिंग से कम नहीं हो सकती!")

    # 2. दैनिक जमा एवं खर्च
    st.subheader("📝 2. दैनिक जमा एवं खर्च विवरण")
    col_in, col_out = st.columns(2)
    with col_in:
        st.text_area("प्राप्त राशि (जमा / कैश इन):", placeholder="उदा: ₹5000 - ऑनलाइन, ₹10000 - कैश जमा")
    with col_out:
        st.text_area("दिया गया पैसा (खर्च / उधार):", placeholder="उदा: ₹2000 - टैंकर चालान, ₹500 - स्टाफ खर्च")

    # 3. तीन अलग-अलग फोटो अपलोडर
    st.subheader("📷 3. पर्ची एवं डायरी की डिजिटल कॉपी अपलोड करें")
    up1, up2, up3 = st.columns(3)
    with up1:
        st.file_uploader("1. सुबह की मशीन रीडिंग पर्ची", type=["jpg", "jpeg", "png"], key="m_pic")
    with up2:
        st.file_uploader("2. शाम की नोज़ल रीडिंग पर्ची", type=["jpg", "jpeg", "png"], key="e_pic")
    with up3:
        st.file_uploader("3. दैनिक डायरी / कॉपी का फोटो", type=["jpg", "jpeg", "png"], key="d_pic")

    st.button("🔍 AI द्वारा पर्ची स्कैन व ऑटो-रीडिंग करें")


# ==========================================
# 🛒 3. अन्य व्यवसायों के लिए साइड्स
# ==========================================
elif st.session_state.current_page == "kirana":
    if st.button("⬅️ मुख्य पृष्ठ (Home) पर वापस जाएं"):
        st.session_state.current_page = "home"
        st.rerun()
    st.header("🛒 किराना एवं जनरल स्टोर दैनिक बही-खाता")

elif st.session_state.current_page == "sabji":
    if st.button("⬅️ मुख्य पृष्ठ (Home) पर वापस जाएं"):
        st.session_state.current_page = "home"
        st.rerun()
    st.header("🥦 सब्जी एवं फल मंडी दैनिक व्यापार रजिस्टर")

elif st.session_state.current_page == "hardware":
    if st.button("⬅️ मुख्य पृष्ठ (Home) पर वापस जाएं"):
        st.session_state.current_page = "home"
        st.rerun()
    st.header("🔩 हार्डवेयर, लोहा एवं स्टील ट्रेडर्स लेजर")

elif st.session_state.current_page == "mobile":
    if st.button("⬅️ मुख्य पृष्ठ (Home) पर वापस जाएं"):
        st.session_state.current_page = "home"
        st.rerun()
    st.header("📱 मोबाइल, इलेक्ट्रॉनिक्स एवं सॉफ्टवेयर शॉप खाता")
    
