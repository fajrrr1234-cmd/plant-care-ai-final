import streamlit as st
import requests
st.set_page_config(
    page_title="PlantCare AI",
    page_icon="🌱",
    layout="wide"
)
if "analysis" not in st.session_state:
    st.session_state.analysis = None

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

div[data-testid="stAlert"] {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)


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
        "light": (200, 1500),
        "temperature": (15, 30)
    },
    "زنبق السلام": {
        "moisture": (45, 70),
        "light": (300, 1000),
        "temperature": (18, 28)
    },
    "نبات العنكبوت": {
        "moisture": (30, 60),
        "light": (500, 1200),
        "temperature": (16, 27)
    }
}


# =========================
# تحليل قراءات المستشعرات
# =========================

def analyze_plant(plant, moisture, light, temperature):

    data = plant_data[plant]
    recommendations = []

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
        recommendations.append({
            "title": "الإضاءة مناسبة",
            "priority": "منخفضة",
            "description": "مستوى الإضاءة ضمن النطاق المناسب.",
            "action": "حافظي على مكان النبات الحالي."
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
        recommendations.append({
            "title": "درجة الحرارة مناسبة",
            "priority": "منخفضة",
            "description": "درجة الحرارة ضمن النطاق المناسب.",
            "action": "حافظي على درجة حرارة مستقرة."
        })

    # حساب مؤشر الحالة
    good_conditions = 0

    if data["moisture"][0] <= moisture <= data["moisture"][1]:
        good_conditions += 1

    if data["light"][0] <= light <= data["light"][1]:
        good_conditions += 1

    if data["temperature"][0] <= temperature <= data["temperature"][1]:
        good_conditions += 1

    score = round((good_conditions / 3) * 100)

    return recommendations, score


# =========================
# القائمة الجانبية
# =========================
def identify_plant(image_file):
    api_key = st.secrets["PLANTNET_API_KEY"]

    url = "https://my-api.plantnet.org/v2/identify/all"

    files = [
        ("images", (
            image_file.name,
            image_file.getvalue(),
            image_file.type or "image/jpeg"
        ))
    ]

    response = requests.post(
        url,
        params={"api-key": api_key},
        files=files,
        data={"organs": "auto"},
        timeout=60
    )

    response.raise_for_status()
    return response.json()
with st.sidebar:

    st.title("🌱 PlantCare AI")
    st.caption("Smart Plant Monitoring")

    st.markdown("---")

    page = st.radio(
        "القائمة الرئيسية",
        ["الرئيسية", "تحليل النباتات","مراقبة المستشعرات", "النتائج", "عن المشروع"]
    )


# تخزين آخر تحليل
if "analysis" not in st.session_state:
    st.session_state.analysis = None


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
        باستخدام مستشعرات الرطوبة والإضاءة ودرجة الحرارة،
        وتحليل القراءات لتقديم توصيات مناسبة للعناية بالنبات.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.subheader("🌿 خدمات النظام")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h2>💧</h2>
            <h3>مستشعر رطوبة التربة</h3>
            <p>متابعة مستوى الرطوبة وتحديد احتياج النبات للماء.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h2>☀️</h2>
            <h3>مستشعر الإضاءة</h3>
            <p>قياس شدة الإضاءة وتحديد مدى ملاءمتها للنبات.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h2>🌡️</h2>
            <h3>مستشعر الحرارة</h3>
            <p>متابعة درجة الحرارة المناسبة لنمو النبات.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.info("انتقلي إلى صفحة مراقبة المستشعرات لإدخال القراءات وتحليل حالة النبات.")


# =========================
# صفحة مراقبة المستشعرات
# =========================

elif page == "مراقبة المستشعرات":

    st.title("📡 مراقبة مستشعرات النبات")

    st.write(
        "اختاري نوع النبات وأدخلي قراءات المستشعرات لمراقبة حالته."
    )

    st.warning(
        "نموذج تجريبي: أدخلي القراءات يدويًا إلى حين توصيل المستشعرات الفعلية."
    )

    st.markdown("---")

  
st.markdown("---")
st.subheader("📷 التعرف على النبات بالصورة")

plant_image = st.file_uploader(
    "ارفعي صورة النبات للتعرف على نوعه",
    type=["jpg", "jpeg", "png"]
)

if plant_image is not None:
    st.image(plant_image, caption="صورة النبات", use_container_width=True)

    if st.button("🌱 تعرف على النبات"):
        try:
            with st.spinner("جاري التعرف على النبات..."):
                result = identify_plant(plant_image)

            results = result.get("results", [])

            if results:
                st.success("تم التعرف على النبات!")

                for item in results[:3]:
                    species = item.get("species", {})
                    name = species.get(
                        "scientificNameWithoutAuthor",
                        "اسم غير متوفر"
                    )
                    st.write("🌿", name)

                    common_names = species.get("commonNames", [])
                    if common_names:
                        st.write("الأسماء الشائعة:", "، ".join(common_names))

            else:
                st.warning("لم يتم التعرف على النبات، جربي صورة أوضح.")

        except Exception as e:
            st.error(f"حدث خطأ أثناء التحليل: {e}")
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

    plant = st.selectbox(
    "🌱 اختاري نوع النبات",
    list(plant_data.keys())
)
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

        st.info("لا توجد نتائج بعد. انتقلي إلى مراقبة المستشعرات وابدئي التحليل.")

    else:

        st.subheader("🌱 النبات المحدد: " + result["plant"])

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "💧 رطوبة التربة",
                str(result["moisture"]) + "%"
            )

        with col2:
            st.metric(
                "☀️ الإضاءة",
                str(result["light"]) + " Lux"
            )

        with col3:
            st.metric(
                "🌡️ درجة الحرارة",
                str(result["temperature"]) + "°C"
            )

        st.markdown("---")

        st.subheader("🌿 مؤشر حالة النبات")

        st.progress(result["score"] / 100)

        st.metric(
            "مؤشر توافق الظروف",
            str(result["score"]) + "%"
        )

        st.caption(
            "هذا المؤشر يوضح توافق القراءات الثلاث مع النطاقات المحددة للنبات، "
            "ولا يمثل قياسًا طبيًا أو مباشرًا لصحة النبات."
        )

        st.markdown("---")

        st.subheader("💡 توصيات العناية بالنبات")

        for item in result["recommendations"]:

            st.markdown(f"""
            <div class="card">
                <h3>{item['title']}</h3>
                <p><b>الأولوية:</b> {item['priority']}</p>
                <p>{item['description']}</p>
                <p><b>الإجراء المقترح:</b> {item['action']}</p>
            </div>
            """, unsafe_allow_html=True)


# =========================
# صفحة عن المشروع
# =========================

elif page == "عن المشروع":

    st.title("🌱 عن المشروع")

    st.markdown("""
    <div class="card">
        <h3>ما هو PlantCare AI؟</h3>
        <p>
        PlantCare AI هو نظام ذكي لمراقبة صحة النباتات الداخلية،
        يعتمد على قراءات مستشعرات رطوبة التربة وشدة الإضاءة
        ودرجة الحرارة، ثم يحلل هذه القراءات لتقديم توصيات
        تساعد على تحسين العناية بالنباتات.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🎯 أهداف المشروع")

    st.write("💧 مراقبة مستوى رطوبة التربة.")

    st.write("☀️ قياس شدة الإضاءة.")

    st.write("🌡️ متابعة درجة الحرارة.")

    st.write("📊 تحليل قراءات المستشعرات.")

    st.write("🌿 تقديم توصيات مناسبة للعناية بالنباتات.")

    st.markdown("---")

    st.caption("PlantCare AI | Smart Plant Monitoring")
