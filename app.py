import streamlit as st

# =====================================
# إعداد الصفحة
# =====================================

st.set_page_config(
    page_title="PlantCare AI",
    page_icon="🌱",
    layout="wide"
)

# =====================================
# تنسيق الواجهة
# =====================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
}

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background-color: #E5F1DF;
}

h1, h2, h3, h4, p, label {
    color: #174B32 !important;
}

.stMarkdown {
    color: #174B32;
}

/* المربعات */
.card {
    background-color: #F5FAF2;
    border: 1px solid #B5D6A7;
    border-radius: 15px;
    padding: 22px;
    margin-bottom: 15px;
    text-align: right;
    min-height: 150px;
}

.card h1, .card h2, .card h3 {
    color: #174B32 !important;
}

.card p {
    color: #42634D !important;
    line-height: 1.9;
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
    font-family: 'Cairo', sans-serif;
    font-weight: bold;
    min-height: 42px;
}

.stButton button:hover {
    background-color: #286644;
}

/* التنبيهات */
div[data-testid="stAlert"] {
    border-radius: 15px;
    padding: 15px;
}

/* بطاقات النتائج */
.metric-card {
    background-color: #F5FAF2;
    border: 1px solid #B5D6A7;
    border-radius: 15px;
    padding: 18px;
    text-align: center;
    margin-bottom: 12px;
}

.metric-value {
    color: #174B32;
    font-size: 25px;
    font-weight: bold;
}

.metric-label {
    color: #55745D;
    font-size: 14px;
}

/* بطاقات التوصيات */
.recommendation-card {
    background: #FFFFFF;
    border-radius: 15px;
    padding: 18px;
    margin-bottom: 15px;
    border-right: 5px solid #5B9B64;
}

.recommendation-card h3 {
    color: #24543A !important;
}

.recommendation-card p {
    color: #555 !important;
    line-height: 1.8;
}

