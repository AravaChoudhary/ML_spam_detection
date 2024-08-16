import streamlit as st
from custommodel import custommodel

def main():
    st.set_page_config(page_title="Email Detection", page_icon=":email:", layout="centered")
    
    st.title("Email Detection App")
    st.markdown("""
        **Welcome to the Email Detection App!**  
        Enter the content of an email to determine if it's legitimate or unwanted.
    """)
    
    st.sidebar.header("Instructions")
    st.sidebar.markdown("""
        1. Enter the content of the email address in the text box below.
        2. Click the "Predict" button to analyze the email.
        3. View the result indicating whether the email is legitimate or unwanted.
    """)
    
    email = st.text_area("Email Content", height=150)
    
    if st.button("Predict"):
        if not email:
            st.warning("Please enter the content of the email.")
        else:
            processed_text_numeric_is_legit = custommodel(mail_text=email)
            is_legit = processed_text_numeric_is_legit.is_legit

            if is_legit:
                st.success("The email is considered legitimate.")
            else:
                st.error("The email is considered unwanted.")
    
    st.markdown("---")
    st.markdown("""
        **Need Help?**  
        For further assistance, contact support or visit our [Help Center](#).
    """)

if __name__ == "__main__":
    main()
