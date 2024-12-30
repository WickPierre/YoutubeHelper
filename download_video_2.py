import os
from pytubefix import YouTube
from pytubefix.cli import on_progress


def combine(audio: str, video: str, output: str) -> None:

    if os.path.exists(output):
        os.remove(output)

    code = os.system(
        f'ffmpeg -i "{video}" -i "{audio}" -c copy "{output}"')

    if code != 0:
        raise SystemError(code)


def download(url):
    yt = YouTube(
        proxies={"http": "http://127.0.0.1:8881",
                 "https": "http://127.0.0.1:8881"},
        url=url,
        on_progress_callback=on_progress,
    )

    video_stream = yt.streams.\
        filter(type='video').\
        order_by('resolution').\
        desc().first()

    audio_stream = yt.streams.\
        filter(mime_type='audio/mp4').\
        order_by('filesize').\
        desc().first()

    print('Information:')
    print("\tTitle:", yt.title)
    print("\tAuthor:", yt.author)
    print("\tDate:", yt.publish_date)
    print("\tResolution:", video_stream.resolution)
    print("\tViews:", yt.views)
    print("\tLength:", round(yt.length/60), "minutes")
    print("\tFilename of the video:", video_stream.default_filename)
    print("\tFilesize of the video:", round(
        video_stream.filesize / 1000000), "MB")

    print('Download video...')
    video_stream.download()
    print('\nDownload audio...')
    audio_stream.download()
    combine(audio_stream.default_filename, video_stream.default_filename, 'output.mp4')