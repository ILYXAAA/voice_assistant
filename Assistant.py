import configparser
import os.path

class Assistant:
    def __init__(self):
        config = configparser.ConfigParser()
        if os.path.exists("settings.ini"):
            config.read("settings.ini")
        else:
            print("Settings file does not exists!")
            with open('settings.ini', 'w') as file:
                file.write('')

        try:
            self.name = config["Assistant"]["assistant_name"]
            self.age = config["Assistant"]["assistant_age"]
            self.sex = config["Assistant"]["assistant_sex"]
            self.voice_type = config["Assistant"]["assistant_voice_type"]

        except Exception as error:
            print('Assistant settings file is broken. Set settings to default..')
            config.add_section("Assistant")
            config.set('Assistant', 'assistant_name', 'Default')
            config.set('Assistant', 'assistant_age', 'Default')
            config.set('Assistant', 'assistant_sex', 'Default')
            config.set('Assistant', 'assistant_voice_type', 'Default')

            self.name = config["Assistant"]["assistant_name"]
            self.age = config["Assistant"]["assistant_age"]
            self.sex = config["Assistant"]["assistant_sex"]
            self.voice_type = config["Assistant"]["assistant_voice_type"]

            self.update_settings_file(config)

    def update_settings_file(self, config, path='settings.ini'):
        with open(path, "w") as config_file:
            config.write(config_file)

    def change_name(self, new):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        config.set('Assistant', 'assistant_name', new)
        self.update_settings_file(config)
        self.name = config["Assistant"]["assistant_name"]

    def change_age(self, new):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        config.set('Assistant', 'assistant_age', new)
        self.update_settings_file(config)
        self.age = config["Assistant"]["assistant_age"]

    def change_sex(self, new):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        config.set('Assistant', 'assistant_sex', new)
        self.update_settings_file(config)
        self.sex = config["Assistant"]["assistant_sex"]

    def change_voice_type(self, new):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        config.set('Assistant', 'assistant_voice_type', new)
        self.update_settings_file(config)
        self.voice_type = config["Assistant"]["assistant_voice_type"]

    def print_all_stat(self):
        print('')
        print('[Assistant]')
        print('================')
        print(f'NAME = {self.name}')
        print(f'AGE = {self.age}')
        print(f'SEX = {self.sex}')
        print(f'VOICE TYPE = {self.voice_type}')
        print('================')