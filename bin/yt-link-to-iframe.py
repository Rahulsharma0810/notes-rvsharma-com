#!/usr/bin/env python
import re

def convert_youtube_html_to_embedded_iframe(file_contents):
    youtube_html_url_pattern = re.compile(r'https://www.youtube.com/watch\?v=([a-zA-Z0-9_]+)')
    embedded_iframe_template = '<iframe width="560" height="315" src="https://www.youtube.com/embed/{}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in- picture" allowfullscreen></iframe>'

    match = youtube_html_url_pattern.search(file_contents)
    if match:
        print(f"Found match: {match.group(0)}")
    else:
        print("No match found.")

    return re.sub(youtube_html_url_pattern, lambda match: embedded_iframe_template.format(match.group(1)), file_contents)
