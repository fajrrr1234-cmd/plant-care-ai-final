import streamlit as st
import pandas as pd

# ==============================
# إعداد الصفحة
# ==============================

st.set_page_config(
    page_title="PlantCare AI",
    page_icon="🌱",
    layout="wide"
)

# ==============================
# تصميم الموقع
# ==============================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
    direction: rtl;
}

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background-color: #E5F1DF;
}

h1, h2, h3, h4, p, label, span {
    color: #174B32;
}

[data-testid="stSidebar"] {
    background-color: #B5D6A7;
}

[data-testid="stSidebar"] * {
    color: #174B32 !important;
}

.stButton > button {
    background-color: #174B32;
    color: white !important;
    border-radius: 10px;
    border: none;
    padding: 10px 22px;
    font-family: 'Cairo', sans-serif;
    font-weight: bold;
    width: 100%;
}

.stButton > button:hover {
    background-color: #286644;
    color: white !important;
}

.card {
    background-color: #F5FAF2;
    border: 1px solid #B5D6A7;
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 15px;
    text-align: right;
    min-height: 150px;
}

.card h3 {
    color: #174B32;
}

.card p {
    color: #42634D;
    line-height: 1.8;
}

.metric-card {
    background: #F5FAF2;
    border: 1px solid #B5D6A7;
    border-radius: 14px;
    padding: 18px;
    text-align: center;
}

.metric-value {
    font-size: 28px;
    font-weight: bold;
    color: #174B32;
}

.metric-label {
    font-size: 14px;
    color: #55745D;
}

