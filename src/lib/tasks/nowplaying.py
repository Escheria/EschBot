import threading
import time

#TODO: figure out how to import song() command properly instead of copypasta
from ScriptingBridge import SBApplication

iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
delay = 5
npfile = '/Users/escherichiarinku/Documents/Stream/NowPlaying.txt'
current_song = 'asd'

class nowplaying (threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    #IMPORTANT, otherwise thread will still run and python wont exit
    self.setDaemon(True)
    current_song = ''
  def run(self):
    while True:
      update_song()
      time.sleep(5)

def update_song():
  song = get_song()
  if(current_song != song):
    update_song_file(song)

def update_song_file(songname):
  np = open(npfile, 'w')
  np.write('') #clear
  np.write(songname)
  np.close()

#import instead of copypasta :()
iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")

def get_song():
  song = ['Now Playing: '+iTunes.currentTrack().name()]
  if iTunes.currentTrack().artist():
    song.append('- '+iTunes.currentTrack().artist())
  if iTunes.currentTrack().album():
    song.append('['+iTunes.currentTrack().album()+']')
  if iTunes.currentTrack().rating():
    rating = int(iTunes.currentTrack().rating())
    str_rating = ''.join(['*' for x in range(rating/20)])
    song.append('Rating: '+str_rating)

  return ' '.join(song);