# Herramienta para Descargar Videos y Audios de YouTube 🎥🎶

Este repositorio contiene dos scripts de Python que te permiten descargar videos y audios de YouTube en la mejor calidad.  

-------------------------------------------------------------------------------------------------------------------------

## 🛠️ **Requisitos Previos**

Antes de ejecutar los scripts, asegúrate de tener instalado lo siguiente:

1. **Python** (versión 3.8 o superior).  
   Descárgalo desde [python.org](https://www.python.org/).

2. **FFmpeg** (necesario para fusionar videos y audios).  

-------------------------------------------------------------------------------------------------------------------------

## 🛠️ **Instalación de FFmpeg**

1. **Descargar FFmpeg**:  
   - Abre el FFmpeg.txt, copia el link y pegalo en una nueva pestalla de Google, se procedera a la descarga automaticamente.

2. **Extraer el archivo**:  
   - Extrae el archivo descargado en una carpeta de tu preferencia, por ejemplo:
     ```text
     C:\Program Files\FFmpeg\bin
     ```
   - La carpeta "bin" es donde esta el programa.exe

3. **Agregar FFmpeg al PATH del sistema**:  
   - Abre la Configuracion, busca **"PATH"**.  
   - Haz clic en **Variables de entorno**.  
   - Busca la variable **Path** y haz clic en **Editar**.  
   - Agrega la ruta donde se encuentra la carpeta "bin" de FFmpeg:  
     ```text
     C:\Program Files\FFmpeg\bin
     ```
   - Guarda los cambios y cierra todas las ventanas.

4. **Verificar la instalación**:  
   Abre una terminal (CMD o PowerShell) y ejecuta el siguiente comando:  
   ```text
   ffmpeg -version
   ```
   
-------------------------------------------------------------------------------------------------------------------------

## 🚀 **Ejecucion de Descargar_Videos.py**

5. **Descargar_Videos.py**
  - Ejecuta el script:
    ```text
    Descargar_Videos.py
    ```
  - Pega el enlace del video de YouTube cuando se te solicite.
  - El video se descargará en formato MP4 con el nombre original del video.

-------------------------------------------------------------------------------------------------------------------------

## 🚀 **Ejecucion de Descargar_Audios.py**

6. **Descargar_Audios.py**
  - Ejecuta el script:
    ```text
    Descargar_Audios.py
    ```
  - Pega el enlace del video de YouTube cuando se te solicite.
  - El archivo de audio se descargará en formato MP3 con el nombre original del video.

-------------------------------------------------------------------------------------------------------------------------

##  **Ejemplo de ejecucion de Descargar_Videos.py**

  ```text
  Por favor, pega el enlace del video de YouTube que deseas descargar: https://youtu.be/VIDEO_ID

  Descargando video y fusionando audio...

  ✅ ¡Video descargado exitosamente con audio incluido!

  ```


-------------------------------------------------------------------------------------------------------------------------

##  **Ejemplo de ejecucion de Descargar_Audios.py**

  ```text
  Por favor, pega el enlace del video de YouTube para descargar solo el audio: https://youtu.be/VIDEO_ID
  
  Descargando audio...
  
  ✅ ¡Audio descargado exitosamente!
  ```

