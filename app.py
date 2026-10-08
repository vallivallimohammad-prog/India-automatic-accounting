import streamlit as st
import google.generativeai as genai
from PIL import Image

# Page setup
st.set_page_config(page_title="स्वचालित खाता प्रणाली", page_icon="📝", layout="centered")

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

st.markdown("<div class='title-banner'>📋 ऑटोमैटिक खाता एवं बही-खाता सिस्टम</div>", unsafe_allow_html=True)

# Retrieve Key from Streamlit Secrets
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ सिस्टम त्रुटि: अकाउंटिंग की कुंजी सेट नहीं है। कृपया Secrets की जांच करें।")
    st.stop()

genai.configure(api_key=api_key)

uploaded_file = st.file_uploader("📸 पर्ची, बिल या रीडिंग के पन्ने की फोटो चुनें", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="अपलोड किया गया पन्ना", use_column_width=True)
    
    with st.spinner("प्रोसेसिंग जारी है... हिसाब निकाला जा रहा है..."):
        try:
            # Using stable model for accurate OCR and arithmetic
            model = genai.GenerativeModel("gemini-1.5-flash")
            
            system_prompt = """
            आप एक अत्यंत सटीक और एडवांस ऑटोमैटिक अकाउंटेंट हैं। इस फोटो को गहराई से विश्लेषित करें और निम्नलिखित नियमों के अनुसार सीधे परिणाम तैयार करें:

            1. **प्रकार की पहचान (Category Identification):**
               - सबसे पहले पहचानें कि यह किस प्रकार का हिसाब है (जैसे: फ्यूल/पंप रीडिंग, किराना/दुकान बिल, निर्माण सामग्री, या केवल सामान्य संख्याओं का जोड़)।

            2. **पंप/फ्यूल रीडिंग होने की स्थिति में:**
               - प्रारंभिक रीडिंग (Start Reading) और अंतिम रीडिंग (End Reading) पहचानें।
               - कुल बिकी मात्रा (Total Liters) = अंतिम रीडिंग - प्रारंभिक रीडिंग।
               - यदि दर/रेट (Rate per Liter) दिया गया है, तो: कुल राशि = कुल लीटर × रेट।
               - स्पष्ट और सुंदर टेबल में यह पूरा हिसाब दिखाएं।

            3. **दुकान/सामान का बिल होने की स्थिति में:**
               - प्रत्येक सामान का नाम, मात्रा (Quantity), दर (Rate), और कुल कीमत की टेबल बनाएं।
               - नीचे स्पष्ट अक्षरों में 'कुल योग (Total Amount)' लिखें।

            4. **यदि केवल नंबर/संख्याएं लिखी हैं (कोई नाम या विवरण नहीं है):**
               - पर्चे में लिखे सभी नंबरों/संख्याओं को क्रमानुसार सूचीबद्ध (List) करें।
               - उन सभी संख्याओं का सही और बिल्कुल सटीक कुल जोड़ (Total) निकालें।

            5. **आउटपुट का रूप (Formatting):**
               - आउटपुट पूरी तरह केवल शुद्ध हिंदी में दें।
               - एआई, मॉडल, स्कैनर, जेमिनी या किसी तकनीक का जिक्र बिल्कुल न करें।
               - सीधे अंतिम निष्कर्ष, विवरण और हिसाब की तालिका प्रस्तुत करें।
            """
            
            response = model.generate_content([system_prompt, image])
            
            st.markdown("<div class='result-box'>", unsafe_allow_html=True)
            st.markdown("### 📊 तैयार हिसाब-किताब रिपोर्ट")
            st.markdown(response.text)
            st.markdown("</div>", unsafe_allow_html=True)
            
        except Exception as e:
            st.error("⚠️ पर्चा सही से पढ़ा नहीं जा सका। कृपया स्पष्ट और सीधी फोटो अपलोड करें।")
