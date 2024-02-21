import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

"""En esta unidad lo que haremos será programar un asistente de voz al estilo de Siri o de Cortana por ejemplo
Tomar nota de todas las librerías que se han importado

Ejercicio 4 - Decir al usuario el día de la semana y la hora"""

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
        audio = r.listen(origen)
        try:
            # Buscaremos en google lo que se ha escuchado
            solicitud = r.recognize_google(audio, language="es-ar")

            # Prueba de que si se almaceno bien
            print("Dijiste: " + solicitud)

            # Devolver la solicitud
            return  solicitud

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


# Función para pedir la hora
def pedir_hora():
    """Variable que contiene los datos de la hora"""
    hora = datetime.datetime.now()
    hora = f'Actualmente son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    hablar(hora)


# Con este código hicimos un barrido y pudimos ver todas las voces inicialmente disponibles en la PC (ID 1 y 2)
"""engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)"""

pedir_hora()
