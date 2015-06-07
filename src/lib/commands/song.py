from ScriptingBridge import SBApplication

iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")

def song():
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