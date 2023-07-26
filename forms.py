from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from string import ascii_letters
from random import choice, randint

def enviar_form(url):
    # Abrir el formulario de google forms
    driver.get(url)

    # Esperar un momento
    sleep(1)

    # Responder preguntas correspondientes a cada categoria
    # Opcion Multiple
    opcion_multiple()
    # Casillas de Verificacion
    casillas_verificacion()
    # Preguna abierta
    input_text()
    # Escala lineal
    escala_lineal()
    # Cuadricula de opción multiple
    cuadricula_opcion_multiple()
    # Cuadricula de casillas de verificacion
    cuadricula_casillas_verificacion()
    # Lista desplegable
    lista_desplegable()

    # Encontrar boton de enviar
    boton_enviar = driver.find_element(By.CLASS_NAME, "lRwqcd")
    boton_enviar = boton_enviar.find_element(By.TAG_NAME, "div")

    # Hacer click en enviar
    #boton_enviar.click()

    # Esperar un momento
    sleep(1)

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

def lista_desplegable():
    try:
        # Encontrar todoas las preguntas
        preguntas = driver.find_elements(By.CLASS_NAME, "jgvuAb")

        # Ciclar preguntas
        for pregunta in preguntas:
            
            # Desplegar la lista de opciones
            pregunta.find_element(By.TAG_NAME, "div").click()
            sleep(1)

            # Generar arreglo de todas las respuestas posibles
            respuestas = pregunta.find_element(By.CLASS_NAME, "OA0qNb").find_elements(By.CLASS_NAME, "MocG8c")
            respuestas.pop(0)
            
            # Elegir una respuesta aleatoria y seleccionarla
            choice(respuestas).click()
            sleep(1)

    except Exception as e:
        print(f'Error: {e}')

def input_text():
    letras = ascii_letters
    try:
        # Encontrar todoas las preguntas
        preguntas = driver.find_elements(By.CSS_SELECTOR, '.AgroKb input[type="text"]')
        preguntas += driver.find_elements(By.TAG_NAME, "textarea")

        # Ciclar preguntas
        for pregunta in preguntas:
            # Generar un texto aleatoria de 20 letras
            texto = ''.join(choice(letras) for a in range(20))
            # Escribir el texto dentro del input
            pregunta.send_keys(texto)

    except Exception as e:
        print(f'Error: {e}')

def escala_lineal():
    try:
        # Encontrar todoas las preguntas
        preguntas = driver.find_elements(By.CLASS_NAME, "N9Qcwe")

        # Ciclar preguntas
        for pregunta in preguntas:
            # Encontrar el elemento div por su nombre de clase
            respuestas = pregunta.find_elements(By.CLASS_NAME, "T5pZmf")

            # Elegir respuesta
            respuesta_final = choice(respuestas)

            # Encontrar zona donde hacer click
            respuesta_final = respuesta_final.find_element(By.CLASS_NAME, "Od2TWd")

            # Hacer clic en la respuseta final
            respuesta_final.click()

    except Exception as e:
        print(f'Error: {e}')

def cuadricula_opcion_multiple():
    try:
        # Encontrar todoas las preguntas
        lineas = driver.find_elements(By.CSS_SELECTOR, ".lLfZXe.EzyPc")

        # Ciclar preguntas
        for linea in lineas:
            # Encontrar el elemento div por su nombre de clase
            respuestas = linea.find_elements(By.CLASS_NAME, "d7L4fc")

            # Elegir una respuesta aleatoria y seleccionarla
            choice(respuestas).click()

    except Exception as e:
        print(f'Error: {e}')

def cuadricula_casillas_verificacion():
    try:
        # Encontrar todoas las preguntas
        lineas = driver.find_elements(By.CSS_SELECTOR, ".EzyPc.mxSrOe")

        # Ciclar preguntas
        for linea in lineas:
            # Encontrar el elemento div por su nombre de clase
            respuestas = linea.find_elements(By.CLASS_NAME, "uHMk6b")

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
    #options.add_argument("--headless")

    # Inicializar el navegador en la variable driver
    global driver
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)

def cerrar_nav():
    driver.quit()

if __name__ == "__main__":
    abrir_nav()
    enviar_form("https://forms.gle/QeQwZrfShZ9rV3EDA")
