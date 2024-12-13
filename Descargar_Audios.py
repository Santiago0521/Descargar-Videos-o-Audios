import yt_dlp as youtube_dl

def descargar_audio(url):
    # Configuramos las opciones de descarga para solo audio
    ydl_opts = {
        'format': 'bestaudio/best',           # Descarga el mejor audio disponible
        'outtmpl': '%(title)s.%(ext)s',       # Guarda el archivo con el título original
        'postprocessors': [{                  # Convierte el audio a MP3 usando FFmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',          # Formato de salida: MP3
            'preferredquality': '192',        # Calidad de audio: 192 kbps
        }],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("\nDescargando audio...\n")
            ydl.download([url])
            print("\n✅ ¡Audio descargado exitosamente!")
    except Exception as e:
        print(f"\n❌ Ocurrió un error: {e}")

# Pedimos al usuario que ingrese el link del video
url = input("Por favor, pega el enlace del video de YouTube para descargar solo el audio: ").strip()
descargar_audio(url)
