import streamlit as st

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="Environment Quiz App",
    page_icon="🌍",
    layout="centered"
)

# ---------------------------------------------------
# CUSTOM GREEN THEME
# ---------------------------------------------------

st.markdown("""
    <style>
    .stApp {
        background-color: #e8f5e9;
    }

    h1 {
        color: #1b5e20;
        text-align: center;
    }

    .stButton>button {
        background-color: #43a047;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
    }

    .result-box {
        background-color: #c8e6c9;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 24px;
        color: #1b5e20;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

# ---------------------------------------------------
# QUIZ QUESTIONS
# ---------------------------------------------------

questions = [
    {
        "question": "1. Which gas causes global warming?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "2. Which is a renewable source of energy?",
        "options": ["Coal", "Petrol", "Solar Energy"],
        "answer": "Solar Energy"
    },
    {
        "question": "3. What do plants absorb from air?",
        "options": ["Carbon Dioxide", "Helium", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "4. Which method helps save water?",
        "options": ["Keeping tap open", "Rainwater Harvesting", "Wasting water"],
        "answer": "Rainwater Harvesting"
    },
    {
        "question": "5. Which dustbin is for biodegradable waste?",
        "options": ["Green", "Red", "Blue"],
        "answer": "Green"
    },
    {
        "question": "6. Which layer protects Earth from UV rays?",
        "options": ["Ozone Layer", "Cloud Layer", "Water Layer"],
        "answer": "Ozone Layer"
    },
    {
        "question": "7. What should we reduce to protect environment?",
        "options": ["Plastic Usage", "Tree Plantation", "Recycling"],
        "answer": "Plastic Usage"
    },
    {
        "question": "8. Which process converts waste into reusable material?",
        "options": ["Burning", "Recycling", "Dumping"],
        "answer": "Recycling"
    },
    {
        "question": "9. Which is called the lungs of Earth?",
        "options": ["Amazon Forest", "Sahara Desert", "Pacific Ocean"],
        "answer": "Amazon Forest"
    },
    {
        "question": "10. What can we plant to save environment?",
        "options": ["Plastic", "Trees", "Chemicals"],
        "answer": "Trees"
    }
]

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("🌍 Environment Quiz App")

# ---------------------------------------------------
# START PAGE
# ---------------------------------------------------

if not st.session_state.quiz_started:

    name = st.text_input("Enter Your Name")

    if st.button("Start Quiz"):

        if name.strip() == "":
            st.warning("Please enter your name.")
        else:
            st.session_state.quiz_started = True
            st.session_state.name = name

# ---------------------------------------------------
# QUIZ PAGE
# ---------------------------------------------------

if st.session_state.quiz_started:

    st.success(
        f"Welcome {st.session_state.name}! 🌱 Let's start the quiz."
    )

    user_answers = []

    # Form prevents rerun issue
    with st.form("quiz_form"):

        for i, q in enumerate(questions):

            answer = st.radio(
                q["question"],
                q["options"],
                key=i
            )

            user_answers.append(answer)

        submit = st.form_submit_button("Submit Quiz")

    # ---------------------------------------------------
    # RESULT SECTION
    # ---------------------------------------------------

    if submit:

        score = 0

        for i in range(len(questions)):

            if user_answers[i] == questions[i]["answer"]:
                score += 10

        st.markdown(f"""
            <div class="result-box">
                🎯 {st.session_state.name}, Your Score is: {score}/100
            </div>
        """, unsafe_allow_html=True)

        # Result Messages
        if score == 100:
            st.balloons()
            st.success("🎉 Congratulations. You grabbed all the points")

        elif 71 <= score <= 99:
            st.balloons()
            st.success("🌟 Super. You almost nailed it")

        elif 50 <= score <= 70:
            st.info("👍 Well tried. Aim for the maximum next time")

        elif 1 <= score <= 49:
            st.warning("🙂 Its ok. Try better next time")

        else:
            st.error("😅 Better luck next time!")