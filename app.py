import streamlit as st

# 1. पेज कॉन्फ़िगरेशन
st.set_page_config(page_title="राष्ट्रीय ई-लेखा एवं बही-खाता पोर्टल", layout="wide")

# 2. कस्टम CSS (घूमता हुआ 'V' बैज और बॉक्स डिज़ाइन)
st.markdown("""
<style>
    /* V Badge Rotating Animation */
    @keyframes spinV {
        0% { transform: rotateY(0deg); }
        50% { transform: rotateY(180deg); }
        100% { transform: rotateY(360deg); }
    }
    .v-badge {
        display: inline-block;
        width: 28px;
        height: 28px;
        line-height: 28px;
        text-align: center;
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
        font-weight: bold;
        border-radius: 6px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.3);
        animation: spinV 3s infinite linear;
        font-family: sans-serif;
    }
    
    /* Category Card Style */
    .biz-card {
        background-color: #ffffff;
        border: 1px solid #d1d5db;
        border-left: 5px solid #1e3c72;
        padding: 12px 18px;
        margin-bottom: 10px;
        border-radius: 8px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
</style>
""", unsafe_allow_html=True)

# 3. टॉप हेडर
st.markdown("### 🏛️ राष्ट्रीय ई-लेखा एवं बही-खाता सत्यापन पोर्टल")
st.caption("भारत सरकार / राज्य डिजिटल सेवा से प्रेरित - स्वचालित बही-खाता एवं डिजिटल मिलान प्रणाली")

# 4. डिस्क्लेमर बॉक्स
st.warning("""
⚠️ **आवश्यक सूचना एवं कानूनी अस्वीकरण (Disclaimer):**  
यह प्रणाली केवल स्वचालित डिजिटल गणना एवं संदर्भ सहायता हेतु उपलब्ध कराई गई है। हिसाब-किताब में किसी भी प्रकार की भिन्नता होने पर प्रणाली जिम्मेदार नहीं होगी।
""")

st.markdown("---")

# 5. व्यवसाय चयन अनुभाग (अनाउंसमेंट बॉक्स स्टाइल)
st.subheader("📋 अपना व्यवसाय चुनें (दैनिक हिसाब-किताब हेतु)")

# सेलेक्ट बॉक्स के विकल्प
biz_options = [
    "⛽ पेट्रोल पंप दैनिक लेखा-जोखा एवं रीडिंग मिलान",
    "🛒 किराना एवं जनरल स्टोर दैनिक बिक्री व बही-खाता",
    "🥦 सब्जी एवं फल मंडी दैनिक व्यापार रजिस्टर",
    "🔩 हार्डवेयर, लोहा एवं स्टील ट्रेडर्स लेजर",
    "📱 मोबाइल, इलेक्ट्रॉनिक्स एवं सॉफ्टवेयर शॉप खाता"
]

selected_biz = st.selectbox("नीचे दी गई सूची में से अपना व्यापार चुनें:", biz_options)

# घूमते हुए 'V' मार्क के साथ सूची दर्शाना
for biz in biz_options:
    st.markdown(f"""
    <div class="biz-card">
        <span style="font-size: 16px; font-weight: 600; color: #1f2937;">{biz}</span>
        <span class="v-badge">V</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 6. पेट्रोल पंप मॉड्यूल (जब पेट्रोल पंप चुना गया हो)
if "पेट्रोल पंप" in selected_biz:
    st.header("⛽ पेट्रोल पंप दैनिक हिसाब-किताब एवं नोज़ल रीडिंग")
    
    # 6.1 रीडिंग व रेट इनपुट
    st.subheader("📊 1. नोज़ल रीडिंग एवं दर (Rate) दर्ज करें")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        morning_read = st.number_input("सुबह की रीडिंग (Morning Reading):", min_value=0.0, step=0.1)
    with col2:
        evening_read = st.number_input("शाम की रीडिंग (Evening Reading):", min_value=0.0, step=0.1)
    with col3:
        rate = st.number_input("ईंधन की दर / प्रति लीटर रेट (₹):", min_value=0.0, step=0.01)
        
    # रीडिंग कैलकुलेशन
    if evening_read >= morning_read and morning_read > 0:
        total_liters = evening_read - morning_read
        total_sale_amount = total_liters * rate
        
        st.success(f"✅ **कुल बिका हुआ ईंधन:** {total_liters:.2f} लीटर")
        st.info(f"💰 **कुल बिक्री राशि:** ₹ {total_sale_amount:,.2f}")
    elif evening_read < morning_read and evening_read > 0:
        st.error("⚠️ शाम की रीडिंग सुबह की रीडिंग से कम नहीं हो सकती!")

    # 6.2 दैनिक नकदी व उधारी खाता
    st.subheader("📝 2. दैनिक जमा एवं खर्च विवरण")
    col_in, col_out = st.columns(2)
    with col_in:
        st.text_area("प्राप्त राशि (जमा / कैश इन):", placeholder="उदा: ₹5000 - पेटीएम, ₹10000 - कैश जमा")
    with col_out:
        st.text_area("दिया गया पैसा (खर्च / उधार):", placeholder="उदा: ₹2000 - टैंकर चालान, ₹500 - स्टाफ चाय")

    # 6.3 3 फोटो अपलोडर (सुबह की पर्ची, शाम की पर्ची, कॉपी की फोटो)
    st.subheader("📷 3. पर्ची एवं डायरी की डिजिटल कॉपी अपलोड करें")
    
    up_col1, up_col2, up_col3 = st.columns(3)
    
    with up_col1:
        st.file_uploader("1. सुबह की मशीन रीडिंग पर्ची", type=["jpg", "jpeg", "png"], key="morning_pic")
        
    with up_col2:
        st.file_uploader("2. शाम की नोज़ल रीडिंग पर्ची", type=["jpg", "jpeg", "png"], key="evening_pic")
        
    with up_col3:
        st.file_uploader("3. दैनिक डायरी / कॉपी का फोटो", type=["jpg", "jpeg", "png"], key="diary_pic")

    st.button("🔄 AI द्वारा पर्ची से ऑटो-रीडिंग स्कैन करें")

else:
    st.info(f"👉 **{selected_biz}** का मॉड्यूल चुनने के लिए धन्यवाद! इसका फॉर्म नीचे ओपन कर दिया गया है।")
    
