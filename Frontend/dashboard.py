import streamlit as st
from datetime import date
# from Backend.apod_api import ApodAPI


class Dashboard:

    def init_dashboard(self):
        self.__config()
        self.__main_page()

    @staticmethod
    def __main_page():
        index = st.sidebar.selectbox(
            "Navigation",
            ('Welcome page', 'App'),
            index=0
        )

        if index == 'Welcome page':
            st.title('Astronomy Picture of The Day')
            st.subheader('Welcome in APOD Client')
            st.text('This web application was made for people who are interesting in...')
        elif index == 'App':
            st.title('APOD Application')

            col_0, col_1 = st.columns(2)

            with col_0:
                start_date = st.date_input(
                    'Please select date',
                    min_value=date(1995, 6, 17),
                    max_value=date.today()
                )
                end_date = st.date_input(
                    'Please select end date',
                    min_value=date(1995, 6, 17),
                    max_value=date.today(),
                    value=None
                )

                randomise = st.checkbox('Would you like to choose random picture?')
                if randomise:
                    count = st.number_input("Please, select how many random pictures you'd like to display", min_value=1)
                else:
                    count = 1
            with col_1:
                st.image('graphics/galaxy.png')

    def __download_data(self):
        pass

    def __display_data(self):
        pass

    @staticmethod
    def __config():
        st.set_page_config(
            page_title='APOD client',
            layout='wide'
        )

