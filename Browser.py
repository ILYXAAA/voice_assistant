import webbrowser as wb
class Browser:
    def __init__(self):
        self.chrome_path = 'C:/Users/ILYXAAA/AppData/Local/Google/Chrome/Application/chrome.exe %s --incognito'

    def open_search(self, task):
        f_text = 'https://www.google.co.in/search?q=' + task
        wb.get(self.chrome_path).open(f_text)