import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import time

"""Primer proyecto integrador de Python. En este proyecto buscaremos integrar varias funciones que ofrece python con 
sus librerias, siendo esto gestionado mediante un asistente de voz.

Ing. Antonio Gómez Ruiz"""

id_1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id_2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'


# Primero haremos que el micrófono nos escuche y transforme audio en texto
def audio_a_texto():
    """Almacenar recognizer en variable"""
    r = sr.Recognizer()

    """Configurar el micrófono"""
    with sr.Microphone() as origen:
        """Pondremos un pequeño momento de espera antes de que el micrófono se active"""
        r.pause_threshold = 0.8
        print('Ya puedes hablar')

        # Guardar el audio captado
        start_time = time.time()
        audio = r.listen(origen)
        print("Ya guarde el audio", time.time() - start_time)
        try:
            # Buscaremos en google lo que se ha escuchado
            solicitud = r.recognize_google(audio, language="es-ar", )

            # Prueba de que si se almaceno bien
            print("Dijiste: " + solicitud)

            # Devolver la solicitud
            return solicitud

        # Una opción en caso de que el audio no sea reconocido
        except sr.UnknownValueError:

            # Mensaje de que ocurrio un error
            print("Disculpa, no entendí")

            # Retornar mensaje de error
            return "Sigo esperando"

        # En caso de que la solicitud no sea resuelta
        except sr.RequestError:

            print("Disculpa, estoy fuera de servicio")
            return "Sigo esperando"

        # Cualquier error no esperado
        except:

            print("Ups, algo ha salido mal")
            return "Sigo esperando"


# Función para que el asistente sea escuchado
def hablar(mensaje):
    """Iniciar el 'motor' """
    engine = pyttsx3.init()
    """Por el momento podemos elegir entre ID 1 y 2, es importante que el lenguaje del texto coincida con el lenguaje 
    configurado para la voz"""
    engine.setProperty('voice', id_1)

    """Pronunciar el mensaje"""
    engine.say(mensaje)
    engine.runAndWait()


def pedir_dia():
    """Variable para almacenar la fecha del día de hoy"""
    dia = datetime.date.today()

    """Saber en que día de la semana estamos"""
    dia_semana = dia.weekday()

    # Calendario con todos los días de la semana
    calendario = {0: 'Lunes', 1: 'Martes', 2: 'Miércoles', 3: 'Jueves', 4: 'Viernes', 5: 'Sábado', 6: 'Domingo'}

    # Pedirle al asistente que diga un día de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')


# Función para saber cuanto falta o si estamos en fin de semana
def fin_semana():
    dia = datetime.date.today()
    dia_semana = dia.weekday()

    calendario = {0: 'Lunes', 1: 'Martes', 2: 'Miércoles', 3: 'Jueves', 4: 'Viernes', 5: 'Sábado', 6: 'Domingo'}

    if dia_semana < 4:
        res = 4 - dia_semana
        if res < 1:
            hablar(f'Faltan {res} día para que sea fin de semana')
        elif res > 1:
            hablar(f'Faltan {res} días para que sea fin de semana')
    elif dia_semana >= 4:
        hablar(f'Ya estamos en fin de semana, hoy es {calendario[dia_semana]}')


# Función para pedir la hora
def pedir_hora():
    """Variable que contiene los datos de la hora"""
    hora = datetime.datetime.now()
    hora = f'Actualmente son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    hablar(hora)


# Función para que nuestra asistente de un saludo inicial
def saludo_inicial():
    """Determinar si es la mañana o la tarde"""
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 19:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 12:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'
    hablar(f'{momento} Antonio, soy Luperdo Esteban Gonzalez Rodríguez, tu asistente virtual. ¿En que puedo ayudarte?')


# Función principal-central de nuestra asistente
def pedir_cosas():
    saludo_inicial()

    bandera = True
    while bandera:
        """Primero activaremos el micrófono y lo guardaremos"""
        solicitud = audio_a_texto().lower()

        if 'abrir youtube' in solicitud:
            hablar('Con gusto inicio YouTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in solicitud:
            hablar('Con gusto abro el navegador')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in solicitud:
            pedir_dia()
            continue
        elif 'fin de semana' in solicitud:
            fin_semana()
            continue
        elif 'qué hora es' in solicitud:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in solicitud:
            hablar('Okay, lo buscare en wikipedia')
            """En esta línea eliminamos el texto de buscar, para dejar solo las palabras a buscar en wikipedia"""
            solicitud = solicitud.replace('busca en wikipedia', '')
            """Aqui configuramos a wikipedia para que esté en español"""
            wikipedia.set_lang('es')
            """Le pedimos a wikipedia que lo busque, y que nos guarde solo la primera oración"""
            resultado = wikipedia.summary(solicitud, sentences=1)
            hablar('Wikipedia dice lo siguiente ')
            hablar(resultado)
            continue
        elif 'busca en internet' in solicitud:
            hablar('Okay, estoy en eso')
            solicitud = solicitud.replace('busca en internet', '')
            pywhatkit.search(solicitud)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproduce' in solicitud:
            hablar('Claro, ya inicia la reproducción')
            solicitud = solicitud.replace('reproduce', '')
            pywhatkit.playonyt(solicitud)
            continue
        elif 'broma' in solicitud:
            """Aqui nos dira un chiste al azar en español"""
            hablar(pyjokes.get_joke('es'))
            continue
        elif "precio de las acciones" in solicitud:
            accion = solicitud.split('de')[-1].split()
            """Debemos crear todo un diccionario que correlacione a la empresa, con su etiqueta en la bolsa para que 
            su búsqueda pueda ser posible"""
            cartera = {'apple': 'APPL', 'amazon': 'AMZN', 'google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'Aqui está, el precion de {accion} es {precio_actual}')
                continue
            except:
                hablar('perdon, pero no la he podido encontrar')
        elif 'hasta luego' in solicitud:
            bandera = False
    hablar('Hasta luego Antonio. Nos vemos')


# Con este código hicimos un barrido y pudimos ver todas las voces inicialmente disponibles en la PC (ID 1 y 2)
"""engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)"""

pedir_cosas()
