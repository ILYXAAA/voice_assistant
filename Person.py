import configparser
import os.path

class Person:
    def __init__(self):
        config = configparser.ConfigParser()
        if os.path.exists("settings.ini"):
            config.read("settings.ini")
        else:
            print("Settings file does not exists!")
            with open('settings.ini', 'w') as file:
                file.write('')

        try:
            self.name = config["Person"]["user_name"]
            self.age = config["Person"]["user_age"]
            self.sex = config["Person"]["user_sex"]
            self.height = config["Person"]["user_height"]
            self.weight = config["Person"]["user_weight"]
            self.birthday_date = config["Person"]["user_birthday"]

        except Exception as error:
            print('Person settings file is broken. Set settings to default..')
            config.add_section("Person")
            config.set('Person', 'user_name', 'Default')
            config.set('Person', 'user_age', 'Default')
            config.set('Person', 'user_sex', 'Default')
            config.set('Person', 'user_height', 'Default')
            config.set('Person', 'user_weight', 'Default')
            config.set('Person', 'user_birthday', 'Default')

            self.name = config["Person"]["user_name"]
            self.age = config["Person"]["user_age"]
            self.sex = config["Person"]["user_sex"]
            self.height = config["Person"]["user_height"]
            self.weight = config["Person"]["user_weight"]
            self.birthday_date = config["Person"]["user_birthday"]

            self.update_settings_file(config)

    def update_settings_file(self, config, path='settings.ini'):
        with open(path, "w") as config_file:
            config.write(config_file)

    def change_name(self, new):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        config.set('Person', 'user_name', new)
        self.update_settings_file(config)
        self.name = config["Person"]["user_name"]

    def change_age(self, new):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        config.set('Person', 'user_age', new)
        self.update_settings_file(config)
        self.age = config["Person"]["user_age"]

    def change_sex(self, new):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        config.set('Person', 'user_sex', new)
        self.update_settings_file(config)
        self.sex = config["Person"]["user_sex"]

    def change_height(self, new):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        config.set('Person', 'user_height', new)
        self.update_settings_file(config)
        self.height = config["Person"]["user_height"]

    def change_weight(self, new):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        config.set('Person', 'user_weight', new)
        self.update_settings_file(config)
        self.weight = config["Person"]["user_weight"]

    def change_birthday(self, new):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        config.set('Person', 'user_birthday', new)
        self.update_settings_file(config)
        self.birthday_date = config["Person"]["user_birthday"]
    
    def print_all_stat(self):
        print('')
        print('[Person]')
        print('================')
        print(f'NAME = {self.name}')
        print(f'AGE = {self.age}')
        print(f'SEX = {self.sex}')
        print(f'HEIGHT = {self.height}')
        print(f'WEIGHT = {self.weight}')
        print(f'BIRTHDAY = {self.birthday_date}')
        print('================')
