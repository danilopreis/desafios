import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import messagebox

def gerar_fatura(email, senha, diretorio_download):
    print(f"Processando fatura para {usuario}")

    user_data_dir = r"C:\Users\danil\OneDrive\Área de Trabalho\Desafio\cache"
    profile_name = "Profile 2"

    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={user_data_dir}")
    options.add_argument(f"--profile-directory={profile_name}")

    prefs = {
        "download.default_directory": diretorio_download,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    
    options.add_experimental_option("prefs", prefs)
    
    driver = webdriver.Chrome(options=options)

    driver.get("https://portalhome.eneldistribuicaosp.com.br/#/segunda-via")

    espera1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='btnLogin']")))

    user = driver.find_element(By.ID, "email").send_keys(email)
    passw = driver.find_element(By.ID, "senha").send_keys(senha)
    click_btnLogin = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "btnLoginEmail")))
    click_btnLogin.click()


    login = driver.find_element(By.ID, "btnLoginEmail").submit()

    espera2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='segunda-via']/div[2]/div[1]/div/generate-pdf/button")))

    try:
        elemento_fatura = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='segunda-via']/div[2]/div[2]/div[3]/md-list/md-list-item/div[6]/div[2]")))
        elemento_fatura.click()
    except:
        messagebox.showinfo("Informação", "Não há faturas para baixar.")
        driver.quit()
        exit()

       

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python fatura.py <usuario>")
    else:
        usuario = sys.argv[1]
        senha = sys.argv[2]
        diretorio_download = sys.argv[3]
        gerar_fatura(usuario, senha, diretorio_download)