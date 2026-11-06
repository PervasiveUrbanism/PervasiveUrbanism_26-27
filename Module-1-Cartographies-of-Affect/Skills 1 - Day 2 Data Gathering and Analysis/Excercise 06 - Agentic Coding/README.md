# Exercise 06 — Agentic Coding

Large language models can do more than answer questions or generate code. When connected to tools, an **AI agent** can pursue a goal through several steps: searching for information, inspecting results, deciding what to do next and, when permitted, taking further actions.

This is different from a conventional program, where we specify the operations in advance, and from a single exchange with a chatbot. In an **agentic workflow**, we delegate some decisions about *how* to complete a task. The agent does not necessarily act without us: we can define limits, inspect intermediate results and decide which actions require approval.

For urban research, this creates opportunities to collect and interpret information that would otherwise take considerable manual effort. It also raises methodological questions. Which sources did the agent choose? Which results did it exclude? What assumptions did it make? Can we verify its work and repeat the process?

We will investigate these questions in two stages:

- **Agentic search:** delegate the discovery of Berlin events to an AI agent and evaluate its recommendations.
- **Agentic coding:** work with a coding agent to build a more explicit, testable process for collecting event information.

Both stages start with the same problem. The difference is **where we place control**: first we delegate much of the search; then we decide how the search should operate and ask an agent to help implement it.

## 1. Agentic Search

A conventional web search begins with a **query**, such as *experimental music Berlin this weekend*. A search engine returns a collection of pages, and we decide which ones are relevant.

**Query → Search → Results → Human interpretation**

![Google Search](GoogleSearch.png)

With agentic search, we describe a **goal** rather than just a query. For example, we might ask an agent to find activities suitable for someone who has recently moved to Berlin. The agent may try several searches, inspect different sources, compare information and refine its approach before presenting recommendations.

**Brief → Search → Inspect sources → Compare and filter → Recommendations**

![Agentic Search](SearchStrategy.png)

The distinction is not simply that the answer is longer or more personalised. The important change is that the agent makes **intermediate decisions**. It decides which searches to try, which pages to inspect and which results to include. These decisions depend on its instructions, the tools it can access and the information available. They may also be mistaken.

This makes agentic search particularly interesting for urban research. The same city can offer very different possibilities depending on someone's interests, income, mobility, language or available time. A search designed for a particular person can reveal those differences—but only through the assumptions built into the brief and the agent's choices.

In this exercise, we will work with **Tomaso**, a fictional resident of Berlin. First, we will ask an agent to find activities for him. Then we will examine what it found, what it missed and whether we can verify its claims. Finally, we will take control of more of the process by designing a repeatable data-collection workflow.

The aim is not merely to obtain convincing recommendations. It is to understand **how a result was produced, what we can trust and which decisions we should keep under our control**.

## 2. Meet Tomaso

![Tomaso still in Bologna](tomaso_bologna.png)

**Tomaso Bianchi** is a 24-year-old Italian who moved from Bologna to Berlin six months ago. He lives at **Wipperstraße 13 in Neukölln** and works part-time in a café.

His income is limited, so he generally looks for **free activities or events costing no more than €15**. He doesn't own a car and travels by **walking, bicycle and public transport**. He prefers things within about **30 minutes of home**, although he is willing to travel further for something exceptional.

Tomaso speaks **Italian and English** and is learning German, but is not yet comfortable attending events that require fluent German.

He is interested in **electronic and experimental music, small concerts, architecture and urban culture, photography, independent cinema, markets, food and cooking**. He enjoys discovering less obvious parts of Berlin rather than conventional tourist attractions or large commercial events.

Most importantly, Tomaso is **still building a social life in Berlin**. He would like to meet new people and make friends, so he particularly values events and activities that encourage **conversation, participation or repeated encounters**, rather than simply attending as a spectator.

Because he works irregular shifts, **evenings and weekends** are usually the best times for him.

## 3. Your First Agent

Instead of searching for events ourselves, we can ask ChatGPT to search on Tomaso's behalf. We will **run the search once**, inspect what it finds and then make it repeat automatically.

