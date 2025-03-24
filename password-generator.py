import streamlit as st
import random
import string

def generate_password(length, use_digit, use_special):
    characters = string.ascii_letters
    
    if use_digit:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

st.title("Password Generator")

length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)
use_digit = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digit, use_special)
    st.write(f"Generated Password: `{password}`")

st.write("----------------------------")
st.write("Built with ❤️ by [Madiha Ansari](https://github.com/madiha-ansari/password-generator)")


# pip install streamlit
#  streamlit run password-generator.py