import streamlit as st

# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Student Hub",
    page_icon="📚",
    layout="wide"
)

# =========================================================
# CUSTOM CSS (ENHANCED DESIGN)
# =========================================================

st.markdown("""
<style>

/* Main Typography */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-top: 10px;
}

.subtitle {
    text-align: center;
    color: #6B7280;
    font-size: 16px;
    margin-bottom: 30px;
}

/* Custom Cards */
.box {
    padding: 24px;
    border-radius: 16px;
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    margin-bottom: 20px;
}

/* Clickable Calculator Display */
.calc-display {
    background-color: #1F2937;
    color: #10B981;
    font-family: 'Courier New', Courier, monospace;
    font-size: 36px;
    font-weight: 700;
    text-align: right;
    padding: 16px 24px;
    border-radius: 12px;
    margin-bottom: 16px;
    border: 2px solid #374151;
    word-wrap: break-word;
    min-height: 75px;
}

/* GPA Container Card */
.gpa-card {
    padding: 30px;
    border-radius: 20px;
    background: linear-gradient(135deg, #4F46E5 0%, #6366F1 100%);
    color: #FFFFFF;
    text-align: center;
    box-shadow: 0 10px 25px -5px rgba(79, 70, 229, 0.4);
    margin-top: 30px;
}

.gpa-label {
    font-size: 16px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    opacity: 0.9;
    font-weight: 600;
}

.gpa-val {
    font-size: 64px;
    font-weight: 900;
    line-height: 1.1;
    margin: 10px 0;
}

.gpa-scale {
    font-size: 14px;
    opacity: 0.8;
}

/* Subject Score Row */
.subject-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 20px;
    background-color: #F9FAFB;
    border-radius: 12px;
    border: 1px solid #F3F4F6;
    margin-bottom: 12px;
}

/* Grade Badges */
.badge {
    padding: 4px 12px;
    border-radius: 9999px;
    font-weight: 700;
    font-size: 14px;
}
.badge-a { background-color: #DEF7EC; color: #03543F; }
.badge-b { background-color: #E1EFFE; color: #1E40AF; }
.badge-c { background-color: #FEF08A; color: #713F12; }
.badge-d { background-color: #FFEDD5; color: #9A3412; }
.badge-f { background-color: #FDE8E8; color: #9B1C1C; }

/* Score Box for Quiz */
.score-box {
    padding: 30px;
    border-radius: 20px;
    background: linear-gradient(135deg, #10B981 0%, #059669 100%);
    color: white;
    text-align: center;
    margin: 25px 0;
    box-shadow: 0 10px 25px -5px rgba(16, 185, 129, 0.4);
}

.big-score {
    font-size: 56px;
    font-weight: 900;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "profile_created" not in st.session_state:
    st.session_state.profile_created = False

if "subjects" not in st.session_state:
    st.session_state.subjects = 1

if "questions" not in st.session_state:
    st.session_state.questions = []

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False

if "calc_expr" not in st.session_state:
    st.session_state.calc_expr = ""


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("📚 Student Hub")

page = st.sidebar.radio(
    "Choose a section",
    [
        "👤 Profile",
        "🧮 Calculator",
        "🎓 GPA / Grade Calculator",
        "🧠 Quiz"
    ]
)

st.sidebar.divider()
st.sidebar.caption("Made with Python + Streamlit")


# =========================================================
# 1. PROFILE
# =========================================================

if page == "👤 Profile":

    st.markdown(
        '<div class="title">👤 My Profile</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Create your personal student profile</div>',
        unsafe_allow_html=True
    )

    st.header("📝 Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input(
            "Your name",
            placeholder="Enter your name"
        )

        age = st.number_input(
            "Your age",
            min_value=1,
            max_value=100,
            value=16,
            step=1
        )

        location = st.text_input(
            "Where are you from?",
            placeholder="Enter your location"
        )

    with col2:
        school = st.text_input(
            "Your school",
            placeholder="Enter your school"
        )

        grade = st.text_input(
            "Your grade",
            placeholder="e.g. Grade 10"
        )

        hobby = st.text_input(
            "Your main hobby",
            placeholder="e.g. Guitar"
        )

    st.header("⭐ Favorites")

    col1, col2 = st.columns(2)

    with col1:
        favorite_subject = st.text_input("Favorite subject")
        favorite_game = st.text_input("Favorite game")

    with col2:
        favorite_movie = st.text_input("Favorite movie")
        favorite_music = st.text_input("Favorite music")

    personality = st.text_area(
        "🧠 Describe yourself",
        placeholder="Tell us about yourself..."
    )

    goal = st.text_area(
        "🎯 What's one of your biggest goals?",
        placeholder="Write your goal here..."
    )

    if st.button("✨ Create My Profile", use_container_width=True):
        st.session_state.profile_created = True
        st.success("Profile created successfully!")

    if st.session_state.profile_created:
        st.divider()

        st.header("📋 Your Profile")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**👤 Name:** {name}")
            st.write(f"**🎂 Age:** {age}")
            st.write(f"**📍 Location:** {location}")
            st.write(f"**🏫 School:** {school}")
            st.write(f"**📚 Grade:** {grade}")

        with col2:
            st.write(f"**🎮 Hobby:** {hobby}")
            st.write(f"**📖 Favorite Subject:** {favorite_subject}")
            st.write(f"**🎮 Favorite Game:** {favorite_game}")
            st.write(f"**🎬 Favorite Movie:** {favorite_movie}")
            st.write(f"**🎵 Favorite Music:** {favorite_music}")

        st.divider()

        st.subheader("🧠 About Me")
        st.write(personality if personality else "N/A")

        st.subheader("🎯 My Goal")
        st.write(goal if goal else "N/A")


# =========================================================
# 2. CLICKABLE CALCULATOR
# =========================================================

elif page == "🧮 Calculator":

    st.markdown(
        '<div class="title">🧮 Calculator</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Click the buttons to perform calculations</div>',
        unsafe_allow_html=True
    )

    col_centered = st.columns([1, 2, 1])

    with col_centered[1]:
        display_val = st.session_state.calc_expr if st.session_state.calc_expr else "0"
        st.markdown(
            f'<div class="calc-display">{display_val}</div>',
            unsafe_allow_html=True
        )

        buttons = [
            ["C", "⌫", "(", ")"],
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]

        def handle_click(char):
            if char == "C":
                st.session_state.calc_expr = ""
            elif char == "⌫":
                st.session_state.calc_expr = st.session_state.calc_expr[:-1]
            elif char == "=":
                try:
                    expr = (
                        st.session_state.calc_expr
                        .replace("×", "*")
                        .replace("÷", "/")
                    )
                    res = eval(expr)
                    if isinstance(res, float) and res.is_integer():
                        res = int(res)
                    st.session_state.calc_expr = str(res)
                except Exception:
                    st.session_state.calc_expr = "Error"
            else:
                if st.session_state.calc_expr == "Error":
                    st.session_state.calc_expr = ""
                st.session_state.calc_expr += char

        for row in buttons:
            cols = st.columns(4)
            for i, btn in enumerate(row):
                if cols[i].button(btn, use_container_width=True, key=f"btn_{btn}_{row}"):
                    handle_click(btn)
                    st.rerun()


# =========================================================
# 3. GPA / GRADE CALCULATOR
# =========================================================

elif page == "🎓 GPA / Grade Calculator":

    st.markdown(
        '<div class="title">🎓 GPA Calculator</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Enter your subjects and exact percentage scores</div>',
        unsafe_allow_html=True
    )

    def calculate_grade(score):
        if score >= 90:
            letter = "A"
        elif score >= 80:
            letter = "B"
        elif score >= 70:
            letter = "C"
        elif score >= 60:
            letter = "D"
        else:
            letter = "F"

        gpa_val = (score / 100.0) * 4.0
        return letter, gpa_val

    col1, col2, col3 = st.columns([3, 1, 1])

    with col1:
        st.header("📚 Your Subjects")

    with col2:
        if st.button("➕ Add Subject"):
            st.session_state.subjects += 1
            st.rerun()

    with col3:
        if st.button("🔄 Reset"):
            st.session_state.subjects = 1
            st.rerun()

    results = []

    for i in range(st.session_state.subjects):
        col1, col2 = st.columns(2)

        with col1:
            subject = st.text_input(
                f"Subject {i + 1}",
                key=f"subject_{i}",
                placeholder="e.g. Mathematics"
            )

        with col2:
            score = st.number_input(
                f"Score {i + 1} (%)",
                min_value=0.0,
                max_value=100.0,
                value=90.25 if i == 0 else 85.0,
                step=0.1,
                key=f"score_{i}"
            )

        if subject.strip():
            grade, gpa = calculate_grade(score)
            results.append({
                "subject": subject,
                "score": score,
                "grade": grade,
                "gpa": gpa
            })

    if results:
        st.divider()
        st.header("📊 Performance Breakdown")

        for r in results:
            badge_class = f"badge-{r['grade'].lower()}"
            
            st.markdown(
                f"""
                <div class="subject-row">
                    <span style="font-size: 18px; font-weight: 600;">{r['subject']}</span>
                    <span>
                        <span style="font-size: 16px; margin-right: 15px; color: #4B5563;">Score: <b>{r['score']:.2f}%</b></span>
                        <span class="badge {badge_class}">Grade {r['grade']}</span>
                        <span style="font-size: 16px; margin-left: 15px; color: #4F46E5; font-weight: 700;">{r['gpa']:.2f} pts</span>
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

        overall_gpa = sum(r["gpa"] for r in results) / len(results)

        st.markdown(
            f"""
            <div class="gpa-card">
                <div class="gpa-label">Overall Calculated GPA</div>
                <div class="gpa-val">{overall_gpa:.2f}</div>
                <div class="gpa-scale">out of 4.00 max continuous scale</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.info("Enter at least one subject name above to calculate your detailed GPA.")


# =========================================================
# 4. CUSTOMIZABLE MULTIPLE CHOICE QUIZ
# =========================================================

elif page == "🧠 Quiz":

    st.markdown(
        '<div class="title">🧠 Custom Multiple Choice Quiz</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Create your own multiple-choice quiz and test yourself!</div>',
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # CREATE QUIZ
    # -----------------------------------------------------

    if not st.session_state.quiz_started:

        st.header("✏️ Create Your Quiz")

        number = st.number_input(
            "How many questions?",
            min_value=1,
            max_value=50,
            value=3,
            step=1
        )

        questions = []

        for i in range(number):
            st.subheader(f"❓ Question {i + 1}")

            q_text = st.text_area(
                "Question Prompt",
                key=f"mc_q_{i}",
                placeholder="Type your question..."
            )

            num_opts = st.number_input(
                "Number of options for this question",
                min_value=2,
                max_value=5,
                value=4,
                step=1,
                key=f"num_opts_{i}"
            )

            options = {}
            opt_labels = [f"Option {chr(65 + j)}" for j in range(num_opts)]

            cols = st.columns(min(num_opts, 3))
            for j in range(num_opts):
                col_idx = j % len(cols)
                label = opt_labels[j]
                opt_val = cols[col_idx].text_input(
                    f"{label}",
                    key=f"opt_{j}_{i}",
                    placeholder=f"Enter {label}"
                )
                options[label] = opt_val

            correct_opt = st.selectbox(
                "Select Correct Option",
                opt_labels,
                key=f"correct_{i}"
            )

            st.divider()

            questions.append({
                "question": q_text,
                "options": options,
                "correct_option": correct_opt
            })

        if st.button("🚀 Start Quiz", use_container_width=True):
            valid = True
            for q in questions:
                if not q["question"].strip() or any(not opt.strip() for opt in q["options"].values()):
                    valid = False
                    break

            if valid:
                st.session_state.questions = questions
                st.session_state.quiz_started = True
                st.session_state.quiz_finished = False
                st.rerun()
            else:
                st.error("❌ Please fill in every question text field and all defined options before starting.")

    # -----------------------------------------------------
    # TAKE QUIZ
    # -----------------------------------------------------

    elif not st.session_state.quiz_finished:

        st.header("📝 Quiz Time!")

        for i, q in enumerate(st.session_state.questions):
            st.subheader(f"Question {i + 1}")
            st.write(q["question"])

            options_list = [
                f"{k}: {v}" for k, v in q["options"].items()
            ]

            st.radio(
                "Choose your answer:",
                options_list,
                key=f"mc_user_ans_{i}"
            )
            st.divider()

        if st.button("✅ Submit Quiz", use_container_width=True):
            score = 0
            mistakes = []

            for i, q in enumerate(st.session_state.questions):
                user_selected = st.session_state.get(f"mc_user_ans_{i}", "")
                selected_key = user_selected.split(":")[0].strip()

                if selected_key == q["correct_option"]:
                    score += 1
                else:
                    correct_key = q["correct_option"]
                    mistakes.append({
                        "number": i + 1,
                        "question": q["question"],
                        "your_answer": f"{selected_key} ({q['options'].get(selected_key, '')})",
                        "correct_answer": f"{correct_key} ({q['options'].get(correct_key, '')})"
                    })

            st.session_state.score = score
            st.session_state.mistakes = mistakes
            st.session_state.quiz_finished = True
            st.rerun()

    # -----------------------------------------------------
    # QUIZ RESULTS
    # -----------------------------------------------------

    else:

        total = len(st.session_state.questions)
        score = st.session_state.score
        percentage = (score / total) * 100 if total > 0 else 0.0

        st.header("🏆 Quiz Results")

        st.markdown(
            f"""
            <div class="score-box">
                <div style="text-transform: uppercase; letter-spacing: 1px; opacity: 0.9;">Your Final Score</div>
                <div class="big-score">
                    {score} / {total}
                </div>
                <div style="font-size: 20px; font-weight: 600;">
                    {percentage:.1f}% Accuracy
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.header("🔍 Review Your Mistakes")

        if len(st.session_state.mistakes) == 0:
            st.success("🎉 Perfect score! You got everything correct!")
        else:
            for mistake in st.session_state.mistakes:
                st.error(f"❌ Question {mistake['number']}: {mistake['question']}")
                st.write(f"**Your answer:** {mistake['your_answer']}")
                st.write(f"**Correct answer:** {mistake['correct_answer']}")
                st.divider()

        if st.button("🔄 Create New Quiz", use_container_width=True):
            st.session_state.questions = []
            st.session_state.quiz_started = False
            st.session_state.quiz_finished = False
            st.rerun()
            