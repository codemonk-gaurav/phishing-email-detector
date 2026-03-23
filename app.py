import streamlit as st

def check_phishing(email):
    suspicious_words = ["urgent", "click", "verify", "password", "bank", "login"]
    
    score = 0
    email_lower = email.lower()
    
    for word in suspicious_words:
        if word in email_lower:
            score += 1
    
    if "http" in email_lower or "www" in email_lower:
        score += 2
    
    if email.isupper():
        score += 1

    if score >= 4:
        return "🔴 High Risk Phishing Email", score
    elif score >= 2:
        return "🟡 Medium Risk", score
    else:
        return "🟢 Low Risk", score


# UI
st.set_page_config(page_title="Phishing Detector", page_icon="🔐")

st.title("🔐 Phishing Email Detector")
st.markdown("### 🛡️ Detect suspicious emails instantly")
st.write("Paste email content below:")

email = st.text_area("📩 Email Content", height=200)

if st.button("🔍 Analyze Email"):
    result, score = check_phishing(email)

    st.markdown("## Result")
    
    if "High" in result:
        st.error(result)
    elif "Medium" in result:
        st.warning(result)
    else:
        st.success(result)

    st.write(f"Risk Score: {score}")