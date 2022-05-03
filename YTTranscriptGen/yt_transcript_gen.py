"""
In this Script we will be getting the subtitles and captions
from a youtube video

Install youtube-transcript-api
if you use anaconda:
    conda install -c conda-forge youtube-transcript-api
otherwise:
    pip install youtube-transcript-api # for windows
    pip3 install youtube-transcript-api # for Linux and MacOs

Documentation for youtube transcript api:
    https://pypi.org/project/youtube-transcript-api/

"""

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api.formatters import WebVTTFormatter


def main():
    vid_id = "1b-ofhkH2po"
    base_lang = "es"
    wanted_lang = "en"

    transcripts = YouTubeTranscriptApi.list_transcripts(vid_id)
    # print(transcripts)

    # now that we know what languages are available
    # we can get the actual transcript object
    base_obj = transcripts.find_transcript([base_lang])
    base_tran = base_obj.fetch()

    # print(base_tran)

    # Now we can get our transcript
    fmt = TextFormatter()
    base_txt = fmt.format_transcript(base_tran)
    print("Writing {} Transcript ...".format(base_lang), end="")
    with open("transcripts/{}_transcript.txt".format(base_lang), "w") as f:
        f.write(base_txt)
    print("DONE")

    # translate to another language
    if base_obj.is_translatable:
        wanted_tran = base_obj.translate(wanted_lang).fetch()
    else:
        print("CAN NOT translate transcript to {}".format(wanted_lang))
        quit()

    # print(wanted_tran)

    # Print our translated transcript
    wanted_txt = fmt.format_transcript(wanted_tran)
    print("Writing {} Transcript ...".format(wanted_lang), end="")
    with open("transcripts/{}_transcript.txt".format(wanted_lang), "w") as f:
        f.write(wanted_txt)
    print("DONE")

    # Get subtitles for the YT video
    fmt = WebVTTFormatter()
    wanted_subs = fmt.format_transcript(wanted_tran)
    print("Writing {} Subtitles ...".format(wanted_lang), end="")
    with open("transcripts/{}_subs.vtt".format(wanted_lang), "w") as f:
        f.write(wanted_subs)
    print("DONE")


main()
