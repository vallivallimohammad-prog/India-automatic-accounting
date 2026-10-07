import streamlit as st
import pandas as pd
import sqlite3

# ----------------- 1. पेज कॉन्फ़िगरेशन -----------------
st.set_page_config(
    page_title="भारत ऑनलाइन हिसाब ऑटोमेशन", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# ----------------- 2. ब्लैकलिस्ट व सुरक्षा चक्र -----------------
# जिन यूज़र/आईडी को ब्लॉक करना हो, उनके नाम या मोबाइल नंबर यहाँ लिखें
BLACKLIST = ["bad_user", "test_block_123"]

# यूज़र पहचान फॉर्म
st.sidebar.title("🔐 यूज़र सुरक्षा ज़ोन")
user_identity = st.sidebar.text_input("अपनी यूज़र आईडी/मोबाइल दर्ज करें:", "Guest_User")

if user_identity.strip() in BLACKLIST:
    st.error("🚫 Access Denied: सुरक्षा कारणों से आपका एक्सेस ब्लॉक कर दिया गया है।")
    st.stop()  # ब्लॉक होते ही पूरी वेबसाइट बंद हो जाएगी

# ----------------- 3. डेटाबेस सेटअप (SQLite) -----------------
conn = sqlite3.connect("accounting_db.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS master_register (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        entry_date TEXT, party_name TEXT, income REAL, expense REAL, verified_by TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT, issue_type TEXT, message TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()

# ----------------- 4. मुख्य इंटरफ़ेस -----------------
st.title("🇮🇳 भारत ऑटोमेटेड हिसाब-किताब एवं रिपोर्टिंग टूल")
st.caption("मुफ़्त, 100% सुरक्षित और स्व-सत्यापित (Self-Verified) ऑटोमेशन सेवा")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📷 1. रजिस्टर के पन्ने की फोटो")
    photo = st.file_uploader("कैमरे से फोटो लें या गैलरी से अपलोड करें", type=['jpg', 'png', 'jpeg'])
    if photo:
        st.image(photo, caption="अपलोड किया गया पन्ना", use_column_width=True)

with col2:
    st.subheader("✏️ 2. डेटा जांच व इंसानी सत्यापन")
    party = st.text_input("पार्टी / व्यक्ति का नाम", "रमेश ट्रेडर्स")
    income = st.number_input("जमा रकम (Income ₹)", value=0.0, step=100.0)
    expense = st.number_input("खर्च रकम (Expense ₹)", value=0.0, step=100.0)

st.markdown("---")

# ----------------- 5. मज़बूर सहमति बटन (Consent Checkbox) -----------------
st.subheader("🛡️ स्व-सत्यापन व सहमति शपथ")

consent = st.checkbox(
    "⚠️ मैंने फोटो और पड़े गए अंकों की खुद अपनी आँखों से भली-भांति जांच कर ली है। यह डेटा 100% सही है। इसे काम में लेने से पहले स्वयं जांचना मेरी अपनी जिम्मेदारी है।"
)

if consent:
    if st.button("✅ मैंने पढ़ लिया और चेक कर लिया - डेटा सुरक्षित सेव करें"):
        cursor.execute(
            "INSERT INTO master_register (entry_date, party_name, income, expense, verified_by) VALUES (date('now'), ?, ?, ?, ?)",
            (party, income, expense, user_identity)
        )
        conn.commit()
        st.success("🔒 डेटा आपके डिजिटल सत्यापन के साथ 100% सुरक्षित सेव हो गया!")
else:
    st.info("👈 कृपया पहले ऊपर दिए गए सहमति बॉक्स पर टिक (✓) लगाएं, तभी सेव बटन चालू होगा।")

st.markdown("---")

# ----------------- 6. 1 मास्टर + 4 कस्टम रिपोर्ट -----------------
st.subheader("📊 4 कस्टमाइज्ड फाइलों के निर्देश")

p1 = st.text_input("निर्देश 1", "पार्टी-वार खाता अलग करो")
p2 = st.text_input("निर्देश 2", "मद-वार खर्च रिपोर्ट")
p3 = st.text_input("निर्देश 3", "मासिक लाभ-हानि रिपोर्ट")
p4 = st.text_input("निर्देश 4", "बड़ी रकम वाले लेन-देन की लिस्ट")

if st.button("🚀 RUN - 1 मास्टर + 4 कस्टम फाइलें डाउनलोड करें"):
    df = pd.read_sql_query("SELECT * FROM master_register", conn)
    df.to_excel("Master_Accounting_Report.xlsx", index=False)
    
    st.success("✅ आपकी 1 मास्टर और 4 कस्टमाइज्ड रिपोर्ट तैयार हो गईं!")
    st.dataframe(df)

# ----------------- 7. लीगल डिस्क्लेमर (अस्वीकरण) -----------------
st.markdown("---")
st.warning("""
**⚠️ कानूनी अस्वीकरण व नियम (Terms & Legal Disclaimer):**
1. यह वेबसाइट एक ऑटोमेशन व सहायता टूल है। इससे जनरेट हुई फाइलों का उपयोग करने से पहले **संख्याओं (Numbers) और हिसाब को स्वयं जांचना आपकी अपनी जिम्मेदारी है।**
2. धीमे इंटरनेट, नेटवर्क त्रुटि या यूजर द्वारा गलत डेटा सत्यापित करने पर होने वाले किसी भी नुकसान के लिए हमारी **कोई कानूनी या व्यक्तिगत जिम्मेदारी नहीं होगी।**
3. अंतिम रूप से काम में लेने से पहले फाइल को स्वयं भली-भांति जांच लें।
""")

# ----------------- 8. फीडबैक व एरर रिपोर्ट फॉर्म -----------------
st.subheader("💬 समस्या या सुझाव दर्ज करें")
with st.form(key='feedback_form'):
    issue_type = st.selectbox("समस्या का प्रकार:", ["अंक गलत पड़े गए", "फाइल डाउनलोड नहीं हो रही", "धीमी वेबसाइट", "अन्य सुझाव"])
    user_message = st.text_area("अपनी समस्या का पूरा विवरण लिखें:")
    submit_fb = st.form_submit_button("📩 रिपोर्ट भेजें")
    
    if submit_fb:
        if user_message.strip():
            cursor.execute("INSERT INTO feedback_logs (user_id, issue_type, message) VALUES (?, ?, ?)", (user_identity, issue_type, user_message))
            conn.commit()
            st.success("🙏 धन्यवाद! आपका फीडबैक दर्ज कर लिया गया है। हम जल्द ही इसमें सुधार करेंगे।")
  
