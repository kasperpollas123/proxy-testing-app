import streamlit as st
import requests

# Bright Data rotating proxy details
PROXY_HOST = "brd.superproxy.io"  # From your dashboard
PROXY_PORT = "33335"  # From your dashboard
PROXY_USERNAME = "brd-customer-hL_522ca3d8-zone-residential_proxy1"  # From your dashboard
PROXY_PASSWORD = "fsdr2c8hv7b11"  # From your dashboard

# Proxy URL
proxy_url = f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{PROXY_HOST}:{PROXY_PORT}"

# Streamlit app
st.title("Bright Data Rotating Proxy Tester")
st.write("Enter a URL to fetch its content using the Bright Data rotating proxy.")

# Input URL
url = st.text_input("Enter URL:", "https://example.com")

if st.button("Fetch Content"):
    if url:
        try:
            # Make the request using the proxy
            response = requests.get(url, proxies={"http": proxy_url, "https": proxy_url})
            
            # Display the response
            st.subheader("Response Content:")
            st.text(response.text)
            st.subheader("Response Status Code:")
            st.write(response.status_code)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid URL.")