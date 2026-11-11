import streamlit as st

st.set_page_config(
    page_title="PlantCare AI",
    page_icon="🌱",
    layout="wide"
)

# تنسيق الواجهة والألوان
st.markdown("""
<style>
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background-color: #E5F1DF;
}

/* النصوص على الخلفيات الفاتحة */
h1, h2, h3, p, label,
.stMarkdown, .stText {
    color: #174B32 !important;
}

/* المربعات الغامقة */
.dark-box {
    background-color: #174B32;
    color: white;
    padding: 20px;
    border-radius: 15px;
}

.dark-box * {
    color: white !important;
}

/* القائمة الجانبية */
section[data-testid="stSidebar"] {
    background-color: #B5D6A7;
}

section[data-testid="stSidebar"] * {
    color: #174B32 !important;
}

/* الأزرار */
.stButton button {
    background-color: #174B32;
    color: white !important;
    border-radius: 12px;
    border: none;
}
</style>
""", unsafe_allow_html=True)
# القائمة الجانبية
with st.sidebar:
    st.title("🌱 PlantCare AI")
    st.caption("Smart Plant Monitoring")

    page = st.radio(
        "القائمة",
        ["الرئيسية", "تحليل النباتات", "النتائج", "عن المشروع"]
    )

# الصفحة الرئيسية
if page == "الرئيسية":

    st.markdown("""
    <div class="card">
        <h1>🌱 PlantCare AI</h1>
        <h3>اعتنِ بنباتك بذكاء</h3>
        <p>
        نظام ذكي يساعدك على التعرف على النباتات الداخلية
        ومراقبة احتياجاتها وتقديم توصيات مناسبة للعناية بها.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.subheader("🌿 خدمات النظام")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h2>🌱</h2>
        <h3>التعرف على النباتات</h3>
        <p>التعرف على نوع النبات من خلال صورته.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h2>💧</h2>
        <h3>مراقبة الرطوبة</h3>
        <p>متابعة احتياجات النبات من الماء.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h2>☀️</h2>
        <h3>مراقبة الإضاءة</h3>
        <p>تحديد احتياجات النبات من الضوء.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.subheader("ابدئي رحلة العناية بنباتك")

    if st.button("🌿 ابدأ الآن"):
        st.info("انتقلي إلى صفحة تحليل النباتات من القائمة الجانبية.")

# صفحة تحليل النباتات
elif page == "تحليل النباتات":

    st.title("🌿 تحليل النباتات")
    st.subheader("ارفعي صورة نباتك أو التقطي صورة بالكاميرا")

    st.write("يمكنك اختيار صورة من جهازك أو استخدام الكاميرا.")

    uploaded_image = st.file_uploader(
        "📁 اختاري صورة النبات",
        type=["jpg", "jpeg", "png"]
    )

    camera_image = st.camera_input("📷 التقطي صورة للنبات")

    image = camera_image if camera_image else uploaded_image

    if image is not None:
        st.image(
            image,
            caption="صورة النبات",
            use_container_width=True
        )

        if st.button("🌱 ابدأ تحليل النبات"):
            st.success("تم رفع الصورة بنجاح!")
            st.info("الخطوة القادمة: ربط الصورة بنموذج الذكاء الاصطناعي للتعرف على النبات.")
# صفحة النتائج
elif page == "النتائج":
    st.title("📊 نتائج التحليل")
    st.info("ستظهر هنا نتائج تحليل حالة النباتات وتوصيات العناية بها.")

# صفحة عن المشروع
elif page == "عن المشروع":
    st.title("🌱 عن المشروع")
    st.write("""
    PlantCare AI هو نظام ذكي يهدف إلى مساعدة أصحاب النباتات
    الداخلية على التعرف على نباتاتهم ومراقبة احتياجاتها
    وتقديم إرشادات تساعدهم على العناية بها.
    """)
    st.subheader("أهداف المشروع")
    st.write("- التعرف على أنواع النباتات.")
    st.write("- متابعة احتياجات النباتات.")
    st.write("- تقديم توصيات للعناية بالنباتات.")
