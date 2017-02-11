import shlex
import pipes
import youtube_dl
import subprocess

def lookup(lookup_string):
        """
        A shitty youtube cli
        """
        opts = {
            'format': 'mp3[abr>0]/bestaudio/best',
            'prefer_ffmpeg': True,
            'default_search': 'auto',
            'quiet': True,
        }
        ydl = youtube_dl.YoutubeDL(opts)
        # player.kill()
        response = ydl.extract_info(url=lookup_string, download=False)
        info = response['entries'][0]
        derp = format_command(info['url'], info['http_headers'])
        print("Playing: " + info['title'] )
        #subprocess.call(derp)
        player = subprocess.Popen(derp)
        return player

def format_command(url, headers, binary="ffplay"):
    """
    formats a command to call

    Keyword Arguments:
    -   binary the binary to use
    """

    args = ""
    before_args = ""
    if isinstance(headers, dict):
        for key, value in headers.items():
            before_args += "{}: {}\n".format(key, value)
        before_args = ' -headers ' + pipes.quote(before_args)

    args = binary + ' {} -i {} -nodisp -loglevel panic'

    args = args.format(before_args, url,)
    return  shlex.split(args)
