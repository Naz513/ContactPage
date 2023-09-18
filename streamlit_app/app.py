import streamlit as st
import requests

st.title('Contact Page')

# Creating input fields for user to enter details
name = st.text_input("Name", "")
email = st.text_input("Email", "")
message = st.text_area("Message", "")

# Send button. When clicked, the following code will execute
if st.button('Send'):
    data = {
        'name': name,
        'email': email,
        'message': message
    }

    # Triggering the lambda function via the API Gateway endpoint
    response = requests.post('YOUR_API_GATEWAY_ENDPOINT', json=data)

    # Checking if email was sent successfully
    if response.status_code == 200:
        st.success("Your message was sent successfully!")
    else:
        st.error("An error occurred. Please try again.")