import streamlit as st
import pandas as pd

# --- पेज सेटिंग्स ---
st.set_page_config(
    page_title="पेट्रोल पंप प्रबंधन",
    page_icon="⛽",
    layout="wide"
)

if "current_page" not in st.session_state:
    st.session_state["current_page"] = "home"

# ==========================================
# 🏠 1. मुख्य मेनू (Home)
# ==========================================
if st.session_state["current_page"] == "home":
    st.title("⛽ पेट्रोल पंप प्रबंधन प्रणाली")
    st.markdown("---")
    
    st.subheader("📋 मुख्य विकल्प (Menu)")
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("### 🧾 दैनिक जमा-खर्च व हिसाब")
        st.write("8 नोज़ल रीडिंग, MS/HSD सेलेक्ट, सुबह की टेस्टिंग, पर्चियाँ और दैनिक लेनदेन का पूरा हिसाब मिलाएँ।")
        if st.button("👉 हिसाब-किताब पेज खोलें", type="primary", use_container_width=True):
            st.session_state["current_page"] = "hisab_page"
            st.rerun()

    with col2:
        st.success("### 📊 स्टॉक व बिक्री रिपोर्ट्स")
        st.write("पुराने दैनिक हिसाब और बिक्री की समरी रिपोर्ट देखें।")
        st.button("📁 रिपोर्ट्स देखें (शीघ्र उपलब्ध)", disabled=True, use_container_width=True)

