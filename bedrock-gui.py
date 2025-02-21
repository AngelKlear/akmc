import time
import webbrowser
import tkinter as tk
from tkinter import messagebox

def download_server():
    versionmc = entry.get()
    
    if versionmc:
        url = 'https://www.minecraft.net/bedrockdedicatedserver/bin-win/bedrock-server-' + versionmc + '.zip'
        
        with open('bedrock.akmcgui', 'w') as file:
            file.write(versionmc + ' - ' + url)
        
        messagebox.showinfo("Успех", f'Ссылка: {url}\nСтраница скачивания откроется через 5 сек...')
        
        # Задержка 10 секунд перед открытием ссылки
        root.after(5000, lambda: webbrowser.open(url))
    else:
        messagebox.showwarning("Ошибка", "Пожалуйста, введите версию Minecraft.")

# Настройка Tkinter
root = tk.Tk()
root.title("AKmc - Bedrock Server")
root.geometry("500x300")

label = tk.Label(root, text="Введите версию Minecraft:")
label.pack(pady=10)

entry = tk.Entry(root, width=25)
entry.pack(pady=5)

button = tk.Button(root, text="Скачать сервер", command=download_server)
button.pack(pady=20)

quits = tk.Button(root, text='Выход', command=root.quit)
quits.pack(pady=20)

root.mainloop()
