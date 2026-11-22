# Data Representation — Day 3

Day 2 introduces graphs and interactive maps in Python. Day 3 builds on these methods by bringing spatial data into Rhino and Grasshopper for mapping, terrain modelling and grid sampling. The Grasshopper examples are working files for exploration in Rhino.

For Python graphs and web maps, see [Day 2 — Python visualisation](../Skills%201%20-%20Day%202%20Data%20Gathering%20and%20Analysis/#python-visualisation).

## Before the workshop — Install Heron

Use the [official Heron GitHub releases](https://github.com/blueherongis/Heron/releases) to check the current version and compatibility. For this workshop, skip the Food4Rhino download and use the version listed on GitHub. [Heron v0.5.1](https://github.com/blueherongis/Heron/releases/tag/v0.5.1) is a Windows release for Rhino 8 or later.

1. In Rhino, run `PackageManager`.
2. Search for **Heron**, select the version listed on GitHub, and click **Install**. The release page also provides the packaged ZIP under **Assets** if you need the manual download.
3. Restart Rhino, open Grasshopper, and check that the **Heron** tab appears before opening the workshop files.

If you use an older version of Rhino or work on a Mac, check the compatibility notes on the release page before installing.

## Workshop sequence

### Exercise 01 — Importing Spatial Data into Grasshopper

1. [Text and Coordinates](Exercise%2001%20-%20Importing%20Spatial%20Data%20into%20Grasshopper/01%20-%20Text%20and%20Coordinates) — Read a table of coordinates and check that the points land in the right place.
2. [OpenStreetMap](Exercise%2001%20-%20Importing%20Spatial%20Data%20into%20Grasshopper/02%20-%20OpenStreetMap) — Bring in map features for spatial context.
3. [Raster Images](Exercise%2001%20-%20Importing%20Spatial%20Data%20into%20Grasshopper/03%20-%20Raster%20Images) — Add a background image.
4. [Shapefiles](Exercise%2001%20-%20Importing%20Spatial%20Data%20into%20Grasshopper/04%20-%20Shapefiles) — Import vector geometry from a shapefile.
5. [Topography](Exercise%2001%20-%20Importing%20Spatial%20Data%20into%20Grasshopper/05%20-%20Topography) — Use Heron to turn elevation data into terrain in Rhino.
6. [Heron Example Files](Exercise%2001%20-%20Importing%20Spatial%20Data%20into%20Grasshopper/06%20-%20Heron%20Example%20Files/heronexample) — Explore the bundled Rhino and Grasshopper example.

### Exercise 02 — Grid Sampling and Spatial Analysis

1. [Grid Sampling Principles](Exercise%2002%20-%20Grid%20Sampling%20and%20Spatial%20Analysis/01%20-%20Grid%20Sampling%20Principles) — Count the points that fall within each grid cell.
2. [Full Example](Exercise%2002%20-%20Grid%20Sampling%20and%20Spatial%20Analysis/02%20-%20Full%20Example) — Explore two ways to represent sampled values using the Topography and Density Dots Grasshopper definitions.

### Exercise 03 — Image Analysis with Python (optional)

Use the [Image Analysis notebook](Exercise%2003%20-%20Image%20Analysis%20with%20Python/Image_Analysis.ipynb) to examine visual data in Python.

## Working with these materials

The Grasshopper folders contain `.gh` definitions, Rhino models and source data. Open the example’s Rhino model, then load its Grasshopper definition. If a file input still points to an older location or to the author’s computer, update it to use the source file in the example folder.

The larger CSV, OSM, shapefile, image and Rhino files remain alongside their examples. Some duplicate datasets, temporary files and `.3dmbak` backups may be unnecessary, but have been kept until we can verify which files are needed.
