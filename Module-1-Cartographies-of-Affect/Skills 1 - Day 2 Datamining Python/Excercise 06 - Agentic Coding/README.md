# Exercise 06 — Agentic Coding

## 1. Agentic Search

Conventional web search begins with a query. We enter a set of keywords, receive a ranked list of results, and decide for ourselves which sources and information are relevant.

**Agentic search starts with a brief rather than a query.**

We describe a task, a perspective and a desired outcome. An AI agent can then decide what to search for, which sources to inspect, how to interpret what it finds, and how to structure the result.

This places agentic search somewhere between **retrieval and simulation**. It does not simply ask what exists in a city. It can ask what becomes relevant **for a particular person, in a particular place, at a particular time**.

For urban research, this is interesting because the same city can be searched from very different positions. Age, income, mobility, language, interests and social circumstances all change what the city appears to offer.

In this exercise we will explore this through a fictional resident called Tomaso:

> **What should Tomaso do in Berlin this weekend?**

We will begin by giving an AI agent considerable freedom to answer this question. We will then examine how it searched, what it ignored, which assumptions it made, and whether its results can be trusted. Finally, we will progressively take control of parts of the process ourselves.

The aim is therefore not simply to use an AI agent, but to understand **what changes when search itself becomes agentic**.

## 2. Meet Tomaso

![Tomaso in Bologna](tomaso_bologna.png)

**Tomaso Bianchi** is a 24-year-old Italian who moved from Bologna to Berlin six months ago. He lives at **Wipperstraße 13 in Neukölln** and works part-time in a café.

His income is limited, so he generally looks for **free activities or events costing no more than €15**. He doesn't own a car and travels by **walking, bicycle and public transport**. He prefers things within about **30 minutes of home**, although he is willing to travel further for something exceptional.

Tomaso speaks **Italian and English** and is learning German, but is not yet comfortable attending events that require fluent German.

He is interested in **electronic and experimental music, small concerts, architecture and urban culture, photography, independent cinema, markets, food and cooking**. He enjoys discovering less obvious parts of Berlin rather than conventional tourist attractions or large commercial events.

Most importantly, Tomaso is **still building a social life in Berlin**. He would like to meet new people and make friends, so he particularly values events and activities that encourage **conversation, participation or repeated encounters**, rather than simply attending as a spectator.

Because he works irregular shifts, **evenings and weekends** are usually the best times for him.

## 3. Your First Agent

Instead of searching for events ourselves, we can ask ChatGPT to do this repeatedly on Tomaso's behalf:

> **Every Thursday, find things Tomaso could do in Berlin during the coming week.**

We can turn this into a **scheduled task** in ChatGPT. No Python is required. We describe the goal in natural language and tell the agent when it should run.

### Exercise

Create a new scheduled task in ChatGPT using a prompt similar to:

> Every Thursday, search for events and activities happening in Berlin during the following seven days that Tomaso might enjoy.
>
> Tomaso is 24, moved from Bologna to Berlin six months ago, lives at Wipperstraße 13 in Neukölln, works part-time in a café, and is looking to meet people and make friends. He likes electronic and experimental music, small concerts, architecture and urban culture, photography, independent cinema, markets, food and cooking.
>
> Prioritise free events or events costing no more than €15, preferably within approximately 30 minutes by public transport or bicycle from his home. Tomaso speaks Italian and English and only basic German.
>
> Recommend 10 activities. For each recommendation provide the **event name, date, time, venue, full address, latitude, longitude, price, original source URL, and a short explanation of why it suits Tomaso**. Give latitude and longitude in **decimal degrees** and identify the event venue as accurately as possible.

The requested output has a simple spatial data structure:

`event | date | time | venue | address | latitude | longitude | price | source_url | recommendation`

> **Run the task once and examine the results.**

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

### First observations

At first sight, the result is impressive. The agent has searched for current events, interpreted Tomaso's preferences and returned structured spatial data. But the table also exposes the limits of the process.

Not every requested field is equally reliable. Proximity to Tomaso's home may be inferred from a neighbourhood rather than calculated as travel time. The likelihood of meeting people is an interpretation of an event description. Coordinates may require a second lookup, and for distributed events such as **Klangstraße**, a single coordinate may be the wrong representation altogether. Unresolved coordinates are therefore left blank rather than given false precision.

The search also combines very different kinds of sources: event aggregators, neighbourhood websites, public calendars and individual organisers. The agent decides which sources to search, which results to ignore and which events to recommend.

Checking the results can change the answer. An apparently suitable creative workshop from an earlier search turned out to be intended for **10–18 year olds**. **MUSK ON MARS**, another strong-looking recommendation, was listed from **€20** and therefore exceeded Tomaso's €15 budget.

The result is not necessarily bad. Many recommendations are useful. The problem is that the **method is opaque**.

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

That is powerful, but it also creates a methodological problem.

> **Which parts of this process should we delegate to AI, and which parts should we control ourselves?**

### Taking control of the search

One obvious place to intervene is at the beginning.

Instead of asking an agent to decide **where on the web to search**, we can define the sources ourselves.

For example:

**Known Berlin websites → collect events → structured dataset**

Now we know where the information came from. We can inspect the original pages, repeat the process later, and compare what different sources contribute.

This changes the role of AI. Rather than asking it to perform the entire search, we can use it to help us **build the search process itself**.

## 5. Building a Controlled Search

In the previous experiment, ChatGPT decided where to search. We will now take control of that decision.

Rather than searching the entire web, we will define a small collection of Berlin event websites ourselves.

Our new workflow becomes:

**Known websites → scraper → structured CSV**

The aim is not to become expert web scrapers. Instead, we will use **Codex as a coding agent** to help us build the scraper.

This is a different kind of agentic behaviour.

Previously we asked:

> **Find events for Tomaso.**

Now we ask:

> **Help me build a system that collects events from sources I have chosen.**

### Start with one source

Don't try to scrape ten websites immediately.

Choose **one Berlin event website** and inspect it in your browser. Look at how events are presented. Can you identify the event title, date, venue, price and link to the original event?

Then open Codex and describe what you want to build.

For example:

> I want to build a Python script that collects upcoming events from this website:
>
> `[URL]`
>
> For each event I want to collect:
>
> `event | date | time | venue | address | price | source_url | description`
>
> First inspect the structure of the website and explain how you propose to collect the information. Do not write the complete program yet.

### Inspect the proposal

Before accepting any code, ask:

> **What pages will you access?**
>
> **How will you identify individual events?**
>
> **Which information comes directly from the website, and which information would need to be inferred?**
>
> **What could cause this scraper to fail?**

Only then do we let Codex implement the first version.

The distinction is important:

**First we used an agent as the search engine. Now we use an agent to help us construct the search engine.**

