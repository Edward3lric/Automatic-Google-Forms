from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from random import choice

def enviar_form(url, driver):
    # Abrir el formulario de google forms
    driver.get(url)

    # Esperar un momento para asegurarse de que la página se cargue completamente
    time.sleep(2)

    try:
        # Encontrar todoas las preguntas
        preguntas = driver.find_elements_by_class_name("SG0AAe")

        # Ciclar preguntas
        for pregunta in preguntas:
            # Encontrar el elemento div por su nombre de clase
            respuestas = pregunta.find_elements_by_class_name("d7L4fc")

            # Elegir respuesta
            respuesta_final = respuestas[choice(range(0, len(respuestas)))]

            # Hacer clic en la respuseta final
            respuesta_final.click()
        
        # Encontrar boton de enviar
        boton_enviar = driver.find_element_by_class_name("lRwqcd")
        boton_enviar = boton_enviar.find_element_by_tag_name("div")

        # Hacer click en enviar
        boton_enviar.click()


    except Exception as e:
        print(f'Error: {e}')

    # Esperar un momento para asegurarse de que la página se cargue completamente
    time.sleep(2)


def obtener_driver():
    # Ruta del controlador del navegador 
    DRIVER_PATH = ".\chromedriver.exe"

    options = Options()
    options.add_argument("--headless")

    # Inicializar el navegador
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)

    return driver


if __name__ == "__main__":
    pass
