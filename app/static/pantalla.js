  function toggleCamera() {
    var toggleButton = document.getElementById('toggle_button');
    var videoFeed = document.getElementById('video_feed');
    
    if (toggleButton.innerText == 'Encender Cámara') {
        videoFeed.src = videoUrl;
        toggleButton.innerText = 'Apagar Cámara';
        
    } else {
        videoFeed.src = '';
        toggleButton.innerText = 'Encender Cámara';
        videoFeed.style.backgroundImage = "url('/static/image/camara_apagada.png')";
    }
  }

  function refreshCamera() {
    var videoFeed = document.getElementById('video_feed');
    videoFeed.src = "/static/image/refrescar.png"; // Ruta estática a la imagen
    setTimeout(function() {
        videoFeed.src = videoUrl;
    }, 2000);
  }

  function toggleSwitch() {
    var switchElement = document.getElementById('customSwitch');
    switchElement.checked = !switchElement.checked;
  }
  document.getElementById('customSwitch').addEventListener('change', function() {
    var contenedor = document.querySelector('.contenedor');
    if (this.checked) {
        contenedor.style.backgroundColor = '#ffffff'; // Cambia a tu color deseado cuando el toggle está activado
    } else {
        contenedor.style.backgroundColor = '#292929'; // Cambia a tu color deseado cuando el toggle está desactivado
    }
  }); 

 