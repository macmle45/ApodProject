from Backend.env import Env
from Frontend.dashboard import Dashboard


def main():
    env_variables = Env.load_env()
    api_key = env_variables['API_KEY']
    config_file = env_variables['CONFIG_FILE_PATH']

    configs = Env.get_config(filepath=config_file, section='api')
    url = configs['url']

    dashboard = Dashboard()
    dashboard.init_dashboard()


if __name__ == '__main__':
    main()