A **one-off agentic search** runs when we ask for it. A **scheduled task** runs a similar brief at a specified time, such as every Thursday. Scheduling does not make the results more accurate; it only makes the task repeat. We still need to examine where the information came from and whether it is reliable.

> **Every Thursday, find things Tomaso could do in Berlin during the coming week.**

No Python is required for this first experiment. We describe the goal in natural language, let ChatGPT search and inspect the results before adding a schedule.

![Scheduled Task](ScheduledTask.png)

### Exercise — Run the search

Start a new ChatGPT conversation and use a prompt similar to:

> Search for events and activities happening in Berlin during the next seven days that Tomaso might enjoy.
>
> Tomaso is 24, moved from Bologna to Berlin six months ago, lives at Wipperstraße 13 in Neukölln, works part-time in a café, and is looking to meet people and make friends. He likes electronic and experimental music, small concerts, architecture and urban culture, photography, independent cinema, markets, food and cooking.
>
> Prioritise free events or events costing no more than €15, preferably within approximately 30 minutes by public transport or bicycle from his home. Tomaso speaks Italian and English and only basic German.
>
> Recommend 10 activities. For each recommendation provide the **event name, date, time, venue, full address, latitude, longitude, price, original source URL, and a short explanation of why it suits Tomaso**. Give latitude and longitude in **decimal degrees** and identify the event venue as accurately as possible.

The requested output has a simple spatial data structure:

`event | date | time | venue | address | latitude | longitude | price | source_url | recommendation`

Run this **one-off search** first. Read the recommendations and open some of their source links. Then create a **scheduled task** using the same brief, asking ChatGPT to run it every Thursday and search for the following seven days. If scheduling is unavailable, the one-off search is sufficient for the exercise.

The original sources and dates matter more than how convincing the final recommendations sound. The next step is to check this.

### Reference run — 4 October 2026

We tested the brief with a live search for **5–11 October 2026**. The table below is kept as a reference example of the agent's output. It is useful precisely because it is not perfectly clean: some information can be verified directly, while other fields depend on interpretation or secondary lookup.

| Event | Date / time | Venue / address | Lat | Lon | Price | Why it fits Tomaso | Source |
|---|---|---|---:|---:|---|---|---|
| Creative Media Lab | Wed 07.10, 16:00–18:00 | Medienkompetenzzentrum Neukölln, Mittelweg 30, 12053 Berlin | 52.47475 | 13.43519 | Free | Hands-on media workshop involving film, VR and 3D printing; local and participatory. | https://jup.berlin/events/creative-media-lab |
| Open Calligraphy Workshop | Thu 08.10, 16:00–20:00 | Stadtteilzentrum Kiezbegegnung, Warthestraße 73, 12051 Berlin | 52.47017 | 13.42693 | Free | Drop-in creative activity with no prior knowledge required; strong potential for informal interaction. | https://www.gratis-in-berlin.de/component/flexicontent/36-kunst/2072643-offene-kalligraphie-werkstatt-in-neukoelln |
| Open Lab: Recycling, Repackaged | Thu 08.10, 17:00–20:00 | Futurium, Alexanderufer 2, 10117 Berlin | — | — | Free | Participatory workshop combining AI, design and future thinking; further away, but unusually close to Tomaso's interests. | https://www.berlin.de/en/tickets/education-lectures/open-lab-evening-recycling-repackaged/2026-10-08-n-a-b5bf2e04-fc8f-4013-a4f2-1dd82832cd61/ |
| 52nd Berlin Night of Spiritual Songs | Fri 09.10, 19:30–23:00 | Martin-Luther-Kirche, Fuldastraße 50, 12045 Berlin | 52.48431 | 13.43584 | Free / donation | Collective singing rather than passive spectatorship; very local and explicitly social. | https://www.eli-berlin.de/liedernacht/ |
| Big Band Night 2026 | Fri 09.10, 19:30 | Kulturstall, Schloss & Gutshof Britz, Alt-Britz 81, 12359 Berlin | 52.4469 | 13.4378 | Free / pay what you can | Live music in Neukölln with a low financial barrier. | https://www.berlin.de/musikschule-neukoelln/veranstaltungen/big-band-night-1295669.php |
| Sound Canteen w/ Tobi Fries | Fri 09.10, 20:00 | Orangerie Neukölln, Schierker Straße 8, 12051 Berlin | 52.47058 | 13.43609 | Free | Ambient/Balearic music in a small local venue; close to Tomaso's electronic-music interests. | https://www.orangerie-nk.de/ |
| Klangstraße Music Festival | Fri 09.10, 15:00–21:00 | Multiple venues along Residenzstraße, 13409 Berlin | — | — | Free | 27 short concerts across 15 locations; further away, but informal, exploratory and easy to move between. | https://www.berlin.de/events/7755495-2229501-reinickendorfer-klangstrasse.html |
| Gartenrundgang | Sat 10.10, 11:00–13:00 | KGA Zufriedenheit, Koppelweg 30, 12347 Berlin | — | — | Free | Urban gardening, discussion and shared knowledge in a relaxed setting; strong social potential. | https://www.umweltkalender-berlin.de/angebote/details/99663?dat=2026-10-10 |
| Mit allen Sinnen im Waldgarten | Sat 10.10, 15:00–16:30 | Waldgarten Berlin-Britz, Leonberger Ring 54, 12349 Berlin | 52.42721 | 13.42883 | Free | Guided sensory walk through a community garden; participatory and locally grounded. Registration required. | https://www.umweltkalender-berlin.de/angebote/details/99821?dat=2026-10-10 |
| Gardens of Disco | Sat 10.10, 21:00 | Orangerie Neukölln, Schierker Straße 8, 12051 Berlin | 52.47058 | 13.43609 | €12 | Small-scale Disco, Italo, House and experimental electronic music in a local setting; probably the strongest music match. | https://www.orangerie-nk.de/ |

