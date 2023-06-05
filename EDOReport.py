from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import tkinter as tk
import threading
import pyautogui

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.start_button = tk.Button(self)
        self.start_button["text"] = "Загрузить отчёт"
        self.start_button["command"] = self.start_script
        self.start_button.pack(side="left")
        # Связываем нажатие клавиши Enter с функцией start_script
        self.master.bind('<Return>', lambda event: self.start_script())

        self.start_date_label = tk.Label(self, text="Дата начала отчета:")
        self.start_date_label.pack()
        self.start_date_entry = tk.Entry(self)
        self.start_date_entry.pack()
        # Устанавливаем фокус на виджет self.start_date_entry
        self.start_date_entry.focus_set()

        self.end_date_label = tk.Label(self, text="Дата окончания отчета:")
        self.end_date_label.pack()
        self.end_date_entry = tk.Entry(self)
        self.end_date_entry.pack()
        
    def add_dot(self, event):
        # Получаем введенную пользователем дату
        date = self.start_date_entry.get()

        # Проверяем, оканчивается ли введенная дата на точку
        if not date.endswith("."):
            # Если нет, добавляем точку
            self.start_date_entry.insert(tk.END, ".")
        
    def start_script(self):
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        self.script_thread = threading.Thread(target=self.run_script, args=(start_date, end_date))
        self.script_thread.start()
        
    def run_script(self, start_date, end_date):

        options = Options()
        options.add_argument('--ignore-local-proxy')
        driver = webdriver.Chrome(options=options)

        driver.get("https://mosedo.mos.ru/")
        time.sleep(2)

        elem = driver.find_element(By.ID, "organizations")
        elem.clear()
        elem.send_keys('///')
        time.sleep(0.5)
        search_buttons = driver.find_elements(By.CLASS_NAME, "ui-menu-item")
        second_element = search_buttons[0]
        second_element.click()
        time.sleep(0.5)

        elem = driver.find_element(By.ID, "logins")
        elem.clear()
        elem.send_keys('///')
        time.sleep(0.5)
        search_buttons = driver.find_elements(By.CLASS_NAME, "ui-menu-item")
        second_element = search_buttons[1]
        second_element.click()
        time.sleep(0.5)

        elem = driver.find_element(By.ID, "password_input")
        elem.clear()
        elem.send_keys('///')
        time.sleep(0.5)
        search_buttons = driver.find_elements(By.CLASS_NAME, "btn_enter")
        second_element = search_buttons[0]
        second_element.click()
        time.sleep(2)
        
        pyautogui.press('escape', interval=0.2)
        time.sleep(1)
        
        menu_box = driver.find_element(By.ID, "s-menu-stat")
        menu_links = menu_box.find_elements(By.TAG_NAME, "a")
        for link in menu_links:
            if link.text == "///":
                link.click()
                break
        time.sleep(2)
                
        # search_button = driver.find_element(By.XPATH, "//h3[contains(@class, 's-menu__title') and contains(text(), 'Статистика и исполнение документов')]")
        # search_button.click()
        # time.sleep(2)
    
        # search_button = driver.find_element(By.XPATH, '//div[@class="s-menu__menu"]/a/b[text()="///"]')
        # search_button.click()
        # time.sleep(2)

        search_button = driver.find_element(By.LINK_TEXT, "Оперативный отчет")
        search_button.click()
        time.sleep(2)

        search_buttons = driver.find_elements(By.LINK_TEXT, "(выбрать все)")
        second_element = search_buttons[0]
        second_element.click()
        time.sleep(0.5)

        elem = driver.find_element(By.ID, "start_date")
        elem.clear()
        elem.send_keys(start_date)
        time.sleep(1)
        elem = driver.find_element(By.ID, "end_date")
        elem.clear()
        elem.send_keys(end_date)
        time.sleep(1)

        search_button = driver.find_element(By.ID, "executor_type_3")
        search_button.click()
        time.sleep(0.5)

        search_button = driver.find_element(By.NAME, "ex_plus_coex_3")
        search_button.click()
        time.sleep(0.5)

        search_button = driver.find_element(By.NAME, "exo_id[13166043]")
        search_button.click()
        time.sleep(0.5)


        search_button = driver.find_element(By.NAME, "immediately")
        search_button.click()
        time.sleep(0.5)

        time.sleep(5000)
        driver.quit()

def stop_script(self):
    self.script_thread.stop()

root = tk.Tk()
app = Application(master=root)

app.mainloop()