.recommendation-card {
    background: white;
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 15px;
    border-right: 5px solid #5B9B64;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

.recommendation-card h3 {
    color: #24543A;
    font-size: 19px;
}

.recommendation-card p {
    color: #666;
    line-height: 1.8;
}

.priority {
    display: inline-block;
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 13px;
    margin-bottom: 10px;
    font-weight: bold;
}

.high {
    background: #FEE2E2;
    color: #DC2626;
}

.medium {
    background: #FEF3C7;
    color: #B45309;
}

.low {
    background: #DCFCE7;
    color: #15803D;
}

.action-box {
    background: #EDF6ED;
    padding: 12px;
    border-radius: 10px;
    margin-top: 12px;
    color: #24543A;
}

hr {
    border-color: #B5D6A7;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# بيانات النباتات
# القيم إرشادية وليست قياسات فعلية
# ==============================

plant_data = {
    "بوتس": {
        "moisture_min": 30,
        "moisture_max": 60,
        "light_min": 500,
        "light_max": 1500,
        "temp_min": 18,
        "temp_max": 30
    },
    "مونستيرا": {
        "moisture_min": 35,
        "moisture_max": 65,
        "light_min": 800,
        "light_max": 2000,
        "temp_min": 18,
        "temp_max": 30
    },
    "سانسيفيريا": {
        "moisture_min": 15,
        "moisture_max": 40,
        "light_min": 300,
        "light_max": 1500,
        "temp_min": 15,
        "temp_max": 32
    },
    "زنبق السلام": {
        "moisture_min": 45,
        "moisture_max": 70,
        "light_min": 500,
        "light_max": 1200,
        "temp_min": 18,
        "temp_max": 28
    },
    "نبات العنكبوت": {
        "moisture_min": 30,
        "moisture_max": 60,
        "light_min": 500,
        "light_max": 1500,
        "temp_min": 15,
        "temp_max": 30
    }
}

# ==============================
# القائمة الجانبية
# ==============================

st.sidebar.title("🌱 PlantCare AI")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "القائمة الرئيسية",
    [
        "الرئيسية",
        "تحليل النبات",
        "لوحة المعلومات",
        "التوصيات",
        "عن المشروع"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("نظام ذكي لمراقبة صحة النباتات الداخلية")

# ==============================
# الصفحة الرئيسية
# ==============================

if page == "الرئيسية":

    st.markdown(
        "<h1 style='text-align:center;'>🌱 PlantCare AI</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align:center;'>نظام ذكي لمراقبة صحة النباتات الداخلية</h3>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("""
    <div class="card">
        <h3>مرحباً بك في PlantCare AI</h3>
        <p>
        يساعدك النظام على متابعة حالة النباتات الداخلية
        ومعرفة احتياجاتها من الماء والإضاءة ودرجة الحرارة،
        مع تقديم توصيات تساعد على تحسين العناية بالنبات.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>📷 تحليل النبات</h3>
            <p>إمكانية رفع صورة النبات أو التقاط صورة له.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>📊 متابعة الحالة</h3>
            <p>متابعة الرطوبة والإضاءة ودرجة الحرارة.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>💡 التوصيات الذكية</h3>
            <p>الحصول على إرشادات للعناية بالنبات حسب القراءات.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.info("اختاري إحدى الصفحات من القائمة الجانبية للبدء.")

# ==============================
# تحليل النبات
# ==============================

elif page == "تحليل النبات":

    st.title("📷 تحليل النبات")
    st.write("اختاري صورة للنبات أو التقطي صورة باستخدام الكاميرا.")

    selected_plant = st.selectbox(
        "اختاري نوع النبات",
        list(plant_data.keys())
    )

    uploaded_image = st.file_uploader(
        "ارفعي صورة النبات",
        type=["jpg", "jpeg", "png"]
    )

    camera_image = st.camera_input("أو التقطي صورة للنبات")

    image = uploaded_image if uploaded_image is not None else camera_image

    if image is not None:
        st.image(
            image,
            caption="صورة النبات",
            use_container_width=True
        )

        st.success("تم تحميل الصورة بنجاح.")

        st.warning(
            "الصورة معروضة للمراجعة فقط في هذه النسخة؛ "
            "التعرف الآلي على نوع النبات والأمراض يحتاج إلى ربط نموذج ذكاء اصطناعي."
        )

    st.markdown("---")
    st.subheader("متابعة احتياجات النبات")

    col1, col2 = st.columns(2)

    with col1:
        moisture = st.slider(
            "رطوبة التربة (%)",
            min_value=0,
            max_value=100,
            value=45
        )

        light = st.slider(
            "شدة الإضاءة (Lux)",
            min_value=0,
            max_value=5000,
            value=1000
        )

    with col2:
        temperature = st.slider(
            "درجة الحرارة (°C)",
            min_value=0,
            max_value=50,
            value=24
        )

    if st.button("ابدأ تحليل حالة النبات"):

        st.session_state["plant"] = selected_plant
        st.session_state["moisture"] = moisture
        st.session_state["light"] = light
        st.session_state["temperature"] = temperature
        st.session_state["analyzed"] = True

        st.success("تم تحليل القراءات بنجاح!")
        st.info("انتقلي إلى لوحة المعلومات والتوصيات لمشاهدة النتيجة.")

# ==============================
# تجهيز حالة النبات
# ==============================

def analyze_plant(plant, moisture, light, temperature):

    data = plant_data[plant]
    recommendations = []

    if moisture < data["moisture_min"]:
        recommendations.append({
            "title": "تحسين عملية الري",
            "priority": "high",
            "priority_text": "أولوية عالية",
            "description": "مستوى رطوبة التربة أقل من النطاق الإرشادي.",
            "action": "تحققي من جفاف التربة واسقي النبات عند الحاجة."
        })

    elif moisture > data["moisture_max"]:
        recommendations.append({
            "title": "تقليل الري",
            "priority": "high",
            "priority_text": "أولوية عالية",
            "description": "رطوبة التربة أعلى من النطاق الإرشادي.",
            "action": "تأكدي من تصريف الماء واتركي التربة تجف جزئياً."
        })

    else:
        recommendations.append({
            "title": "رطوبة التربة مناسبة",
            "priority": "low",
            "priority_text": "أولوية منخفضة",
            "description": "قراءة الرطوبة ضمن النطاق الإرشادي.",
            "action": "استمري في متابعة التربة قبل كل عملية ري."
        })

    if light < data["light_min"]:
        recommendations.append({
            "title": "تحسين الإضاءة",
            "priority": "medium",
            "priority_text": "أولوية متوسطة",
            "description": "الإضاءة أقل من النطاق الإرشادي للنبات.",
            "action": "انقلي النبات إلى مكان أكثر إضاءة غير مباشرة."
        })

    elif light > data["light_max"]:
        recommendations.append({
            "title": "تقليل التعرض للضوء",
            "priority": "medium",
            "priority_text": "أولوية متوسطة",
            "description": "الإضاءة أعلى من النطاق الإرشادي.",
            "action": "أبعدي النبات عن أشعة الشمس المباشرة القوية."
        })

    else:
        recommendations.append({
            "title": "الإضاءة مناسبة",
            "priority": "low",
            "priority_text": "أولوية منخفضة",
            "description": "قراءة الإضاءة ضمن النطاق الإرشادي.",
            "action": "حافظي على مكان النبات وراقبي نموه."
        })

    if temperature < data["temp_min"]:
        recommendations.append({
            "title": "رفع درجة الحرارة",
            "priority": "medium",
            "priority_text": "أولوية متوسطة",
            "description": "درجة الحرارة أقل من النطاق الإرشادي.",
            "action": "ضعي النبات في مكان أكثر دفئاً بعيداً عن التيارات الباردة."
        })

    elif temperature > data["temp_max"]:
        recommendations.append({
            "title": "خفض درجة الحرارة",
            "priority": "high",
            "priority_text": "أولوية عالية",
            "description": "درجة الحرارة أعلى من النطاق الإرشادي.",
            "action": "أبعدي النبات عن مصادر الحرارة المباشرة."
        })

    else:
        recommendations.append({
            "title": "درجة الحرارة مناسبة",
            "priority": "low",
            "priority_text": "أولوية منخفضة",
            "description": "درجة الحرارة ضمن النطاق الإرشادي.",
            "action": "حافظي على درجة حرارة مستقرة."
        })

    high_count = sum(
        1 for item in recommendations
        if item["priority"] == "high"
    )

    medium_count = sum(
        1 for item in recommendations
        if item["priority"] == "medium"
    )

    score = max(0, 100 - high_count * 25 - medium_count * 10)

    return recommendations, score

# ==============================
# لوحة المعلومات
# ==============================

elif page == "لوحة المعلومات":

    st.title("📊 لوحة معلومات صحة النبات")

    if not st.session_state.get("analyzed", False):
        st.info("يرجى تحليل النبات أولاً من صفحة تحليل النبات.")
    else:

        plant = st.session_state["plant"]
        moisture = st.session_state["moisture"]
        light = st.session_state["light"]
        temperature = st.session_state["temperature"]

        recommendations, score = analyze_plant(
            plant, moisture, light, temperature
        )

        st.subheader(f"نتائج نبات {plant}")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">رطوبة التربة</div>
                <div class="metric-value">{moisture}%</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">الإضاءة</div>
                <div class="metric-value">{light}</div>
                <div class="metric-label">Lux</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">درجة الحرارة</div>
                <div class="metric-value">{temperature}°</div>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">مؤشر الحالة</div>
                <div class="metric-value">{score}%</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("ملخص حالة النبات")

        st.progress(score / 100)

        if score >= 80:
            st.success("حالة القراءات جيدة وفق النطاقات الإرشادية.")
        elif score >= 50:
            st.warning("النبات يحتاج إلى بعض التعديلات في العناية.")
        else:
            st.error("توجد قراءات تحتاج إلى متابعة.")

        st.caption(
            "مؤشر إرشادي مبني على القراءات المدخلة، وليس تشخيصاً طبياً أو قياساً من مستشعر فعلي."
        )

        st.markdown("---")
        st.subheader("القراءات الحالية")

        chart_data = pd.DataFrame({
            "القراءة": [moisture, light, temperature]
        }, index=["رطوبة التربة (%)", "الإضاءة (Lux)", "الحرارة (°C)"])

        st.bar_chart(chart_data)

# ==============================
# التوصيات
# ==============================

elif page == "التوصيات":

    st.title("💡 توصيات صحة النباتات")

    if not st.session_state.get("analyzed", False):

        st.info("حللي النبات أولاً حتى تظهر توصيات مبنية على قراءاته.")

    else:

        plant = st.session_state["plant"]
        moisture = st.session_state["moisture"]
        light = st.session_state["light"]
        temperature = st.session_state["temperature"]

        recommendations, score = analyze_plant(
            plant, moisture, light, temperature
        )

        st.write(f"التوصيات الخاصة بنبات: **{plant}**")

        for item in recommendations:

            st.markdown(f"""
            <div class="recommendation-card">

                <span class="priority {item['priority']}">
                    {item['priority_text']}
                </span>

                <h3>{item['title']}</h3>

                <p>{item['description']}</p>

                <div class="action-box">
                    <strong>الإجراء المقترح:</strong>
                    {item['action']}
                </div>

            </div>
            """, unsafe_allow_html=True)

# ==============================
# عن المشروع
# ==============================

elif page == "عن المشروع":

    st.title("🌱 عن مشروع PlantCare AI")

    st.markdown("""
    <div class="card">
        <h3>نبذة عن المشروع</h3>
        <p>
        PlantCare AI هو نظام يهدف إلى مساعدة المستخدمين
        في مراقبة صحة النباتات الداخلية وتقديم توصيات
        مناسبة لاحتياجات النبات.
        </p>
    </div>

    <div class="card">
        <h3>أهداف المشروع</h3>
        <p>
        • تسهيل متابعة النباتات الداخلية.<br>
        • المساعدة في تنظيم عملية الري.<br>
        • متابعة الإضاءة ودرجة الحرارة.<br>
        • تقديم توصيات لتحسين العناية بالنبات.<br>
        • توظيف التقنيات الذكية في خدمة الزراعة.
        </p>
    </div>

    <div class="card">
        <h3>التقنيات المستخدمة</h3>
        <p>
        Python – Streamlit – Pandas
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(
        "<h4 style='text-align:center;'>PlantCare AI 🌿</h4>",
        unsafe_allow_html=True
    )