### Exercise — Verify three recommendations

Select **three events** from your own search results. For each event, open its **original organiser or venue page**, where available, rather than relying only on an event aggregator. Record whether you can confirm:

- **Date and time:** Is the event happening during the requested week?
- **Price and access:** Is the stated price correct? Are there booking requirements or age restrictions?
- **Place:** Does the address match the venue? Are the coordinates plausible?
- **Source:** Does the link lead to information about this particular event, rather than a generic homepage?

Mark each field as **verified**, **uncertain** or **incorrect**, and note the source you checked. If you cannot establish a fact, leave it uncertain instead of guessing. Compare the verification with the agent's original recommendation: did any result become less suitable for Tomaso?

### First observations

At first sight, the result is impressive. The agent has searched for current events, interpreted Tomaso's preferences and returned structured spatial data. But the table also exposes the limits of the process.

Not every requested field is equally reliable. Proximity to Tomaso's home may be inferred from a neighbourhood rather than calculated as travel time. The likelihood of meeting people is an interpretation of an event description. Coordinates may require a second lookup, and for distributed events such as **Klangstraße**, a single coordinate may be the wrong representation altogether. Unresolved coordinates are therefore left blank rather than given false precision.

The search also combines very different kinds of sources: event aggregators, neighbourhood websites, public calendars and individual organisers. The agent decides which sources to search, which results to ignore and which events to recommend.

Checking the results can change the answer. An apparently suitable creative workshop from an earlier search turned out to be intended for **10–18 year olds**. **MUSK ON MARS**, another strong-looking recommendation, was listed from **€20** and therefore exceeded Tomaso's €15 budget.

More importantly, agentic search is **not guaranteed to be factually correct**. A result may contain an incorrect date, an outdated or broken link, a wrong address, or occasionally an event that cannot be verified at all. Better instructions — for example, requiring original source pages and asking the agent to verify each event — can reduce these errors, but they cannot remove the risk completely. ChatGPT itself warns that it can make mistakes and that important information should be checked.

![ChatGPTMistakes](Mistakes.png)

For casual discovery, a result that is *mostly correct* may still be useful. For a data-collection workflow, however, **a plausible recommendation is not yet a verified data record**. A few invented or incorrect records can contaminate the dataset and affect everything that happens afterwards.

This gives us a reason to look beyond the quality of the recommendations themselves. The problem is not simply whether the answer looks convincing; it is that the **method is opaque**.

We know the brief and we can see the output, but we do not yet know exactly how the agent moved from one to the other.

> **What actually happened?**

## 4. Inside the Search

