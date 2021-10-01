
########### Downloading YouTube videos¶ ##########
##################################################

# Creating video lists
# video_list = ['https://www.youtube.com/watch?v=xTN2ktqKSBk',
#               'https://www.youtube.com/watch?v=w5Ji-VEnbmc']

# #Looping through the list
# for i in video_list:
#   try:
#     yt = YouTube(i)
#     print('Downloading Link: ' + i)
#     print('Downloading video: ' + yt.streams[0].title)
#   except:
#     print("Connection Error")

#   #filters out all the files with "mp4" extension
#   stream = yt.streams.filter(res="360p").first()
#   stream.download("Downloads/")
# print('Task Completed!')


########### Downloading YouTube Playlists ##########
##################################################

# from pytube import Playlist
# play_list = []

# #Accessing the Playlist
# playlist = Playlist('https://www.youtube.com/playlist?list=PLPhnQz-ILJ_HCs7GSRIIso3cdJ2gOvUx_')

# #Checking the number of videos in the playlist
# print('Number of videos in playlist: %s' % len(playlist.video_urls))

# #Parsing through the playlist and appending the video urls in play_list
# for video_url in playlist.video_urls:
#     print(video_url)
#     play_list.append(video_url)

# #Looping through the list
# for i in play_list:
#   try:
#     yt = YouTube(i)
#     print('Downloading Link: ' + i)
#     print('Downloading video: ' + yt.streams[0].title)
#   except:
#     print("Connection Error")

# 	#filters out all the files with "mp4" extension
#   stream = yt.streams.filter(res="480p").first()
#   stream.download("Playlist_Videos")
#   # stream.download("E:\DOWNLOADS\DOWNLOADED VIDEOS")
# print('Task Completed!')

##################################################

# from pytube import Playlist

# playlist = Playlist(
#     'https://www.youtube.com/playlist?list=FLB2Duu9a_k3mrvyAgFOzHHg')
# print('Number of videos in playlist: %s' % len(playlist.video_urls))
# playlist.download_all()
###################################################
########### Downloading Entire YouTube Channel ##########
##################################################
from pytube import Channel

channel = Channel(
    "https://www.youtube.com/channel/UCKZwpZfOUtnDuRRx9ngMIcg")
for i, video in enumerate(channel):
    print(i, video)

print('Number of videos in channel: %s' % len(channel.video_urls))

for video in channel.videos:
    video.streams.get_lowest_resolution().download(
        output_path="/Users/Brahim/Downloads")

##################################################


# from pytube import YouTube

# from pytube import Playlist
# Playlist_link = "https://www.youtube.com/playlist?list=PLPhnQz-ILJ_HCs7GSRIIso3cdJ2gOvUx_"
# playlist = Playlist(Playlist_link)

# print('Number of videos in playlist: %s' % len(playlist.video_urls))

# for video in playlist.videos:
#     video.streams.get_lowest_resolution().download(
#         output_path="/Users/Brahim/Downloads")

