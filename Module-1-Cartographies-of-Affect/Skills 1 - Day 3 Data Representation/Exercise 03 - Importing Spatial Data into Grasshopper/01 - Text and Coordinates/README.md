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

## 3. Understanding Coordinates, Coordinate Systems and Map Projections

Our dataset includes the location `51.547253, -0.023358`. We recognise this as a position in London, and it looks like a pair of numbers that could be entered directly into Grasshopper's **Construct Point** component. But doing so would not place the point correctly in a model measured in metres. To understand why, we need to distinguish **geographical coordinates**, **projected coordinates** and **Rhino's model coordinates**.

### Latitude and longitude: a position on the Earth

Imagine the Earth as a globe. We describe positions on its curved surface using two angles:

- **Latitude** tells us how far north or south a place is from the Equator. It ranges from −90° to +90°.
- **Longitude** tells us how far east or west a place is from the Greenwich meridian. It ranges from −180° to +180°.

Our first recorded point is approximately **51.547° north, 0.023° west**. These are **degrees**, not metres. One degree of latitude corresponds to roughly 111 km, but the distance represented by a degree of longitude changes with latitude. A degree of longitude becomes progressively shorter towards the poles.

Coordinates also need a **reference system** to define precisely what they mean. GPS-style latitude and longitude are commonly expressed using **WGS 84**, identified as **EPSG:4326**. An EPSG code is a convenient identifier for a coordinate reference system (CRS). The two numbers alone do not tell us which CRS was used, so we must check the data source. For this exercise, we treat the recorded values as WGS 84-style geographical coordinates.

### Why do we need map projections?

Rhino works in a flat, three-dimensional **Cartesian space**, with X, Y and Z axes. Its coordinates represent distances in the model's chosen units, usually millimetres or metres. The Earth, however, is curved.

A **map projection** provides a mathematical method for representing positions on the curved Earth on a flat plane. Imagine trying to flatten the surface of a globe onto a sheet of paper. Something must change: depending on the projection, there will be distortions of **shape, area, distance or direction**. There is no single projection that perfectly preserves everything everywhere.

For a city-scale investigation, we usually choose a **projected coordinate reference system** appropriate to the location and purpose. It gives us coordinates in linear units, allowing us to work with distances and spatial geometry.

### Three coordinate spaces

| Coordinate space | Example / identifier | Units | What it tells us |
| --- | --- | --- | --- |
| **Geographic CRS** | WGS 84 — `EPSG:4326` | Degrees | Latitude and longitude on the Earth |
| **Projected CRS** | British National Grid — `EPSG:27700` | Metres | Easting and northing for locations in Great Britain |
| **Rhino model space** | X, Y, Z | Model units (choose metres for this workflow) | Position of geometry relative to a model origin |

The **British National Grid** is a useful choice for London because it provides easting and northing in metres. Other locations require different projected systems: Berlin, for example, would not normally use the British National Grid.

**Important:** `EPSG:4326` and `EPSG:27700` are not alternative labels for the same numbers. Changing the label does **not** convert the coordinates. They refer to different ways of expressing locations, based on different coordinate reference systems. The coordinates must be **transformed** correctly, including the appropriate projection and datum transformation.

### What happens if we use longitude as X and latitude as Y?

Suppose we connect our dataset directly to Grasshopper using `X = Long`, `Y = Lat` and `Z = 0`. Grasshopper can draw points, but their X/Y coordinates would be tiny angular values such as `(-0.023358, 51.547253)`, not metre-based positions in London.

The resulting geometry might resemble the route if we zoom in far enough, but **distances, scale and orientation cannot be trusted as a metric map**. Multiplying every degree by a single constant does not solve the problem, since degrees of latitude and longitude represent different ground distances.

### A practical workflow: from GPS to Rhino

1. **Identify the source CRS.** For latitude/longitude collected by GPS, this is commonly WGS 84 (`EPSG:4326`), but check the documentation.
2. **Choose a suitable projected CRS.** For our London dataset, we can use British National Grid (`EPSG:27700`).
3. **Transform the coordinates**, for example in **QGIS**, or with a properly configured geospatial workflow in Python or Grasshopper/Heron. In QGIS, assigning a layer's CRS tells the software how to interpret existing numbers; **reprojecting/exporting** into a target CRS calculates new coordinates. These are different operations.
4. **Bring the projected X/Y values into Rhino**, setting the model units to metres. Easting becomes X and northing becomes Y.
5. **Choose a local origin if needed.** National-grid coordinates can be very large; subtracting one fixed easting/northing origin from every point moves the geometry closer to Rhino's `(0, 0)` while preserving local distances. Record the original CRS and the translation so the points can be placed back in their real-world position.

A small but important additional distinction: the dataset's `Altitude` column is not automatically compatible with every map projection or height reference. For our first exercise, we can work in **2D** with `Z = 0`. Later, when introducing topography, we will need to consider elevation units and vertical reference systems too.

**The essential lesson:** Latitude and longitude tell us *where* something is on Earth; projected coordinates let us work with that location in a measured drawing. Before generating geometry, always ask **which CRS, which units and which origin?**

For further reading, see [Ordnance Survey's explanation of coordinate reference systems](https://docs.os.uk/osngd/getting-started/os-ngd-fundamentals/coordinate-reference-systems) and the [QGIS documentation on projections and CRS](https://docs.qgis.org/latest/en/docs/user_manual/working_with_projections/working_with_projections.html).

## 4. From coordinates to geometry

Next, open **`2 Display Coordinates.gh`**. Locate the parts of the definition that use the `Lat` and `Long` columns, and see how the recorded positions are represented in Rhino.

Use the distinctions introduced above as you inspect the definition: is it plotting angular longitude/latitude values as a **schematic visualisation**, or is it converting them into a suitable **projected coordinate system** for a metric drawing? If the definition relies on a geospatial plugin such as Heron, check which coordinate system and model origin it uses. The original Grasshopper files have not yet been inspected component by component, so do not assume that their output is already georeferenced or metrically correct.

When you inspect the result in Rhino, ask yourself whether the geometry is correctly located and scaled, or merely shows the relative sequence of values.

## 5. Think about the recorded walk

The dataset offers more than a route. Each geographical position is associated with a moment in time and other measurements, including GSR. Later, these values can influence the **size, colour, height or another property of the geometry**. But first, establish a dependable relationship between the table and the spatial representation.

Consider: Do the points follow the expected route? Are successive coordinates repeated? Do the time and distance between measurements make sense? What information might be lost if we draw the walk as a single continuous line?

## Files and further resources

The original `.gh` definitions and dataset have been retained without modification. These notes are an introduction to exploring them rather than a verified component-by-component reconstruction.

For geographical data, QGIS and Heron, see the [RC15 Resources — Mapping and Visual Communication](../../../../Resources.md#mapping-and-visual-communication). The next examples introduce [OpenStreetMap](../02%20-%20OpenStreetMap), [raster images](../03%20-%20Raster%20Images) and [shapefiles](../04%20-%20Shapefiles).
