#! /usr/bin/python3

banner = r'''
###########################################################################
#      ____ 	   ______     _____                                             #
#     /   \     |      \    |   |                                           #
#    / |_) \    |  |_)  |   |   |                                           #
#   /       \   |       |   |   |                                           #
#  /         \  |______/    |___|                                           #
#                                                                         #
#                                  >> https://github.com/HOGAKE-ke-7      #
###########################################################################



#EXTINF:-1 group-title="Info - Must Read" tvg-logo="https://yt3.ggpht.com/ytc/AMLnZu-Pwuqij2lDrpgyFWvvAhxyiYEj5u9XFRutQf-3fw=s48-c-k-c0x00ffffff-no-rj" tvg-id="", Playlist is for Free
https://raw.githubusercontent.com/HOGAKE-ke-7/IPTV-live---adi/gitPertama/assets/info.m3u8


'''

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = s.get(url, timeout=15).text
    if '.m3u8' not in response:
        response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/naveenland4/YouTube_to_m3u/main/assets/info.m3u8')
                return
            #os.system(f'wget {url} -O temp.txt')
            os.system(f'curl "{url}" > temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/naveenland4/YouTube_to_m3u/main/assets/info.m3u8')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print(banner)
s = requests.Session()
with open('../youtube_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