Our first agent appears simple. We gave it a description of Tomaso and received ten recommendations.

But between those two things, quite a lot happened.

**Tomaso's brief → Search → Sources → Extraction → Interpretation → Filtering → Ranking → Output**

The agent had to decide:

- **where to search** — which websites, calendars and event platforms to inspect;
- **what to extract** — dates, prices, addresses, coordinates and descriptions;
- **what to interpret** — whether an event feels social, interesting or appropriate for Tomaso;
- **what to exclude** — events that are too expensive, too far away, require fluent German or otherwise conflict with the brief;
- **how to rank** — which ten events are ultimately worth recommending.

In our first experiment, all of these decisions were bundled together inside a single agentic search.

We defined the **input** — Tomaso — and the **output** — ten recommendations — but we had very little control over what happened in between.

That is powerful, but it also creates a methodological problem:

> **Which parts of this process should we delegate to AI, and which parts should we control ourselves?**

### Taking control of the search

One obvious place to intervene is at the beginning.

Instead of asking an agent to decide **where on the web to search**, we can define the sources ourselves.

**Known Berlin websites → collect events → structured dataset**

Now we know where the information came from. We can inspect the original pages, repeat the process later, and compare what different sources contribute.

This changes the role of AI. Rather than asking it to perform the entire search, we can use it to help us **build the search process itself**.

## 5. Building a Controlled Search

We now move from **using an agent** to **developing with an agent**. This requires a different kind of conversation.

If we simply ask a coding agent to *build an event scraper for Tomaso*, it may immediately start making decisions about sources, data structures, libraries and workflow. Some of those decisions may be sensible, but we have again created a black box — this time in the development process.

A more useful approach is to establish three connected things before coding:

![Preparing Agentic Code](Strategy.PNG)

The **brief** defines the intended outcome. The **architecture** explains the system and its execution order. The **roadmap** breaks development into stages that can be implemented and checked one at a time.

These three parts are not a rigid specification written once and then forgotten. They should evolve together. What we learn from a website, an initial scraper or a failed run may change the architecture, the brief or the next development step.

This is the central strategy we will use for agentic coding:

**understand the system → describe the intention → break the work into stages → delegate one stage → inspect → revise**

In a typical workflow, we can discuss the brief, architecture and roadmap with ChatGPT first, before moving into implementation with a coding agent such as Codex. This front-loads some thinking, but it gives us a way to judge what the coding agent produces and prevents the project from becoming a collection of unrelated AI-generated changes.

If you work in a **GitHub repository**, save each working stage as a commit before moving on. These checkpoints let you inspect changes and roll back to a known working version if something goes wrong.

### 5.1 Overall Architecture

We will build a system that collects event information from selected websites, combines it into a large table, and gives that table to an LLM. The LLM then selects and ranks events that match Tomaso's interests and circumstances.


![](Sequence.PNG)


Each website needs its own **scraper**: a Python script that extracts event information. Websites organise their pages differently, so each scraper must be adapted to its source. All scrapers return the same set of fields, allowing their results to be added to one shared events table.

Why a table? A website contains navigation, adverts, formatting and other material alongside its events. Extracting the relevant information into rows and columns gives us a consistent dataset: each row represents an event, with fields such as its date, venue, address, price and description. This makes it easier to inspect and compare events, combine information from many sources, and enrich the data with cleaned addresses, English descriptions and coordinates before asking the LLM to make recommendations.

