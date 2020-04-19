import spotipy
import spotipy.oauth2

SPOTIPY_CLIENT_ID='96f9df47559a40c085188bde95c5301e'
SPOTIPY_CLIENT_SECRET='96f9df47559a40c085188bde95c5301e'
SPOTIPY_REDIRECT_URI='https://example.com/callback/'


# spotify controls setup
my_username = 'garbuiostefano'
pi_device_id = 'RaspberryPI'
my_client_id = '2700cd25271042509a5e34cbb3cca2ee'
my_client_secret = '96f9df47559a40c085188bde95c5301e'
my_redirect_uri = 'https://www.last.fm/user/george_____t/library/artists'
my_redirect_uri = 'https://example.com/callback/'
my_scope = 'streaming user-read-currently-playing user-read-playback-state'

spotipy.util.prompt_for_user_token(username=my_username,
                           scope=my_scope,
                           client_id=my_client_id,
                           client_secret=my_client_secret,
                           redirect_uri=my_redirect_uri)




#refreshToken = ''
#auth = spotipy.oauth2.SpotifyOAuth(client_id=my_client_id, client_secret=my_client_secret, redirect_uri=my_redirect_uri, scope=my_scope)
#token_info = auth.get_cached_token()
print("Refresh user toke")

#sp_oauth = oauth2.SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri,scope=scopes)
#token_info = sp_oauth.get_cached_token() 

#auth_url = sp_oauth.get_authorize_url(show_dialog=True)
#print(auth_url)

#refreshToken = ''
#cache_path = None 
#cache_path = cache_path or ".cache-" + my_username
#spotify=spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(my_client_id,my_client_secret,my_redirect_uri,scope=my_scope,cache_path=cache_path))
#me = spotify.me()
#pprint(me)

#token = spotipy.util.prompt_for_user_token(my_client_id, my_scope, redirect_uri = my_redirect_uri)
#print("Refresh user toke 2")

#refreshToken = spotipy.util.prompt_for_user_token(my_client_id, my_scope)
#token = util.prompt_for_user_token(username,scope=my_scope,client_id=my_client_id,client_secret=my_client_secret, redirect_uri=my_redirect_uri)
#sp = spotipy.Spotify(auth=token)

print("Refresh user toke 56")


def refreshAccessToken():
    global accessTokenInfo, accessToken, spotify
    print("Step 1")
    refredhToken = cache_path
    accessTokenInfo = auth.refresh_access_token(refreshToken)
    print("Step 2")
    accessToken = accessTokenInfo['access_token']
    print("Step 3")
    spotify = spotipy.Spotify(accessToken)
    print("Step 4")

refreshAccessToken()

# wrapper for refreshing token - should make sure 'action' can be run partially then fully without any issues
def spotifyAction(action, description):
  try: # in case of failure (eg. wifi off, no song playing), don't do anything
    action()
  except Exception as e:
    print('Failed to ' + description + ': ' + str(e))
    if spotipy.oauth2.is_token_expired(accessTokenInfo):
      refreshAccessToken()
      spotifyAction(action, description)

def playPauseAction():
  isOnPi = (d for d in spotify.devices()['devices'] if d['id'] == pi_device_id).next()['is_active']    
  if not isOnPi:
    spotify.transfer_playback(pi_device_id)
  else:
    isPlaying = spotify.current_user_playing_track()[u'is_playing']
    spotify.pause_playback() if isPlaying else spotify.start_playback()

playPause = lambda: spotifyAction(playPauseAction, 'play/pause')
nextTrack = lambda: spotifyAction(spotify.next_track, 'go to next track')
prevTrack = lambda: spotifyAction(spotify.previous_track, 'go to previous track')
impossibleSoul = lambda: spotifyAction(seqComp([lambda: spotify.start_playback(uris=['spotify:track:5CLs0uFRmU0U9VcnsI6jwv']), lambda: spotify.seek_track(765000), lambda: spotify.transfer_playback(pi_device_id)]), 'get hype')
