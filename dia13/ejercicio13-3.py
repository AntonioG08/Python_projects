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

Ejercicio 3 - ahora podremos configurar la voz que nuestra asistente usará 

Guía para descargar otros tipos de voz
https://support.microsoft.com/es-es/topic/descargar-idiomas-y-voces-para-lector-inmersivo-el-modo-lectura-y-lectura-en-voz-alta-4c83a8d8-7486-42f7-8e46-2b0fdf753130
"""


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


# Con este código hicimos un barrido y pudimos ver todas las voces inicialmente disponibles en la PC (ID 1 y 2)
"""engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)"""

id_1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id_2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
