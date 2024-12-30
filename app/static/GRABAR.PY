from gtts import gTTS
import os

# Lista de letras o palabras para las cuales quieres generar audio
letras_o_palabras = ["e", "b", "u", "d", "c", "h", "s", "n",
        "a", "g", "o", "y", "t", "i",
        "p", "j", "k", "w", "m", "r", "z", "l",
        "v", "q", "f", "x","POR FAVOR", "BUENOS DIAS", "HOLA", "GRACIAS", "NO", "BIEN"]  # Agrega todas las letras o palabras deseadas aquí

# Directorio donde se guardarán los archivos de audio
directorio_audio = 'C:/Users/MINEDUCYT/Desktop/proyecto/app/static/audio/audio_'

# Asegúrate de que el directorio existe
if not os.path.exists(directorio_audio):
    os.makedirs(directorio_audio)

# Generar y guardar los archivos de audio
for letra in letras_o_palabras:
    tts = gTTS(text=letra, lang='es')
    tts.save(f'{directorio_audio}{letra}.mp3')
    print(f'Archivo de audio generado para: {letra}')