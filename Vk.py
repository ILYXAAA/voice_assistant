class Vk:
    def __init__(self):
        with open ('commands/vk.txt', 'r', encoding='UTF-8') as file:
            self.check_words = list(file)
            self.check_words = [line.rstrip() for line in self.check_words]

    def trigger(self):
        print('HEY, I"M TRIGGERED')
