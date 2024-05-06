# Paraleas Y Distribuidas Parcial 1

### Integrantes
- **Herney Eduardo Quintero Trochez** 1528556

### Descripción

### Requerimientos
- Crear una Api Key en https://console.cloud.google.com/
- instalar los requerimientos 
```bash
pip<python_version> install -r requirements.txt
```
- Hacer una copia de config.template.json en el directorio config y renombrarla a config.json
  - Agregar la Api Key en el archivo config.json
  - Agregar los datos de los canales en el archivo config.json
  - Para el channel_id se puede usar el id del canal o un id personalizado
  - Si se usa un id personalizado se debe agregar el campo channel_has_id como true sino se debe agregar como false
```json
{
  "youtube_api_key": "<api_key>",
  "youtube_channel_list": [
    {
      "channel_name": "<channel_name>",
      "chanel_has_id": <true/false>,
      "channel_id": "<channel_id/channel_custom_id>"
    }
  ],
  "ytdlp_download_link": "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp"
}
```
### Uso
Para la ejecución del programa se debe correr el archivo run.py
- mode: Modo de ejecución del programa
    - sequential: realiza la descarga usando un solo hilo
    - multithreaded: realiza la descarga usando multiples hilos, por defecto 4
    - multiprocessing: realiza la descarga usando multiples procesos, por defecto 4
- num: Aplica solo para multithreaded y multiprocessing, indica el numero de hilos o procesos a usar
```bash
python<python_version> run.py --mode <mode> --num <num>
```

- La descarga de los videos se realiza en la carpeta src/output/downloads
- El archivo de logs se encuentra en src/output/log.log
- El aplicativo de yt-dlp se descarga en src/output/yt-dlp