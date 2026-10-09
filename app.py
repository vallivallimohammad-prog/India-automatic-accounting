import streamlit as st
import streamlit.components.v1 as components

# राजस्थान बोर्ड जैसी डिजाइन के लिए HTML और CSS कोड
news_box_html = """
<style>
    /* मुख्य न्यूज बॉक्स की डिजाइन */
    .news-container {
        border: 2px solid #800000; /* बोर्ड वेबसाइट जैसा मेरून/लाल बॉर्डर */
        background-color: #fff8dc; /* हल्का क्रीम रंग का बैकग्राउंड */
        width: 100%;
        max-width: 320px;
        padding: 5px;
        border-radius: 4px;
        font-family: Arial, sans-serif;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
    }
    
    /* बॉक्स की हेडिंग */
    .news-header {
        background-color: #800000;
        color: white;
        text-align: center;
        font-weight: bold;
        font-size: 14px;
        padding: 4px;
        margin-bottom: 5px;
        text-transform: uppercase;
    }

    /* स्क्रॉल होने वाली हर लाइन */
    .news-item {
        padding: 6px 4px;
        border-bottom: 1px dashed #b8860b;
        font-size: 13px;
        font-weight: bold;
        color: #000080; /* बोर्ड स्टाइल का डार्क ब्लू टेक्स्ट */
        display: flex;
        justify-content: space-between;
        align-items: center;
        text-decoration: none;
    }

    /* नीले रंग का V आइकॉन */
    .v-icon {
        background-color: #0d6efd;
        color: white;
        font-weight: bold;
        font-size: 11px;
        padding: 2px 6px;
        border-radius: 3px;
        margin-left: 8px;
        flex-shrink: 0;
    }
</style>

<div class="news-container">
    <div class="news-header">NEWS UPDATE</div>
    
    <!-- ऊपर की तरफ स्क्रॉल होने वाला टैग -->
    <marquee direction="up" scrollamount="2" onmouseover="this.stop();" onmouseout="this.start();" height="260px">
        
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

# Streamlit में दिखाने के लिए लेआउट बनाएँ
col1, col2 = st.columns([2, 1])

with col1:
    st.write("यहाँ आपकी वेबसाइट का मुख्य कंटेंट रहेगा...")

with col2:
    # दाईं तरफ बोर्ड जैसी न्यूज स्क्रॉलिंग बॉक्स दिखेगी
    components.html(news_box_html, height=320)
    
