import streamlit as st
from PIL import Image
from datetime import date
from Backend.env import Env
from Backend.apod_api import ApodAPI
from Backend.apod_data import ApodData


class Dashboard:

    def init_dashboard(self):
        self.__config()
        self.__main_page()

    def __main_page(self):
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
            st.title('APOD Client Application')

            col_0, col_1 = st.columns(2)

            today = date.today()

            # with col_0:
            start_date = st.sidebar.date_input(
                'Please select the date for which you want to display the picture of the day',
                min_value=date(1995, 6, 17),
                max_value=today,
            )

            date_range = st.sidebar.checkbox('Would you like to display range of pictures')
            if date_range:
                end_date = st.sidebar.date_input(
                    'Please select end date',
                    min_value=date(1995, 6, 17),
                    max_value=today
                )
            else:
                end_date = today

            randomise = st.sidebar.checkbox('Would you like to choose random picture?')
            if randomise:
                count = st.sidebar.number_input(
                    "Please, select how many random pictures you'd like to display",
                    min_value=1
                )
            else:
                count = 1

            download_button = st.sidebar.button('Show picture')
            if download_button:
                apod_params = {
                    'date': start_date
                    # 'start_date': start_date,
                    # 'end_date': end_date,
                    # 'count': count
                }
                progress = st.spinner(text="Downloading...")
                with progress:
                    data = self.__get_data(apod_params)
                data_download_flag = True
            else:
                data_download_flag = False
            # with col_1:
                # image = Image.open('Frontend/graphics/galaxy.png')
                # st.image(image, use_column_width='auto')

            if data_download_flag:
                self.__display_data(data)

    @staticmethod
    def __get_data(params):
        env_variables = Env.load_env()
        api_key = env_variables['API_KEY']
        config_file = env_variables['CONFIG_FILE_PATH']

        configs = Env.get_config(filepath=config_file, section='api')
        url = configs['url']
        url = f'{url}?api_key={api_key}'

        # downloading raw data
        raw_data = ApodAPI.download_apod_data(url, params)

        # retrieving needed data
        apod_data = ApodAPI.retrieve_json_data(raw_data)

        # downloading picture using media url
        image_url = apod_data['media_hdurl']
        image = ApodAPI.download_apod_data(image_url)

        apod_date = apod_data['date']
        title = apod_data['title']
        description = apod_data['description']
        copyrights = apod_data['copyright']

        parsed_apod_data = ApodData(
            apod_date=apod_date,
            title=title,
            media=image.content,
            description=description,
            copyright=copyrights
        )

        return parsed_apod_data

    @staticmethod
    def __display_data(apod_data):
        apod_date = apod_data.apod_date
        title = apod_data.title
        image = apod_data.media
        description = apod_data.description

        st.subheader(f'Date: {apod_date}')
        st.subheader(f'Title: {title}')

        st.image(image)

        desc_expander = st.expander('Description')
        with desc_expander:
            st.write(description)

    @staticmethod
    def __config():
        st.set_page_config(
            page_title='APOD client',
            layout='wide'
        )
