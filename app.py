import streamlit as st
import streamlit.components.v1 as components

# 1. ऊपर की आधिकारिक सरकारी स्टाइल पट्टी (Header Bar)
st.markdown("""
<style>
    .gov-header {
        background-color: #0b1f3a;
        color: white;
        padding: 10px 15px;
        border-radius: 4px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 3px solid #ff9933;
        margin-bottom: 15px;
    }
    .gov-header-title {
        font-size: 14px;
        font-weight: bold;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .gov-header-sub {
        font-size: 12px;
        text-align: right;
        opacity: 0.9;
    }
    
    /* 2. मुख्य शीर्षक बैनर (Main Banner Box) */
    .banner-box {
        background-color: #1a2b40;
        color: white;
        text-align: center;
        padding: 20px 15px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    .banner-title {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 8px;
    }
    .banner-subtitle {
        font-size: 13px;
        color: #b0c4de;
    }

    /* 3. आवश्यक सूचना एवं चेतावनी नोट बॉक्स (Disclaimer Box) */
    .disclaimer-box {
        background-color: #fff5f5;
        border-left: 5px solid #d9534f;
        border-top: 1px solid #f5c6cb;
        border-right: 1px solid #f5c6cb;
        border-bottom: 1px solid #f5c6cb;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 20px;
    }
    .disclaimer-title {
        color: #a94442;
        font-weight: bold;
        font-size: 15px;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    .disclaimer-text {
        color: #721c24;
        font-size: 13px;
        line-height: 1.5;
    }
</style>

<!-- सरकारी हेडर पट्टी -->
<div class="gov-header">
    <div class="gov-header-title">
        🏛️ राष्ट्रीय ई-लेखा एवं बही-खाता सत्यापन पोर्टल
    </div>
    <div class="gov-header-sub">
        भारत सरकार / राज्य डिजिटल सेवा
    </div>
</div>

<!-- मुख्य बैनर -->
<div class="banner-box">
    <div class="banner-title">स्वचालित ईंधन बही-खाता एवं डिजिटल मिलान प्रणाली</div>
    <div class="banner-subtitle">Automated Fuel Station Reconciliation & Ledger Audit System</div>
</div>

<!-- चेतावनी/अस्वीकरण नोट बॉक्स -->
<div class="disclaimer-box">
    <div class="disclaimer-title">
        ⚠️ आवश्यक सूचना एवं कानूनी अस्वीकरण (Disclaimer):
    </div>
    <div class="disclaimer-text">
        यह प्रणाली केवल स्वचालित डिजिटल गणना एवं संदर्भ सहायता हेतु उपलब्ध कराई गई है। हिसाब-किताब में किसी भी प्रकार की भिन्नता, त्रुटि या गड़बड़ी होने पर प्रणाली/डेवलपर की कोई ज़िम्मेदारी नहीं होगी। उपयोगकर्ता स्वयं अपने अंतिम मिलान एवं बही-खाते के लिए ज़िम्मेदार होंगे।
    </div>
</div>
""", unsafe_allow_html=True)

# 4. फ़ाइल अपलोडर बॉक्स (आपकी पुरानी डिज़ाइन के अनुसार)
st.write("📂 **पर्चियों / मशीन रीडिंग / लेजर दस्तावेज़ों की डिजिटल प्रति (फोटो) अपलोड करें:**")
uploaded_file = st.file_uploader("", type=["jpg", "png", "pdf"])

st.markdown("<br>", unsafe_allow_html=True)

# 5. इन सभी डिब्बों के ठीक नीचे नया स्क्रॉलिंग न्यूज़ अपडेट वाला बॉक्स (News Ticker Box)
news_box_html = """
<style>
    .news-container {
        border: 2px solid #800000;
        background-color: #fff8dc;
        width: 100%;
        padding: 5px;
        border-radius: 6px;
        font-family: Arial, sans-serif;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.15);
        box-sizing: border-box;
    }
    .news-header {
        background-color: #800000;
        color: white;
        text-align: center;
        font-weight: bold;
        font-size: 14px;
        padding: 6px;
        margin-bottom: 5px;
        letter-spacing: 1px;
    }
    .news-item {
        padding: 10px 8px;
        border-bottom: 1px dashed #b8860b;
        font-size: 13.5px;
        font-weight: bold;
        color: #000080;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .v-icon {
        background-color: #0d6efd;
        color: white;
        font-weight: bold;
        font-size: 11px;
        padding: 2px 7px;
        border-radius: 3px;
        margin-left: 10px;
        flex-shrink: 0;
    }
</style>

<div class="news-container">
    <div class="news-header">NEWS UPDATE</div>
    <marquee direction="up" scrollamount="2" onmouseover="this.stop();" onmouseout="this.start();" height="230px">
        
        <div class="news-item">
            <span>⛽ पेट्रोल पंप दैनिक लेखा-जोखा एवं नोज़ल रीडिंग मिलान</span>
            <span class="v-icon">V</span>
        </div>
        
        <div class="news-item">
            <span>🛒 किराना एवं जनरल स्टोर दैनिक बिक्री व बही-खाता</span>
            <span class="v-icon">V</span>
        </div>
        
        <div class="news-item">
            <span>🥦 सब्जी एवं फल मंडी दैनिक व्यापार रजिस्टर</span>
            <span class="v-icon">V</span>
        </div>
        
        <div class="news-item">
            <span>🔩 हार्डवेयर, लोहा एवं स्टील ट्रेडर्स लेजर</span>
            <span class="v-icon">V</span>
        </div>
        
        <div class="news-item">
            <span>📱 मोबाइल, इलेक्ट्रॉनिक्स एवं सॉफ्टवेयर शॉप खाता</span>
            <span class="v-icon">V</span>
        </div>

    </marquee>
</div>
"""

# स्क्रॉलिंग डिब्बे को नीचे प्रदर्शित करना
components.html(news_box_html, height=290)
