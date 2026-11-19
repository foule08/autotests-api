import platform
import sys

from config import settings


def create_allure_enviroment_file():
    items = [
        f'os_info={platform.system()}, {platform.release()}',
        f'python_version={sys.version}',
    ]
    items.extend(f'{key}={value}' for key, value in settings.model_dump().items())
    properties = '\n'.join(items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)