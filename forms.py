from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from random import choice, randint

def enviar_form(url):
    # Abrir el formulario de google forms
    driver.get(url)

    # Esperar un momento
    time.sleep(1)

    # Responder preguntas correspondientes a cada categoria
    # Opcion Multiple
    opcion_multiple()
    # Casillas de Verificacion
    casillas_verificacion()

    # Encontrar boton de enviar
    boton_enviar = driver.find_element(By.CLASS_NAME, "lRwqcd")
    boton_enviar = boton_enviar.find_element(By.TAG_NAME, "div")

    # Hacer click en enviar
    boton_enviar.click()

    # Esperar un momento
    time.sleep(1)

def opcion_multiple():
    try:
        # Encontrar todoas las preguntas
        preguntas = driver.find_elements(By.CLASS_NAME, "SG0AAe")

        # Ciclar preguntas
        for pregunta in preguntas:
            # Encontrar el elemento div por su nombre de clase
            respuestas = pregunta.find_elements(By.CLASS_NAME, "d7L4fc")

            # Elegir respuesta
            respuesta_final = choice(respuestas)

            # Hacer clic en la respuseta final
            respuesta_final.click()

    except Exception as e:
        print(f'Error: {e}')

def casillas_verificacion():
    try:
        # Encontrar todoas las preguntas
        preguntas = driver.find_elements(By.CLASS_NAME, "Y6Myld")

        # Ciclar preguntas
        for pregunta in preguntas:
            # Encontrar el elemento div por su nombre de clase
            respuestas = pregunta.find_elements(By.CLASS_NAME, "uVccjd")

            # Ciclar posibles respuestas
            for respuesta in respuestas:
                # Eligir respuestas
                if bool(randint(0, 1)):
                    # Hacer clik si salio eligida
                    respuesta.click()

    except Exception as e:
        print(f'Error: {e}')

def abrir_nav():
    # Ruta del controlador del navegador 
    DRIVER_PATH = ".\chromedriver.exe"

    options = Options()
    options.add_argument("--headless")

    # Inicializar el navegador en la variable driver
    global driver
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)

def cerrar_nav():
    driver.quit()

if __name__ == "__main__":
    pass
