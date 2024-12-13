import yt_dlp as youtube_dl

def descargar_videos(url):
    # Configuramos las opciones de descarga
    ydl_opts = {
        'format': 'bv*[ext=mp4]+ba*[ext=m4a]/b[ext=mp4]',  # Selecciona el mejor video y audio compatibles
        'merge_output_format': 'mp4',                     # Fusiona video y audio en formato MP4
        'outtmpl': '%(title)s.%(ext)s',                   # Guarda el video con el título original
        'postprocessors': [{                              # Asegura la fusión con FFmpeg
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("\nDescargando video y fusionando audio...\n")
            ydl.download([url])
            print("\n✅ ¡Video descargado exitosamente!")
    except Exception as e:
        print(f"\n❌ Ocurrió un error: {e}")

# Pedimos al usuario que ingrese el link del video
url = input("Por favor, pega el enlace del video de YouTube que deseas descargar: ").strip()
descargar_videos(url)
