# googlemaps-timeline-heatmap
Create a heatmap from your google maps timeline location data, or any geographical data, as long as it's in the correct format. 
[![Google map heatline](https://img.youtube.com/vi/iwANnV8Z6sk/0.jpg)](https://www.youtube.com/watch?v=iwANnV8Z6sk)

## Google Maps TimeLine
Google Maps has a feature that tracks the location of your mobile device over time. They call this feature 'TimeLine'.
For some, it's turned on by default, for others it's not. Either way, if your device has been collecting geographical data for a while, it's an interesting source of information
to explore. Google has their own tool to explore this data, but it's more focused on day-to-day activities and specific places you visited (i.e. stores; your work).
The goal of this tool is to visualize you aggregated location data in a colorful way.

* Google Maps TimeLine: https://www.google.nl/maps/timeline

## Downloading your TimeLine data
1. Visit your Timeline: https://www.google.com/maps/timeline
2. Click the cog icon at the bottom right corner of the screen and select the option "Download a copy of all your data"
3. This will re-direct you to the Takeout site. From where you can download any personal data that google has.
4. Create a new archive selecting at least "Location history" in JSON
5. Follow steps to download archive, extract archive and replace 'locationdata.json' in this repository with your personal json file.

## Alternatively: Using your own geographical data.
This is possible if you reformat your data to a json file of the same structure as locationdata.json. Use the file in repo as an example. The geographical data itself is randomized to protect my privacy.
