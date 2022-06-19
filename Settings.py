import configparser
import os.path

class Settings:
    def __init__(self):
        config = configparser.ConfigParser()
        if os.path.exists("settings.ini"):
            config.read("settings.ini")
        else:
            print("Settings file does not exists!")
            with open('settings.ini', 'w') as file:
                file.write('')

        try:
            self.database_path = config["Settings"]["database_path"]

        except Exception as error:
            print('Settings file is broken. Set settings to default..')
            config.add_section("Settings")
            config.set('Settings', 'database_path', 'Default')

            self.database_path = config["Settings"]["database_path"]

            self.update_settings_file(config)

    def update_settings_file(self, config, path='settings.ini'):
        with open(path, "w") as config_file:
            config.write(config_file)

    def change_database_path(self, new):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        config.set('Settings', 'database_path', new)
        self.update_settings_file(config)
        self.database_path = config["Settings"]["database_path"]


    def print_all_stat(self):
        print('')
        print('[Settings]')
        print('================')
        print(f'Database Path = {self.database_path}')
        print('================')
