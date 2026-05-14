import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="ProGrammar: English-Python Pilot", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("ProGrammar Navigation")
st.sidebar.info("Select a level to explore how programming logic reinforces English acquisition.")

level = st.sidebar.selectbox("Go to Level:", [
    "Level 1: The Word Lab (Nouns)", 
    "Level 2: The Sentence Builder (Syntax)", 
    "Level 3: The Choice Chamber (Conditionals)", 
    "Level 4: The Synonym Vault (Vocabulary)", 
    "Level 5: The Narrative Loop (Sequence)"
])

st.title("ProGrammar: Literacy through Logic")
st.markdown("---")

# --- LEVEL 1: THE WORD LAB ---
if "Level 1" in level:
    st.header("Level 1: Categorizing Words")
    st.write("In Python, we use **variables** to store words. Think of a variable as a labeled box for a noun.")
    
    user_noun = st.text_input("Type a noun (a person, place, or thing):", "Scientist")
    
    st.subheader("Your Python Code:")
    st.code(f"subject = '{user_noun}'", language="python")
    
    st.subheader("Linguistic Outcome:")
    st.success(f"The word '{user_noun}' is now stored as a 'subject'.")
    st.info("**Research Note:** This stage establishes the concept of 'Data vs Label,' helping learners isolate parts of speech.")

# --- LEVEL 2: THE SENTENCE BUILDER ---
elif "Level 2" in level:
    st.header("Level 2: Sentence Structure (S-V-O)")
    st.write("English follow a Subject-Verb-Object order. Python uses **f-strings** to join these parts into a complete thought.")

    col1, col2, col3 = st.columns(3)
    with col1: s = st.text_input("Subject", "The researcher")
    with col2: v = st.text_input("Verb", "analyzes")
    with col3: o = st.text_input("Object", "the environment")

    full_sentence = f"{s} {v} {o}."
    
    st.subheader("Python Syntax:")
    st.code(f"print(f'{{subject}} {{verb}} {{object}}.')", language="python")
    
    st.subheader("English Output:")
    
    # --- GROWTH MINDSET CHECK: Casing Bug ---
    if len(s) > 0 and not s[0].isupper():
        st.warning("⚠️ **Linguistic Bug Detected:** In English code, the first letter of a sentence must be capitalized. Try fixing your 'Subject' input!")
    
    st.success(full_sentence)
    st.info("**Research Note:** By treating capitalization as a 'bug,' we reduce the anxiety of formal correction.")

# --- LEVEL 3: THE CHOICE CHAMBER ---
elif "Level 3" in level:
    st.header("Level 3: Cause and Effect (If/Then)")
    st.write("Using 'If' allows us to change the narrative flow based on a condition.")

    choice = st.radio("Is the student tired?", ["Yes", "No"])

    if choice == "Yes":
        action = "rest"
        connector = "because"
        reason = "they are exhausted"
    else:
        action = "study"
        connector = "since"
        reason = "they have high energy"

    st.subheader("The Logic Gate:")
    st.code(f"if student_is_tired == True:\n    action = 'rest'\nelse:\n    action = 'study'", language="python")
    
    st.subheader("Narrative Result:")
    st.success(f"The student will {action} {connector} {reason}.")
    st.info("**Research Note:** This demonstrates how conjunctions (because/since) serve as logical operators in a sentence.")

# --- LEVEL 4: THE SYNONYM VAULT ---
elif "Level 4" in level:
    st.header("Level 4: Precision in Vocabulary")
    st.write("Python **Dictionaries** map basic words to advanced ones. We use this to upgrade our English.")

    vocab_vault = {
        "happy": "elated",
        "brave": "courageous",
        "smart": "intelligent"
    }

    base_word = st.selectbox("Choose a basic word to 'Debug' and improve:", list(vocab_vault.keys()))
    
    st.subheader("How the 'Vault' works:")
    st.code(f"vault = {vocab_vault}\nbetter_word = vault['{base_word}']", language="python")
    
    st.subheader("Linguistic Upgrade:")
    st.info(f"Instead of the basic word '{base_word}', use the precise academic term: **{vocab_vault[base_word]}**.")

# --- LEVEL 5: THE NARRATIVE LOOP ---
elif "Level 5" in level:
    st.header("Level 5: Sequence and Chronology")
    st.write("A **For Loop** helps us describe a series of actions in order (First, Next, Finally).")

    steps_input = st.text_area("List 3 steps for a process (comma-separated):", 
                               "Open the book, Read the page, Take notes")
    
    steps_list = [step.strip() for step in steps_input.split(",")]

    st.subheader("The Execution Loop:")
    st.code("for step in steps_list:\n    print(f'Next, you {step}.')", language="python")

    st.subheader("Your Sequential Narrative:")
    for i, step in enumerate(steps_list):
        if i == 0:
            st.write(f"**First**, you {step.lower()}.")
        elif i == len(steps_list) - 1:
            st.write(f"**Finally**, you {step.lower()}.")
        else:
            st.write(f"**Next**, you {step.lower()}.")
    st.info("**Research Note:** This reinforces temporal markers and the importance of logical order in communication.")

# --- FOOTER ---
st.sidebar.markdown("---")
if st.sidebar.button("Reset Pilot"):
    st.rerun()
