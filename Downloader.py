import pafy
from pytube import Playlist
import sys,os,time
from termcolor import colored


# def for bunner
def bunner():
    desc = '''

    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
    ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
    ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
    ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
    '''
    desc = colored(desc,"yellow")
    print(desc)

    myname = colored("                              Coded By : Moamen Rabee Mohamed\n\n","red")
    print(myname)

# def for download video
def Download_vid():
    i = 1
    streams = v.streams
    for stream in streams:
        print("["+str(i)+"] "+str(stream))
        i+=1
    choise = colored("Choose the quality number : ","yellow")
    print(choise)
    choise = input(">>>")
    choise = int(choise) -1
    try:
        myvid = v.streams[choise]
        myvid.download()
        done = colored("\nDone Download", "red", "on_white", ["blink", "underline", "dark"])
        print(done)
    except Exception as e:
        e = colored(e,"red")
        print(e)
        sys.exit()

# def for download audio
def Download_aud():
    i = 1
    streams = v.audiostreams
    for stream in streams:
        print("["+str(i)+"] "+str(stream))
        i+=1

    choise = colored("Choose the quality number : ","yellow")
    print(choise)
    choise = input(">>>")
    choise = int(choise) -1
    try:
        myvid = v.audiostreams[choise]
        myvid.download()
        done = colored("\nDone Download", "red", "on_white", ["blink", "underline", "dark"])
        print(done)
    except Exception as e:
        e = colored(e,"red")
        print(e)
        sys.exit()
    

# Start bunner and clean terminal
loading_msg = colored("Loading ....","blue")
print(loading_msg)
time.sleep(2)
#os.system("pip3 install termcolor")
#os.system("pip3 install pafy")
#os.system("pip3 install youtube_dl")
#os.system("pip install pytube")
os.system("clear")
bunner()

# https://www.youtube.com/watch?v=hS5CfP8n_js


video_or_list = colored("[+] press 1 to download video | 2 to download list","magenta")
print(video_or_list)
video_or_list = input(">>>")


if video_or_list == "1":
    # get url for download
    url_msg = colored("Enter The URL : ","cyan")
    print(url_msg)
    url = input(">>> ")
    print(loading_msg)

    # get video from youtube
    try:
        v = pafy.new(url)
        print("#"*80)
        title = v.title
        print("Title : "+title)
        print("#"*80)
    except Exception as e:
        e = colored(e,"red")
        print(e)
        sys.exit()


    # choise bettwen video and audio
    ch = '''
    [1] Video | Ex :mp4
    [2] Audio | Ex :mp3
    '''
    ch = colored(ch,"cyan")
    print(ch)

    choiseDownload = colored("Choose Video | Audio : ","yellow")
    print(choiseDownload)
    choiseDownload = input(">>>")

    # download 
    if choiseDownload == "1":
        Download_vid()
    elif choiseDownload == "2":
        Download_aud()
    else:
        #error choise
        error = colored("[!] Error in choise","red")
        print(error)
        sys.exit()


elif video_or_list == "2":
    
    # get url for download
    url_msg = colored("Enter The Playlist URL : ","cyan")
    print(url_msg)
    url_playlist = input(">>> ")
    print(loading_msg)

    # get playlist from youtube
    try:
        playlist = Playlist(url_playlist)
        print("#"*80)
        title = playlist.title
        videos_count = len(playlist.videos)
        print("Title : "+title)
        print("Videos Count : "+str(videos_count))
        print("#"*80)
    except Exception as e:
        e = colored(e,"red")
        print(e)
        sys.exit()

    # choise bettwen video and audio
    ch = '''
    [1] Video | Ex :mp4
    [2] Audio | Ex :mp3
    '''
    ch = colored(ch,"cyan")
    print(ch)
    choiseDownload = colored("Choose Video | Audio : ","yellow")
    print(choiseDownload)
    choiseDownload = input(">>>")

    # download 
    if choiseDownload == "1":
        try:
            os.mkdir(title)
            os.chdir(title)
        except:
            os.rmdir(title)
            os.mkdir(title)
            os.chdir(title)


        num = 1
        for i in playlist.videos:
            try:
                print("["+str(num)+f"] : Downloading: {i.title}")
                i.streams.filter(mime_type="video/mp4",progressive="True").get_highest_resolution().download()
                num+=1
            except Exception as e:
                e = colored(e,"red")
                print(e)
                sys.exit()
            

    elif choiseDownload == "2":
        try:
            os.mkdir(title)
            os.chdir(title)
        except:
            os.rmdir(title)
            os.mkdir(title)
            os.chdir(title)


        num = 1
        for i in playlist.videos:
            try:
                print("["+str(num)+f"] : Downloading: {i.title}")
                i.streams.get_audio_only().download()
                num+=1
            except Exception as e:
                e = colored(e,"red")
                print(e)
                sys.exit()
    else:
        #error choise
        error = colored("[!] Error in choise","red")
        print(error)
        sys.exit()


else:
    #error choise
    error = colored("[!] Error in choise","red")
    print(error)
    sys.exit()
