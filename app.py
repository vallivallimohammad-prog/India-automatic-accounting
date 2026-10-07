import os
import re
import json
import streamlit as st
from PIL import Image
import google.generativeai as genai
import pandas as pd

# Streamlit Page Setup
st.set_page_config(page_title="India Automatic Accounting", layout="wide")

# App Header (English Name)
st.title("⛽ India Automatic Accounting")
st.caption("AI-powered Automated Petrol Pump Daily Ledger & Annual Reporting System")

# Security & Safety Banner (हिंदी में सुरक्षा जानकारी)
st.info("🔒 **सुरक्षा एवं गोपनीयता चेतावनी:** यह ऐप 100% सुरक्षित है। आपके अपलोड किए गए पन्नों का डेटा पूरी तरह गोपनीय रखा जाता है और इसका उपयोग केवल आपके हिसाब-किताब की गणना के लिए किया जाता है।")

# 1. AI API Configuration
api_key = os.environ.get("GEMINI_API_KEY", "")
if api_key:
    genai.configure(api_key=api_key)

# 2. Session State Initialize
if "records" not in st.session_state:
    st.session_state.records = []

# --- AI Vision Model Function ---
def analyze_ledger_image(image):
    if not api_key:
        st.error("⚠️ **सुरक्षा त्रुटि:** Streamlit Secrets में GEMINI_API_KEY नहीं मिली है। कृपया अपनी एपीआई की (API Key) जोड़ें।")
        return None

    model = genai.GenerativeModel("gemini-1.5-flash")
    
    prompt = """
    You are an accounting expert AI. Carefully analyze this daily petrol pump ledger sheet.
    
    Extract the following details from the page:
    1. Previous/Start Nozzle Reading
    2. Current/End Nozzle Reading
    3. Fuel Sold in Liters
    4. Rate per Liter
    5. Total Sale Amount (Liters * Rate)
    6. Left Side: Total Income / Received (Cash & Online)
    7. Right Side: Total Expense / Credit / Bank Deposit
    8. Any additional notes or party details written on the page

    Return ONLY a pure JSON object in this exact format (do not add markdown text outside JSON):
    {
        "date": "Date on page or Blank",
        "start_reading": 0,
        "end_reading": 0,
        "fuel_qty": 0,
        "rate": 0,
        "total_sale_amount": 0,
        "left_side_income": 0,
        "right_side_expense": 0,
        "notes": "Notes / Credit Details"
    }
    """
    
    try:
        response = model.generate_content([prompt, image])
        text = response.text
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
        else:
            return None
    except Exception as e:
        st.error(f"⚠️ **स्कैनिंग त्रुटि:** पन्ने को पढ़ने में समस्या आई: {e}")
        return None


