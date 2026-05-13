import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Python-English Pilot Study", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Pilot Navigation")
st.sidebar.info("Progress through the levels to explore how Python logic reinforces English acquisition.")
level = st.sidebar.radio("Go to Level:", [
    "1. The Word Lab (Nouns)", 
    "2. The Sentence Builder (Syntax)", 
    "3. The Choice Chamber (Conditionals)", 
    "4. The Synonym Vault (Vocabulary)", 
    "5. The Narrative Loop (Sequence)"
])

st.title("Literacy through Logic: An English-Python Pilot")
st.markdown("---")

# --- LEVEL 1: THE WORD LAB ---
if level == "1. The Word Lab (Nouns)":
    st.header("Level 1: Categorizing Words")
    st.write("In Python, we use **variables** to store words. This is like labeling a box.")
    
    user_noun = st.text_input("Type a noun (a person, place, or thing):", "Scientist")
    
    st.subheader("Your Python Code:")
    st.code(f"subject = '{user_noun}'", language="python")
    
    st.subheader("Linguistic Outcome:")
    st.success(f"The word '{user_noun}' is now stored as a subject for our future sentences.")

# --- LEVEL 2: THE SENTENCE BUILDER ---
elif level == "2. The Sentence Builder (Syntax)":
    st.header("Level 2: Sentence Structure (S-V-O)")
    st.write("English follows a Subject-Verb-Object order. Python uses **f-strings** to join these parts.")

    col1, col2, col3 = st.columns(3)
    with col1: s = st.text_input("Subject", "The researcher")
    with col2: v = st.text_input("Verb", "analyzes")
    with col3: o = st.text_input("Object", "the environment")

    full_sentence = f"{s} {v} {o}."
    
    st.subheader("Python Syntax:")
    st.code(f"print(f'{{subject}} {{verb}} {{object}}.')", language="python")
    
    st.subheader("English Output:")
    if not s[0].isupper():
        st.warning("Note: Remember that English sentences start with a Capital Letter!")
    st.success(full_sentence)

# --- LEVEL 3: THE CHOICE CHAMBER ---
elif level == "3. The Choice Chamber (Conditionals)":
    st.header("Level 3: Cause and Effect (If/Then)")
    st.write("Using 'If' allows us to change the story based on a condition.")

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
    st.code(f"if tired == True:\n    action = 'rest'\nelse:\n    action = 'study'", language="python")
    
    st.subheader("Narrative Result:")
    st.success(f"The student will {action} {connector} {reason}.")

# --- LEVEL 4: THE SYNONYM VAULT ---
elif level == "4. The Synonym Vault (Vocabulary)":
    st.header("Level 4: Precision in Vocabulary")
    st.write("Python **Dictionaries** map one word to another. We can use this to find better synonyms.")

    vocab_vault = {
        "happy": "elated",
        "brave": "courageous",
        "smart": "intelligent"
    }

    base_word = st.selectbox("Choose a basic word to improve:", list(vocab_vault.keys()))
    
    st.subheader("How the 'Vault' works:")
    st.code(f"vault = {vocab_vault}\nbetter_word = vault['{base_word}']", language="python")
    
    st.subheader("Linguistic Upgrade:")
    st.info(f"Instead of saying '{base_word}', a more precise academic word is **{vocab_vault[base_word]}**.")

# --- LEVEL 5: THE NARRATIVE LOOP ---
elif level == "5. The Narrative Loop (Sequence)":
    st.header("Level 5: Sequence and Chronology")
    st.write("A **For Loop** helps us describe a series of actions in order (First, Next, Finally).")

    steps_input = st.text_area("List 3 steps for a process (comma-separated):", 
                               "Open the book, Read the page, Take notes")
    
    steps_list = [step.strip() for step in steps_input.split(",")]

    st.subheader("The Execution Loop:")
    st.code("for step in process_list:\n    print(f'Then, the student will {step}.')", language="python")

    st.subheader("Your Sequential Narrative:")
    for i, step in enumerate(steps_list):
        if i == 0:
            st.write(f"**First**, you {step.lower()}.")
        elif i == len(steps_list) - 1:
            st.write(f"**Finally**, you {step.lower()}.")
        else:
            st.write(f"**Next**, you {step.lower()}.")

# --- FOOTER ---
st.sidebar.markdown("---")
if st.sidebar.button("Reset Pilot"):
    st.rerun()
