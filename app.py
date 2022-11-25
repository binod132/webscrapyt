from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns
import requests
from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import youtubeanalysis


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/load', methods=['POST'])
def load():
    api_key= 'AIzaSyBAGxAbUWFTwkY91bOM2einkJvBnycMos4'
    youtube = build('youtube', 'v3', developerKey=api_key)
    channel_ids = ['UCL1Zr3XniRSwZOcqnpAKtfg',     #primetime
              'UC3yDoaqQzOd1bNP74ZrGPTA',       #ekantipur
              'UCczsYSRGukY9LA7Fd_govMw',        #himalaya
              'UCbs0xk6PavMVDt5UJqxGV6g'         #galaxy
              ]
    channels_stats = youtubeanalysis.get_chans_stats(youtube, channel_ids)
    channels_data = pd.DataFrame(channels_stats)
    channels_data['subscriber']=pd.to_numeric(channels_data['subscriber'])
    channels_data['views']=pd.to_numeric(channels_data['views'])
    channels_data['total_videos']=pd.to_numeric(channels_data['total_videos'])

    ax = sns.barplot(x='channel_name', y='subscriber', data = channels_data)
    fig = ax.get_figure()
    fig.savefig('/Users/shantiadhikari/Desktop/MLops_demo/webscrapyt/static/images/sub.png')
    
    ax1 = sns.barplot(x='channel_name', y='views', data = channels_data)
    fig1 = ax1.get_figure()
    fig1.savefig('/Users/shantiadhikari/Desktop/MLops_demo/webscrapyt/static/images/view.png')
    
    ax2 = sns.barplot(x='channel_name', y='total_videos', data = channels_data)
    fig2 = ax2.get_figure()
    fig2.savefig('/Users/shantiadhikari/Desktop/MLops_demo/webscrapyt/static/images/videos.png')


    return render_template('index.html', name = 'Channel Compare', url1 ='/static/images/sub.png', 
                        url2 ='/static/images/view.png',
                        url3 ='/static/images/videos.png'
                        )

if __name__=="__main__":
    app.run(debug=True)