**For this tutorial, we will build just two scrapers:** one for [Berlin.de Events](https://www.berlin.de/en/events/) and one for [Gratis in Berlin](https://www.gratis-in-berlin.de/). The same architecture could later include more websites, each contributing records to the shared table.

![](architecture.PNG)

**Color key:** Blue = Python script · Green = table · Purple = LLM action.

The eventual pipeline should run **every Monday**, collecting events from **Monday through Sunday of that week**, using Berlin local dates. Build and check the manual pipeline before adding automation. **This tutorial builds only the two scrapers**; the diagram shows how their outputs will support the later stages.

### 5.2 Development Brief

Give Codex a clear brief before asking it to write code:

> Develop this system in stages, following the roadmap in Section 5.3. Implement and check one stage before moving to the next; this tutorial builds only the two scrapers and combines their outputs. Revise the plan as we learn while keeping the goal of recommendations for Tomaso clear.
>
> Build two Python scrapers: Scraper 01 for Berlin.de Events and Scraper 02 for Gratis in Berlin. Both must accept the same Monday–Sunday date range and append records using an identical CSV schema to a raw/master events table.
>
> Collect all available factual event information in that period, including details from individual event pages where needed. Do not select events for Tomaso and do not deduplicate within or between sources. Preserve provenance and leave unavailable information blank rather than inventing it.
>
> Use latitude and longitude supplied by the source when available, in decimal degrees. Otherwise leave them blank for the later shared geocoding stage. Do not geocode inside either scraper.
>
> In the later shared enrichment stage, use the LLM to clean addresses and write a short factual English description of each event from its source text. Preserve the original German description and address, keep official street and venue names, and flag missing or uncertain details rather than inventing them.
>
> First inspect both websites and propose how to collect their data. Explain which pages you will access, how you will identify events and dates, which fields are available, and what could cause collection to fail. Implement one scraper at a time after we review the proposal.

Use this shared schema:

`event | date | end_date | time | end_time | venue | address | latitude | longitude | price | category | description | language | age_restrictions | registration | source | source_url | collected_at`

Use `YYYY-MM-DD` for dates and consistent column names and order in both outputs. Keep source wording where useful, including price conditions, language requirements and registration details. `source` identifies the website; `source_url` links to the event page; `collected_at` records when it was collected. These fields let us check the dataset against its sources.

Later enrichment should preserve the original `address` and `description` and add `cleaned_address`, `description_en`, coordinate provenance and geocoding status. The LLM writes `description_en` as one or two factual English sentences based on the source; this describes the event rather than recommending it for Tomaso. Ambiguous or unresolved locations remain flagged for review; a coordinate alone does not establish travel time from Tomaso's home.

### 5.3 Development Steps

Develop one stage at a time. The prompts below are starting points; use the shared schema and brief from Section 5.2 throughout. **The tutorial implements steps 1–4; steps 5–7 describe later development.**

1. **Inspect both sources.** Open listings and individual event pages. Review date coverage, pagination, available fields and likely failure points.

   > Inspect Berlin.de Events and Gratis in Berlin. Explain how each scraper could collect events for a Monday–Sunday week. Identify which fields come directly from the pages and which are unavailable. Propose an approach before writing code.

2. **Build Scraper 01.** Run it manually for one explicit week and compare sample rows with the original pages.

   > Implement the Berlin.de scraper using our shared schema and a configurable Monday–Sunday date range. Preserve source facts and links, leave missing values blank, and do not filter for Tomaso or deduplicate. Explain how to run it and check its output.

3. **Build Scraper 02.** Use exactly the same schema and date range, adapting extraction to the second website.

   > Implement the Gratis in Berlin scraper with the same output columns and date range as Scraper 01. Adapt it to this website's structure. Run it and check sample rows against the source pages.

4. **Combine and inspect.** Append both outputs to the raw/master events table and check consistency and coverage.

   > Combine the two scraper outputs into one raw events table. Check column names, date coverage and missing values. Retain overlapping event records and their source references, and report any collection problems.

5. **Later: enrich the data.** Clean addresses and write English descriptions with the LLM, then geocode missing coordinates with Python.

   > Preserve the original addresses and descriptions. Add cleaned addresses and short factual English descriptions using the LLM. Then use Python to geocode only missing coordinates, record their provenance, and flag unresolved locations for review. Save an enriched events table.

6. **Later: evaluate with the LLM.** Check its recommendations against the enriched data and source pages.

   > Read the enriched events table and Tomaso's profile in Section 2. Recognise and reconcile duplicate events while retaining source references. Filter and rank suitable events, then return a table of daily recommendations with a short explanation for each. Identify uncertain information.

7. **Finally: automate.** Complete and check the manual pipeline before scheduling it.

   > The manual pipeline has been checked. Schedule it to run every Monday, using Berlin local dates to collect events from Monday through Sunday of that week. Record failures so we can review incomplete runs.

**First we used an agent as the search engine. Now we use an agent to help us construct the search engine.**
