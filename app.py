import streamlit as st

st.set_page_config(
    page_title="PlantCare AI",
    page_icon="🌱",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #E5F1DF;
    color: #174B32;
}

section[data-testid="stSidebar"] {
    background-color: #B5D6A7;
}

h1, h2, h3, p, label {
    color: #174B32 !important;
}

.stButton button {
    background-color: #174B32;
    color: white;
    border-radius: 12px;
    border: none;
}

.stButton button:hover {
    background-color: #286B47;
    color: white;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("🌱 PlantCare AI")
    st.caption("Smart Plant Monitoring")
    page = st.radio("القائمة", [
        "الرئيسية", "تحليل النباتات", "النتائج", "عن المشروع"
    ])

if page == "الرئيسية":
    st.title("🌱 PlantCare AI")
    st.subheader("اعتنِ بنباتك بذكاء")

    st.write("""
    نظام ذكي يساعدك على التعرف على النباتات
    ومراقبة احتياجاتها وتقديم توصيات للعناية بها.
    """)

    a, b, c = st.columns(3)

    a.info("🌿 التعرف على النباتات")
    b.info("💧 مراقبة الرطوبة")
    c.info("☀️ متابعة الإضاءة")

    st.divider()
    st.subheader("ابدئي رحلة العناية بنباتك")

    if st.button("ابدئي الآن"):
        st.success("واجهة تحليل النباتات ستكون جاهزة في المرحلة القادمة.")

elif page == "تحليل النباتات":
    st.title("تحليل النباتات")
    st.info("سيتم بناء هذه الواجهة في الجزء القادم.")

elif page == "النتائج":
    st.title("نتائج التحليل")
    st.info("ستظهر نتائج النبات هنا.")

else:
    st.title("عن المشروع")
    st.write("PlantCare AI هو نظام ذكي لمراقبة صحة النباتات الداخلية.")
