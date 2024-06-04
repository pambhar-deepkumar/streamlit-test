import streamlit as st
import pandas as pd

def load_file():
    st.title('Upload your Excel file')
    file = st.file_uploader("", type=['xlsx', 'xls'])
    if file:
        df = pd.read_excel(file)
        st.session_state['dataframe'] = df
        st.success("Successfully loaded excel file!")

def quote_price():
    st.write("This is the 'Quote Price' tab.")
    if 'dataframe' in st.session_state:
        df = st.session_state['dataframe']
        print(df.head())
        print(df.columns)
        if not df.empty and 'Item Description' in df.columns:
            rows_to_select = st.multiselect("Select the products you want to quote", df['Item Description'])
            selected_data = df[df['Item Description'].isin(rows_to_select)]
            price_up_range = st.radio("Select the Price Up range", (35, 45, 55, 75))

            if st.button('Submit'):
                msg_str = ""
                for index, row in selected_data.iterrows():
                    msg_str += f"Row {index+1}: The product {row['Item Description']} is priced at {row[price_up_range]}. \n"
                st.text(msg_str)
        else:
            st.error("Your DataFrame is either empty or does not contain 'Description' column")
    else:
        st.info("Please upload the Excel file first in 'Upload Excel File' section")
        
def create_invoice():
    st.write("This is the 'Create Invoice' tab.")
    # Add your functionality here

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Upload Excel File", "Quote Price", "Create Invoice"])

    if 'dataframe' not in st.session_state:
        st.session_state['dataframe'] = pd.DataFrame()

    if selection == "Upload Excel File":
        load_file()
    elif selection == "Quote Price":
        quote_price()
    elif selection == "Create Invoice":
        create_invoice()

if __name__ == "__main__":
    main()