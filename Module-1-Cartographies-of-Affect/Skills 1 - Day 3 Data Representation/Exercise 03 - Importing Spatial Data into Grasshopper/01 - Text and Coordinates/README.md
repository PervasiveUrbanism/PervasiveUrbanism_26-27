# Importing Text Files and Coordinates into Grasshopper

A dataset becomes spatially meaningful when we can connect its measurements to locations. In this example, we begin with a recorded walk and work towards representing the data in **Rhino and Grasshopper**. The aim is to understand how a text file becomes a series of values, and how those values can eventually become geometry.

This example contains two original Grasshopper definitions:

1. **[1 Reading FIles.gh](1%20Reading%20FIles.gh)** — the starting definition for reading the data file.
2. **[2 Display Coordinates.gh](2%20Display%20Coordinates.gh)** — the follow-up definition concerned with representing coordinates.

The definitions are provided as existing workshop examples. The instructions below describe the **data and intended workflow**; open the files in Grasshopper to inspect the precise components and connections.

## 1. Start with the dataset

Download **[004RC16S.CSV](004RC16S.CSV)** and open it in a text editor or spreadsheet. The file has a `.CSV` extension but is actually **tab-separated**, so each tab marks a new column. It contains a sequence of measurements recorded during a walk.

| Column | Meaning |
| --- | --- |
| `Count` | Measurement sequence |
| `Date`, `Time` | Date and time of the reading |
| `Lat`, `Long` | Geographical coordinates |
| `Speed` | Recorded speed |
| `Altitude` | Recorded elevation |
| `GSR` | Galvanic skin response sensor reading |

The first row of values begins with `Lat = 51.547253`, `Long = -0.023358` and `GSR = 379`. These coordinates refer to a location in London. Notice that latitude and longitude are **decimal-degree coordinates**, not distances measured in metres.

Before making geometry, check the file's structure: do the headings match the columns, are the numbers consistent, and are any readings missing? Treat the sensor fields as recorded measurements rather than assuming that their calibration or units are known.

## 2. Read the text in Grasshopper

Open **`1 Reading FIles.gh`** in Rhino 8 / Grasshopper. Find the component used to select or read an external file and point it to the accompanying `004RC16S.CSV` on **your own computer**. The saved definition may still contain a path from the original author's machine.

Follow the data through the definition, observing how the incoming text is divided into **rows** and **columns**. Since this file is tab-separated, it should be split at tabs rather than commas. Look for the distinction between the **header row**, which contains names, and the **data rows**, which contain the measurements.

Use Grasshopper Panels to inspect intermediate results as you follow the wires. At this stage, our aim is to **read and understand the data**, not to generate complex geometry.

## 3. From coordinates to geometry

Next, open **`2 Display Coordinates.gh`**. Locate the parts of the definition that use the `Lat` and `Long` columns, and see how the recorded positions are represented in Rhino.

An important distinction: **geographical coordinates are not ordinary Rhino X/Y coordinates**. Latitude and longitude are angular values in degrees, while a Rhino model normally works in a planar coordinate system with defined length units. For an accurately scaled spatial drawing, the coordinates must be **transformed to a suitable projected coordinate system** (for London, a British National Grid workflow is one option), or placed through a geospatial tool such as Heron that handles the appropriate conversion. Simply using longitude as X and latitude as Y produces a schematic plot, not a metric map.

When you inspect the result in Rhino, ask yourself whether the geometry is correctly located and scaled, or merely shows the relative sequence of values.

## 4. Think about the recorded walk

The dataset offers more than a route. Each geographical position is associated with a moment in time and other measurements, including GSR. Later, these values can influence the **size, colour, height or another property of the geometry**. But first, establish a dependable relationship between the table and the spatial representation.

Consider: Do the points follow the expected route? Are successive coordinates repeated? Do the time and distance between measurements make sense? What information might be lost if we draw the walk as a single continuous line?

## Files and further resources

The original `.gh` definitions and dataset have been retained without modification. These notes are an introduction to exploring them rather than a verified component-by-component reconstruction.

For geographical data, QGIS and Heron, see the [RC15 Resources — Mapping and Visual Communication](../../../../Resources.md#mapping-and-visual-communication). The next examples introduce [OpenStreetMap](../02%20-%20OpenStreetMap), [raster images](../03%20-%20Raster%20Images) and [shapefiles](../04%20-%20Shapefiles).
