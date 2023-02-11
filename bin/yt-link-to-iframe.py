# -*- coding: utf-8 -*-
import sys

def youtube_link_to_iframe(line):
    if not line.strip().startswith("https://www.youtube.com/watch?v="):
        return line
    video_id = line.strip().split("v=")[1]
    if "&" in video_id:
        video_id = video_id.split("&")[0]
    iframe = f'<iframe width="100%" height="315" src="https://www.youtube.com/embed/{video_id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in- picture; web-share" allowfullscreen></iframe>'
    return iframe + "\n"

filename = sys.argv[1]
with open(filename, "r") as f:
    lines = f.readlines()

with open(filename, "w") as f:
    for line in lines:
        f.write(youtube_link_to_iframe(line))
