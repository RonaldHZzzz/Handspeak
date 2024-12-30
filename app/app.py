from flask import Flask, Response, render_template
import cv2
from ultralytics import YOLO
from deteccion_manos.SeguimientoManos import detectormanos
from flask_socketio import SocketIO
from gtts import gTTS
import time
import os


width = 300
height = 320

model_palabras = YOLO('C:/Users/MINEDUCYT/desktop/proyecto/modelos_entrenados/modelo_palabra.pt')   
model_alfabeto = YOLO('C:/Users/MINEDUCYT/desktop/proyecto/modelos_entrenados/modelo_alfabeto.pt')  

detector = detectormanos(Confdeteccion=0.50)

cap = cv2.VideoCapture(0)

def realizar_inferencia(frame):
    nombres_clases_detectadas = []  # Lista para almacenar los nombres de las clases detectadas
  
    frame = detector.encontrarmanos(frame, dibujar=False)
    lista1, bbox, mano = detector.encontrarposicion(frame, ManoNum=0, dibujarPuntos=False, dibujarBox=False, color=[0, 225, 0])

    # Procesamiento para el modelo de palabras y alfabeto
    if mano in [1, 2]:
        xmin, ymin, xmax, ymax = bbox
        h, w, _ = frame.shape
        xmin = max(0, xmin - 40)
        ymin = max(0, ymin - 40)    
        xmax = min(w, xmax + 40)
        ymax = min(h, ymax + 40)

        corte = frame[ymin:ymax, xmin:xmax]

        if corte is not None and corte.shape[0] != 0 and corte.shape[1] != 0:
            corte_resized = cv2.resize(corte, (width, height))
            resultados = model_palabras.predict(corte, conf=0.20) if mano == 1 else model_alfabeto.predict(corte, conf=0.55)

            if len(resultados) != 0:
                for result in resultados:
                    for box in result.boxes:
                        clase_id = box.cls.item()
                        if clase_id in result.names:
                            nombre_clase = result.names[clase_id]
                            nombres_clases_detectadas.append(nombre_clase)
                            anotaciones = result.plot()
                            frame[ymin:ymax, xmin:xmax] = anotaciones
                            
                            

    if nombres_clases_detectadas:
        letras_detectadas = ", ".join(nombres_clases_detectadas)
        socketio.emit('update_letras', {'letras': letras_detectadas})

        # Reproducir audio para la primera coincidencia
        for letra in nombres_clases_detectadas:
            audio_file = f'static/audio/{letra}.mp3'
            if os.path.exists(audio_file):
                socketio.emit('update_audio', {'audio_file': audio_file})
                break  # Sale del bucle después de encontrar la primera coincidencia

    else:
        letras_detectadas = "No se detectaron letras"
        


    return frame



def frame():    
    while True:
        ret, frame = cap.read() 

        if not ret:
            break
        else:
            frame = realizar_inferencia(frame)
            suc, encode = cv2.imencode('.jpg', frame)
            frame = encode.tobytes()

        yield (b'--frame\r\n'
               b'content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/') 
def index():
    
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(frame(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
     socketio.run(app, debug=False, port=5000)
