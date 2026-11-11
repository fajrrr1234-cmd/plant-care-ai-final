import streamlit as st

st.set_page_config(
    page_title="PlantCare AI",
    page_icon="🌱",
    layout="wide"
)

st.markdown("""
<style>
.stApp {background:#101713; color:white}
h1,h2,h3 {color:#D6B96C}
section[data-testid="stSidebar"] {background:#1B2920}
.stButton button {
    background:#28543A;
    color:white;
    border:1px solid #D6B96C;
    border-radius:12px;
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
