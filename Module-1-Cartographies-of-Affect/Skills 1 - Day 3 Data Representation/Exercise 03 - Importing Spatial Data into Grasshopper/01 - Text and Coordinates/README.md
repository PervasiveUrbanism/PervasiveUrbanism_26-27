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

## 3. From Latitude and Longitude to a Flat Map

Our first recorded location is `51.547253, -0.023358`. These look like two numbers that we could connect directly to a Grasshopper **Construct Point** component. But they are not ordinary X and Y distances. To understand why, we need to look at what latitude and longitude mean and how online maps display them.

### How far is one degree?

Imagine two people standing on the Equator, one at longitude 0° and the other at longitude 1°. They are approximately **111 km apart**. Now imagine the same one-degree change in longitude in London: the separation is only about **69 km**. Near the poles, lines of longitude converge, so the distance corresponding to one degree of longitude approaches zero.

**Latitude behaves differently.** Moving one degree north or south corresponds to roughly **111 km** almost everywhere on Earth.

| Change of geographical coordinates | Approximate ground distance |
| --- | ---: |
| 1° of **latitude**, in London | 111 km |
| 1° of **longitude**, at the Equator | 111 km |
| 1° of **longitude**, in London | 69 km |

Why? Lines of latitude run around the globe in circles, and those circles become smaller towards the poles. By contrast, a degree of latitude moves us along a north–south meridian. The figures above are rounded: the exact distances also depend slightly on the Earth's shape.

**The key insight:** A degree is an **angle**, not a fixed distance. Two coordinates that differ by `1` do not necessarily represent the same distance on the ground. So treating longitude as X and latitude as Y in a Rhino model does not produce correctly scaled geometry.

### What is a coordinate reference system?

A **coordinate reference system (CRS)** tells software how to interpret coordinates and relate them to places on Earth. There are two types that matter for this exercise:

- A **geographic CRS** describes locations using latitude and longitude, measured in **degrees**. Our dataset is assumed to use **WGS 84 (EPSG:4326)**, the familiar geographic reference system used for GPS-style coordinates.
- A **projected CRS** describes locations on a **flat map**, using X and Y coordinates, generally measured in **metres**. It includes a **map projection**: mathematical rules that transform geographical positions into positions on a plane.

An **EPSG code** is simply an identifier that lets software recognise a particular coordinate reference system. It is not a coordinate value.

A projected CRS does more than assign another address to a place. It establishes **how the curved Earth is represented on a flat surface**, including the projection, its parameters, the coordinate axes and units. There are many projected CRSs because different projections are useful for different parts of the world and different purposes.

Flattening a curved surface always introduces some distortion. Depending on the projection, distances, areas, shapes or directions can be distorted. No flat projection represents the entire Earth perfectly.

### The example we already know: Google Maps and OpenStreetMap

When we open **Google Maps** or a typical **OpenStreetMap** web map, the geographical positions are displayed using a projection known as **Web Mercator (EPSG:3857)**. Web Mercator is widely used for online map tiles because it provides a consistent flat map that is convenient to pan and zoom.

It helps to distinguish three stages:

1. **Geographic position:** We begin with WGS 84 latitude and longitude in degrees, such as `51.547253, -0.023358`.
2. **Projected map position:** Web Mercator mathematically converts that position to **X/Y coordinates on a flat map**. EPSG:3857 coordinates are expressed in metres, but those *map metres* do not give correct ground distances everywhere.
3. **Screen position:** The mapping application then uses the map centre, zoom level and viewport size to determine **which pixels** show that location. Your screen itself does not have an EPSG coordinate system.

For example, at London's latitude the Web Mercator map enlarges local distances by roughly **1.6 times**. This is why a ruler applied directly to EPSG:3857 X/Y coordinates does not measure accurate ground distance in London. **Web Mercator is excellent for displaying interactive maps; it is not a guarantee of accurate dimensions for architectural drawings.**

Google Maps and OpenStreetMap are useful examples because we already use them, but Web Mercator is **one projection among many**, not the definition of a projected CRS.

### The same place, different numbers

Consider our London point:

| System | How the position is expressed | Units |
| --- | --- | --- |
| **WGS 84 — EPSG:4326** | Latitude `51.547253`, longitude `-0.023358` | Degrees |
| **Web Mercator — EPSG:3857** | A different pair of projected X/Y numbers | Metres in the projected map |
| **Rhino model** | Local X/Y/Z values relative to the chosen model origin | Rhino model units |

