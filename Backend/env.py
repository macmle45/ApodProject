from dotenv import load_dotenv
from configparser import ConfigParser
import os
import getpass


def load_env():
    load_dotenv('Backend/ConfigFiles/.env')

    env_variables = dict()
    env_variables['API_KEY'] = os.getenv('API_KEY')

    temp_path = os.getenv('CONFIG_FILE_PATH')
    env_variables['CONFIG_FILE_PATH'] = temp_path.replace('_user_', getpass.getuser())

    return env_variables


def get_config(filepath, section):
    parser = ConfigParser()
    parser.read(filepath)

    if parser.has_section(section):
        params = dict(parser.items(section))
    else:
        raise Exception(f'Section {section} not found in config file.')

    return params