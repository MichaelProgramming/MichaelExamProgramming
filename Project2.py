import ast
import base64
import math
import operator
import os
import streamlit as st

# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Student Hub", page_icon="📚", layout="wide"
)

# =========================================================
# CACHED BACKGROUND IMAGE ENCODER (PERFORMANCE OPTIMIZATION)
# =========================================================

BACKGROUND_IMAGE_PATH = "background.jpg"


@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


if os.path.exists(BACKGROUND_IMAGE_PATH):
    img_base64 = get_base64_of_bin_file(BACKGROUND_IMAGE_PATH)
    bg_style = f"""
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpeg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    """
else:
    bg_style = """
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #1A1325 0%, #3B2032 40%, #703338 70%, #111B27 100%);
        background-attachment: fixed;
    }
    """

# =========================================================
# LIGHTWEIGHT CSS (FAST GPU RENDERING)
# =========================================================

st.markdown(
    f"""
<style>
{bg_style}

/* Mobile Column Grid Fix */
@media (max-width: 640px) {{
    div[data-testid="column"] {{
        width: 18% !important;
        flex: 1 1 18% !important;
        min-width: 0 !important;
    }}
    div[data-testid="stHorizontalBlock"] {{
        flex-wrap: nowrap !important;
        gap: 4px !important;
    }}
}}

/* Sidebar */
[data-testid="stSidebar"] {{
    background-color: rgba(18, 18, 28, 0.85) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.1);
}}

/* Text */
.stApp, p, label, .stMarkdown {{
    color: #F3F4F6 !important;
}}

/* Calculator Display Box */
.calc-display {{
    background-color: rgba(10, 15, 25, 0.9);
    color: #34D399;
    font-family: monospace;
    font-size: 32px;
    font-weight: 700;
    text-align: right;
    padding: 14px 18px;
    border-radius: 12px;
    margin-bottom: 12px;
    border: 1px solid rgba(52, 211, 153, 0.4);
    word-wrap: break-word;
    min-height: 65px;
}}

/* Fast Render Buttons */
.stButton > button {{
    background: rgba(255, 255, 255, 0.12) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    border-radius: 10px !important;
}}

/* GPA Cards */
.gpa-card {{
    padding: 20px;
    border-radius: 16px;
    background: linear-gradient(135deg, rgba(255, 126, 95, 0.85) 0%, rgba(224, 86, 136, 0.85) 100%);
    color: #FFFFFF;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.3);
    margin-top: 15px;
}}

.gpa-label {{
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    font-weight: 700;
}}

.gpa-val {{
    font-size: 52px;
    font-weight: 900;
    line-height: 1.1;
    margin: 6px 0;
}}

.gpa-scale {{
    font-size: 12px;
    opacity: 0.9;
}}

/* Subject Breakdown Row */
.subject-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 16px;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    margin-bottom: 8px;
}}

/* Grade Badges */
.badge {{
    padding: 3px 10px;
    border-radius: 9999px;
    font-weight: 800;
    font-size: 12px;
}}
.badge-a {{ background-color: #059669; color: #FFFFFF; }}
.badge-b {{ background-color: #2563EB; color: #FFFFFF; }}
.badge-c {{ background-color: #D97706; color: #FFFFFF; }}
.badge-d {{ background-color: #EA580C; color: #FFFFFF; }}
.badge-f {{ background-color: #DC2626; color: #FFFFFF; }}

/* Quiz Score Card */
.score-box {{
    padding: 24px;
    border-radius: 18px;
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.85) 0%, rgba(5, 150, 105, 0.85) 100%);
    color: white;
    text-align: center;
    margin: 15px 0;
    border: 1px solid rgba(255, 255, 255, 0.25);
}}

.big-score {{
    font-size: 48px;
    font-weight: 900;
}}

/* Inputs */
div[data-baseweb="input"] > div, div[data-baseweb="textarea"] > div {{
    background-color: rgba(15, 15, 25, 0.7) !important;
    border-color: rgba(255, 255, 255, 0.2) !important;
    color: white !important;
    border-radius: 8px !important;
}}
</style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# HEADER BANNER
# =========================================================

st.markdown(
    """
<div style="
    text-align: center;
    padding: 14px;
    border-radius: 16px;
    background: rgba(0, 0, 0, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.15);
    margin-bottom: 16px;
">
    <span style="font-size: 11px; letter-spacing: 2px; text-transform: uppercase; color: #FF7E5F; font-weight: 800;">Academic Toolkit</span>
    <h1 style="margin: 2px 0 0 0; font-size: 32px; font-weight: 900; background: linear-gradient(90deg, #FF7E5F, #FEB47B, #E73C7E); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">STUDENT HUB</h1>
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# FAST SAFE MATH EVALUATOR
# =========================================================

SAFE_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def safe_eval(node):
    if isinstance(node, ast.Expression):
        return safe_eval(node.body)
    elif isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.BinOp):
        return SAFE_OPERATORS[type(node.op)](
            safe_eval(node.left), safe_eval(node.right)
        )
    elif isinstance(node, ast.UnaryOp):
        return SAFE_OPERATORS[type(node.op)](safe_eval(node.operand))
    elif isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name) and node.func.id == "sqrt":
            return math.sqrt(safe_eval(node.args[0]))
    raise ValueError("Unsupported operation")


