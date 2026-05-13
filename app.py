import streamlit as st

st.set_page_config(page_title="Code-English Pilot", layout="wide")

st.title("Literacy through Logic: Python & English")
st.markdown("---")

# Sidebar for Level Selection
level = st.sidebar.selectbox("Select Study Level", 
                             ["Level 1: The Word Lab", "Level 2: The Sentence Builder"])

# --- LEVEL 1: THE WORD LAB ---
if level == "Level 1: The Word Lab":
    st.header("Level 1: Identifying Nouns")
    st.write("In Python, a **String** is just a sequence of characters. We use them to store words.")
    
    # Input field for student
    user_noun = st.text_input("Enter a common noun (e.g., Cat, Book, River):", "...")
    
    if user_noun != "...":
        st.subheader("Your Resulting Code:")
        st.code(f"subject = '{user_noun}'", language="python")
        
        st.success(f"Great! You've assigned the English noun '{user_noun}' to a Python variable.")
        st.info(f"**Linguistic Note:** In programming, we keep the data (the word) separate from the label (the variable).")

# --- LEVEL 2: THE SENTENCE BUILDER ---
elif level == "Level 2: The Sentence Builder":
    st.header("Level 2: Constructing SVO Sentences")
    st.write("Let's build a **Subject-Verb-Object** structure using code.")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        s = st.text_input("Subject (Noun)", "The scientist")
    with col2:
        v = st.text_input("Verb (Action)", "discovers")
    with col3:
        o = st.text_input("Object (Noun)", "the truth")

    # The 'Logic' of building the sentence
    sentence = f"{s} {v} {o}."
    
    st.subheader("How Python builds this:")
    st.code(f"sentence = subject + ' ' + verb + ' ' + object + '.'\nprint(sentence)")
    
    st.subheader("English Output:")
    st.success(sentence)

    # Simple validation check
    if not s[0].isupper():
        st.warning("English Rule Check: Remember to start your sentence (Subject) with a capital letter!")
