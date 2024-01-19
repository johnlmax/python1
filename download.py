from pytube import YouTube

def download_video(video_url, save_path):

    # Create You Tube object from pytube library
    yt = YouTube(video_url)

    # Get highest resolution stream
    video_stream = yt.streams.get_highest_resolution()

    # Download Video
    video_stream.download(output_path = save_path)
    
video_link = "https://youtu.be/ujNeHIo7oTE%22"
save_path = "videos"
    
download_video(video_link, save_path)