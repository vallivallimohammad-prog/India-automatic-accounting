import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. पेज सेटअप (आधिकारिक पोर्टल टाइटल)
st.set_page_config(
    page_title="स्वचालित ईंधन बही-खाता एवं डिजिटल मिलान पोर्टल", 
    page_icon="🏛️", 
    layout="centered"
)

# 2. कस्टम CSS (Official Government Portal Look & Red Disclaimer Box)
custom_css = """
    <style>
    /* Streamlit डिफॉल्ट एलिमेंट छुपाना */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #F8FAFC; }
    
    /* 1. शीर्ष आधिकारिक बार (Govt Top Bar) */
    .gov-top-bar {
        background-color: #0F172A;
        color: #E2E8F0;
        padding: 6px 15px;
        font-size: 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid #D97706;
        margin-top: -50px;
        margin-bottom: 15px;
    }
    .gov-title {
        font-weight: 600;
        letter-spacing: 0.5px;
    }

    /* 2. मुख्य आधिकारिक हेडर कार्ड */
    .official-header {
        background: #1E293B;
        color: #FFFFFF;
        padding: 20px;
        border-radius: 6px;
        border-top: 4px solid #1E40AF;
        text-align: center;
        margin-bottom: 18px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .main-portal-title {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 4px;
        color: #F8FAFC;
    }
    .sub-portal-title {
        font-size: 13px;
        color: #94A3B8;
    }

    /* 3. लाल रंग का चेतावनी / अस्वीकरण (Notice Box) */
    .red-notice-box {
        background-color: #FEF2F2;
        color: #991B1B;
        padding: 12px 16px;
        border-radius: 6px;
        border: 1px solid #FCA5A5;
        border-left: 6px solid #DC2626;
        font-size: 13.5px;
        font-weight: 500;
        margin-bottom: 20px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    .notice-title {
        font-weight: 700;
        color: #7F1D1D;
        margin-bottom: 3px;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    /* 4. रिजल्ट बॉक्स डिज़ाइन */
    .result-box {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #CBD5E1;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        margin-top: 20px;
    }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# टॉप गवर्नमेंट बार
st.markdown("""
    <div class='gov-top-bar'>
        <span class='gov-title'>🏛️ राष्ट्रीय ई-लेखा एवं बही-खाता सत्यापन पोर्टल</span>
        <span>भारत सरकार / राज्य डिजिटल सेवा</span>
    </div>
""", unsafe_allow_html=True)

# मुख्य आधिकारिक हेडर
st.markdown("""
    <div class='official-header'>
        <div class='main-portal-title'>स्वचालित ईंधन बही-खाता एवं डिजिटल मिलान प्रणाली</div>
        <div class='sub-portal-title'>Automated Fuel Station Reconciliation & Ledger Audit System</div>
    </div>
""", unsafe_allow_html=True)

# लाल रंग में अनिवार्य चेतावनी नोटिस
st.markdown("""
    <div class='red-notice-box'>
        <div class='notice-title'>⚠️ आवश्यक सूचना एवं कानूनी अस्वीकरण (Disclaimer):</div>
        यह प्रणाली केवल स्वचालित डिजिटल गणना एवं संदर्भ सहायता हेतु उपलब्ध कराई गई है। हिसाब-किताब में किसी भी प्रकार की भिन्नता, त्रुटि या गड़बड़ी होने पर प्रणाली/डेवलपर की कोई ज़िम्मेदारी नहीं होगी। उपयोगकर्ता स्वयं अपने अंतिम मिलान एवं बही-खाते के लिए ज़िम्मेदार होंगे।
    </div>
