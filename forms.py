from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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
    # Fechas
    fecha()
    # Horas
    hora()
    # Lista desplegable
    lista_desplegable()

    # Encontrar boton de enviar
    boton_enviar = driver.find_element(By.CLASS_NAME, "lRwqcd")
    boton_enviar = boton_enviar.find_element(By.TAG_NAME, "div")

    # Hacer click en enviar
    boton_enviar.click()

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
            sleep(0.5)

            # Generar arreglo de todas las respuestas posibles
            respuestas = pregunta.find_element(By.CLASS_NAME, "OA0qNb").find_elements(By.CLASS_NAME, "MocG8c")
            respuestas.pop(0)
            
            # Elegir una respuesta aleatoria y seleccionarla
            choice(respuestas).click()
            sleep(0.5)

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

def fecha():
    try:
        # Encontrar todoas las preguntas
        preguntas = driver.find_elements(By.CSS_SELECTOR, 'input[type="date"]')

        # Ciclar preguntas
        for pregunta in preguntas:
            # Escribir el texto dentro del input
            pregunta.send_keys(generar_fecha_aleatoria())

    except Exception as e:
        print(f'Error: {e}')

def hora():
    try:
        # Encontrar todoas las preguntas
        preguntas = driver.find_elements(By.CLASS_NAME, "PfQ8Lb")

        # Ciclar preguntas
        for pregunta in preguntas:
            # Encontrar los inputs de texto
            inputs = pregunta.find_elements(By.CSS_SELECTOR, 'input[type="text"]')

            # Responder el primer valor
            inputs[0].send_keys(f"{(randint(0, 23)):02d}")
            # Responder el segudno valor
            inputs[1].send_keys(f"{(randint(0, 59)):02d}")
    
    except Exception as e:
        print(f'Error: {e}')

def generar_fecha_aleatoria():
        # Generar un año aleatorio entre 1900 y 2100
        anio = randint(1900, 2070)

        # Generar un mes aleatorio entre 1 y 12
        mes = randint(1, 12)

        # Generar un día aleatorio, teniendo en cuenta la cantidad de días en el mes seleccionado
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            dia = randint(1, 31)
        elif mes in [4, 6, 9, 11]:
            dia = randint(1, 30)
        else:
            # Si es febrero (mes 2), considerar si el año es bisiesto o no (divisible por 4 pero no por 100, o divisible por 400)
            if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
                dia = randint(1, 29)
            else:
                dia = randint(1, 28)

        # Formatear la fecha en el formato "dd/mm/aaaa"
        fecha_aleatoria = f"{dia:02d}/{mes:02d}/{anio:04d}"

        return fecha_aleatoria


def abrir_nav():
    # Ruta del controlador del navegador 
    DRIVER_PATH = ".\chromedriver.exe"

    # Añadir opciones para el navegador
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--incognito")

    # Inicializar el navegador en la variable driver
    global driver
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)

def cerrar_nav():
    driver.quit()

if __name__ == "__main__":
    pass