# ==========================================
# 📄 2. नया हिसाब-किताब पेज
# ==========================================
elif st.session_state["current_page"] == "hisab_page":
    
    if st.button("⬅️ मुख्य मेनू (Home) पर वापस जाएँ"):
        st.session_state["current_page"] = "home"
        st.rerun()

    st.title("📝 दैनिक जमा-खर्च व संपूर्ण हिसाब पर्ची")
    st.markdown("---")

    # ------------------------------------------
    # 1. पेट्रोल (MS) व डीजल (HSD) की दर (Rate)
    # ------------------------------------------
    st.header("1. ईंधन दरें दर्ज करें (Fuel Rates in ₹/Liter)")
    
    col_rate1, col_rate2 = st.columns(2)
    with col_rate1:
        ms_rate = st.number_input("🔴 MS Rate - पेट्रोल (₹/लीटर)", min_value=0.0, value=104.50, step=0.50)
    with col_rate2:
        hsd_rate = st.number_input("🔵 HSD Rate - डीजल (₹/लीटर)", min_value=0.0, value=90.20, step=0.50)

    st.markdown("---")

    # ------------------------------------------
    # 2. 8 नोज़ल रीडिंग एवं MS / HSD सिलेक्शन
    # ------------------------------------------
    st.header("2. नोज़ल रीडिंग एवं टाइप सेलेक्ट करें (8 नोज़ल्स)")
    st.info("हर नोज़ल के लिए MS (पेट्रोल) या HSD (डीजल) सेलेक्ट करें। केवल उन्हीं नोज़लों का हिसाब जुड़ेगा जिनकी सुबह और शाम दोनों रीडिंग भरी होंगी।")

    col_m_files, col_e_files = st.columns(2)

    with col_m_files:
        st.subheader("🌅 सुबह की नोज़ल पर्चियाँ (Opening)")
        m_files = [st.file_uploader(f"सुबह की पर्ची {i}", type=["jpg", "jpeg", "png"], key=f"m_file_{i}") for i in range(1, 5)]

    with col_e_files:
        st.subheader("🌆 शाम की नोज़ल पर्चियाँ (Closing)")
        e_files = [st.file_uploader(f"शाम की पर्ची {i}", type=["jpg", "jpeg", "png"], key=f"e_file_{i}") for i in range(1, 5)]

    st.markdown("#### 🔢 मैन्युअल नोज़ल रीडिंग व फ़्यूल टाइप (8 नोज़ल्स):")
    
    morning_readings = {}
    evening_readings = {}
    fuel_types = {}

    for i in range(1, 9):
        c1, c2, c3 = st.columns([2, 3, 3])
        with c1:
            fuel_types[f"Nozzle {i}"] = st.selectbox(
                f"नोज़ल {i} का तेल",
                options=["MS (पेट्रोल)", "HSD (डीजल)"],
                key=f"fuel_type_{i}"
            )
        with c2:
            morning_readings[f"Nozzle {i}"] = st.number_input(
                f"नोज़ल {i} (सुबह)", min_value=0.0, value=0.0, step=0.01, key=f"m_read_{i}"
            )
        with c3:
            evening_readings[f"Nozzle {i}"] = st.number_input(
                f"नोज़ल {i} (शाम)", min_value=0.0, value=0.0, step=0.01, key=f"e_read_{i}"
            )

    st.markdown("---")

    # ------------------------------------------
    # 3. सुबह की टेस्टिंग (Testing Oil)
    # ------------------------------------------
    st.header("3. सुबह की टेस्टिंग")
    col_t1, col_t2, col_t3 = st.columns(3)
    with col_t1:
        test_fuel_type = st.selectbox("टेस्टिंग का तेल टाइप", options=["MS (पेट्रोल)", "HSD (डीजल)"])
    with col_t2:
        testing_liters = st.number_input("टेस्टिंग का तेल (लीटर)", min_value=0.0, value=0.0, step=0.5)
    with col_t3:
        applicable_rate = ms_rate if test_fuel_type == "MS (पेट्रोल)" else hsd_rate
        default_test_rs = testing_liters * applicable_rate
        testing_rupees = st.number_input("टेस्टिंग के रुपये (₹)", min_value=0.0, value=default_test_rs, step=1.0)

    st.markdown("---")

    # ------------------------------------------
    # 4. दिनभर के लेनदेन का हिसाब (Cash/Credit)
    # ------------------------------------------
    st.header("4. दिनभर के लेनदेन का हिसाब (कैश / जमा-खर्च / उधारी)")
    st.caption("आप चाहें तो लेनदेन टाइप करके भरें या रजिस्टर की पर्चियाँ अपलोड करें।")

    col_trans1, col_trans2 = st.columns(2)
    with col_trans1:
        cash_received = st.number_input("💵 कुल प्राप्त नकद / ऑनलाइन भुगतान (Received ₹)", min_value=0.0, value=0.0, step=100.0)
    with col_trans2:
        expenses_paid = st.number_input("💸 कुल दिया गया / खर्च / उधारी (Expenses/Credit ₹)", min_value=0.0, value=0.0, step=100.0)

    st.subheader("📸 या हाथ के रजिस्टर की पर्चियाँ अपलोड करें (4 ऑप्शन)")
    reg_cols = st.columns(4)
    register_files = []
    for i in range(1, 5):
        with reg_cols[i-1]:
            rf = st.file_uploader(f"रजिस्टर पर्ची {i}", type=["jpg", "jpeg", "png"], key=f"reg_file_{i}")
            if rf:
                register_files.append(rf)

    st.markdown("---")

    # ------------------------------------------
    # 5. स्वचालित हिसाब मिलाएँ
    # ------------------------------------------
    if st.button("🔄 स्वचालित हिसाब मिलाएँ", type="primary", use_container_width=True):
        nozzle_data = []
        
        ms_gross_liters = 0.0
        hsd_gross_liters = 0.0
        
        ms_gross_amount = 0.0
        hsd_gross_amount = 0.0
        
        for i in range(1, 9):
            f_type = fuel_types[f"Nozzle {i}"]
            rate = ms_rate if f_type == "MS (पेट्रोल)" else hsd_rate
            
            m_val = morning_readings[f"Nozzle {i}"]
            e_val = evening_readings[f"Nozzle {i}"]
            
            if m_val > 0 and e_val > 0 and e_val >= m_val:
                diff = e_val - m_val
                status_str = f"{diff:,.2f} L"
                amt = diff * rate
                
                if f_type == "MS (पेट्रोल)":
                    ms_gross_liters += diff
                    ms_gross_amount += amt
                else:
                    hsd_gross_liters += diff
                    hsd_gross_amount += amt
            elif m_val > 0 and e_val == 0:
                diff = 0.0
                amt = 0.0
                status_str = "0.00 L (शाम की रीडिंग खाली)"
            elif m_val == 0 and e_val > 0:
                diff = 0.0
                amt = 0.0
                status_str = "0.00 L (सुबह की रीडिंग खाली)"
            else:
                diff = 0.0
                amt = 0.0
                status_str = "0.00 L"

            nozzle_data.append({
                "नोज़ल नं.": f"नोज़ल {i}",
                "ईंधन टाइप": f_type,
                "सुबह रीडिंग": f"{m_val:,.2f}" if m_val > 0 else "---",
                "शाम रीडिंग": f"{e_val:,.2f}" if e_val > 0 else "---",
                "बिक्री (लीटर)": status_str,
                "लागू दर (Rate)": f"₹ {rate:,.2f}",
                "बिक्री (रुपये ₹)": f"₹ {amt:,.2f}"
            })
        
        st.success("हिसाब सफलतापूर्वक मिल गया है!")
        
        df_nozzles = pd.DataFrame(nozzle_data)
        st.subheader("📊 1. नोज़ल-वार बिक्री विवरण (MS/HSD Separate)")
        st.table(df_nozzles)
        
        total_gross_liters = ms_gross_liters + hsd_gross_liters
        total_gross_amount = ms_gross_amount + hsd_gross_amount
        
        test_rate = ms_rate if test_fuel_type == "MS (पेट्रोल)" else hsd_rate
        testing_amount = testing_rupees if testing_rupees > 0 else (testing_liters * test_rate)
        
        net_total_amount = max(0.0, total_gross_amount - testing_amount)
        
        st.subheader("📝 2. संपूर्ण बिक्री एवं ईंधन-वार समरी")
        st.write(f"• **🔴 MS (पेट्रोल) कुल बिक्री:** {ms_gross_liters:,.2f} लीटर (दर: ₹ {ms_rate:,.2f}) = **₹ {ms_gross_amount:,.2f}**")
        st.write(f"• **🔵 HSD (डीजल) कुल बिक्री:** {hsd_gross_liters:,.2f} लीटर (दर: ₹ {hsd_rate:,.2f}) = **₹ {hsd_gross_amount:,.2f}**")
        st.write(f"• **⛽ कुल ग्रॉस बिक्री:** {total_gross_liters:,.2f} लीटर = **₹ {total_gross_amount:,.2f}**")
        
        if testing_liters > 0 or testing_rupees > 0:
            st.write(f"• **🧪 टेस्टिंग कटौती ({test_fuel_type}):** {testing_liters:,.2f} लीटर = **₹ {testing_amount:,.2f}** (घटाया गया)")
            st.write(f"• **✅ शुद्ध देय राशि (Net Sale Amount):** **₹ {net_total_amount:,.2f}**")
        else:
            st.write(f"• **✅ शुद्ध देय राशि (Net Sale Amount):** **₹ {total_gross_amount:,.2f}**")
            
        st.markdown("---")
        st.subheader("💰 3. दैनिक जमा-खर्च एवं शेष कैश मिलान")
        st.write(f"• **प्राप्त नकद / ऑनलाइन कुल जमा (Received):** ₹ {cash_received:,.2f}")
        st.write(f"• **कुल दिया गया / खर्च / उधारी (Paid/Out):** ₹ {expenses_paid:,.2f}")
        
        calculated_balance = cash_received - expenses_paid
        st.write(f"• **निवल कैश शेष (Net Cash Balance):** **₹ {calculated_balance:,.2f}**")
        
        if len(register_files) > 0:
            st.write(f"• **अपलोड की गई रजिस्टर पर्चियाँ:** {len(register_files)} फोटो मिलाई गईं।")

        st.markdown("---")
        
        summary_text = (
            f"पेट्रोल पंप दैनिक रिपोर्ट\n"
            f"MS Rate: Rs. {ms_rate}/L | HSD Rate: Rs. {hsd_rate}/L\n"
            f"MS Sale: {ms_gross_liters:.2f} L (Rs. {ms_gross_amount:.2f})\n"
            f"HSD Sale: {hsd_gross_liters:.2f} L (Rs. {hsd_gross_amount:.2f})\n"
            f"Gross Total: {total_gross_liters:.2f} L (Rs. {total_gross_amount:.2f})\n"
            f"Testing Deduction ({test_fuel_type}): {testing_liters:.2f} L (Rs. {testing_amount:.2f})\n"
            f"Net Total Amount: Rs. {net_total_amount:.2f}\n"
            f"Received Cash: Rs. {cash_received:.2f}\n"
            f"Expenses/Credit: Rs. {expenses_paid:.2f}\n"
            f"Net Cash Balance: Rs. {calculated_balance:.2f}\n"
        )
        
        st.download_button(
            label="📥 संपूर्ण MS/HSD दैनिक रिपोर्ट डाउनलोड करें (Text)",
            data=summary_text,
            file_name="Daily_Petrol_Pump_MS_HSD_Report.txt",
            mime="text/plain",
            use_container_width=True
    )
        
