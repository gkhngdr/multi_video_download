from Google import Create_Service
from googleapiclient.http import MediaFileUpload
import datetime
import random
import os
import time
CLIENT_SECRET_FILE = 'client.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


tags = ['parkour', 'night', 'party', 'competition', 'craziness', 'guitar', 'stamina', 'confusion', 'fun', 'Free Sound',
        'upbeat', 'speed', 'club', 'delay', 'motorbike', 'electric', 'synth', 'Nocopyright', 'Royalty Free',
        'Free Music', 'commercial', 'disarray', 'model', 'advert', 'snowboard', 'bike', 'energetic', 'powerful', 'NCS',
        'advertising', 'hallucination', 'photoshoot', 'racing', 'action', 'magazine', 'Video Music', 'product', 'car',
        'city', 'dance', 'mountain', 'challenge', 'sport', 'motocross', 'Free', 'confidence', 'disco', 'move', 'youth',
        'rhythm', 'synthpad', 'fast', 'house', 'life', 'techno', 'electronica', 'skate', 'adventure', 'rallycross',
        'rampage', 'adrenaline', 'teens', 'beat', 'danger', 'sordid', 'catwalk', 'energy', 'electronic', 'energy',
        'drinks', 'extreme', 'fashion', 'dancing', 'race']
texti = """Chill Out electro music track with a laid back mood great for videos about travel, vlog, youtube videos, 
advertising and much more. Features synthesizers, snaps, drums, electric bass, piano and voice samples. """
texti1 = """
Video by Rostislav Uzunov from Pexels"""
descs = ["No Copyright Music for your videos.",
         "NCS Music.",
         "Fallow For More.",
         "Modern and energetic royalty-free Dubstep Trap music."]
titles= ["Trap", "Energetic", "Background Music", "Mood","NCS","Sound","Dubstep","Royalty Free" ,"AFM"]

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
        str1 += " "
    return str1

directory = os.getcwd()
directory= directory+r"\VİDEOLAR"
hour= 0
for filename in os.listdir(directory):
    cur_file_name = os.path.join(directory, filename)

    upload_date_time = datetime.datetime(2022, 2, 10, hour, 20, 0).isoformat() + '.000Z'
    hour += 2
    random.shuffle(descs)
    shuffled_text = listToString(descs)
    last_text = texti + "\n" + shuffled_text +"\n"+ texti1
    selected_tags = list(set(random.choices(tags, k=60)))
    selected_titles= set(random.choices(titles, k=8))
    str_selected_titles= listToString(selected_titles)
    name_of_it = "NoCopyRight Free Music " + filename.replace(".mp4","")+" "+str_selected_titles
    request_body = {
        'snippet': {
            'categoryId': 10,
            'title': name_of_it,
            'description': last_text,
            'tags': ['Travel', 'video test', 'Travel Tips']
        },
        'status': {
            'privacyStatus': 'private',
            'publishAt': upload_date_time,
            'selfDeclaredMadeForKids': False,
        },
        'notifySubscribers': False
    }

    mediaFile = MediaFileUpload(cur_file_name)

    response_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()
    time.sleep(60)