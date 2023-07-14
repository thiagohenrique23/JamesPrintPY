from selenium import webdriver
import time
import pyautogui
import schedule

# Define o caminho para o driver do Chrome
driver_path = 'https://drive.google.com/drive/folders/1l9QxAL5K5-ZDpTpTm95h0c16QLGckW5B?usp=sharing'

# Inicializa o driver do Chrome
driver = webdriver.Chrome(executable_path=driver_path)

# Abre a página do Google
driver.get('https://vtnews.com.br/')

# Função para tirar o print screen
def tirar_print_screen():
    # Obtém a altura total da página
    altura_pagina = driver.execute_script('return document.body.scrollHeight')

    # Define as dimensões da janela do navegador
    largura_janela = driver.execute_script('return window.innerWidth')
    altura_janela = driver.execute_script('return window.innerHeight')

    # Calcula o número de capturas de tela necessárias
    num_capturas = altura_pagina // altura_janela + 1

    # Captura as capturas de tela da página inteira
    imagens = []
    for i in range(num_capturas):
        # Tira o print screen da parte visível da página
        screenshot = driver.get_screenshot_as_png()
        imagens.append(screenshot)

        # Simula a rolagem para a próxima posição
        pyautogui.scroll(altura_janela)

    # Combina as capturas de tela em uma única imagem
    screenshot_completo = pyautogui.stitch(imagens)

    # Salva o print screen da página completa
    screenshot_path = f'https://drive.google.com/drive/folders/1l9QxAL5K5-ZDpTpTm95h0c16QLGckW5B?usp=sharing{time.strftime("%Y-%m-%d_%H-%M")}.png'
    with open(screenshot_path, 'wb') as f:
        f.write(screenshot_completo)

    print(f'Print screen completo salvo em: {screenshot_path}')

# Agendamento para tirar o print screen diariamente às 18:00
schedule.every().day.at('18:00').do(tirar_print_screen)

# Loop principal para verificar as tarefas agendadas
while True:
    schedule.run_pending()
    time.sleep(1)

# Fecha o navegador
driver.quit()