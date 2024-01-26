from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import schedule

# Define o caminho para o driver do Chrome

service = Service(executable_path='./chromedriver.exe')

# Configuração da instância do navegador

options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")
options.add_argument("--headless") 
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

# Inicializa o driver do Chrome
driver = webdriver.Chrome(service=service, options=options)

# Abre a página

driver.get('https://vtnews.com.br/')

# Ajusta o tamanho da janela

driver.set_window_size(1920, 1080)

# Função para tirar o print screen

def tirar_print_screen():
    
    # Tira um screenshot da página
    
    screenshot_path = f'Caminho{time.strftime("%Y-%m-%d_%H-%M")}.png' # Observação não esquecer de trocar o caminho para o print 
    driver.save_screenshot(screenshot_path)

    print(f'Print screen completo salvo em: {screenshot_path}')

# Agendamento para tirar o print screen diariamente às 18:00

schedule.every().day.at('18:00').do(tirar_print_screen)

# Loop principal para verificar as tarefas agendadas
while True:
    schedule.run_pending()
    time.sleep(1)

# Fecha o navegador
driver.quit()
