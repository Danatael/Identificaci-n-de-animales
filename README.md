# Identificación de Animales - HTTPS y pruebas de cámara

Este proyecto es una pequeña app Flask para identificar animales usando imágenes.

Este README explica cómo habilitar HTTPS localmente para que `getUserMedia` funcione desde un móvil (los navegadores exigen HTTPS cuando la página se sirve por IP remota).

Opciones para HTTPS / probar la cámara desde móvil

1) Opción rápida: ngrok (recomendado para desarrollo)
- Descarga e instala ngrok: https://ngrok.com/
- Ejecuta tu servidor Flask en el puerto 5000:
  ```powershell
  python .\index.py
  ```
- En otra terminal ejecuta:
  ```powershell
  ngrok http 5000
  ```
- Ngrok te dará una URL pública HTTPS. Ábrela en tu móvil; `getUserMedia` funcionará.

2) Usar un certificado local (mkcert recomendado)
- Instala mkcert: https://github.com/FiloSottile/mkcert
- Genera certificados para tu máquina:
  ```powershell
  mkcert -install
  mkcert 192.168.137.219 localhost 127.0.0.1
  ```
  Esto creará archivos `.pem` en el directorio actual. Usa esas rutas en las variables de entorno:
  ```powershell
  $env:USE_HTTPS='1'
  $env:SSL_CERT_PATH='C:\ruta\a\cert.pem'
  $env:SSL_KEY_PATH='C:\ruta\a\key.pem'
  python .\index.py
  ```
- Abre la URL `https://192.168.137.219:5000` en tu móvil (puede que necesites confiar en el certificado si no lo agrega mkcert al almacén del móvil).

3) Ad-hoc SSL (Werkzeug) - solo para desarrollo y localhost
- Puedes permitir que Werkzeug genere un certificado temporal (no recomendado para redes). En PowerShell:
  ```powershell
  $env:USE_HTTPS='1'
  $env:USE_ADHOC_SSL='1'
  python .\index.py
  ```
- Esto funciona para `https://localhost:5000`.

4) Crear un ejecutable (desktop)
- Si prefieres no depender del navegador, crea una app/ejecutable que capture la cámara localmente (por ejemplo con OpenCV) y la procese localmente o la envíe al servidor.

Notas de seguridad
- No uses certificados auto-generados en producción.
- Para producción, despliega detrás de un servidor WSGI (gunicorn/uWSGI) y un proxy TLS (nginx) con certificados válidos.

Si quieres, te guío paso a paso en la opción que prefieras (ngrok, mkcert o ad-hoc).