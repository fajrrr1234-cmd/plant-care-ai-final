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

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background-color: #E5F1DF;
}

h1, h2, h3, h4, p, label,
.stMarkdown, .stText {
    color: #174B32 !important;
}

section[data-testid="stSidebar"] {
    background-color: #B5D6A7;
}

section[data-testid="stSidebar"] * {
    color: #174B32 !important;
}

.stButton button {
    background-color: #174B32;
    color: white !important;
    border-radius: 12px;
    border: none;
    padding: 10px 20px;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

div[data-testid="stMetric"] {
    background-color: #F5FAF2;
    border: 1px solid #B5D6A7;
    border-radius: 15px;
    padding: 18px;
}

.card {
    background-color: #F5FAF2;
    border: 1px solid #B5D6A7;
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 15px;
    text-align: right;
}

</style>
""", unsafe_allow_html=True)


# =====================================
# بيانات النباتات
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
        "moisture_min": 40,
        "moisture_max": 70,
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
        "moisture_max": 75,
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
# تحليل حالة النبات
# =====================================

def analyze_plant(plant, moisture, light, temperature):

    data = plant_data[plant]
    recommendations = []

    score = 100

    # تحليل رطوبة التربة
    if moisture < data["moisture_min"]:
        recommendations.append({
            "title": "تحسين عملية الري",
            "priority": "عالية",
            "description": "مستوى رطوبة التربة أقل من النطاق الإرشادي.",
            "action": "تحققي من جفاف التربة واسقي النبات عند الحاجة."
        })
        score -= 25

    elif moisture > data["moisture_max"]:
        recommendations.append({
            "title": "تقليل الري",
            "priority": "عالية",
            "description": "رطوبة التربة أعلى من النطاق الإرشادي.",
            "action": "قللي الري وتأكدي من وجود تصريف جيد للماء."
        })
        score -= 25

    else:
        recommendations.append({
            "title": "رطوبة التربة مناسبة",
            "priority": "منخفضة",
            "description": "رطوبة التربة ضمن النطاق الإرشادي.",
            "action": "استمري في متابعة رطوبة التربة."
        })

    # تحليل الإضاءة
    if light < data["light_min"]:
        recommendations.append({
            "title": "زيادة الإضاءة",
            "priority": "متوسطة",
            "description": "مستوى الإضاءة أقل من احتياج النبات.",
            "action": "ضعي النبات في مكان تصله إضاءة مناسبة."
        })
        score -= 25

    elif light > data["light_max"]:
        recommendations.append({
            "title": "تقليل الإضاءة",
            "priority": "متوسطة",
            "description": "مستوى الإضاءة أعلى من النطاق الإرشادي.",
            "action": "أبعدي النبات عن أشعة الشمس المباشرة."
        })
        score -= 25

    else:
        recommendations.append({
            "title": "الإضاءة مناسبة",
            "priority": "منخفضة",
            "description": "مستوى الإضاءة ضمن النطاق الإرشادي.",
            "action": "استمري في توفير الإضاءة المناسبة."
        })

    # تحليل درجة الحرارة
    if temperature < data["temp_min"]:
        recommendations.append({
            "title": "رفع درجة الحرارة",
            "priority": "متوسطة",
            "description": "درجة الحرارة أقل من النطاق الإرشادي.",
            "action": "انقلي النبات إلى مكان أكثر دفئًا."
        })
        score -= 25

    elif temperature > data["temp_max"]:
        recommendations.append({
            "title": "خفض درجة الحرارة",
            "priority": "متوسطة",
            "description": "درجة الحرارة أعلى من النطاق الإرشادي.",
            "action": "أبعدي النبات عن مصادر الحرارة."
        })
        score -= 25

    else:
        recommendations.append({
            "title": "درجة الحرارة مناسبة",
            "priority": "منخفضة",
            "description": "درجة الحرارة ضمن النطاق الإرشادي.",
            "action": "حافظي على درجة حرارة مستقرة."
        })

    score = max(0, score)

    return recommendations, score


# =====================================
# القائمة الجانبية
# =====================================

with st.sidebar:

    st.title("🌱 PlantCare AI")
    st.caption("نظام ذكي لمراقبة صحة النباتات الداخلية")

    st.markdown("---")

    page = st.radio(
        "القائمة الرئيسية",
        [
            "الرئيسية",
            "تحليل النباتات",
            "لوحة المعلومات",
            "التوصيات",
            "عن المشروع"
        ]
    )


# =====================================
# الصفحة الرئيسية
# =====================================

if page == "الرئيسية":

    st.markdown("""
    <div class="card">
        <h1>🌱 PlantCare AI</h1>
        <h3>اعتنِ بنباتك بذكاء</h3>
        <p>
        نظام ذكي يساعدك على متابعة احتياجات النباتات الداخلية
        من الماء والإضاءة ودرجة الحرارة،
        ويقدم توصيات مناسبة للعناية بها.
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
            <h3>تحليل النباتات</h3>
            <p>اختيار النبات وتحليل ظروف العناية به.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h2>💧</h2>
            <h3>مراقبة الرطوبة</h3>
            <p>متابعة مستوى رطوبة التربة.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h2>☀️</h2>
            <h3>مراقبة الإضاءة</h3>
            <p>متابعة مستوى الإضاءة ودرجة الحرارة.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.info("انتقلي إلى صفحة تحليل النباتات لبدء التحليل.")


# =====================================
# صفحة تحليل النباتات
# =====================================

elif page == "تحليل النباتات":

    st.title("🌿 تحليل النباتات")

    st.write("اختاري نوع النبات وأدخلي القراءات لمتابعة حالته.")

    selected_plant = st.selectbox(
        "اختاري نوع النبات",
        list(plant_data.keys())
    )

    st.markdown("---")

    st.subheader("📊 بيانات النبات")

    col1, col2 = st.columns(2)

    with col1:

        moisture = st.slider(
            "💧 رطوبة التربة (%)",
            min_value=0,
            max_value=100,
            value=45
        )

        light = st.slider(
            "☀️ مستوى الإضاءة (Lux)",
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

    st.caption(
        "ملاحظة: أدخلي القراءات يدويًا. القيم هنا ليست قراءات مستشعرات فعلية."
    )

    st.markdown("---")

    if st.button("🌱 ابدأ تحليل النبات"):

        recommendations, score = analyze_plant(
            selected_plant,
            moisture,
            light,
            temperature
        )

        st.session_state["plant"] = selected_plant
        st.session_state["moisture"] = moisture
        st.session_state["light"] = light
        st.session_state["temperature"] = temperature
        st.session_state["recommendations"] = recommendations
        st.session_state["score"] = score
        st.session_state["analyzed"] = True

        st.success("تم تحليل البيانات بنجاح!")
        st.info("انتقلي إلى لوحة المعلومات لمشاهدة النتائج.")


# =====================================
# لوحة المعلومات
# =====================================

elif page == "لوحة المعلومات":

    st.title("📊 لوحة معلومات صحة النبات")

    if not st.session_state.get("analyzed", False):

        st.info("يرجى تحليل النبات أولًا من صفحة تحليل النباتات.")

    else:

        st.subheader(
            "نتائج نبات " + st.session_state["plant"]
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "رطوبة التربة",
                str(st.session_state["moisture"]) + "%"
            )

            st.metric(
                "الإضاءة",
                str(st.session_state["light"]) + " Lux"
            )

        with col2:
            st.metric(
                "درجة الحرارة",
                str(st.session_state["temperature"]) + "°C"
            )

            st.metric(
                "مؤشر الحالة",
                str(st.session_state["score"]) + "%"
            )

        st.progress(
            st.session_state["score"] / 100
        )

        if st.session_state["score"] >= 75:
            st.success("حالة النبات جيدة وفقًا للقراءات المدخلة.")

        elif st.session_state["score"] >= 50:
            st.warning("يحتاج النبات إلى بعض التحسينات.")

        else:
            st.error("النبات يحتاج إلى عناية ومتابعة.")


# =====================================
# صفحة التوصيات
# =====================================

elif page == "التوصيات":

    st.title("💡 توصيات العناية بالنباتات")

    if not st.session_state.get("analyzed", False):

        st.info("يرجى تحليل النبات أولًا لعرض التوصيات.")

    else:

        recommendations = st.session_state["recommendations"]

        for item in recommendations:

            with st.container(border=True):

                st.subheader(item["title"])

                st.caption(
                    "الأولوية: " + item["priority"]
                )

                st.write(item["description"])

                st.markdown(
                    "**الإجراء المقترح:** " + item["action"]
                )


# =====================================
# صفحة عن المشروع
# =====================================

elif page == "عن المشروع":

    st.title("🌱 عن المشروع")

    st.markdown("""
    <div class="card">
        <h3>ما هو PlantCare AI؟</h3>
        <p>
        PlantCare AI هو نظام ذكي يهدف إلى مساعدة أصحاب
        النباتات الداخلية على متابعة احتياجات نباتاتهم
        وتقديم إرشادات مناسبة للعناية بها.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🎯 أهداف المشروع")

    st.write("🌱 التعرف على أنواع النباتات.")
    st.write("💧 متابعة احتياجات النباتات من الماء.")
    st.write("☀️ متابعة احتياجات النباتات من الإضاءة.")
    st.write("🌡️ متابعة درجة الحرارة.")
    st.write("💡 تقديم توصيات مناسبة للعناية بالنباتات.")

    st.subheader("⚙️ آلية عمل النظام")

    st.write("""
    1. اختيار نوع النبات.
    2. إدخال بيانات الرطوبة والإضاءة والحرارة.
    3. تحليل البيانات ومقارنتها بالنطاقات الإرشادية.
    4. عرض حالة النبات والتوصيات المناسبة.
    """)
