import streamlit as st
import pandas as pd
import os

class WineDataApp:
    def __init__(self):
        self.data_path_red = "data/winequality-red.xlsx"
        self.data_path_white = "data/winequality-white.xlsx"
        self.df_red = None
        self.df_white = None
        self.df_combined = None

    def load_data(self):
        if os.path.exists(self.data_path_red) and os.path.exists(self.data_path_white):
            self.df_red = pd.read_excel(self.data_path_red)
            self.df_white = pd.read_excel(self.data_path_white)
            st.success("Loaded wine data from 'data/' folder.")
        else:
            st.info("Please upload red and white wine datasets.")
            uploaded_red = st.file_uploader("Upload Red Wine Data", type=["xlsx"])
            uploaded_white = st.file_uploader("Upload White Wine Data", type=["xlsx"])
            if uploaded_red is not None and uploaded_white is not None:
                self.df_red = pd.read_excel(uploaded_red)
                self.df_white = pd.read_excel(uploaded_white)
                st.success("Wine data uploaded successfully!")
            else:
                st.warning("Waiting for both datasets to be uploaded.")
                st.stop()

    def combine_data(self):
        # Add a 'type' column to each dataframe
        self.df_red['type'] = 'red'
        self.df_white['type'] = 'white'
        # Concatenate dataframes
        self.df_combined = pd.concat([self.df_red, self.df_white], ignore_index=True)

    def show_data(self):
        st.header("Red Wine Data Sample")
        st.dataframe(self.df_red.head())

        st.header("White Wine Data Sample")
        st.dataframe(self.df_white.head())

        st.header("Combined Wine Data Sample")
        st.dataframe(self.df_combined.head())

    def run(self):
        st.title("Wine Quality Data Exploration")
        self.load_data()
        self.combine_data()
        self.show_data()

# Run the app
if __name__ == "__main__":
    app = WineDataApp()
    app.run()
