import streamlit as st

st.set_page_config(
    page_title="Symptom Awareness Chatbot",
    page_icon="🩺",
    layout="centered"
)

st.markdown("""
<style>
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# ---------------- PAGE SETUP ----------------

st.set_page_config(
    page_title="Symptom Awareness Chatbot",
    page_icon="🩺",
    layout="centered"
)

# ---------------- TITLE ----------------

st.title("🩺 Symptom Awareness Chatbot")


# ---------------- SYMPTOM INPUT ----------------

symptom = st.text_input(
    "Enter your symptom:",
    placeholder="Example: Cough, Fever, Headache"
)

# ---------------- PROCESS INPUT ----------------

if symptom:

    symptom = symptom.strip().lower()

    # ---------------- RUNNY NOSE ----------------

    if symptom == "runny nose":

        st.subheader("Possible conditions:")
        st.write("• Common cold")
        st.write("• Allergic rhinitis")
        st.write("• Flu")

        st.subheader("⚠️ Warning signs:")
        st.write("• Difficulty breathing")
        st.write("• Symptoms becoming much worse")

    # ---------------- COUGH ----------------

    elif symptom == "cough":

        st.subheader("Possible conditions:")
        st.write("• Common cold")
        st.write("• Flu")
        st.write("• Bronchitis")
        st.write("• Asthma")

        st.subheader("⚠️ Warning signs:")
        st.write("• Difficulty breathing")
        st.write("• Chest pain")
        st.write("• Blood in cough")

    # ---------------- FEVER ----------------

    elif symptom == "fever":

        st.subheader("Possible conditions:")
        st.write("• Viral infection")
        st.write("• Flu")
        st.write("• Dengue")
        st.write("• COVID-19")
        st.write("• Other infections")

        st.subheader("⚠️ Warning signs:")
        st.write("• Very high or persistent fever")
        st.write("• Confusion")
        st.write("• Difficulty breathing")

    # ---------------- HEADACHE ----------------

    elif symptom == "headache":

        st.subheader("Possible conditions:")
        st.write("• Tension headache")
        st.write("• Migraine")
        st.write("• Viral infection")
        st.write("• Dehydration")

        st.subheader("⚠️ Warning signs:")
        st.write("• Sudden severe headache")
        st.write("• Confusion")
        st.write("• Weakness")
        st.write("• Difficulty speaking")

    # ---------------- SORE THROAT ----------------

    elif symptom == "sore throat":

        st.subheader("Possible conditions:")
        st.write("• Common cold")
        st.write("• Flu")
        st.write("• Viral throat infection")
        st.write("• Bacterial throat infection")

        st.subheader("⚠️ Warning signs:")
        st.write("• Difficulty breathing")
        st.write("• Difficulty swallowing")
        st.write("• Severe swelling")

    # ---------------- FATIGUE ----------------

    elif symptom == "fatigue":

        st.subheader("Possible conditions:")
        st.write("• Lack of sleep")
        st.write("• Viral infection")
        st.write("• Anemia")
        st.write("• Nutritional deficiency")
        st.write("• Thyroid problems")

        st.subheader("⚠️ Warning signs:")
        st.write("• Severe weakness")
        st.write("• Fainting")
        st.write("• Fatigue continuing for a long time")

    # ---------------- NAUSEA ----------------

    elif symptom == "nausea":

        st.subheader("Possible conditions:")
        st.write("• Food poisoning")
        st.write("• Stomach infection")
        st.write("• Migraine")
        st.write("• Medication side effects")

        st.subheader("⚠️ Warning signs:")
        st.write("• Severe dehydration")
        st.write("• Blood in vomit")
        st.write("• Severe abdominal pain")

    # ---------------- VOMITING ----------------

    elif symptom == "vomiting":

        st.subheader("Possible conditions:")
        st.write("• Food poisoning")
        st.write("• Stomach infection")
        st.write("• Gastroenteritis")
        st.write("• Migraine")

        st.subheader("⚠️ Warning signs:")
        st.write("• Blood in vomit")
        st.write("• Severe dehydration")
        st.write("• Severe abdominal pain")

    # ---------------- DIARRHEA ----------------

    elif symptom == "diarrhea":

        st.subheader("Possible conditions:")
        st.write("• Gastroenteritis")
        st.write("• Food poisoning")
        st.write("• Bacterial infection")
        st.write("• Viral infection")

        st.subheader("⚠️ Warning signs:")
        st.write("• Blood in stool")
        st.write("• Severe dehydration")
        st.write("• Severe abdominal pain")

    # ---------------- STOMACH PAIN ----------------

    elif symptom == "stomach pain":

        st.subheader("Possible conditions:")
        st.write("• Indigestion")
        st.write("• Gas")
        st.write("• Gastritis")
        st.write("• Stomach infection")

        st.subheader("⚠️ Warning signs:")
        st.write("• Severe or sudden pain")
        st.write("• Blood in vomit or stool")
        st.write("• Fainting")

    # ---------------- CHEST PAIN ----------------

    elif symptom == "chest pain":

        st.subheader("Possible conditions:")
        st.write("• Muscle strain")
        st.write("• Acid reflux")
        st.write("• Respiratory conditions")
        st.write("• Heart-related conditions")

        st.error(
            "🚨 IMPORTANT: Severe or sudden chest pain, "
            "especially with difficulty breathing, sweating, "
            "fainting, or pain spreading to the arm/jaw "
            "requires urgent medical evaluation."
        )

    # ---------------- BACK PAIN ----------------

    elif symptom == "back pain":

        st.subheader("Possible conditions:")
        st.write("• Muscle strain")
        st.write("• Poor posture")
        st.write("• Muscle tension")
        st.write("• Spine-related problems")

        st.subheader("⚠️ Warning signs:")
        st.write("• Severe pain after an injury")
        st.write("• Weakness or numbness")
        st.write("• Loss of bladder or bowel control")

    # ---------------- DIZZINESS ----------------

    elif symptom == "dizziness":

        st.subheader("Possible conditions:")
        st.write("• Dehydration")
        st.write("• Low blood pressure")
        st.write("• Low blood sugar")
        st.write("• Inner ear problems")

        st.subheader("⚠️ Warning signs:")
        st.write("• Fainting")
        st.write("• Severe headache")
        st.write("• Difficulty speaking")
        st.write("• Weakness")

    # ---------------- BODY PAIN ----------------

    elif symptom == "body pain":

        st.subheader("Possible conditions:")
        st.write("• Flu")
        st.write("• Viral infection")
        st.write("• Muscle strain")
        st.write("• Physical overexertion")

        st.subheader("⚠️ Warning signs:")
        st.write("• Severe pain")
        st.write("• High or persistent fever")
        st.write("• Severe weakness")

    # ---------------- SNEEZING ----------------

    elif symptom == "sneezing":

        st.subheader("Possible conditions:")
        st.write("• Allergic rhinitis")
        st.write("• Common cold")
        st.write("• Environmental irritation")

        st.subheader("⚠️ Warning signs:")
        st.write("• Difficulty breathing")
        st.write("• Severe allergic reaction")

    # ---------------- CONGESTION ----------------

    elif symptom == "congestion":

        st.subheader("Possible conditions:")
        st.write("• Common cold")
        st.write("• Flu")
        st.write("• Allergies")
        st.write("• Sinus infection")

        st.subheader("⚠️ Warning signs:")
        st.write("• Difficulty breathing")
        st.write("• Severe facial pain")
        st.write("• Symptoms getting worse")

    # ---------------- SHORTNESS OF BREATH ----------------

    elif symptom == "shortness of breath":

        st.subheader("Possible conditions:")
        st.write("• Asthma")
        st.write("• Respiratory infection")
        st.write("• Allergic reaction")
        st.write("• Heart or lung conditions")

        st.error(
            "🚨 IMPORTANT: Severe or sudden difficulty "
            "breathing requires urgent medical evaluation."
        )

    # ---------------- JOINT PAIN ----------------

    elif symptom == "joint pain":

        st.subheader("Possible conditions:")
        st.write("• Muscle/joint strain")
        st.write("• Viral infection")
        st.write("• Arthritis")
        st.write("• Other inflammatory conditions")

        st.subheader("⚠️ Warning signs:")
        st.write("• Severe swelling")
        st.write("• Red or very hot joint")
        st.write("• Inability to move the joint")

    # ---------------- SKIN RASH ----------------

    elif symptom == "skin rash":

        st.subheader("Possible conditions:")
        st.write("• Allergy")
        st.write("• Skin irritation")
        st.write("• Viral infection")
        st.write("• Dermatitis")

        st.subheader("⚠️ Warning signs:")
        st.write("• Rapidly spreading rash")
        st.write("• Difficulty breathing")
        st.write("• Swelling of face or throat")

    # ---------------- EYE REDNESS ----------------

    elif symptom == "red eyes":

        st.subheader("Possible conditions:")
        st.write("• Eye irritation")
        st.write("• Allergies")
        st.write("• Conjunctivitis")
        st.write("• Dry eyes")

        st.subheader("⚠️ Warning signs:")
        st.write("• Severe eye pain")
        st.write("• Vision changes")
        st.write("• Injury to the eye")

    # ---------------- TOOTHACHE ----------------

    elif symptom == "toothache":

        st.subheader("Possible conditions:")
        st.write("• Dental cavity")
        st.write("• Gum infection")
        st.write("• Tooth damage")
        st.write("• Dental abscess")

        st.subheader("⚠️ Warning signs:")
        st.write("• Facial swelling")
        st.write("• Fever")
        st.write("• Difficulty swallowing")

    # ---------------- LOSS OF APPETITE ----------------

    elif symptom == "loss of appetite":

        st.subheader("Possible conditions:")
        st.write("• Viral infection")
        st.write("• Stress")
        st.write("• Stomach infection")
        st.write("• Medication side effects")

        st.subheader("⚠️ Warning signs:")
        st.write("• Significant unexplained weight loss")
        st.write("• Severe weakness")
        st.write("• Persistent loss of appetite")

    # ---------------- CHILLS ----------------

    elif symptom == "chills":

        st.subheader("Possible conditions:")
        st.write("• Fever")
        st.write("• Flu")
        st.write("• Viral infection")
        st.write("• Other infections")

        st.subheader("⚠️ Warning signs:")
        st.write("• Severe or persistent chills")
        st.write("• Confusion")
        st.write("• Difficulty breathing")

    # ---------------- UNKNOWN SYMPTOM ----------------

    else:

        st.warning(
            "❌ Sorry, I don't have information about this symptom."
        )

        st.write("Try symptoms such as:")
        st.write(
            "Runny nose, Cough, Fever, Headache, "
            "Sore throat, Fatigue, Nausea, etc."
        )
