# OpenStreetMap in Grasshopper

In the previous exercise, we imported a table of recorded positions. Here we take the next step: importing **existing urban geography**. OpenStreetMap (OSM) contains more than coordinates. It describes streets, buildings and other features, together with information about what those features are.

We will use an existing OSM extract for East London and explore how **Heron** turns geographical data into Rhino / Grasshopper geometry. We will also look at how to retain and filter the information associated with that geometry.

## 1. What is OpenStreetMap?

[OpenStreetMap](https://www.openstreetmap.org/) is a collaboratively maintained geographical database. It is often used as the background for online maps, but the underlying data is much richer than the rendered map. An OSM file stores both **geometry and attributes**.

OSM organises features into three basic elements:

| Element | What it contains | Example |
| --- | --- | --- |
| **Node** | One geographical point, usually a latitude and longitude | A point of interest or a vertex of a street |
| **Way** | An ordered sequence of nodes | A street centreline or a building outline |
| **Relation** | A collection of nodes, ways or other relations with defined roles | A complex building outline, route or boundary |

Features can also have **tags**, written as pairs of keys and values. For instance, `building=yes` identifies a building feature and `highway=residential` describes a road type. The same basic geometry can contain different kinds of information depending on its tags. See the [OpenStreetMap map features reference](https://wiki.openstreetmap.org/wiki/Map_features).

A useful distinction: **the lines and polygons are geometry; the tags describe their meaning**. When importing OSM into Grasshopper, we should pay attention to both.

## 2. Explore the supplied data

The files for this exercise are:

- **[map.osm](map.osm)** — the supplied OpenStreetMap extract.
- **[4 Import OSM.gh](4%20Import%20OSM.gh)** — the original Grasshopper definition.
- **[OSM.3dm](OSM.3dm)** — the accompanying Rhino model.

Our `map.osm` file covers an area of East London close to the previous walking dataset. Its recorded bounding box extends approximately from **51.5386° to 51.5514° latitude** and **−0.03485° to −0.01485° longitude**.

The file contains approximately **26,500 nodes**, **4,600 ways** and **260 relations**. Not all of these are complete buildings or streets: some nodes are simply the vertices that make up longer features.

OSM files use a structured text format (XML). If you open the file in a text editor, you will find entries such as:

```xml
<node id="..." lat="51.54..." lon="-0.02..." />
```

and ways containing references to those nodes, together with tags. **You do not need to understand all the XML** to use the file with Heron. The important point is that the geometry and descriptive information are stored together.

## 3. Import the OSM file with Heron

Open `OSM.3dm` in Rhino and then open `4 Import OSM.gh` in Grasshopper. The saved Grasshopper file may reference a location on the original author's computer. Update the file path so that it points to your local copy of `map.osm`.

Heron provides an **Import OSM** component, which is intended to read OSM vector data and convert it to geometry within Rhino's geographical reference. In current Heron documentation, its important inputs include:

- **OSM Data Location** — the path to the OSM file.
- **Boundary** — an optional curve defining an area to import or clip.
- **Filter Fields** — keys such as `building` or `highway` that can be used to select features.
- **Filter Field,Value** — more specific filters using a key/value pair.

The component exposes **Feature Geometry**, **Fields** and **Values**, as well as a separate **Buildings** output and an **Extents** outline. This makes it possible to investigate both the spatial geometry and the metadata attached to each feature.

The supplied Grasshopper definition has not yet been inspected component by component, so use these descriptions to identify the relevant elements in your version rather than assuming the saved definition uses precisely the same component inputs.

Reference: [Heron — Import OSM](https://grasshopperdocs.com/components/heron/importOSM.html).

## 4. Check the coordinates and the model origin

OSM nodes store geographical locations using **latitude and longitude**. These are not ordinary Rhino distances. As discussed in the [previous chapter on coordinate systems](../01%20-%20Text%20and%20Coordinates/README.md#3-from-latitude-and-longitude-to-a-flat-map), they need to be converted into a suitable local model space.

Heron uses Rhino's **Earth Anchor Point** and coordinate-conversion workflow to relate geographical data to Rhino geometry. Before importing, check the model's units and geographical reference. Keep the Earth Anchor Point close to the study area to limit errors associated with approximating the curved Earth in a local flat model.

This is also an opportunity to revisit a crucial point: **Web Mercator is commonly used to display online map tiles, but that does not mean every geographical feature imported by Heron is automatically drawn in Web Mercator coordinates.** Check the actual georeferencing workflow rather than making that assumption.

When the import has completed, inspect the geometry in Rhino. Are the building outlines and streets in the expected area? Do their sizes appear reasonable? Compare a known street or building dimension with an independent map or survey reference.

## 5. Filter the urban landscape

An OSM file contains many different kinds of features. For urban analysis, we rarely need all of them at once.

Try locating these categories through the imported **fields and values**:

- `building` — footprints and building-related geometry.
- `highway` — roads, paths and other mapped routes.
- `waterway` or `natural` — selected landscape and water features, where present.

Start with **buildings**. Inspect the resulting outlines, then investigate whether Heron's building output produces additional geometry from height-related OSM tags. Not every building has reliable height information, so an outline does not automatically guarantee a correctly dimensioned 3D building.

Next, compare buildings with the **street network**. Think about which information is immediately useful for an urban-design investigation and what remains absent from the dataset.

**A question to consider:** Does a street represented by a line tell us its actual pavement width, or only the route of its centreline? How might that difference affect a drawing?

## 6. From geographical data to a drawing

Once the imported geometry is available, you can combine and represent different layers in Rhino: buildings, streets, open spaces and other features. This can become the starting point for a wider spatial investigation.

Remember that **OSM is not a survey**. Its coverage, positional accuracy, classifications and level of detail vary. A useful urban diagram may be produced from this data, but any dimensions needed for detailed design must be verified independently.

### Further reading

- [OpenStreetMap — Elements](https://wiki.openstreetmap.org/wiki/Elements)
- [OpenStreetMap — Map features](https://wiki.openstreetmap.org/wiki/Map_features)
- [Heron — Grasshopper GIS plugin](https://github.com/blueherongis/Heron)
- [RC15 Resources — Mapping and Visual Communication](../../../../Resources.md#mapping-and-visual-communication)

The next examples investigate **[raster images](../03%20-%20Raster%20Images)** and **[shapefiles](../04%20-%20Shapefiles)**, extending the range of data we can bring into Rhino and Grasshopper.
