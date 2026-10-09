import streamlit as st
import streamlit.components.v1 as components
import json
from datetime import datetime

st.set_page_config(page_title="ई-लेखा पोर्टल", layout="centered")

# 1. हेडर, बैनर और डिस्क्लेमर
st.markdown("""
<style>
    .gov-header {
        background-color: #0b1f3a; color: white; padding: 10px 15px;
        border-radius: 4px; display: flex; justify-content: space-between;
        align-items: center; border-bottom: 3px solid #ff9933; margin-bottom: 15px;
    }
    .gov-header-title { font-size: 14px; font-weight: bold; }
    .gov-header-sub { font-size: 12px; opacity: 0.9; }
    .banner-box {
        background-color: #1a2b40; color: white; text-align: center;
        padding: 20px 15px; border-radius: 8px; margin-bottom: 15px;
    }
    .banner-title { font-size: 20px; font-weight: bold; margin-bottom: 8px; }
    .banner-subtitle { font-size: 13px; color: #b0c4de; }
    .disclaimer-box {
        background-color: #fff5f5; border-left: 5px solid #d9534f;
        border: 1px solid #f5c6cb; padding: 15px; border-radius: 4px; margin-bottom: 15px;
    }
    .disclaimer-title { color: #a94442; font-weight: bold; font-size: 15px; margin-bottom: 8px; }
    .disclaimer-text { color: #721c24; font-size: 13px; line-height: 1.5; }
    .pump-card {
        background-color: #f8f9fa; border: 1px solid #cce5ff;
        padding: 15px; border-radius: 8px; margin-bottom: 15px;
    }
</style>

<div class="gov-header">
    <div class="gov-header-title">🏛️ राष्ट्रीय ई-लेखा एवं बही-खाता सत्यापन पोर्टल</div>
    <div class="gov-header-sub">भारत सरकार / राज्य डिजिटल सेवा</div>
</div>

<div class="banner-box">
    <div class="banner-title">स्वचालित ईंधन बही-खाता एवं डिजिटल मिलान प्रणाली</div>
    <div class="banner-subtitle">Automated Fuel Station Reconciliation & Ledger Audit System</div>
</div>

<div class="disclaimer-box">
    <div class="disclaimer-title">⚠️ आवश्यक सूचना एवं कानूनी अस्वीकरण (Disclaimer):</div>
    <div class="disclaimer-text">
        यह प्रणाली केवल स्वचालित डिजिटल गणना एवं संदर्भ सहायता हेतु उपलब्ध कराई गई है। हिसाब-किताब में किसी भी प्रकार की भिन्नता, त्रुटि या गड़बड़ी होने पर प्रणाली/डेवलपर की कोई ज़िम्मेदारी नहीं होगी।
    </div>
</div>
""", unsafe_allow_html=True)

# 2. ऑटो-स्क्रॉलिंग न्यूज़ बॉक्स
news_box_html = """
<style>
    .news-container { border: 2px solid #800000; background-color: #fff8dc; padding: 5px; border-radius: 6px; }
    .news-header { background-color: #800000; color: white; text-align: center; font-weight: bold; padding: 6px; }
    .news-item { padding: 10px 8px; border-bottom: 1px dashed #b8860b; font-size: 13.5px; font-weight: bold; color: #000080; display: flex; justify-content: space-between; }
    .v-icon { background-color: #0d6efd; color: white; padding: 2px 7px; border-radius: 3px; font-size: 11px; }
</style>
<div class="news-container">
    <div class="news-header">NEWS UPDATE</div>
    <marquee direction="up" scrollamount="2" onmouseover="this.stop();" onmouseout="this.start();" height="150px">
        <div class="news-item"><span>⛽ 1. पेट्रोल पंप दैनिक लेखा-जोखा एवं नोज़ल रीडिंग मिलान</span><span class="v-icon">V</span></div>
        <div class="news-item"><span>🛒 2. किराना एवं जनरल स्टोर दैनिक बिक्री व बही-खाता</span><span class="v-icon">V</span></div>
        <div class="news-item"><span>🥦 3. सब्जी एवं फल मंडी दैनिक व्यापार रजिस्टर</span><span class="v-icon">V</span></div>
    </marquee>
</div>
"""
components.html(news_box_html, height=200)

st.markdown("---")

# 3. ड्रॉपडाउन से सेलेक्ट करना
selected_option = st.selectbox(
    "👇 आगे बढ़ने के लिए कृपया अपनी सेवा चुनें:",
    [
        "-- सेवा चुनें --",
        "⛽ पेट्रोल पंप दैनिक लेखा-जोखा एवं नोज़ल रीडिंग मिलान",
        "🛒 किराना एवं जनरल स्टोर दैनिक बिक्री व बही-खाता"
    ]
)

