# Resources for Pervasive Urbanism 2026–27

This page brings together software, learning materials, workshop access, data sources and tools for RC15. Further links and resources will be added as the modules develop. Start with software setup and learning resources, then explore the references relevant to your project. Optional tools are provided for further exploration; you do not need to install everything listed here.

- [Software setup](#software-setup)
- [Learning resources](#learning-resources)
- [Mapping and visual communication](#mapping-and-visual-communication)
- [Data sources](#data-sources)
- [Workshops, equipment and components](#workshops-equipment-and-components)
- [Collaboration and backup](#collaboration-and-backup)
- [Optional tools and services](#optional-tools-and-services)

## Software setup

### Rhino / Grasshopper

* **Rhino:**
  Rhino 8 and Grasshopper are available through the educational license linked to your UCL account.

* **Plug-ins:**
  Rhino 8 / Grasshopper plug-ins can be found on [Food4Rhino](https://www.food4rhino.com/). Below is a non-exhaustive list of plug-ins we will use:

  * **Elk:** Import data from [OpenStreetMap](https://www.openstreetmap.org/#map=15/51.5390/-0.0177) into Rhino.
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
  * **[VS Code](https://code.visualstudio.com/):** Requires local Python and libraries. Supports **[GitHub Copilot](https://github.com/features/copilot)** for AI-assisted code completion (free with your UCL account).

### Adobe

Your UCL account includes an **educational license** for Adobe Creative Cloud. Please install the relevant applications (e.g., Photoshop, Illustrator, After Effects, Premiere Pro) ahead of time.
**We strongly recommend using Adobe InDesign, Illustrator and the wider Creative Cloud suite for your studio output, including weekly presentations.** InDesign supports consistent page layouts and typography; Illustrator gives you precise control over vector drawings, diagrams and maps, which remain sharp at different scales. Use Photoshop for raster images and the video tools when appropriate. Develop your presentations as carefully composed visual documents. **Please avoid PowerPoint for RC15 presentations**: our preference is for the control and graphic quality offered by an Adobe workflow, rather than standard slide templates.

### ChatGPT, Codex and other AI tools

The teaching demonstrations will primarily refer to **ChatGPT** and **Codex**, OpenAI's coding assistant. This is a practical choice for teaching, rather than a ranking of products. **Claude, Cursor and other tools are welcome**, and the principles of defining a task, guiding the model, testing and reviewing results apply across them.

We recommend **ChatGPT Plus or Claude Pro** for students who intend to use AI regularly. A paid subscription is recommended, rather than required; choose one that suits your workflow and check current features and limits before subscribing. Both can support writing, reasoning and coding. Their capabilities overlap considerably, and differences change quickly.

ChatGPT offers [image generation and editing](https://learn.chatgpt.com/docs/image-generation) alongside its conversational and coding workflows. Connected apps and plugins extend its uses, including [Figma workflows for visual assets and slide decks](https://www.figma.com/blog/slides-buzz-figma-app-in-chatgpt/). Claude is another option for writing and revising text; its [Artifacts interface](https://claude.com/features/artifacts) lets you preview and develop documents, interactive visuals and presentation-style web content alongside a conversation. Some students may prefer that interface. Try the tools on your own tasks rather than assume that one is universally better at text or code.

For coding work, use an assistant to explain unfamiliar code, develop a first implementation and help debug it, then review and test the result yourself. See [AI-assisted coding and assessment](README.md#ai-assisted-coding-and-assessment) for the RC15 expectations and acknowledgement requirements.

## Learning resources

### LinkedIn Learning

The three **RC15 Foundations** paths cover Rhino and Grasshopper, Python and Arduino, and Visual Communication & Presentation. They are required during the first three weeks. **Mapping with QGIS** is an additional recommended path. See the [README's foundation skills section](README.md#foundation-skills-for-rc15--linkedin-learning) for deadlines, UCL access, invitations and preparation requirements.

### O’Reilly

[O’Reilly](https://www.oreilly.com/) offers books and video tutorials with a strong focus on computing and data. Free for UCL students—excellent for **advanced topics**.

### Rhino / Grasshopper

Download the official [tutorials and user manuals](https://www.rhino3d.com/en/tutorials/).
For Grasshopper, see this [curated selection](https://www.grasshopper3d.com/page/tutorials-1). Recommended: **ModeLab** PDFs and resources by **Zubin Khabazi**.

Consider *Arturo Tedeschi’s* **Algorithms-Aided Design (AAD)** for practical examples.
Check **Jose Sanchez’s** [YouTube channel](https://www.youtube.com/channel/UC5dMacit2C5fYiS4lMNq3ow) (still valuable though slightly dated).
Explore **[Rhino Secrets](http://runxel.xyz/rhino-secrets/)** for tips and tricks.

### Python

A curated, tried-and-tested set:

* *Automate the Boring Stuff with Python* — free [online](https://automatetheboringstuff.com/#toc).
* [W3Schools Python](https://www.w3schools.com/python/) — concise reference.

### Arduino

* **Exploring Arduino** — Jeremy Blum
  A strong introduction blending hands-on electronics with programming fundamentals.
* **Programming Arduino: Getting Started with Sketches** — Simon Monk (Intermediate)
  In-depth C/Arduino programming concepts for those ready to level up.
* **Programming Arduino: Next Steps** — Simon Monk (Advanced)
  Optimisation techniques (less relevant to RC15, but excellent background reading).

## Mapping and visual communication

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

In our teaching experience, **LLMs such as ChatGPT can be particularly helpful for QGIS questions**: explaining tools, suggesting processing steps, interpreting errors and helping with expressions or Python scripts. We have found this support more useful than their troubleshooting suggestions for Autodesk Revit. This is an observation from our use, rather than a guarantee: provide your software version, the relevant data and the exact error, then check suggestions against the documentation and test them on a copy of your data.

### Graphics references

Reference sites for inspiration:

* [**Asset Library**](https://shop.studioinnate.com/product/cyberpunk-asset-pack/)
* [**Gmunk**](https://gmunk.com/OBLIVION-GFX)
* [**Ryoji Ikeda**](https://www.ryojiikeda.com/)
* [**Refik Anadol**](https://refikanadol.com/)
* [**Ryoichi Kurokawa**](https://www.ryoichikurokawa.com/)

**Maps and Infographics**

Creating readable, beautiful maps that clearly communicate information is not as easy as it sounds. There are many references available, but I always return to the website of [**Morphocode**](https://morphocode.com/), which offers excellent blog posts, reference maps and educational PDFs:

* Blog post: **[Location and Time: Urban Data Visualisation](https://morphocode.com/location-time-urban-data-visualization/)**
* PDF / Ebook: **[Urban Cartography](https://morphocode.com/wp-content/uploads/resources/morphocode-urban-cartography-ebook-web.pdf)**
* Blog post: **[Using Colors in Maps](https://morphocode.com/the-use-of-color-in-maps/)**

## Data sources

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

### News and event data

- **[GDELT Project](https://www.gdeltproject.org/)** — global news/event data that could be revisited as a source for a future data-mining, mapping or spatial-analysis exercise. Note: this link came from reviewing a student project; the student project itself is not being recorded here.

## Workshops, equipment and components

### Inductions at B-Made

[B-Made](https://www.ucl.ac.uk/bartlett/about/our-locations-and-facilities/b-made-bartlett-workshops) offers access to **laser cutters, 3D printers, and model-making tools**.

To use these facilities, complete the required [induction](https://moodle.ucl.ac.uk/course/view.php?id=39723&section=1#tabs-tree-start).

Refer to the [B-Made Moodle page](https://moodle.ucl.ac.uk/course/view.php?id=39723&section=0#tabs-tree-start) for details on **file preparation** and workshop protocols.

B-Made also provides **equipment rentals**, such as **3D scanners and cameras**, which require a separate [induction](https://moodle.ucl.ac.uk/course/view.php?id=39723&section=46) before use.

### Institute of Making

UCL's [Institute of Making](https://www.instituteofmaking.org.uk/) is an excellent resource for exploring materials and making processes. Its **Materials Library** invites you to investigate the physical, tactile and sensory qualities of materials: a useful starting point for textile experiments, wearable prototypes and thinking about how a material behaves on the body. Explore the collection alongside the Institute's workshops and making facilities. Membership is available to UCL students and staff; check the Institute's current registration, access and induction arrangements before visiting or using equipment.

### Arduino components and sensors

* [Arduino (Official)](https://www.arduino.cc/)
* [SparkFun](https://www.sparkfun.com/)
* [Seeed Studio](https://www.seeedstudio.com)
* [Robot Shop](https://uk.robotshop.com/)
* [The Pi Hut](https://thepihut.com/)
* [Adafruit](https://www.adafruit.com/)
* [Pimoroni](https://shop.pimoroni.com/)
* [DFRobot](https://www.dfrobot.com/)
* [LilyGO](https://www.lilygo.cc/)

## Collaboration and backup

Groups work most effectively with **shared online storage** (e.g., Dropbox, Google Drive, OneDrive), ensuring everyone has consistent access to the latest files.

UCL provides each student with **100 GB** of cloud storage, which may not be sufficient for all coursework—consider arranging additional space if needed.

Hardware can fail and laptops can be stolen. **Missed submissions due to data loss are not considered valid excuses.** Always ensure your work is securely stored and **regularly backed up**.
Online storage solutions provide peace of mind, as your data remain safe—services like **Dropbox**, for example, allow you to recover accidentally deleted files for up to a year (with an extended recovery option).

Alternatively, a **home-based storage system** such as the [**Synology BeeStation**](https://bee.synology.com/en-us/BeeStation) offers a hybrid setup: local file access at home combined with cloud backup and a sharing system similar to Dropbox.

## Optional tools and services

### Sublime Text Editor

[Sublime Text](https://www.sublimetext.com/) — fast, capable text editor that handles very large files.

### vvvv gamma and FUSE

[**vvvv gamma**](https://visualprogramming.net/) is a visual programming environment for creating **interactive, real-time graphics and computational systems**. You build a program as a graph of connected nodes, working with data, geometry and behaviour while seeing the output change immediately. It supports procedural graphics: forms, images and movement generated through computational rules and parameters.

Its extensive ecosystem connects graphics with sensors, Arduino, cameras, audio, networks, external data and other software. This makes it useful for RC15 projects that respond to bodies, environments or live information. You can combine 2D drawing with Skia, 3D graphics with Stride, computer vision and custom C# code in one evolving program.

[**FUSE**](https://www.thefuselab.io/features) brings visual **GPU programming** into vvvv. It makes shader logic and parallel computation accessible through connected nodes, supporting parametric and unconventional geometries, custom materials and effects, and large particle systems that respond in real time. The GPU allows many calculations to run in parallel, making it possible to explore forms and behaviours beyond conventional modelling workflows.

Start with examples included in the vvvv installation and the [Node Institute's vvvv workshop resources](https://thenodeinstitute.org/courses/node20-vvvv-workshop-bundle/). The [vvvv community](https://forum.vvvv.org/) is also a useful place to ask questions and share experiments.

### Sensor Log

[Sensor Log](http://sensorlog.berndthomas.net/) — iPhone app that turns your phone into a **multi-sensor** device.

### D5

[D5](https://www.d5render.com/) — real-time rendering engine (similar to Enscape/Twinmotion) with educational licenses that unlock all features.

### Mapbox Studio

[Mapbox Studio](https://www.mapbox.com/mapbox-studio) — design custom map styles; can be used as backgrounds in QGIS. The free tier is generous and sufficient for coursework.
How-to: [Use Mapbox backgrounds in QGIS](https://docs.mapbox.com/help/tutorials/mapbox-arcgis-qgis/).

### Kepler GL

[Kepler GL](https://kepler.gl/) — web-based tool for quick, attractive geo-visualisations; simple, fast, and free. It has a python integration as well.

<!--
### Ped Catch

[Ped Catch](http://pedcatch.com/) — generates pedestrian network diagrams that account for slopes; results can be exported to QGIS.
-->

### Google Earth and Google Earth Studio

* [Google Earth](https://earth.google.com) — capture screenshots.
* [Google Earth Studio](https://www.google.com/earth/studio/) — create **flythroughs and animations**; useful for presentations and even 3D point-cloud reconstruction with Autodesk Recap.

### Google Earth Engine and Microsoft Planetary Computer

[Google Earth Engine](https://earthengine.google.com/) combines a large archive of satellite imagery and geospatial datasets with cloud-based analysis. [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com/docs/) provides a geospatial data catalogue and APIs for accessing and analysing datasets. Both support research across large areas and comparisons over time, such as changes in vegetation, land cover or urban expansion. Their catalogues differ; choose a platform by checking the datasets, dates and resolution needed for your question.

These tools are particularly useful at **city, regional and larger scales**. Smaller study areas are possible, but the source imagery's resolution determines the level of detail: a city-wide land-cover study and a detailed investigation of a single block require different data. They are analysis environments, rather than simply tools for zooming into detailed aerial photographs.

Earth Engine's browser-based Code Editor uses **JavaScript**, and its API also supports **Python**. Planetary Computer workflows commonly use **Python** and STAC-based data access. LLMs can help you develop scripts and understand these interfaces, making the coding more approachable. You still need to check dataset selection, dates, cloud masking, spatial resolution and the meaning of your results.

### Best Time

[Best Time](https://besttime.app/) — foot-traffic data for locations worldwide (UI and API). Free tier available.
