import streamlit as st
import requests
import base64

API_KEY = st.secrets["PLANT_ID_API_KEY"]
# =========================
# إعداد الصفحة
# =========================
st.set_page_config(
    page_title="PlantCare AI",
    page_icon="🌱",
    layout="wide"
)

if "analysis" not in st.session_state:
    st.session_state.analysis = None

# =========================
# بيانات النباتات
# =========================
plant_data = {
    "بوتس": {
        "moisture": (30, 60),
        "light": (500, 1500),
        "temperature": (18, 30)
    },
    "مونستيرا": {
        "moisture": (40, 65),
        "light": (800, 2000),
        "temperature": (18, 30)
    },
    "سانسيفيريا": {
        "moisture": (10, 35),
        "light": (300, 1500),
        "temperature": (15, 32)
    },
    "زنبق السلام": {
        "moisture": (45, 70),
        "light": (300, 1200),
        "temperature": (18, 28)
    },
    "نبات العنكبوت": {
        "moisture": (30, 60),
        "light": (500, 1500),
        "temperature": (15, 27)
    }
}

# =========================
# تحليل بيانات النبات
# =========================
def analyze_plant(plant, moisture, light, temperature):

    data = plant_data[plant]
    recommendations = []
    good_conditions = 0

    # تحليل رطوبة التربة
    if moisture < data["moisture"][0]:
        recommendations.append({
            "title": "انخفاض رطوبة التربة",
            "priority": "عالية",
            "description": "رطوبة التربة أقل من النطاق المناسب للنبات.",
            "action": "اسقي النبات بكمية مناسبة من الماء."
        })
    elif moisture > data["moisture"][1]:
        recommendations.append({
            "title": "ارتفاع رطوبة التربة",
            "priority": "عالية",
            "description": "رطوبة التربة أعلى من النطاق المناسب.",
            "action": "أوقفي الري مؤقتًا وتأكدي من تصريف الماء."
        })
    else:
        good_conditions += 1
        recommendations.append({
            "title": "رطوبة التربة مناسبة",
            "priority": "منخفضة",
            "description": "مستوى الرطوبة ضمن النطاق المناسب.",
            "action": "استمري في متابعة رطوبة التربة."
        })

    # تحليل الإضاءة
    if light < data["light"][0]:
        recommendations.append({
            "title": "الإضاءة منخفضة",
            "priority": "متوسطة",
            "description": "النبات لا يحصل على كمية الضوء المناسبة.",
            "action": "انقلي النبات إلى مكان أكثر إضاءة غير مباشرة."
        })
    elif light > data["light"][1]:
        recommendations.append({
            "title": "الإضاءة مرتفعة",
            "priority": "متوسطة",
            "description": "شدة الإضاءة أعلى من النطاق المناسب.",
            "action": "أبعدي النبات عن أشعة الشمس المباشرة."
        })
    else:
        good_conditions += 1
        recommendations.append({
            "title": "الإضاءة مناسبة",
            "priority": "منخفضة",
            "description": "مستوى الإضاءة ضمن النطاق المناسب.",
            "action": "حافظي على موقع النبات الحالي."
        })

    # تحليل درجة الحرارة
    if temperature < data["temperature"][0]:
        recommendations.append({
            "title": "درجة الحرارة منخفضة",
            "priority": "متوسطة",
            "description": "درجة الحرارة أقل من النطاق المناسب.",
            "action": "انقلي النبات إلى مكان أكثر دفئًا."
        })
    elif temperature > data["temperature"][1]:
        recommendations.append({
            "title": "درجة الحرارة مرتفعة",
            "priority": "متوسطة",
            "description": "درجة الحرارة أعلى من النطاق المناسب.",
            "action": "أبعدي النبات عن مصادر الحرارة."
        })
    else:
        good_conditions += 1
        recommendations.append({
            "title": "درجة الحرارة مناسبة",
            "priority": "منخفضة",
            "description": "درجة الحرارة ضمن النطاق المناسب.",
            "action": "حافظي على درجة حرارة مستقرة."
        })

    score = round((good_conditions / 3) * 100)

    return recommendations, score