.priority {
    display: inline-block;
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: bold;
    margin-bottom: 8px;
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

/* تحسين عرض البطاقات على الجوال */
@media (max-width: 768px) {
    .card {
        padding: 15px;
        min-height: auto;
    }

    .metric-value {
        font-size: 20px;
    }
}
</style>
""", unsafe_allow_html=True)


# =====================================
# بيانات النباتات
# القيم إرشادية للمحاكاة
# =====================================

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


# =====================================
# دالة تحليل القراءات
# =====================================

def analyze_plant(plant, moisture, light, temperature):

    data = plant_data[plant]
    recommendations = []

    # تحليل رطوبة التربة
    if moisture < data["moisture_min"]:
        recommendations.append({
            "title": "انخفاض رطوبة التربة",
            "priority": "high",
            "priority_text": "أولوية عالية",
            "description": "رطوبة التربة أقل من النطاق الإرشادي للنبات.",
            "action": "افحصي التربة واسقي النبات عند الحاجة."
        })

    elif moisture > data["moisture_max"]:
        recommendations.append({
            "title": "ارتفاع رطوبة التربة",
            "priority": "high",
            "priority_text": "أولوية عالية",
            "description": "رطوبة التربة أعلى من النطاق الإرشادي.",
            "action": "قللي الري وتأكدي من وجود تصريف جيد للماء."
        })

    else:
        recommendations.append({
            "title": "رطوبة التربة مناسبة",
            "priority": "low",
            "priority_text": "أولوية منخفضة",
            "description": "قراءة الرطوبة ضمن النطاق الإرشادي.",
            "action": "استمري في متابعة رطوبة التربة."
        })

    # تحليل الإضاءة
    if light < data["light_min"]:
        recommendations.append({
            "title": "انخفاض الإضاءة",
            "priority": "medium",
            "priority_text": "أولوية متوسطة",
            "description": "مستوى الإضاءة أقل من احتياج النبات الإرشادي.",
            "action": "ضعي النبات في مكان أكثر إضاءة مناسبة."
        })

    elif light > data["light_max"]:
        recommendations.append({
            "title": "ارتفاع الإضاءة",
            "priority": "medium",
            "priority_text": "أولوية متوسطة",
            "description": "مستوى الإضاءة أعلى من النطاق الإرشادي.",
            "action": "أبعدي النبات عن أشعة الشمس المباشرة القوية."
        })

    else:
        recommendations.append({
            "title": "الإضاءة مناسبة",
            "priority": "low",
            "priority_text": "أولوية منخفضة",
            "description": "مستوى الإضاءة ضمن النطاق الإرشادي.",
            "action": "حافظي على مكان النبات الحالي."
        })

    # تحليل درجة الحرارة
    if temperature < data["temp_min"]:
        recommendations.append({
            "title": "انخفاض درجة الحرارة",
            "priority": "medium",
            "priority_text": "أولوية متوسطة",
            "description": "درجة الحرارة أقل من النطاق الإرشادي.",
            "action": "انقلي النبات إلى مكان أكثر دفئاً."
        })

    elif temperature > data["temp_max"]:
        recommendations.append({
            "title": "ارتفاع درجة الحرارة",
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


# =====================================
# القائمة الجانبية
# =====================================

with st.sidebar:
    st.title("🌱 PlantCare AI")
    st.caption("Smart Plant Monitoring")
    st.markdown("---")

    page = st.radio(
        "القائمة",
        [
            "الرئيسية",
            "تحليل النباتات",
            "النتائج",
            "عن المشروع"
        ]
    )

    st.markdown("---")
    st.caption("اعتنِ بنباتك بذكاء 🌿")


# =====================================
# الصفحة الرئيسية
# =====================================

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
            <p>إمكانية رفع صورة النبات لمراجعتها.</p>
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
            <p>متابعة احتياجات النبات من الضوء.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.subheader("ابدئي رحلة العناية بنباتك")

    if st.button("🌿 ابدأ الآن"):
        st.info("انتقلي إلى صفحة تحليل النباتات من القائمة الجانبية.")


# =====================================
# صفحة تحليل النباتات
# =====================================

elif page == "تحليل النباتات":

    st.title("🌿 تحليل النباتات")
    st.subheader("ارفعي صورة نباتك أو التقطي صورة بالكاميرا")

    st.write("يمكنك اختيار صورة من جهازك أو استخدام الكاميرا.")

    uploaded_image = st.file_uploader(
        "📁 اختاري صورة النبات",
        type=["jpg", "jpeg", "png"]
    )

    camera_image = st.camera_input("📷 التقطي صورة للنبات")

    image = camera_image if camera_image is not None else uploaded_image

    if image is not None:
        st.image(
            image,
            caption="صورة النبات",
            use_container_width=True
        )

        st.success("تم رفع الصورة بنجاح.")

        st.info(
            "الصورة متاحة للعرض، والتعرف الآلي على نوع النبات "
            "يحتاج إلى ربط نموذج ذكاء اصطناعي."
        )

    st.markdown("---")

    st.subheader("بيانات النبات")

    selected_plant = st.selectbox(
        "اختاري نوع النبات",
        list(plant_data.keys())
    )

    st.subheader("محاكاة قراءات المستشعرات")

    st.caption(
        "أدخلي القراءات يدويًا لتجربة النظام. "
        "هذه القيم ليست قراءات من مستشعرات فعلية."
    )

    col1, col2 = st.columns(2)

    with col1:
        moisture = st.slider(
            "💧 رطوبة التربة (%)",
            min_value=0,
            max_value=100,
            value=45
        )

        light = st.slider(
            "☀️ شدة الإضاءة (Lux)",
            min_value=0,
            max_value=5000,
            value=1000
        )

    with col2:
        temperature = st.slider(
            "🌡️ درجة الحرارة (°C)",
            min_value=0,
            max_value=50,
            value=24
        )

    if st.button("🌱 ابدأ تحليل النبات"):

        st.session_state["plant"] = selected_plant
        st.session_state["moisture"] = moisture
        st.session_state["light"] = light
        st.session_state["temperature"] = temperature
        st.session_state["analyzed"] = True

        st.success("تم تحليل القراءات بنجاح!")

        st.info("انتقلي إلى صفحة النتائج لمشاهدة حالة النبات والتوصيات.")


# =====================================
# صفحة النتائج
# =====================================

elif page == "النتائج":

    st.title("📊 نتائج التحليل")

    if not st.session_state.get("analyzed", False):

        st.info("يرجى تحليل النبات أولاً من صفحة تحليل النباتات.")

    else:

        plant = st.session_state["plant"]
        moisture = st.session_state["moisture"]
        light = st.session_state["light"]
        temperature = st.session_state["temperature"]

        recommendations, score = analyze_plant(
            plant,
            moisture,
            light,
            temperature
        )

        st.subheader(f"نتائج نبات {plant}")

        col1, col2, col3 = st.columns(3)

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
                <div class="metric-value">{temperature}°C</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        st.subheader("🌿 مؤشر حالة النبات")

        st.progress(score / 100)

        st.markdown(
            f"<h2 style='text-align:center;'>{score}%</h2>",
            unsafe_allow_html=True
        )

        if score >= 80:
            st.success("حالة القراءات جيدة وفق النطاقات الإرشادية.")

        elif score >= 50:
            st.warning("النبات يحتاج إلى بعض التعديلات في العناية.")

        else:
            st.error("توجد قراءات تحتاج إلى متابعة.")

        st.caption(
            "هذا المؤشر تقديري مبني على القراءات المدخلة "
            "والنطاقات الإرشادية، وليس تشخيصًا فعليًا لصحة النبات."
        )

        st.markdown("---")

        st.subheader("💡 توصيات العناية بالنبات")

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


# =====================================
# صفحة عن المشروع
# =====================================

elif page == "عن المشروع":

    st.title("🌱 عن المشروع")

    st.markdown("""
    <div class="card">
        <h3>نبذة عن المشروع</h3>
        <p>
        PlantCare AI هو نظام ذكي يهدف إلى مساعدة أصحاب
        النباتات الداخلية على متابعة احتياجات نباتاتهم
        وتقديم إرشادات تساعدهم على العناية بها.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("أهداف المشروع")

    st.markdown("""
    <div class="card">
        <p>
        🌱 التعرف على أنواع النباتات.<br>
        💧 متابعة احتياجات النباتات من الماء.<br>
        ☀️ متابعة احتياجات النباتات من الإضاءة.<br>
        🌡️ متابعة درجة الحرارة.<br>
        💡 تقديم توصيات مناسبة للعناية بالنباتات.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("التقنيات المستخدمة")

    st.markdown("""
    <div class="card">
        <p>
        Python<br>
        Streamlit<br>
        محاكاة قراءات المستشعرات
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown(
        "<h4 style='text-align:center;'>PlantCare AI 🌿</h4>",
        unsafe_allow_html=True
    )
