from __future__ import unicode_literals
import shlex
import pipes
import youtube_dl
import subprocess

logger = open("ytplay.log","w")

def lookup(lookup_string):
    """
    Look up the string on youtube
    """
    opts = {
        'extractaudio': True,
        'audioformat': 'vorbis', 
        'videoformat': 'none',
        'prefer_ffmpeg': True,
        'default_search': 'auto',
        'quiet': True,
        'outtmpl' : "ytplay",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'vorbis',
        }]
    }
    ydl = youtube_dl.YoutubeDL(opts)
    response = ydl.extract_info(url=lookup_string, download=True)
    return response['entries']


def play(lookup_string, binary="ffplay"):
    """
    search for a song and play it
    """
    information = lookup(lookup_string)
    logger.write(str(information))
    for info in information:
        try:
            command = format_command(
                info['requested_formats'][0]['url'],
                info['requested_formats'][0]['http_headers'],
                binary=binary)
            print("Playing: " + info['title'])
            break
        except KeyError, e:
            print("no right url found: " + str(e))

    player = subprocess.Popen(command)
    return player

def format_command(url, headers, binary="ffplay"):
    """
    formats a command to call

    Keyword Arguments:
    -   binary the binary to use
        choose between play or ffplay
    """
    if binary == "ffplay":
        args = '-i ytplay.ogg -nodisp -loglevel panic'
    elif binary == "play":
        args = "-q ytplay.ogg"
    else:
       raise Exception("Unsupported audio player: " + binary)
    return  shlex.split(binary +  " " + args)