All three can refer to **the same place**, but their numbers are **not interchangeable**. If you take a longitude/latitude pair from EPSG:4326 and simply tell software that it is EPSG:3857, you have *not* projected it: you have mislabelled the numbers and the point will be misplaced.

A **coordinate transformation** calculates the numbers needed for the target system. Similarly, if two datasets are expressed in different CRSs, you cannot safely combine their X/Y values until they have been brought into a common reference system.

### How does this relate to Rhino and Heron?

Rhino has an ordinary **Cartesian model space**: X, Y and Z are distances measured in the model's chosen units. It does not automatically know that a value is a latitude or longitude.

**Heron** helps connect geographical data to Grasshopper. Its documented **Decimal Degrees to XY** component converts WGS 84 latitude/longitude to X/Y points within Heron's georeferencing workflow; its **Coordinate Transformation** component can transform between explicitly specified coordinate systems. The conversion and the chosen Rhino origin need to be understood together. Do not assume that the output of every Heron component is automatically in EPSG:3857 simply because online map tiles commonly use Web Mercator.

For our example, the intended sequence is:

1. **Read the CSV** and identify its `Lat` and `Long` columns.
2. **Confirm the geographic CRS** of those coordinates (here we assume WGS 84, EPSG:4326).
3. **Use a configured geographical conversion** in Heron (or another suitable geospatial tool) to translate those locations into positions that Rhino can use.
4. **Check units, orientation and model origin.** A local origin makes it easier to work with geometry near Rhino's `(0, 0)`, but the geographic relationship must be retained.
5. **Compare with a known location** in Google Maps or OpenStreetMap to check the placement. If accurate metric dimensions are required, also confirm the coordinate system's distance distortions and suitability for the study area.

The dataset also includes an `Altitude` field, but this introduces another question: the vertical reference and height units. We will work with the points in **2D (`Z = 0`)** initially and return to elevations in the topography exercise.

**Remember:** **Latitude/longitude locates a point on Earth → a map projection places it on a flat map → the mapping application displays it in pixels, or we bring suitable transformed coordinates into Rhino's model space.** These are connected operations, but they are not the same thing.

For further reading, see [Google Maps — Map and Tile Coordinates](https://developers.google.com/maps/documentation/javascript/coordinates), the [OpenStreetMap explanation of slippy-map tiles](https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames), and the Heron references for [Decimal Degrees to XY](https://grasshopperdocs.com/components/heron/decimalDegreesToXY.html) and [Coordinate Transformation](https://grasshopperdocs.com/components/heron/coordinateTransformation.html).

## 4. From coordinates to geometry

Next, open **`2 Display Coordinates.gh`**. Locate the parts of the definition that use the `Lat` and `Long` columns, and see how the recorded positions are represented in Rhino.

Use the distinctions introduced above as you inspect the definition: is it plotting longitude/latitude values directly as a **schematic visualisation**, or converting them into **appropriate metric geometry** using Heron? Check any spatial reference settings and the Rhino model origin. The existing Grasshopper definitions have not yet been inspected component by component, so we should not assume that their output is already geographically aligned or correctly scaled.

When you inspect the result in Rhino, ask yourself whether the geometry is correctly located and scaled, or merely shows the relative sequence of values.

## 5. Think about the recorded walk

The dataset offers more than a route. Each geographical position is associated with a moment in time and other measurements, including GSR. Later, these values can influence the **size, colour, height or another property of the geometry**. But first, establish a dependable relationship between the table and the spatial representation.

Consider: Do the points follow the expected route? Are successive coordinates repeated? Do the time and distance between measurements make sense? What information might be lost if we draw the walk as a single continuous line?

## Files and further resources

The original `.gh` definitions and dataset have been retained without modification. These notes are an introduction to exploring them rather than a verified component-by-component reconstruction.

For geographical data, QGIS and Heron, see the [RC15 Resources — Mapping and Visual Communication](../../../../Resources.md#mapping-and-visual-communication). The next examples introduce [OpenStreetMap](../02%20-%20OpenStreetMap), [raster images](../03%20-%20Raster%20Images) and [shapefiles](../04%20-%20Shapefiles).