def evaluate_expression(expr):
    try:
        formatted_expr = (
            expr.replace("×", "*").replace("÷", "/").replace("^", "**")
        )
        parsed = ast.parse(formatted_expr, mode="eval")
        res = safe_eval(parsed)
        if isinstance(res, float) and res.is_integer():
            return str(int(res))
        return str(round(res, 6))
    except Exception:
        return "Error"


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
    ["👤 Profile", "🧮 Calculator", "🎓 GPA / Grade Calculator", "🧠 Quiz"],
)

st.sidebar.divider()
st.sidebar.caption("Made with Python + Streamlit")

# =========================================================
# 1. PROFILE
# =========================================================

if page == "👤 Profile":

    st.header("📝 Personal Information")
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Your name", placeholder="Enter your name")
        age = st.number_input(
            "Your age", min_value=1, max_value=100, value=16, step=1
        )
        location = st.text_input(
            "Where are you from?", placeholder="Enter your location"
        )

    with col2:
        school = st.text_input("Your school", placeholder="Enter your school")
        grade = st.text_input("Your grade", placeholder="e.g. Grade 10")
        hobby = st.text_input("Your main hobby", placeholder="e.g. Guitar")

    st.header("⭐ Favorites")
    col1, col2 = st.columns(2)

    with col1:
        favorite_subject = st.text_input("Favorite subject")
        favorite_game = st.text_input("Favorite game")

    with col2:
        favorite_movie = st.text_input("Favorite movie")
        favorite_music = st.text_input("Favorite music")

    personality = st.text_area(
        "🧠 Describe yourself", placeholder="Tell us about yourself..."
    )
    goal = st.text_area(
        "🎯 What's one of your biggest goals?",
        placeholder="Write your goal here...",
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
# 2. CALCULATOR (OPTIMIZED BUTTON CALLBACKS)
# =========================================================

elif page == "🧮 Calculator":

    col_centered = st.columns([1, 2, 1])

    with col_centered[1]:
        display_val = (
            st.session_state.calc_expr if st.session_state.calc_expr else "0"
        )
        st.markdown(
            f'<div class="calc-display">{display_val}</div>',
            unsafe_allow_html=True,
        )

        buttons = [
            ["C", "⌫", "(", ")", "^"],
            ["√", "%", "±", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="],
        ]

        def handle_click(char):
            expr = st.session_state.calc_expr
            if char == "C":
                st.session_state.calc_expr = ""
            elif char == "⌫":
                st.session_state.calc_expr = expr[:-1]
            elif char == "=":
                st.session_state.calc_expr = evaluate_expression(expr)
            elif char == "√":
                if expr and expr != "Error":
                    st.session_state.calc_expr = evaluate_expression(
                        f"sqrt({expr})"
                    )
                else:
                    st.session_state.calc_expr = "sqrt("
            elif char == "%":
                if expr and expr != "Error":
                    st.session_state.calc_expr = evaluate_expression(
                        f"({expr})/100"
                    )
            elif char == "±":
                if expr and expr != "Error":
                    if expr.startswith("-"):
                        st.session_state.calc_expr = expr[1:]
                    else:
                        st.session_state.calc_expr = "-" + expr
            else:
                if expr == "Error":
                    st.session_state.calc_expr = ""
                st.session_state.calc_expr += char

        for row in buttons:
            cols = st.columns(len(row))
            for i, btn in enumerate(row):
                cols[i].button(
                    btn,
                    use_container_width=True,
                    key=f"btn_{btn}_{row}",
                    on_click=handle_click,
                    args=(btn,),
                )

# =========================================================
# 3. GPA / GRADE CALCULATOR
# =========================================================

elif page == "🎓 GPA / Grade Calculator":

    def calculate_grade(score):
        if score >= 90:
            letter, point = "A", 4.0
        elif score >= 80:
            letter, point = "B", 3.0
        elif score >= 70:
            letter, point = "C", 2.0
        elif score >= 60:
            letter, point = "D", 1.0
        else:
            letter, point = "F", 0.0

        continuous_gpa = (score / 100.0) * 4.0
        return letter, point, continuous_gpa

    col1, col2, col3 = st.columns([3, 1, 1])

    with col1:
        st.header("📚 Your Subjects")

    with col2:
        if st.button("➕ Add Subject"):
            st.session_state.subjects += 1

    with col3:
        if st.button("🔄 Reset"):
            st.session_state.subjects = 1

    results = []

    for i in range(st.session_state.subjects):
        col1, col2, col3 = st.columns([2, 1.5, 1])

        with col1:
            subject = st.text_input(
                f"Subject {i + 1}",
                key=f"subject_{i}",
                placeholder="e.g. Mathematics",
            )

        with col2:
            score = st.number_input(
                f"Score {i + 1} (%)",
                min_value=0.0,
                max_value=100.0,
                value=90.0 if i == 0 else 85.0,
                step=0.5,
                key=f"score_{i}",
            )

        with col3:
            credits = st.number_input(
                f"Credits {i + 1}",
                min_value=1,
                max_value=10,
                value=3,
                step=1,
                key=f"credits_{i}",
            )

        if subject.strip():
            letter, standard_gpa, continuous_gpa = calculate_grade(score)
            results.append(
                {
                    "subject": subject,
                    "score": score,
                    "grade": letter,
                    "standard_gpa": standard_gpa,
                    "continuous_gpa": continuous_gpa,
                    "credits": credits,
                }
            )

    if results:
        st.divider()
        st.header("📊 Performance Breakdown")

        total_credits = sum(r["credits"] for r in results)
        weighted_standard_gpa = (
            sum(r["standard_gpa"] * r["credits"] for r in results)
            / total_credits
        )
        weighted_continuous_gpa = (
            sum(r["continuous_gpa"] * r["credits"] for r in results)
            / total_credits
        )

        for r in results:
            badge_class = f"badge-{r['grade'].lower()}"
            st.markdown(
                f"""
                <div class="subject-row">
                    <span style="font-size: 16px; font-weight: 600; color: #FFFFFF;">{r['subject']} ({r['credits']} Credits)</span>
                    <span>
                        <span style="font-size: 14px; margin-right: 10px; color: #E5E7EB;">Score: <b>{r['score']:.1f}%</b></span>
                        <span class="badge {badge_class}">Grade {r['grade']}</span>
                        <span style="font-size: 14px; margin-left: 10px; color: #38BDF8; font-weight: 700;">{r['standard_gpa']:.1f} pts</span>
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )

        col_gpa1, col_gpa2 = st.columns(2)

        with col_gpa1:
            st.markdown(
                f"""
                <div class="gpa-card">
                    <div class="gpa-label">Weighted Standard GPA</div>
                    <div class="gpa-val">{weighted_standard_gpa:.2f}</div>
                    <div class="gpa-scale">4.0 Scale (A=4, B=3, C=2, D=1, F=0)</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col_gpa2:
            st.markdown(
                f"""
                <div class="gpa-card" style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.85) 0%, rgba(5, 150, 105, 0.85) 100%);">
                    <div class="gpa-label">Continuous GPA</div>
                    <div class="gpa-val">{weighted_continuous_gpa:.2f}</div>
                    <div class="gpa-scale">Exact Percentage Multiplier Scale</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    else:
        st.info(
            "Enter at least one subject name above to calculate your detailed GPA."
        )

# =========================================================
# 4. CUSTOM MULTIPLE CHOICE QUIZ
# =========================================================

elif page == "🧠 Quiz":

    if not st.session_state.quiz_started:
        st.header("✏️ Create Your Quiz")
        number = st.number_input(
            "How many questions?",
            min_value=1,
            max_value=50,
            value=3,
            step=1,
        )

        questions = []
        for i in range(number):
            st.subheader(f"❓ Question {i + 1}")
            q_text = st.text_area(
                "Question Prompt",
                key=f"mc_q_{i}",
                placeholder="Type your question...",
            )

            num_opts = st.number_input(
                "Number of options for this question",
                min_value=2,
                max_value=5,
                value=4,
                step=1,
                key=f"num_opts_{i}",
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
                    placeholder=f"Enter {label}",
                )
                options[label] = opt_val

            correct_opt = st.selectbox(
                "Select Correct Option", opt_labels, key=f"correct_{i}"
            )
            st.divider()

            questions.append(
                {
                    "question": q_text,
                    "options": options,
                    "correct_option": correct_opt,
                }
            )

        if st.button("🚀 Start Quiz", use_container_width=True):
            valid = True
            for q in questions:
                if not q["question"].strip() or any(
                    not opt.strip() for opt in q["options"].values()
                ):
                    valid = False
                    break

            if valid:
                st.session_state.questions = questions
                st.session_state.quiz_started = True
                st.session_state.quiz_finished = False
            else:
                st.error("❌ Please fill in every question and option.")

    elif not st.session_state.quiz_finished:
        st.header("📝 Quiz Time!")

        for i, q in enumerate(st.session_state.questions):
            st.subheader(f"Question {i + 1}")
            st.write(q["question"])

            options_list = [f"{k}: {v}" for k, v in q["options"].items()]
            st.radio(
                "Choose your answer:", options_list, key=f"mc_user_ans_{i}"
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
                    mistakes.append(
                        {
                            "number": i + 1,
                            "question": q["question"],
                            "your_answer": f"{selected_key} ({q['options'].get(selected_key, '')})",
                            "correct_answer": f"{correct_key} ({q['options'].get(correct_key, '')})",
                        }
                    )

            st.session_state.score = score
            st.session_state.mistakes = mistakes
            st.session_state.quiz_finished = True

    else:
        total = len(st.session_state.questions)
        score = st.session_state.score
        percentage = (score / total) * 100 if total > 0 else 0.0

        st.header("🏆 Quiz Results")
        st.markdown(
            f"""
            <div class="score-box">
                <div style="text-transform: uppercase; letter-spacing: 1px; opacity: 0.9;">Your Final Score</div>
                <div class="big-score">{score} / {total}</div>
                <div style="font-size: 18px; font-weight: 600;">{percentage:.1f}% Accuracy</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.header("🔍 Review Your Mistakes")
        if len(st.session_state.mistakes) == 0:
            st.success("🎉 Perfect score! You got everything correct!")
        else:
            for mistake in st.session_state.mistakes:
                st.error(
                    f"❌ Question {mistake['number']}: {mistake['question']}"
                )
                st.write(f"**Your answer:** {mistake['your_answer']}")
                st.write(f"**Correct answer:** {mistake['correct_answer']}")
                st.divider()

        if st.button("🔄 Create New Quiz", use_container_width=True):
            st.session_state.questions = []
            st.session_state.quiz_started = False
            st.session_state.quiz_finished = False