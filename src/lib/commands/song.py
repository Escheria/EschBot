from ScriptingBridge import SBApplication

iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")

def song():
  song = ['Now Playing: '+iTunes.currentTrack().name()]
  if iTunes.currentTrack().artist():
    song.append('- '+iTunes.currentTrack().artist())
  if iTunes.currentTrack().album():
    song.append('['+iTunes.currentTrack().album()+']')

  return ' '.join(song);