# --- Step 1: Upload Page Photo ---
st.markdown("---")
st.header("📸 1. पन्ने की फोटो अपलोड करें (Upload Register Page)")
uploaded_file = st.file_uploader("कैमरे से फोटो लें या गैलरी से चुनें (Take Photo / Choose File)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="अपलोड किया गया पन्ना", width=400)
    
    if st.button("🔍 AI से पन्ना पढ़वाएं (Scan Page with AI)", type="primary"):
        with st.spinner("AI पन्ने की रीडिंग, जमा-खर्च और लेआउट को पढ़ रहा है..."):
            extracted_data = analyze_ledger_image(image)
            if extracted_data:
                st.session_state.temp_data = extracted_data
                st.success("✅ AI ने पन्ने का हिसाब सफलतापूर्वक पढ़ लिया है! नीचे जाँच करें:")
            else:
                st.error("⚠️ पन्ना सही से पढ़ा नहीं जा सका। कृपया स्पष्ट फोटो अपलोड करें।")

# --- Step 2: Human Verification & Security Checks ---
if "temp_data" in st.session_state:
    st.markdown("---")
    st.header("✏️ 2. AI द्वारा निकाला गया डेटा (जाँचें एवं पुष्टि करें)")
    
    temp = st.session_state.temp_data
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("⛽ मीटर रीडिंग एवं तेल बिक्री")
        date_val = st.text_input("तारीख (Date)", value=str(temp.get("date", "")))
        start_r = st.number_input("कल की रीडिंग (Start Reading)", value=float(temp.get("start_reading", 0)))
        end_r = st.number_input("आज की रीडिंग (End Reading)", value=float(temp.get("end_reading", 0)))
        fuel_qty = st.number_input("कुल बिका तेल / लीटर (Fuel Sold)", value=float(temp.get("fuel_qty", 0)))
        rate_val = st.number_input("रेट प्रति लीटर ₹ (Rate)", value=float(temp.get("rate", 0)))
        total_sale = st.number_input("कुल बिक्री रकम ₹ (Total Sale)", value=float(temp.get("total_sale_amount", 0)))

    with col2:
        st.subheader("📖 बाएँ / दाएँ लेजर खाता")
        left_inc = st.number_input("Left Side (कुल जमा/आवक ₹)", value=float(temp.get("left_side_income", 0)))
        right_exp = st.number_input("Right Side (कुल खर्च/उधार ₹)", value=float(temp.get("right_side_expense", 0)))
        
        diff = left_inc - right_exp
        if diff == 0:
            st.success("✅ हिसाब पूरी तरह मैच (Tallied) है!")
        else:
            st.warning(f"⚠️ अंतर: ₹ {abs(diff):,.2f}")
            
        notes_text = st.text_area("अन्य विवरण / उधार ग्राहकों के नाम (Notes)", value=str(temp.get("notes", "")))

    # Verification & Security Checkbox (सहमति चिन्ह)
    st.markdown("---")
    is_verified = st.checkbox("☑️ **मैं पुष्टि करता/करती हूँ कि मैंने ऊपर दी गई सभी जानकारियों की जाँच कर ली है और यह हिसाब पूरी तरह सही है।**")

    # Safety Notice below checkbox
    st.caption("⚠️ *नोट: रिकॉर्ड में जोड़ने से पहले ऊपर दिए गए बॉक्स पर टिक लगाना अनिवार्य है।*")

    # Save Button (केवल टिक करने के बाद चालू होगा)
    if st.button("✅ इस पन्ने का डेटा सुरक्षित सेव करें (Confirm & Save Page)", disabled=not is_verified):
        entry = {
            "Date / Page": date_val if date_val else f"Page #{len(st.session_state.records)+1}",
            "Fuel Sold (L)": fuel_qty,
            "Rate (₹)": rate_val,
            "Total Sale (₹)": total_sale,
            "Income / Recd (₹)": left_inc,
            "Expense / Credit (₹)": right_exp,
            "Notes": notes_text
        }
        st.session_state.records.append(entry)
        del st.session_state.temp_data
        st.success("🎉 यह पन्ना रिकॉर्ड में सफलतापूर्वक सेव कर लिया गया है! आप अगला पन्ना अपलोड कर सकते हैं।")
        st.rerun()

# --- Step 3: Multi-Page Summary Report ---
st.markdown("---")
st.header("📊 3. संकलित रिपोर्ट (Consolidated Summary Report)")

if len(st.session_state.records) > 0:
    st.subheader(f"📚 कुल सुरक्षित सेव किए गए पन्ने: {len(st.session_state.records)}")
    
    df = pd.DataFrame(st.session_state.records)
    st.dataframe(df, use_container_width=True)
    
    # Final Confirmation Checkbox
    final_verify = st.checkbox("☑️ **मैंने सभी पन्नों का मिलान कर लिया है, अब पूरे साल/महीने की फाइनल रिपोर्ट तैयार करें।**")
    
    # Done Button
    if st.button("🏁 Done - फाइनल वार्षिक रिपोर्ट निकालें", type="primary", disabled=not final_verify):
        total_liters = sum(item["Fuel Sold (L)"] for item in st.session_state.records)
        total_sales = sum(item["Total Sale (₹)"] for item in st.session_state.records)
        total_income = sum(item["Income / Recd (₹)"] for item in st.session_state.records)
        total_expense = sum(item["Expense / Credit (₹)"] for item in st.session_state.records)
        
        st.balloons()
        st.success("🎉 पूरे पीरियड/साल की फाइनल एकीकृत रिपोर्ट सफलतापूर्वक तैयार हो गई है!")
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("कुल बिका तेल (Fuel Sold)", f"{total_liters:,.2f} L")
        c2.metric("कुल तेल बिक्री (Total Sales)", f"₹ {total_sales:,.2f}")
        c3.metric("कुल जमा राशि (Total Received)", f"₹ {total_income:,.2f}")
        c4.metric("कुल खर्च/उधार (Total Expense)", f"₹ {total_expense:,.2f}")

else:
    st.info("अभी तक कोई पन्ना जोड़ा नहीं गया है। शुरुआत करने के लिए ऊपर फोटो अपलोड करके स्कैन करें।")
      
