import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

"""En esta unidad lo que haremos será programar un asistente de voz al estilo de Siri o de Cortana por ejemplo
Tomar nota de todas las librerías que se han importado"""


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


audio_a_texto()
