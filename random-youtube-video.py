#!/usr/bin/env python3

from googleapiclient.discovery import build
import random

DEVELOPER_KEY = 'YOUR_DEVELOPER_KEY'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

prefix = ['VIDEO', 'VIDEO ','VIDEO-', 'VIDEO_', 'IMG ', 'IMG_', 'IMG-', 'DSC ', 'VID', 'VID-', 'VID_', 'VID ']
postfix = [' MOV', '.MOV', 'MOV', 'AVI', ' AVI', '.AVI', ' MP4', '.MP4', 'MP4']

def youtube_search():
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=random.choice(prefix) + str(random.randint(999, 9999)) + random.choice(postfix),
    part='snippet',
    maxResults=5
  ).execute()

  videos = []

  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      videos.append('%s' % (search_result['id']['videoId']))
  if(len(videos) != 0):
    video = "https://www.youtube.com/watch?v=" + videos[random.randint(0, len(videos))]
    return video
  else:
    youtube_search()
print(youtube_search())
