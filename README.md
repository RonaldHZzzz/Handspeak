<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - HaandSpeak</title>
</head>
<body>
    <h1>HaandSpeak</h1>
    <p>
        <strong>HaandSpeak</strong> es una aplicación diseñada para facilitar la comunicación entre personas sordas o 
        con discapacidad auditiva y aquellos que no conocen el lenguaje de señas. Utilizando tecnologías avanzadas como 
        <strong>MediaPipe</strong>, <strong>YOLOv8</strong>, y <strong>Google Text-to-Speech (gTTS)</strong>, este proyecto 
        permite traducir gestos en texto o voz, promoviendo la inclusión y la igualdad de acceso a la información.
    </p>
    <h2>📋 Objetivo</h2>
    <p>
        El principal objetivo de <strong>HaandSpeak</strong> es proporcionar una herramienta inclusiva que:
    </p>
    <ul>
        <li>Traduzca el lenguaje de señas a texto o voz en tiempo real.</li>
        <li>Facilite la interacción en diversas situaciones, como educación, atención médica y conversaciones diarias.</li>
        <li>Empodere a las personas con discapacidad auditiva con un recurso accesible y eficaz.</li>
    </ul>
    <h2>⚙️ Características</h2>
    <ul>
        <li><strong>Reconocimiento de gestos:</strong> Utiliza MediaPipe para identificar movimientos específicos de las manos.</li>
        <li><strong>Traducción de gestos a texto:</strong> Procesa los gestos y los convierte en texto comprensible.</li>
        <li><strong>Salida de voz:</strong> Convierte texto en voz utilizando Google Text-to-Speech.</li>
        <li><strong>Interfaz personalizable:</strong> Permite cambiar el color de fondo para mejorar la experiencia del usuario.</li>
        <li><strong>Gestión de la cámara:</strong> Funciones de refrescar y apagar para una mayor comodidad.</li>
    </ul>
    <h2>🚀 Instalación</h2>
    <h3>Requisitos previos</h3>
    <ul>
        <li>Python 3.7 o superior.</li>
        <li>Un editor de código (por ejemplo, <a href="https://code.visualstudio.com/" target="_blank">Visual Studio Code</a>).</li>
    </ul>
    <h3>Pasos para instalar</h3>
    <ol>
        <li><strong>Instalar Python y Visual Studio Code.</strong> 
            <ul>
                <li>Descarga Python desde <a href="https://www.python.org/" target="_blank">python.org</a>.</li>
                <li>Instala Visual Studio Code desde <a href="https://code.visualstudio.com/" target="_blank">code.visualstudio.com</a>.</li>
            </ul>
        </li>
        <li><strong>Descargar el proyecto.</strong> 
            <p>Descarga el proyecto desde 
                <a href="https://drive.google.com/drive/folders/1vIgBe4wN0_2x2lSLQuke2oDvEv-NSnKv" target="_blank">esta URL</a>.
            </p>
        </li>
        <li><strong>Acceder al proyecto.</strong>
            <ul>
                <li>Abre Visual Studio Code, selecciona <code>File > Open Folder</code>, y localiza la carpeta del proyecto.</li>
            </ul>
        </li>
        <li><strong>Levantar entorno virtual.</strong>
            <pre>
pip install virtualenv
virtualenv venv
source venv/bin/activate   # Para Linux/MacOS
.\venv\Scripts\activate    # Para Windows
            </pre>
        </li>
        <li><strong>Instalar dependencias.</strong>
            <pre>
pip install -r requirements.txt
            </pre>
        </li>
        <li><strong>Ejecutar el programa.</strong>
            <ol>
                <li>Ve a la carpeta <code>app</code>:
                    <pre>cd app</pre>
                </li>
                <li>Inicia la aplicación:
                    <pre>python app.py</pre>
                </li>
            </ol>
        </li>
    </ol>
    <h2>📖 Uso</h2>
    <ol>
        <li>Colócate frente a la cámara y realiza la seña que deseas traducir.</li>
        <li>El programa interpretará el gesto, lo convertirá a texto, y lo reproducirá como voz.</li>
        <li>Puedes cambiar el color de fondo y refrescar o apagar la cámara según sea necesario.</li>
    </ol>
    <h2>📚 Tecnologías utilizadas</h2>
    <ul>
        <li><a href="https://flask.palletsprojects.com/" target="_blank">Flask</a> como framework principal.</li>
        <li><a href="https://mediapipe.dev/" target="_blank">MediaPipe</a> para el reconocimiento de gestos.</li>
        <li><a href="https://github.com/ultralytics/yolov8" target="_blank">YOLOv8</a> para detección de objetos.</li>
        <li><a href="https://pypi.org/project/gTTS/" target="_blank">Google Text-to-Speech (gTTS)</a> para la generación de voz.</li>
    </ul>
    <h2>🛠️ Próximos pasos</h2>
    <ul>
        <li>Ampliar el reconocimiento de señas.</li>
        <li>Soporte para múltiples idiomas.</li>
        <li>Optimización del rendimiento en dispositivos móviles.</li>
    </ul>
    <h2>🤝 Contribuciones</h2>
    <p>
        ¡Contribuciones, reportes de errores, y sugerencias son bienvenidos! Por favor, abre un issue o envía un pull request.
    </p>
    <h2>📄 Licencia</h2>
    <p>Este proyecto está bajo la Licencia MIT. Consulta el archivo <code>LICENSE</code> para más detalles.</p>
</body>
</html>
