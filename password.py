import streamlit as st
import re

st.set_page_config(page_title="🔐 SecurePass Analyzer", page_icon="🛡️")

st.title("🛡️ SecurePass Analyzer")
st.markdown("""
## 🔍 Check Your Password Strength!
🔑 Enter a password to see how strong it is and get smart suggestions to make it even more secure!  
✨ A strong password helps protect your accounts from hackers!  
""")

# Password input with a visibility toggle

password = st.text_input("Enter your password:", type="password" )

# Display info message before user enters a password
if not password:
    st.info("🚀 Start by entering your password above!")

feedback = []
score = 0

if password:  # Process the password after input
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("⚠️ Password should be at least **8 characters long**.")

    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("🔠 Include **both uppercase & lowercase letters** for better security.")

    if re.search("[0-9]", password):
        score += 1
    else:
        feedback.append("🔢 Add **at least one number** to strengthen your password.")

    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("🔑 Use **special characters (!@#$%^&*)** for extra security.")

    # Strength progress bar
    st.progress(score / 4)

    # Strength classification
    if score == 4:
        feedback.append("🎉 **Great job! Your password is very strong. 🔥**")
    elif score == 3:
        feedback.append("🟠 **Good, but you can improve it further! 💪**")
    else:
        feedback.append("🔴 **Weak password! Consider making it stronger. 🚨**")

    # Show suggestions if any
    if feedback:
        st.markdown("### 🛠️ How to Improve Your Password")
        for tip in feedback:
            st.write(tip)
