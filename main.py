from pytube import YouTube
import click


def _download_video(url, name, path):
    yt = YouTube(url)
    for item in yt.streams:
        print(item.resolution)
    stream = yt.streams.filter(resolution="720p").first()
    extension = stream.mime_type.split("/")[-1]
    stream.download(filename=f"{name}.{extension}", output_path=path)


@click.command()
@click.option('--path', default=None, help="Defines the path for saving the output file")
@click.option('--name', default=None, help='Defines the name of the output file')
@click.argument("link")
def download_video(link, name, path):
    """Simple program to download Youtube videos from command line."""
    _download_video(link, name, path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    download_video()
