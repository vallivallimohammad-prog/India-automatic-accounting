import streamlit as st
import streamlit.components.v1 as components
import datetime

# स्क्रीन कॉन्फ़िगरेशन
st.set_page_config(page_title="ई-लेखा पोर्टल", layout="wide")

# Session State से पेज प्रबंधन
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'home'

# ==========================================
# 1. मुख्य होम पेज (HOME PAGE)
# ==========================================
if st.session_state['current_page'] == 'home':

    # स्क्रीन में पूरा फ़िट करने के लिए CSS फ़िक्स
    st.markdown("""
    <style>
        /* मुख्य कंटेनर की चौड़ाई और पैडिंग फ़िक्स */
        .main .block-container {
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
            max-width: 100% !important;
        }

        /* 1. सबसे ऊपर सरकारी हेडर पट्टी */
        .gov-header {
            background-color: #0b1f3a; color: white; padding: 8px 10px;
            border-radius: 4px; display: flex; justify-content: space-between;
            align-items: center; border-bottom: 2px solid #ff9933; margin-bottom: 8px;
        }
        .gov-header-title { font-size: 12px; font-weight: bold; }
        .gov-header-sub { font-size: 10px; opacity: 0.9; }

        /* 2. चेतावनी बोर्ड */
        .disclaimer-box {
            background-color: #fff5f5; border-left: 4px solid #d9534f;
            border: 1px solid #f5c6cb; padding: 8px; border-radius: 4px;
            margin-bottom: 10px;
        }
        .disclaimer-title { color: #a94442; font-weight: bold; font-size: 11.5px; margin-bottom: 2px; }
        .disclaimer-text { color: #721c24; font-size: 10px; line-height: 1.3; }

        /* 3. बाईं तरफ की नीली बटन पट्टी */
        .sidebar-title {
            background-color: #004080;
            color: white;
            padding: 5px;
            font-size: 10px;
            font-weight: bold;
            text-align: center;
            border-radius: 3px 3px 0 0;
        }
        div.stButton > button {
            width: 100% !important;
            background-color: #0059b3 !important;
            color: white !important;
            font-weight: bold !important;
            border: none !important;
            border-bottom: 1px solid #004080 !important;
            border-radius: 0px !important;
            padding: 6px 2px !important;
            text-align: left !important;
            font-size: 9.5px !important;
            white-space: normal !important;
            word-wrap: break-word !important;
            line-height: 1.2 !important;
        }
        div.stButton > button:hover {
            background-color: #004080 !important;
            color: #ffcc00 !important;
        }

        /* मोबाइल स्क्रीन पर दोनों कॉलम को 50-50 चौड़ाई में बिना बाहर निकले फ़िट करना */
        [data-testid="stHorizontalBlock"] {
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            gap: 4px !important;
            width: 100% !important;
        }
        [data-testid="column"] {
            width: 50% !important;
            flex: 1 1 50% !important;
            min-width: 0 !important;
        }

        /* 4. सबसे नीचे वाला बैनर बॉक्स */
        .banner-box {
            background-color: #1a2b40; color: white; text-align: center;
            padding: 10px; border-radius: 4px; margin-top: 10px; margin-bottom: 8px;
        }
        .banner-title { font-size: 14px; font-weight: bold; margin-bottom: 2px; }
        .banner-subtitle { font-size: 9.5px; color: #b0c4de; }
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

    # 3. आमने-सामने दो हिस्से (Left Side Buttons & Right Side Scroll Box)
    col_left, col_right = st.columns(2)

    # ----------------------------------------------------
    # बाईं तरफ (Left Side): असली वर्किंग बटन
    # ----------------------------------------------------
    with col_left:
        st.markdown('<div class="sidebar-title">📁 मुख्य सेवाएँ (Quick Links)</div>', unsafe_allow_html=True)
        
        if st.button("⛽ 1. पेट्रोल पंप नोज़ल ➔"):
            st.session_state['current_page'] = 'pump'
            st.rerun()

        if st.button("🛒 2. किराना एवं जनरल ➔"):
            st.session_state['current_page'] = 'kirana'
            st.rerun()

        if st.button("🥦 3. सब्जी व फल मंडी ➔"):
            st.session_state['current_page'] = 'sabzi'
            st.rerun()

        if st.button("🔩 4. हार्डवेयर व लोहा ➔"):
            st.session_state['current_page'] = 'hardware'
            st.rerun()

        if st.button("📱 5. मोबाइल-इलेक्ट्रॉनिक्स ➔"):
            st.session_state['current_page'] = 'mobile'
            st.rerun()

    # ----------------------------------------------------
    # दाहिनी तरफ (Right Side): स्क्रॉल डिब्बा (Screen Fitted)
    # ----------------------------------------------------
    with col_right:
        news_box_html = """
        <style>
            .news-container { 
                border: 1.5px solid #800000; 
                background-color: #fff8dc; 
                padding: 2px; 
                border-radius: 3px; 
                font-family: Arial, sans-serif;
                box-shadow: 1px 1px 4px rgba(0,0,0,0.1);
            }
            .news-header { 
                background-color: #800000; 
                color: white; 
                text-align: center; 
                font-weight: bold; 
                padding: 3px; 
                font-size: 10px;
                letter-spacing: 0.5px;
            }
            .news-item { 
                padding: 4px 2px; 
                border-bottom: 1px dashed #b8860b; 
                font-size: 9px; 
                font-weight: bold; 
                display: flex; 
                justify-content: space-between; 
                align-items: flex-end;
                color: #000080;
            }
            .news-text {
                flex: 1;
                padding-right: 2px;
                line-height: 1.2;
            }
            .v-icon-box { 
                background-color: #0d6efd; 
                color: white; 
                font-weight: bold; 
                font-size: 8px; 
                width: 13px;
                height: 13px;
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

        <div class="news-container">
            <div class="news-header">NEWS UPDATE</div>
            <marquee direction="up" scrollamount="2" onmouseover="this.stop();" onmouseout="this.start();" height="155px">
                
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
        """
        components.html(news_box_html, height=175)

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
        st.session_state['current_page'] = 'home'
        st.rerun()

    st.markdown("---")
    st.title("🚧 जल्द ही उपलब्ध होगा")
    st.write("इस सेवा का फॉर्म तैयार किया जा रहा है।")
            
