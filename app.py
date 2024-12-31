import streamlit as st
import requests

# Bright Data rotating proxy details - UPDATE THESE WITH YOUR ACTUAL VALUES
PROXY_HOST = "brd.superproxy.io"
PROXY_PORT = "33335"
PROXY_USERNAME = "brd-customer-hL_522ca3d8-zone-residential_proxy1"  # MAKE SURE THIS IS CORRECT
PROXY_PASSWORD = "fsdr2c8hv7b11"  # MAKE SURE THIS IS CORRECT

# Proxy URL
proxy_url = f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{PROXY_HOST}:{PROXY_PORT}"

# Print proxy details for debugging
print("Username:", PROXY_USERNAME)
print("Password:", PROXY_PASSWORD)
print("Proxy URL:", proxy_url)


# Streamlit app
st.title("Bright Data Rotating Proxy Tester")
st.write("Enter a URL to fetch its content using the Bright Data rotating proxy.")

# Input URL
url = st.text_input("Enter URL:", "https://httpbin.org/ip")

if st.button("Fetch Content"):
    if url:
        try:
            # Make the request using the proxy
            proxies = {
                "http": proxy_url,
                "https": proxy_url,
            }

            # Make request with timeout and exception handling
            response = requests.get(url, proxies=proxies, timeout=10)

            # Raise an exception for bad status codes (4xx, 5xx)
            response.raise_for_status()

            # Print the full response object to the terminal when running the script with `streamlit run your_script_name.py`
            print("Full Response:", response)

            # Display the response
            st.subheader("Response Content:")
            st.text(response.text)
            st.subheader("Response Status Code:")
            st.write(response.status_code)

        # Catch common request errors
        except requests.exceptions.RequestException as e:
            st.error(f"Request Error: {e}")
            print(f"Request Error: {e}")  # Additional print for debugging

        # Catch any unexpected errors
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
            print(f"An unexpected error occurred: {e}")  # Additional print for debugging
    else:
        st.warning("Please enter a valid URL.")