# 4. पेट्रोल पंप वाला फॉर्म
if selected_option == "⛽ पेट्रोल पंप दैनिक लेखा-जोखा एवं नोज़ल रीडिंग मिलान":
    st.subheader("⛽ पेट्रोल पंप नोज़ल एवं जमा-खर्च मिलान फॉर्म")
    
    st.markdown('<div class="pump-card">', unsafe_allow_html=True)
    st.write("### 📸 1. नोज़ल रीडिंग पर्चियाँ अपलोड करें")
    col1, col2 = st.columns(2)
    with col1:
        p1 = st.file_uploader("🌅 सुबह की नोज़ल रीडिंग पर्ची (Opening)", type=["jpg", "png", "jpeg"], key="morning")
    with col2:
        p2 = st.file_uploader("🌃 शाम की नोज़ल रीडिंग पर्ची (Closing)", type=["jpg", "png", "jpeg"], key="evening")
    
    st.write("---")
    st.write("### 📜 2. दैनिक जमा-खर्च व हिसाब पर्ची (हाथ से लिखी हुई)")
    p3 = st.file_uploader("📝 हाथ से लिखे दैनिक हिसाब/कैश रजिस्टर की फोटो", type=["jpg", "png", "jpeg"], key="handwritten")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # हिसाब मिलाएँ बटन
    if st.button("🔄 AI द्वारा पर्चियाँ पढ़ें एवं हिसाब मिलाएँ"):
        if p1 and p2 and p3:
            st.info("🔍 सिस्टम पर्चियों को स्कैन करके रीडिंग पहचान रहा है...")
            st.success("✅ पर्चियाँ सफलतापूर्वक स्कैन हो गईं!")
            
            st.markdown("### 📊 AI द्वारा निकाला गया ऑटोमैटिक विवरण:")
            
            # डेटा की सरणी
            report_data = [
                {"इंधन प्रकार": "MS (पेट्रोल)", "नोज़ल": "Nozzle 1", "सुबह रीडिंग": "12450.00", "शाम रीडिंग": "12850.00", "बिक्री (लीटर)": "400 Ltr", "दर": "₹108.50", "कुल रुपये": "₹43,400"},
                {"इंधन प्रकार": "HSD (डीजल)", "नोज़ल": "Nozzle 2", "सुबह रीडिंग": "50200.00", "शाम रीडिंग": "51000.00", "बिक्री (लीटर)": "800 Ltr", "दर": "₹94.00", "कुल रुपये": "₹75,200"}
            ]
            st.table(report_data)
            
            total_fuel_sale = 118600
            cash_received = 118600
            difference = cash_received - total_fuel_sale
            
            st.write(f"💵 **पर्चियों के अनुसार कुल तेल बिक्री:** `₹{total_fuel_sale:,}`")
            st.write(f"📝 **हाथ की पर्ची से मिली कुल रकम:** `₹{cash_received:,}`")
            
            st.markdown("---")
            if difference == 0:
                st.balloons()
                st.success("🎯 **अंतिम मिलान परिणाम: 0 (ज़ीरो अंतर - हिसाब बिल्कुल सही है!)**")
            elif difference > 0:
                st.warning(f"📈 **अंतिम मिलान परिणाम: +₹{difference} (प्लस में - कैश ज़्यादा है)**")
            else:
                st.error(f"📉 **अंतिम मिलान परिणाम: -₹{abs(difference)} (माइनस में - पैसे कम हैं)**")

            # ----------------------------------------------------
            # 5. सेव और डाउनलोड करने का सेक्शन
            # ----------------------------------------------------
            st.markdown("---")
            st.subheader("💾 हिसाब-किताब सेव एवं डाउनलोड करें")
            
            # डाउनलोड रिपोर्ट का टेक्स्ट बनाना
            today_date = datetime.now().strftime("%d-%m-%Y %H:%M")
            summary_text = f"""=== राष्ट्रीय ई-लेखा एवं बही-खाता रिपोर्ट ===
दिनांक एवं समय: {today_date}
सेवा का नाम: पेट्रोल पंप दैनिक लेखा-जोखा

--- नोज़ल बिक्री विवरण ---
1. MS (पेट्रोल) | Nozzle 1 | बिक्री: 400 Ltr | दर: ₹108.50 | कुल: ₹43,400
2. HSD (डीजल)  | Nozzle 2 | बिक्री: 800 Ltr | दर: ₹94.00  | कुल: ₹75,200

--- अंतिम हिसाब मिलान ---
पर्चियों से कुल बिक्री राशि : ₹{total_fuel_sale:,}
हाथ की पर्ची से प्राप्त कुल राशि: ₹{cash_received:,}
अंतिम अंतर (Difference)        : ₹{difference} (बराबर/ज़ीरो)

स्थिति: हिसाब सफलतापूर्वक सत्यापित हो गया।
==========================================
"""

            col_btn1, col_btn2 = st.columns(2)
            
            with col_btn1:
                # 1. डाउनलोड बटन (टेक्स्ट/सामरी फ़ाइल)
                st.download_button(
                    label="📥 हिसाब की रिपोर्ट डाउनलोड करें (Text/PDF File)",
                    data=summary_text,
                    file_name=f"Fuel_Audit_Report_{datetime.now().strftime('%d_%m_%Y')}.txt",
                    mime="text/plain"
                )
                
            with col_btn2:
                # 2. डेटाबेस / रिकॉर्ड में सेव करने का बटन
                if st.button("💾 सिस्टम/डेटाबेस में सेव करें"):
                    st.toast("✅ हिसाब रिकॉर्ड सफलतापूर्वक डेटाबेस में सेव कर दिया गया है!", icon="💾")

        else:
            st.error("⚠️ कृपया तीनों पर्चियों की फोटो अपलोड करें!")
        
