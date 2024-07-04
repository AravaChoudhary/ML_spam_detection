import streamlit as st

from custommodel import custommodel

def main():
    st.title("Email Detection")

    email = st.text_input("Enter the content of your email address")

    if st.button("Predict"):
        if not email:
            st.warning("Please enter your email address")
        else:
            processed_text_numeric_is_legit = custommodel(mail_text = email)
            is_legit = processed_text_numeric_is_legit.is_legit

            if is_legit == True:
                st.success(f"The email is considered legitimate")
            else:
                st.error(f"The email is considered unwanted")

if __name__ == "__main__":
    main()