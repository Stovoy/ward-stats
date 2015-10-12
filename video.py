import youtube_dl


def download(url, title):
    with youtube_dl.YoutubeDL({'outtmpl': 'videos/%s.mp4' % title}) as youtube_downloader:
        result = youtube_downloader.download([url])
