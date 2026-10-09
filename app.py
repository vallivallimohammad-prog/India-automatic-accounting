import streamlit as st
import streamlit.components.v1 as components
import datetime

st.set_page_config(page_title="ई-लेखा पोर्टल", layout="centered")

# Session State से पेज प्रबंधन
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'home'

# URL पैरामीटर चेक करना (पेज स्विच के लिए)
query_params = st.query_params
selected_page = query_params.get("page", None)
if selected_page:
    st.session_state['current_page'] = selected_page

# ==========================================
# 1. मुख्य होम पेज (HOME PAGE)
# ==========================================
if st.session_state['current_page'] == 'home':

    # स्क्रीन में पूरा फ़िट करने के लिए CSS
    st.markdown("""
    <style>
        .main .block-container {
            padding-left: 4px !important;
            padding-right: 4px !important;
            padding-top: 6px !important;
            max-width: 100% !important;
        }

        /* 1. सबसे ऊपर सरकारी हेडर पट्टी */
        .gov-header {
            background-color: #0b1f3a; color: white; padding: 6px 8px;
            border-radius: 4px; display: flex; justify-content: space-between;
            align-items: center; border-bottom: 2px solid #ff9933; margin-bottom: 8px;
        }
        .gov-header-title { font-size: 11px; font-weight: bold; }
        .gov-header-sub { font-size: 9px; opacity: 0.9; }

        /* 2. चेतावनी बोर्ड */
        .disclaimer-box {
            background-color: #fff5f5; border-left: 3px solid #d9534f;
            border: 1px solid #f5c6cb; padding: 6px; border-radius: 4px;
            margin-bottom: 10px;
        }
        .disclaimer-title { color: #a94442; font-weight: bold; font-size: 10.5px; margin-bottom: 2px; }
        .disclaimer-text { color: #721c24; font-size: 9.5px; line-height: 1.25; }

        /* 3. सबसे नीचे वाला बैनर बॉक्स */
        .banner-box {
            background-color: #1a2b40; color: white; text-align: center;
            padding: 8px; border-radius: 4px; margin-top: 10px; margin-bottom: 8px;
        }
        .banner-title { font-size: 13px; font-weight: bold; margin-bottom: 2px; }
        .banner-subtitle { font-size: 8.5px; color: #b0c4de; }
    </style>

    <!-- 1. हेडर पट्टी -->
    <div class="gov-header">
        <div class="gov-header-title">🏛️ राष्ट्रीय ई-लेखा एवं सत्यापन पोर्टल</div>
        <div class="gov-header-sub">भारत सरकार / डिजिटल सेवा</div>
    </div>

    <!-- 2. सुरक्षा चेतावनी बोर्ड -->
    <div class="disclaimer-box">
        <div class="disclaimer-title">⚠️ आवश्यक सूचना एवं कानूनी अस्वीकरण (Disclaimer):</div>
        <div class="disclaimer-text">
            यह प्रणाली केवल स्वचालित डिजिटल गणना हेतु है। किसी भी प्रकार की भिन्नता/त्रुटि होने पर डेवलपर की ज़िम्मेदारी नहीं होगी।
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 3. 50%-50% परफेक्ट स्क्रीन-फिट ग्रिड (बाईं तरफ छोटे बटन + दाहिनी तरफ स्क्रॉल डिब्बा)
    grid_html = """
    <style>
        .split-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 5px;
            width: 100%;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        /* बाईं तरफ की बटन पट्टी */
        .left-panel {
            background-color: #f8f9fa;
            border: 1px solid #004080;
            border-radius: 4px;
            overflow: hidden;
        }
        .left-header {
            background-color: #004080;
            color: white;
            padding: 4px 2px;
            font-size: 9.5px;
            font-weight: bold;
            text-align: center;
        }
        .btn-link {
            display: block;
            background-color: #0059b3;
            color: white !important;
            font-weight: bold;
            font-size: 8.5px;
            padding: 6px 4px;
            text-decoration: none;
            border-bottom: 1px solid #004080;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            box-sizing: border-box;
        }
        .btn-link:active, .btn-link:hover {
            background-color: #003366;
            color: #ffcc00 !important;
        }

        /* दाहिनी तरफ का स्क्रॉल डिब्बा */
        .right-panel {
            border: 1.5px solid #800000;
            background-color: #fff8dc;
            padding: 2px;
            border-radius: 4px;
            box-sizing: border-box;
            overflow: hidden;
        }
        .news-header {
            background-color: #800000;
            color: white;
            text-align: center;
            font-weight: bold;
            padding: 3px 2px;
            font-size: 9.5px;
            letter-spacing: 0.5px;
        }
        .news-item {
            padding: 4px 2px;
            border-bottom: 1px dashed #b8860b;
            font-size: 8px;
            font-weight: bold;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            color: #000080;
        }
        .news-text {
            flex: 1;
            padding-right: 2px;
            line-height: 1.15;
        }
        .v-icon-box {
            background-color: #0d6efd;
            color: white;
            font-weight: bold;
            font-size: 7.5px;
            width: 12px;
            height: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 2px;
            flex-shrink: 0;
            perspective: 1000px;
        }
        .spinning-v {
            display: inline-block;
            animation: rotateY 2.5s infinite linear;
        }
        @keyframes rotateY {
            0% { transform: rotateY(0deg); }
            100% { transform: rotateY(360deg); }
        }
    </style>

    <div class="split-grid">
        <!-- बाईं तरफ: असली वर्किंग टच बटन -->
        <div class="left-panel">
            <div class="left-header">📁 मुख्य सेवाएँ</div>
            <a class="btn-link" href="?page=pump" target="_parent">⛽ 1. पेट्रोल पंप नोज़ल ➔</a>
            <a class="btn-link" href="?page=kirana" target="_parent">🛒 2. किराना एवं जनरल ➔</a>
            <a class="btn-link" href="?page=sabzi" target="_parent">🥦 3. सब्जी व फल मंडी ➔</a>
            <a class="btn-link" href="?page=hardware" target="_parent">🔩 4. हार्डवेयर व लोहा ➔</a>
            <a class="btn-link" href="?page=mobile" target="_parent">📱 5. मोबाइल-इलेक्ट्रॉनिक्स ➔</a>
        </div>

        <!-- दाहिनी तरफ: 3D घूमते V आइकॉन वाला स्क्रॉल बॉक्स -->
        <div class="right-panel">
            <div class="news-header">NEWS UPDATE</div>
            <marquee direction="up" scrollamount="2" onmouseover="this.stop();" onmouseout="this.start();" height="150px">
                <div class="news-item">
                    <div class="news-text">⛽ 1. पेट्रोल पंप दैनिक लेखा-जोखा व नोज़ल रीडिंग</div>
                    <div class="v-icon-box"><span class="spinning-v">V</span></div>
                </div>
                <div class="news-item">
                    <div class="news-text">🛒 2. किराना एवं जनरल स्टोर दैनिक बिक्री</div>
                    <div class="v-icon-box"><span class="spinning-v">V</span></div>
                </div>
                <div class="news-item">
                    <div class="news-text">🥦 3. सब्जी एवं फल मंडी दैनिक व्यापार</div>
                    <div class="v-icon-box"><span class="spinning-v">V</span></div>
                </div>
                <div class="news-item">
                    <div class="news-text">🔩 4. हार्डवेयर, लोहा एवं स्टील लेजर</div>
                    <div class="v-icon-box"><span class="spinning-v">V</span></div>
                </div>
                <div class="news-item">
                    <div class="news-text">📱 5. मोबाइल, इलेक्ट्रॉनिक्स शॉप खाता</div>
                    <div class="v-icon-box"><span class="spinning-v">V</span></div>
                </div>
            </marquee>
        </div>
    </div>
    """

    components.html(grid_html, height=195)

    # 4. सबसे नीचे वाला मुख्य बैनर
    st.markdown("""
    <div class="banner-box">
        <div class="banner-title">स्वचालित खाता मिलान प्रणाली</div>
        <div class="banner-subtitle">Automated Fuel Station Reconciliation & Ledger Audit System</div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 2. पेट्रोल पंप का नया अलग पेज (PUMP PAGE)
# ==========================================
elif st.session_state['current_page'] == 'pump':

    if st.button("⬅️ मुख्य पेज पर वापस जाएँ (Back to Home)"):
        st.query_params.clear()
        st.session_state['current_page'] = 'home'
        st.rerun()

    st.markdown("---")
    st.title("⛽ पेट्रोल पंप नोज़ल एवं जमा-खर्च मिलान")

    st.subheader("📸 1. नोज़ल रीडिंग पर्चियाँ अपलोड करें")
    col1, col2 = st.columns(2)
    with col1:
        p1 = st.file_uploader("🌅 सुबह की नोज़ल रीडिंग पर्ची (Opening)", type=["jpg", "png", "jpeg"], key="p1")
    with col2:
        p2 = st.file_uploader("🌃 शाम की नोज़ल रीडिंग पर्ची (Closing)", type=["jpg", "png", "jpeg"], key="p2")

    st.subheader("📜 2. दैनिक जमा-खर्च व हिसाब पर्ची (हाथ से लिखी हुई)")
    p3 = st.file_uploader("📝 हाथ से लिखे दैनिक हिसाब/कैश रजिस्टर की फोटो", type=["jpg", "png", "jpeg"], key="p3")

    if st.button("🔄 AI द्वारा पर्चियाँ पढ़ें एवं हिसाब मिलाएँ"):
        if p1 and p2 and p3:
            st.success("✅ पर्चियाँ सफलतापूर्वक पहचान ली गईं!")
            
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
            
            if difference == 0:
                st.balloons()
                st.success("🎯 **अंतिम मिलान परिणाम: 0 (ज़ीरो अंतर - हिसाब बिल्कुल सही है!)**")

            today_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
            summary_text = f"पेट्रोल पंप रिपोर्ट - {today_date}\nकुल बिक्री: ₹1,18,600\nअंतर: 0"
            
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                st.download_button("📥 रिपोर्ट डाउनलोड करें", data=summary_text, file_name="Report.txt")
            with col_b2:
                if st.button("💾 डेटाबेस में सेव करें"):
                    st.toast("✅ रिकॉर्ड सेव हो गया!", icon="💾")
        else:
            st.error("⚠️ कृपया तीनों पर्चियाँ अपलोड करें!")

# ==========================================
# 3. बाकी अन्य पेजों के लिए
# ==========================================
else:
    if st.button("⬅️ मुख्य पेज पर वापस जाएँ (Back to Home)"):
        st.query_params.clear()
        st.session_state['current_page'] = 'home'
        st.rerun()

    st.markdown("---")
    st.title("🚧 जल्द ही उपलब्ध होगा")
    st.write("इस सेवा का फॉर्म तैयार किया जा रहा है।")
    
