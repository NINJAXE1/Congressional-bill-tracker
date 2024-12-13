import pandas as pd
import streamlit as st
import requests
API_KEY = 'shJQ4C07xdCbP8BgFPq9lldlG91IIWUSjVkUChnj'
BASE_URL = 'https://api.congress.gov/v3/bill'
def fetch_bills(congress, bill_type ):
    url = f"{BASE_URL}/{congress}/{bill_type}"
    header = {
        'X-Api-Key':API_KEY
    }
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        data = response.json()
        st.write(data)
        if 'bills' in data:
            return data["bills"]
        else:
            st.warning("bills are not found in the database")
            return[]
    else:
        st.error(f"Error  fetching data:{response.status_code}-{response.text}")
        return[]
def processing_bill_data(bills):
    df = pd.DataFrame(bills)
    if df.empty:
        st.warning('there is no bills to display in the database')
        return[]
def main():
    st.set_page_config(page_title = "Conressional bill tracker of the United States",layout = 'wide')
    st.title("📜🇺🇸congerssional bill tracker")
    st.markdown('Explore legislative data using the Congress API.')
    congress = st.sidebar.text_input("Please select your congressional session")
    query_params = st.sidebar.text_input('Query Parameters (optional)", "introduced"')
    bills = fetch_bills(congress,query_params)
    if bills:
        df = pd.DataFrame(bills)
        st.dataframe(df)
if __name__ == '__main__':
    main()


