from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns

#extract channel details of multiple channel; playlist_Id is for later to extracting all video of particular channel
def get_chans_stats(youtube, channel_ids):
    data_all = []
    request = youtube.channels().list(part="snippet,contentDetails,statistics", id=','.join(channel_ids))
    response = request.execute()

    #select items from resonse into dict look at json format of response
    for i in range(len(response['items'])):
      data = dict(channel_name = response['items'][i]['snippet']['title'],
                subscriber = response['items'][i]['statistics']['subscriberCount'],
                views = response['items'][i]['statistics']['viewCount'],
                total_videos = response['items'][i]['statistics']['videoCount'],
                playlist_Id= response['items'][i]['contentDetails']['relatedPlaylists']['uploads']
                )
      data_all.append(data)
    return data_all