import gutenbergpy.textget
from gutenbergpy.gutenbergcache import GutenbergCache
import sqlite3
from os import path
from pydub import AudioSegment
import requests
import wget
import os


def get_mp3_urls():

    conn = sqlite3.connect('gutenbergindex.db')
    cursor = conn.cursor()

    #Get all ebook ids
    get_url = cursor.execute("SELECT name, books.id AS book_id, downloadlinks.id FROM books, downloadlinks WHERE languageid = 1 and downloadtypeid = 15 and books.id = downloadlinks.bookid LIMIT 10")

    mp3_data = []

    for i in get_url:
        mp3_data.append(i)

    return mp3_data


def download_mp3(mp3_data):
    directory = 'mp3'
    for data in mp3_urls:

        URL = data[0]
        book_id = data[1]
        download_link_id = data[2]
        
        current_file = os.path.join(directory, f"mp3/{book_id}-{download_link_id}.mp3")
  
        if not os.path.isfile(current_file): 
            response = requests.get(URL)

            
            open(f"mp3/{book_id}-{download_link_id}.mp3", "wb").write(response.content)

    

    for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            # checking if it is a file
            if os.path.isfile(f):
                if f.endswith(".mp3"):
                    mp3_to_wav(f)


    
def mp3_to_wav(filename):
    input_file = filename 
    output_file = filename.replace('mp3','wav')


    # convert mp3 file to wav file
    if not os.path.isfile(output_file): 

        sound = AudioSegment.from_mp3(input_file)
        sound.export(output_file, format="wav")


#MAIN PROGRAM 
mp3_data = get_mp3_urls()
download_mp3(mp3_data)