# =========================
# تنسيق الواجهة
# =========================
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
    padding: 10px;
}

.card {
    background-color: #F5FAF2;
    border: 1px solid #B5D6A7;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 15px;
}

div[data-testid="stMetric"] {
    background-color: #F5FAF2;
    border: 1px solid #B5D6A7;
    border-radius: 15px;
    padding: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# القائمة الجانبية
# =========================
with st.sidebar:
    st.title("🌱 PlantCare AI")
    st.caption("Smart Plant Monitoring")
    st.markdown("---")

    page = st.radio(
        "القائمة الرئيسية",
        [
            "الرئيسية",
            "تحليل النباتات",
            "مراقبة المستشعرات",
            "النتائج",
            "عن المشروع"
        ]
    )


# =========================
# الصفحة الرئيسية
# =========================
if page == "الرئيسية":

    st.markdown("""
    <div class="card">
        <h1 style="text-align:center;">🌱 PlantCare AI</h1>
        <h3 style="text-align:center;">اعتنِ بنباتك بذكاء</h3>
        <p style="text-align:center;">
        نظام ذكي لمراقبة صحة النباتات الداخلية
        وتحليل احتياجاتها وتقديم توصيات مناسبة للعناية بها.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🌿 خدمات النظام")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h2>📷</h2>
        <h3>التعرف على النباتات</h3>
        <p>التعرف على نوع النبات باستخدام صورته.</p>
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
        <h3>مراقبة البيئة</h3>
        <p>متابعة الإضاءة ودرجة الحرارة.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info("ابدئي من صفحة تحليل النباتات أو مراقبة المستشعرات.")


# =========================
# صفحة تحليل النباتات
# =========================
elif page == "تحليل النباتات":

    st.title("📷 التعرف على النباتات")
    st.write("ارفعي صورة النبات لمحاولة التعرف على نوعه.")

    plant_image = st.file_uploader(
        "اختاري صورة النبات",
        type=["jpg", "jpeg", "png"]
    )

    if plant_image:
        st.image(
            plant_image,
            caption="صورة النبات",
            use_container_width=True
        )

        api_key = st.text_input(
            "مفتاح Plant.id API",
            type="password",
            help="يلزم مفتاح من خدمة Plant.id لتفعيل التعرف الآلي."
        )

        if st.button("🌱 تعرف على النبات", use_container_width=True):

            if not api_key:
                st.warning("أدخلي مفتاح API أولًا لتفعيل التعرف الآلي.")
            else:
                try:
                    image_bytes = plant_image.getvalue()
                    encoded_image = base64.b64encode(
                        image_bytes
                    ).decode("utf-8")

                    response = requests.post(
                        "https://api.plant.id/v3/identification",
                        headers={
                            "Api-Key": api_key,
                            "Content-Type": "application/json"
                        },
                        json={
                            "images": [encoded_image],
                            "similar_images": False
                        },
                        timeout=60
                    )

                    response.raise_for_status()
                    result = response.json()

                    suggestions = result.get(
                        "result", {}
                    ).get("classification", {}).get(
                        "suggestions", []
                    )

                    if suggestions:
                        st.success("تم التعرف على النبات!")

                        for item in suggestions[:3]:
                            st.write(
                                "🌿",
                                item.get("name", "اسم غير معروف"),
                                "- نسبة الثقة:",
                                round(item.get("probability", 0) * 100, 1),
                                "%"
                            )
                    else:
                        st.warning("لم يتم التعرف على النبات. جربي صورة أوضح.")

                except Exception as e:
                    st.error("تعذر إكمال التعرف على الصورة.")
                    st.caption(str(e))


# =========================
# صفحة مراقبة المستشعرات
# =========================
elif page == "مراقبة المستشعرات":

    st.title("🌡️ مراقبة مستشعرات النبات")

    st.info(
        "نموذج تجريبي: أدخلي القراءات يدويًا "
        "إلى حين توصيل المستشعرات الفعلية."
    )

    plant = st.selectbox(
        "🌱 اختاري نوع النبات",
        list(plant_data.keys())
    )

    st.subheader("💧 مستشعر رطوبة التربة")

    moisture = st.slider(
        "رطوبة التربة (%)",
        min_value=0,
        max_value=100,
        value=45
    )

    st.subheader("☀️ مستشعر شدة الإضاءة")

    light = st.slider(
        "شدة الإضاءة (Lux)",
        min_value=0,
        max_value=3000,
        value=1000
    )

    st.subheader("🌡️ مستشعر درجة الحرارة")

    temperature = st.slider(
        "درجة الحرارة (°C)",
        min_value=0,
        max_value=45,
        value=24
    )

    st.markdown("---")

    if st.button("🔍 تحليل قراءات المستشعرات", use_container_width=True):

        recommendations, score = analyze_plant(
            plant,
            moisture,
            light,
            temperature
        )

        st.session_state.analysis = {
            "plant": plant,
            "moisture": moisture,
            "light": light,
            "temperature": temperature,
            "recommendations": recommendations,
            "score": score
        }

        st.success("تم تحليل القراءات بنجاح!")
        st.info("انتقلي إلى صفحة النتائج لمشاهدة التقرير والتوصيات.")


# =========================
# صفحة النتائج
# =========================
elif page == "النتائج":

    st.title("📊 نتائج تحليل النبات")

    result = st.session_state.analysis

    if result is None:

        st.info(
            "لا توجد نتائج حتى الآن. "
            "انتقلي إلى مراقبة المستشعرات وابدئي التحليل."
        )

    else:

        st.subheader("🌱 النبات المحدد: " + result["plant"])

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("💧 رطوبة التربة", f'{result["moisture"]}%')

        with col2:
            st.metric("☀️ شدة الإضاءة", f'{result["light"]} Lux')

        with col3:
            st.metric("🌡️ درجة الحرارة", f'{result["temperature"]} °C')

        st.markdown("---")

        st.subheader("💚 مؤشر صحة النبات")

        st.progress(result["score"] / 100)
        st.metric("نسبة الظروف المناسبة", f'{result["score"]}%')

        if result["score"] == 100:
            st.success("جميع القراءات ضمن النطاق المناسب.")
        elif result["score"] >= 66:
            st.warning("النبات بحالة جيدة نسبيًا، لكن توجد أمور تحتاج إلى متابعة.")
        else:
            st.error("توجد عدة قراءات تحتاج إلى تعديل.")

        st.markdown("---")

        st.subheader("💡 توصيات العناية بالنبات")

        for item in result["recommendations"]:

            with st.container(border=True):

                st.subheader("🌿 " + item["title"])

                st.write("**الأولوية:** " + item["priority"])

                st.write(item["description"])

                st.success("الإجراء المقترح: " + item["action"])


# =========================
# صفحة عن المشروع
# =========================
elif page == "عن المشروع":

    st.title("🌱 عن المشروع")

    st.markdown("""
    <div class="card">
        <h3>PlantCare AI</h3>
        <p>
        نظام ذكي يهدف إلى مساعدة المستخدمين على
        العناية بالنباتات الداخلية من خلال التعرف على النباتات
        ومراقبة الظروف البيئية المحيطة بها.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🎯 أهداف المشروع")

    st.write("🌱 التعرف على أنواع النباتات من الصور.")
    st.write("💧 متابعة مستوى رطوبة التربة.")
    st.write("☀️ مراقبة شدة الإضاءة.")
    st.write("🌡️ متابعة درجة الحرارة.")
    st.write("💡 تقديم توصيات مناسبة للعناية بالنباتات.")

    st.subheader("⚙️ آلية عمل النظام")

    st.write("""
    1. اختيار النبات أو رفع صورته.
    2. إدخال قراءات الظروف البيئية.
    3. تحليل القراءات ومقارنتها بالنطاق المناسب.
    4. حساب مؤشر حالة النبات.
    5. عرض التوصيات والإجراءات المقترحة.
    """)
