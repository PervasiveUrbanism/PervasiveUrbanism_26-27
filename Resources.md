# Resources and Skills Module: Pervasive Urbanism 2025–26

This document provides additional support for the **Skills Module 2025/26**. It is organized into the following sections:

1. [**Main Software Packages:**](#SoftwarePackages)
   Details the core software required for the Skills Module 2025/26.

2. [**Learning Resources:**](#Learning)
   A summary of recommended online resources to support your skills.

3. [**Open-Source Data:**](#Data)
   A collection of links to publicly accessible datasets.

4. [**Optional Software Packages & Web Services:**](#Extra)
   Optional tools and services not covered in the 2025/26 Skills Module.

5. [**Arduino Components and Sensors**](#Sensor)
   Links to key manufacturers and retailers of Arduino parts and sensors.

---

<a name="SoftwarePackages"></a>

## 1. Main Software Packages

Please download and install the following software:

### Rhino / Grasshopper

* **Rhino:**
  Rhino 8 and Grasshopper are available through the educational license linked to your UCL account.

* **Plug-ins:**
  Rhino 8 / Grasshopper plug-ins can be found on [Food4Rhino](https://www.food4rhino.com/). Below is a non-exhaustive list of plug-ins we will use:

  * **Elk:** Import data from [OpenStreetMap](https://www.openstreetmap.org/#map=15/51.5390/-0.0177) into Rhino.
  * **Bison:** Analyze terrain meshes.
  * **Firefly:** Integrate network protocols and Arduino sensors with Grasshopper.
  * **Culebra:** Agent-based simulation.
  * **Pufferfish:** Transformations and morphing tools.
  * **Lunchbox:** Versatile geometry and data utilities.
  * **Heron:** Mapping and geolocation tools.
  * **Human:** Display and visualization components.

### Python

We will use **Python 3.x**, available from the official [Python](https://www.python.org/) website.

* **IDE:**
  We will primarily use **[VS Code](https://code.visualstudio.com/)**, with **[Google Colab](https://colab.research.google.com/)** as an alternative.

  * **[Google Colab](https://colab.research.google.com/):** Browser-based, easy to start; free with an optional paid tier for more compute.
  * **[VS Code](https://code.visualstudio.com/):** Requires local Python and libraries. Supports **[GitHub Copilot](https://github.com/features/copilot)** for AI-assisted code completion (free with your UCL account; highly recommended).

### Graphics Reference

Reference sites for inspiration:

* [**Asset Library**](https://shop.studioinnate.com/product/cyberpunk-asset-pack/)
* [**Gmunk**](https://gmunk.com/OBLIVION-GFX)
* [**Ryoji Ikeda**](https://www.ryojiikeda.com/)
* [**Refik Anadol**](https://refikanadol.com/)

**Maps and Infographics**

Creating readable, beautiful maps that clearly communicate information is not as easy as it sounds. There are many references available, but I always return to the website of [**Morphocode**](https://morphocode.com/), which offers excellent blog posts, refernce maps and educational PDFs:

* Blog post: **[Location and Time: Urban Data Visualisation](https://morphocode.com/location-time-urban-data-visualization/)**
* PDF / Ebook: **[Urban Cartography](https://morphocode.com/wp-content/uploads/resources/morphocode-urban-cartography-ebook-web.pdf)**
* Blog post: **[Using Colors in Maps](https://morphocode.com/the-use-of-color-in-maps/)**



### Adobe

Your UCL account includes an **educational license** for Adobe Creative Cloud. Please install the relevant applications (e.g., Photoshop, Illustrator, After Effects, Premiere Pro) ahead of time.

### Online storage & backup

From experience, groups work most effectively with **shared online storage** (e.g., Dropbox, Google Drive, OneDrive), ensuring everyone has consistent access to the latest files.
UCL provides each student with **100 GB** of cloud storage, which may not be sufficient for all coursework—consider arranging additional space if needed.

Hardware can fail and laptops can be stolen. **Missed submissions due to data loss are not considered valid excuses.** Always ensure your work is securely stored and **regularly backed up**.
Online storage solutions provide peace of mind, as your data remain safe—services like **Dropbox**, for example, allow you to recover accidentally deleted files for up to a year (with an extended recovery option).

Alternatively, a **home-based storage system** such as the [**Synology BeeStation**](https://bee.synology.com/en-us/BeeStation) offers a hybrid setup: local file access at home combined with cloud backup and a sharing system similar to Dropbox.




<a name="Learning"></a>

# 2. Learning Resources

## LinkedIn Learning Foundations RC15

Each student will receive an invite to follow a curated set of LinkedIn Learning tutorials. **The RC15 Foundations learning paths** provide the groundwork for the year. While some topics also appear in the Skills Tutorials, those sessions are compressed — reviewing resources in advance makes the live sessions easier to follow and deepens your understanding.

Some topics are not part of the Skills Tutorials but are **highly valuable**—for example, working effectively in teams, presenting with confidence, or using principles of color and layout in presentations.

### RC15 Foundations 1 – 3D Modelling

Introduces **Rhino** and **Grasshopper** as core modelling tools. Early familiarity lets you focus on design thinking rather than technical hurdles.

### RC15 Foundations 2 – Coding and Physical Computing

Covers **Python** and **Arduino** basics to analyse data, prototype interactions, and connect digital processes with physical devices.

### RC15 Foundations 3 – Visual Communication & Presentation

Focuses on clear, persuasive communication: from design principles to storytelling and teamwork—turning projects into compelling narratives.

*Being familiar with the basics beforehand will make the skills modules smoother to follow.*

## O’Reilly

[O’Reilly](https://www.oreilly.com/) offers books and video tutorials with a strong focus on computing and data. Free for UCL students—excellent for **advanced topics**.

## Rhino / Grasshopper

Download the official [tutorials and user manuals](https://www.rhino3d.com/en/tutorials/).
For Grasshopper, see this [curated selection](https://www.grasshopper3d.com/page/tutorials-1). Recommended: **ModeLab** PDFs and resources by **Zubin Khabazi**.

Consider *Arturo Tedeschi’s* **Algorithms-Aided Design (AAD)** for practical examples.
Check **Jose Sanchez’s** [YouTube channel](https://www.youtube.com/channel/UC5dMacit2C5fYiS4lMNq3ow) (still valuable though slightly dated).
Explore **[Rhino Secrets](http://runxel.xyz/rhino-secrets/)** for tips and tricks.

## Python

A curated, tried-and-tested set:

* *Automate the Boring Stuff with Python* — free [online](https://automatetheboringstuff.com/#toc).
* [W3Schools Python](https://www.w3schools.com/python/) — concise reference.

## Arduino

* **Exploring Arduino** — Jeremy Blum
  A strong introduction blending hands-on electronics with programming fundamentals.
* **Programming Arduino: Getting Started with Sketches** — Simon Monk (Intermediate)
  In-depth C/Arduino programming concepts for those ready to level up.
* **Programming Arduino: Next Steps** — Simon Monk (Advanced)
  Optimisation techniques (less relevant to RC15, but excellent background reading).

---

<a name="Data"></a>

## 3. Open-Source Data

### Earth Vector Files

[Natural Earth](https://www.naturalearthdata.com/) — public domain map datasets at 1:10m, 1:50m, and 1:110m scales.

### OpenStreetMap (OSM)

* Export via [OpenStreetMap](https://www.openstreetmap.org/export).
* For larger extracts, use [Geofabrik](https://www.geofabrik.de).
* Learn about extractable [Map Features](https://wiki.openstreetmap.org/wiki/Map_Features).

### Edina

[Digimap](https://digimap.edina.ac.uk/) — online mapping for UK higher education. Provides well-maintained UK geodata (e.g., DEFRA), though not its own imagery.

### USGS Earth Explorer

[USGS Earth Explorer](https://earthexplorer.usgs.gov) — primary source for global aerial and satellite imagery.

### European Space Agency (ESA)

[Copernicus Open Access Hub](https://scihub.copernicus.eu/dhus/#/home) — extensive satellite imagery archive (often better European coverage than USGS).

### EOS Land Viewer

[EOS Land Viewer](https://eos.com/landviewer/) — free tier for downloading and analysing satellite imagery (e.g., greenness, land-use).

### NASA

[EarthData](https://earthdata.nasa.gov/) — NASA’s comprehensive open data portal.

<!--
### Department for Environment, Food and Rural Affairs (DEFRA)  
[DEFRA](https://environment.data.gov.uk) — 3D topography (heightmaps and point clouds) for the UK, compatible with QGIS raster tools.

### Google Earth Engine & Microsoft Planetary Computer  
[Google Earth Engine](https://earthengine.google.com/) and [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com/) — large satellite libraries and cloud processing (application required). Good for regional studies (~30m/pixel).

### London / UK  
- [London Data Store](http://data.london.gov.uk/)  
- [Data Gov UK](https://data.gov.uk/)  
- [Planning London Datahub](https://www.london.gov.uk/programmes-strategies/planning/digital-planning/planning-london-datahub?ac-60574=60568)  
- [London Air](https://www.londonair.org.uk/LondonAir/Default.aspx)  
- [TFL Open Data](https://tfl.gov.uk/info-for/open-data-users/our-open-data#on-this-page-10)

### General Blog with UK Databases  
[Geospatial Wandering](https://geospatialwandering.wordpress.com/gis-data-sources/)
-->

---

<a name="Extra"></a>

## 4. Additional Software Packages and Web Services

### QGIS

[QGIS](https://qgis.org/en/site/index.html) is a free, open-source GIS for maps, satellite imagery, shapefiles, and databases. It supports many formats and can export DXF/PDF. While predominantly 2D and less polished than some commercial tools (e.g., ArcGIS), RC15 has historically **actively supported QGIS** and can offer help. Many practices favour QGIS after graduation due to its **free license**.

* **Plug-ins** (via QGIS Plugin Manager):

  * **Flickr Metadata Downloader** — Search and download geotagged Flickr images.
  * **MMQGIS** — Hexagon grids, Voronoi, and more.
  * **QuickOSM** — Pull OSM data directly.
  * **TimeManager / Time Series** — Create and export animations.
  * **TravelTime Platform** — Accessibility analyses.
  * **QNEAT3** — Network analysis.

Helpful resources:

* [Patrick Stotz – Mapping 101](https://github.com/PatrickStotz/mapping_101)
* [Gentle Introduction to GIS](https://docs.qgis.org/3.40/en/docs/gentle_gis_introduction/index.html)
* [Training Manual](https://docs.qgis.org/3.22/en/docs/training_manual/index.html)
* [Terrain Analysis](https://docs.qgis.org/2.14/en/docs/training_manual/rasters/terrain_analysis.html)
* [GIS Stack Exchange](https://gis.stackexchange.com/) — for specific questions.

### Sublime Text Editor

[Sublime Text](https://www.sublimetext.com/) — fast, capable text editor that handles very large files.

### vvvv

[**vvvv gamma**](https://visualprogramming.net/) — powerful visual live-programming environment based on C#. Free for non-commercial use. A major competitor is TouchDesigner (its free tier has some limitations).

Find numerous example files within the vvvv installation. Another great resource is the free course from the [Node Institute (Berlin)](https://thenodeinstitute.org/courses/node20-vvvv-workshop-bundle/). The community is small but supportive—use the forum or the “Element” group for questions.

**vvvv** integrates multiple platforms, including a **game engine (Stride)**, a **2D drawing environment (Skia)**, and various powerful libraries such as **OpenCV**. The built-in game engine provides functionality comparable to **Unity** or **Unreal**, but with a key difference — it can be **seamlessly combined with other libraries and data sources**.

For example, reading an **Arduino signal** inside Unity that controls a **Grasshopper definition**—which in turn modifies geometry in **real-time VR**—is possible but complex in Unity. In **vvvv**, such cross-platform communication can be set up **much more easily**.

Overall, **vvvv** tends to produce **more abstract and experimental graphics**, which align well with the aesthetic and conceptual direction of **RC15**.
 

### Sensor Log

[Sensor Log](http://sensorlog.berndthomas.net/) — iPhone app that turns your phone into a **multi-sensor** device.

### D5

[D5](https://www.d5render.com/) — real-time rendering engine (similar to Enscape/Twinmotion) with educational licenses that unlock all features.

### Mapbox Studio

[Mapbox Studio](https://www.mapbox.com/mapbox-studio) — design custom map styles; can be used as backgrounds in QGIS. The free tier is generous and sufficient for coursework.
How-to: [Use Mapbox backgrounds in QGIS](https://docs.mapbox.com/help/tutorials/mapbox-arcgis-qgis/).

### Kepler GL

[Kepler GL](https://kepler.gl/) — web-based tool for quick, attractive geo-visualisations; simple, fast, and free. It has a python integration as well.

### Ped Catch

[Ped Catch](http://pedcatch.com/) — generates pedestrian network diagrams that account for slopes; results can be exported to QGIS.

### Google Earth and Google Earth Studio

* [Google Earth](https://earth.google.com) — capture screenshots.
* [Google Earth Studio](https://www.google.com/earth/studio/) — create **flythroughs and animations**; useful for presentations and even 3D point-cloud reconstruction with Autodesk Recap.

### Best Time

[Best Time](https://besttime.app/) — foot-traffic data for locations worldwide (UI and API). Free tier available.

---

<a name="Sensor"></a>

## 5. Arduino Components and Sensors

* [Arduino (Official)](https://www.arduino.cc/)
* [SparkFun](https://www.sparkfun.com/)
* [Seeed Studio](https://www.seeedstudio.com)
* [Robot Shop](https://uk.robotshop.com/)
* [The Pi Hut](https://thepihut.com/)
* [Adafruit](https://www.adafruit.com/)
* [Pimoroni](https://shop.pimoroni.com/)
* [DFRobot](https://www.dfrobot.com/)
* [LilyGO](https://www.lilygo.cc/)
