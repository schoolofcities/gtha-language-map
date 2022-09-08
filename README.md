# language-map-gtha-2021

## Objective:

Create an interactive map that visualizes the linguistic diversity of the Greater Toronto and Hamilton Area using recently released 2021 Census Data.

This will support our upcoming work in the [Strategic Plan](https://www.schoolofcities.utoronto.ca/sites/www.schoolofcities.utoronto.ca/files/UofT_SchoolofCities_StrategicPlan_FINAL.pdf) on belonging, migration, and thriving


### Examples:

There is this simple popular map, but id doesn't show variation within neighbourhoods:
[link](https://twitter.com/sound_language/status/1560616441849733120)

There was a dot map of languages created a few years ago, but it doesn't seem to be working anymore?
[link](http://vt.anagraph.io/recensement/languesmaternelles/)
[link](https://googlemapsmania.blogspot.com/2017/08/the-dot-map-of-canadian-languages.html)

These are just for the City of Toronto, and not languages, but are quite well done
[link](https://jonathancritchley.ca/todot.html)

## Steps

0 - Do a bit of research to see what other examples there are out there online, beyond the couple I noted above. Even if they aren't focused on Toronto, it would be great to see how linguistic diversity has been mapped in other parts of the world

1 - Download and familiarize yourself with [census data](https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/index.cfm?Lang=E) and [geographic boundaries](https://www12.statcan.gc.ca/census-recensement/2021/geo/index-eng.cfm). I think we can use the smallest geographic boundaries (called Dissemination Areas). Try QGIS for quickly exploring the spatial boundaries.

2 - Filter the census data to just the language variables and join it to Dissemination Area boundaries. I have some code for filtering the data. 

3 - Create a few exploratory maps of common languages across the region (try choropleths, dot density, maybe something else?). The goal here will be for us to better understand patterns and think what the most effective way will be to visualize the data.

4 - Decide what the best tech stack will be to create the interactive website (e.g. vector or raster tiles, any Javascript framework?, etc.)

5 - Think about how difficult it would be scale this to just being a map of the Toronto region, to a map of all of Canada.

6 - Build the site. 