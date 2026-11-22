# Data Representation — Day 3

Day 2 introduces graphs and interactive maps in Python. Day 3 builds on these methods by bringing spatial data into Rhino and Grasshopper for mapping, terrain modelling and grid sampling. The Grasshopper examples are working files for exploration in Rhino. Their step-by-step written explanations are still to be developed.

For Python graphs and web maps, see [Day 2 — Python visualisation](../Skills%201%20-%20Day%202%20Data%20Gathering%20and%20Analysis/#python-visualisation).

## Before the workshop — Install Heron

Use the [official Heron GitHub releases](https://github.com/blueherongis/Heron/releases) to check the current version and compatibility. For this workshop, skip the Food4Rhino download and use the version listed on GitHub. [Heron v0.5.1](https://github.com/blueherongis/Heron/releases/tag/v0.5.1) is a Windows release for Rhino 8 or later.

1. In Rhino, run `PackageManager`.
2. Search for **Heron**, select the version listed on GitHub, and click **Install**. The release page also provides the packaged ZIP under **Assets** if you need the manual download.
3. Restart Rhino, open Grasshopper, and check that the **Heron** tab appears before opening the workshop files.

If you use an older version of Rhino or work on a Mac, check the compatibility notes on the release page before installing.

## Workshop sequence

1. **Bring the data into Grasshopper.** Start with a table of coordinates and check that the points land in the right place. Then add context using OpenStreetMap, a raster image or a shapefile.
2. **Add terrain.** Use the Heron examples to see how elevation data becomes a surface in Rhino.
3. **Work with a grid.** Start with the grid sampling principles, then open the full example to see how sampled values can be represented spatially.

## Rhino, Grasshopper and Heron

| Exercise | Subject | Existing examples |
| --- | --- | --- |
| 01 | **Importing Spatial Data into Grasshopper** — coordinates, OpenStreetMap, raster images and shapefiles | [Text and coordinates](Exercise%2001%20-%20Importing%20Spatial%20Data%20into%20Grasshopper/01%20-%20Text%20and%20Coordinates), [OpenStreetMap](Exercise%2001%20-%20Importing%20Spatial%20Data%20into%20Grasshopper/02%20-%20OpenStreetMap), [raster images](Exercise%2001%20-%20Importing%20Spatial%20Data%20into%20Grasshopper/03%20-%20Raster%20Images), [shapefiles](Exercise%2001%20-%20Importing%20Spatial%20Data%20into%20Grasshopper/04%20-%20Shapefiles) |
| 02 | **Terrain and Topography** — terrain data and Heron workflows | [Topography](Exercise%2002%20-%20Terrain%20and%20Topography/01%20-%20Topography), [Heron example](Exercise%2002%20-%20Terrain%20and%20Topography/02%20-%20Heron%20Example%20Files/heronexample) |
| 03 | **Grid Sampling and Spatial Analysis** — understanding a grid-based method and applying it in a larger example | [Principles](Exercise%2003%20-%20Grid%20Sampling%20and%20Spatial%20Analysis/01%20-%20Grid%20Sampling%20Principles), [full example](Exercise%2003%20-%20Grid%20Sampling%20and%20Spatial%20Analysis/02%20-%20Full%20Example) |

## Optional — Further Python analysis

| Exercise | Subject | Files |
| --- | --- | --- |
| 04 | **Image Analysis with Python** — examining visual data with Python | [Open notebook](Exercise%2004%20-%20Image%20Analysis%20with%20Python/Image%20Analysis.ipynb) |

## Working with these materials

The Grasshopper folders contain original `.gh` definitions, Rhino models and source data. They have been **reorganised but not modified**. Open the Grasshopper definitions in Rhino and check any file paths or linked resources: some definitions may still refer to the original directory structure or to local files on the author's computer.

The larger CSV, OSM, shapefile, image and Rhino files remain alongside their examples. Some duplicate datasets, temporary files and `.3dmbak` backups may be unnecessary, but have been kept until we can verify which files are needed.

We will develop the written explanations and illustrations exercise by exercise, preserving useful diagrams and outputs as we go.
