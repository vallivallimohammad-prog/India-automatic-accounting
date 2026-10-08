import streamlit as st
import google.generativeai as genai
from PIL import Image

# Page setup
st.set_page_config(page_title="स्वचालित खाता एवं पंप मिलान प्रणाली", page_icon="📝", layout="centered")

# Hide Streamlit header/footer for clean stealth UI
hide_ui_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #F8FAFC; }
    .title-banner {
        background-color: #1E293B;
        color: white;
        padding: 16px;
        border-radius: 12px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .result-box {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-top: 15px;
    }
    </style>
"""
st.markdown(hide_ui_style, unsafe_allow_html=True)

st.markdown("<div class='title-banner'>📋 ऑटोमैटिक खाता एवं संपूर्ण बही-खाता सिस्टम</div>", unsafe_allow_html=True)

# Retrieve Key from Streamlit Secrets
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ सिस्टम त्रुटि: अकाउंटिंग की कुंजी सेट नहीं है। कृपया Secrets की जांच करें।")
    st.stop()

genai.configure(api_key=api_key)

# Multi-file uploader (एक साथ 1, 2 या 3 पर्चियां/पर्चे डालने की सुविधा)
uploaded_files = st.file_uploader(
    "📸 पर्चियों/बिल/रीडिंग मशीन की फोटो चुनें (एक साथ कई फोटो अपलोड कर सकते हैं)", 
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if uploaded_files:
    images = []
    cols = st.columns(len(uploaded_files))
    for idx, uploaded_file in enumerate(uploaded_files):
        img = Image.open(uploaded_file)
        images.append(img)
        with cols[idx]:
            st.image(img, caption=f"पर्चा {idx+1}", use_column_width=True)
    
    with st.spinner("सभी पर्चियों का गहन विश्लेषण और अंतिम मिलान किया जा रहा है..."):
        try:
            # सही मॉडल नाम
            model = genai.GenerativeModel("gemini-1.5-flash")
            
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

            4. **संपूर्ण मिलान (Grand Final Reconciliation):**
               यदि multiple पर्चियां हैं, तो सभी का आपस में मिलान करके एक स्पष्ट रिपोर्ट बनाएं:
               - **कुल बिक्री (Total Sales):** मशीन पर्चियों के अनुसार
               - **कुल प्राप्त नकद/ऑनलाइन जमा:**
               - **कुल उधार/बाकी लेन-देन:**
               - **अंतिम बैलेंस / शुद्ध हिसाब (Net Closing Balance):**

            5. **आउटपुट का नियम:**
               - उत्तर केवल शुद्ध हिंदी में स्पष्ट तालिकाओं (Tables) और बिंदुओं में दें।
               - एआई, मॉडल, टेक्नोलॉजी, जेमिनी या स्कैनर जैसे शब्दों का प्रयोग बिल्कुल न करें।
            """
            
            prompt_content = [system_prompt] + images
            response = model.generate_content(prompt_content)
            
            st.markdown("<div class='result-box'>", unsafe_allow_html=True)
            st.markdown("### 📊 संपूर्ण हिसाब-किताब एवं अंतिम मिलान रिपोर्ट")
            st.markdown(response.text)
            st.markdown("</div>", unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"⚠️ त्रुटि विवरण: {e}")
            
