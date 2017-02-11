# youtube-play
A quick and dirty solution to play a YouTube song on a Unix system.

# Usage
```python
import youtube_play
process = youtube_play.play("toto africa") 
# by default it goes to the background
process.wait()
```
# Dependencies 
These are required to run the application:
```
youtube-dl
ffplay
```
These are optionally alternative player backends:
```
play (sox)
```
