import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os

def iniciar_processo():
    email = email_entry.get()
    senha = senha_entry.get()
    diretorio_download = os.path.join(os.getcwd(), "downloads")
    
    if not email or not senha:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return
    
    if '@' not in email:
        messagebox.showerror("Erro", "O email deve conter um '@'.")
        return
    
    messagebox.showwarning(
        "Aviso",
        "Por favor, não mexa no mouse ou no teclado.\nO processo automatizado irá começar."
    )
    
    subprocess.run(["python", "fatura.py", email, senha, diretorio_download])

janela = tk.Tk()
janela.title("Obter Fatura de Energia")
janela.geometry("300x200")

tk.Label(janela, text="Email:").pack(pady=2)
email_entry = tk.Entry(janela)
email_entry.pack(pady=2)

tk.Label(janela, text="Senha:").pack(pady=2)
senha_entry = tk.Entry(janela, show="*")
senha_entry.pack(pady=2)

botao_selecionar = ttk.Button(janela, text="Obter fatura", command=iniciar_processo)
botao_selecionar.pack(pady=10)

janela.mainloop()