""", unsafe_allow_html=True)

# Secrets से API Key प्राप्त करना
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ सिस्टम त्रुटि: पोर्टल प्रामाणिक कुंजी (API Key) कॉन्फ़िगर नहीं है। कृपया Secrets की जांच करें।")
    st.stop()

genai.configure(api_key=api_key)

# फाइल अपलोडर (शासकीय शैली)
uploaded_files = st.file_uploader(
    "📁 पर्चियों / मशीन रीडिंग / लेजर दस्तावज़ों की डिजिटल प्रति (फोटो) अपलोड करें:", 
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if uploaded_files:
    images = [Image.open(file) for file in uploaded_files]
    total_images = len(images)
    
    st.write("---")
    
    # फोटो गैलरी एवं नेविगेशन सिस्टम (1-1 फोटो देखने हेतु)
    if "img_index" not in st.session_state:
        st.session_state.img_index = 0

    if st.session_state.img_index >= total_images:
        st.session_state.img_index = 0

    col_nav1, col_nav2, col_nav3 = st.columns([1, 2, 1])
    
    with col_nav1:
        if st.button("⬅️ पिछला पर्चा", disabled=(st.session_state.img_index == 0)):
            st.session_state.img_index -= 1
            st.rerun()
            
    with col_nav3:
        if st.button("अगला पर्चा ➡️", disabled=(st.session_state.img_index == total_images - 1)):
            st.session_state.img_index += 1
            st.rerun()

    with col_nav2:
        selected_page = st.selectbox(
            "सीधे पर्चे पर जाएँ:",
            options=list(range(1, total_images + 1)),
            index=st.session_state.img_index,
            format_func=lambda x: f"पर्चा संख्या {x} / {total_images}"
        )
        if selected_page - 1 != st.session_state.img_index:
            st.session_state.img_index = selected_page - 1
            st.rerun()

    # वर्तमान चुनी हुई फोटो का प्रदर्शन
    current_img = images[st.session_state.img_index]
    st.image(
        current_img, 
        caption=f"📄 दस्तावेज़ प्रति संख्या {st.session_state.img_index + 1} (कुल {total_images} में से)", 
        use_column_width=True
    )
    
    st.write("---")

    # प्रसंस्करण और मिलान बटन
    if st.button("📊 सभी दस्तावेज़ों का आधिकारिक मिलान एवं हिसाब निकालें", type="primary", use_container_width=True):
        with st.spinner("सभी पर्चियों एवं बही-खाता प्रविष्टियों का सत्यापन किया जा रहा है..."):
            try:
                # अद्यतन मॉडल
                model = genai.GenerativeModel("gemini-3.8-flash")
                
                system_prompt = """
                आप एक अत्यंत चतुर, सटीक और वरिष्ठ ऑटोमैटिक अकाउंटेंट हैं। आपको 1 या 1 से अधिक पर्चियों/दस्तावेजों की फोटो दी गई हैं। सभी फोटो को आपस में मिलाकर निम्नलिखित नियमानुसार अंतिम हिसाब तैयार करें:

                1. **पंप की सुबह/शाम मशीन पर्चियों (Shift Slips) की स्थिति में:**
                   - सभी पर्चों से शुरुआती रीडिंग (Opening Reading) और अंतिम रीडिंग (Closing Reading) पहचानें।
                   - कुल लीटर बिक्री = (अंतिम रीडिंग - शुरुआती रीडिंग)।
                   - प्रति लीटर दर (Rate) निकालकर कुल सेल राशि (Total Sales Amount) की गणना करें।

                2. **उधार/जमा/लैन-देन/खर्च पर्चियों की स्थिति में:**
                   - जो पैसे आए/जमा हुए (+ चिह्नों या विवरण अनुसार) उन्हें 'जमा/प्राप्ति' में रखें।
                   - जो पैसे उधार दिए/खर्चे हुए (- चिह्नों या विवरण अनुसार) उन्हें 'उधार/खर्च' में रखें।

                3. **प्लस (+) और माइनस (-) के निशानों का नियम:**
                   - पर्चियों में दर्ज संख्याओं पर लगे + और - के निशानों को ध्यानपूर्वक देखें और उसी अनुसार गणितीय गणना करें।

                4. **यदि पर्ची में साधारण हाथ से लिखे नंबर हैं:**
                   - पर्चे में दर्ज सभी नंबरों का बिल्कुल सटीक कुल जोड़ (Total) निकालें।

                5. **संपूर्ण मिलान (Grand Final Reconciliation):**
                   यदि multiple पर्चियां हैं, तो सभी का आपस में मिलान करके एक स्पष्ट रिपोर्ट बनाएं:
                   - **कुल बिक्री (Total Sales):** मशीन पर्चियों के अनुसार
                   - **कुल प्राप्त नकद/ऑनलाइन जमा:**
                   - **कुल उधार/बाकी लेन-देन:**
                   - **अंतिम बैलेंस / शुद्ध हिसाब (Net Closing Balance):**

                6. **आउटपुट का नियम:**
                   - उत्तर केवल शुद्ध हिंदी में स्पष्ट तालिकाओं (Tables) और बिंदुओं में दें।
                   - एआई, मॉडल, टेक्नोलॉजी, जेमिनी या स्कैनर जैसे शब्दों का प्रयोग बिल्कुल न करें।
                """
                
                prompt_content = [system_prompt] + images
                response = model.generate_content(prompt_content)
                
                st.markdown("<div class='result-box'>", unsafe_allow_html=True)
                st.markdown("### 📋 संपूर्ण बही-खाता एवं अंकेक्षण (Audit) रिपोर्ट")
                st.markdown(response.text)
                st.markdown("</div>", unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"⚠️ त्रुटि विवरण: {e}")
                
