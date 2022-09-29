![monsoon_wordmark](https://user-images.githubusercontent.com/87099578/193130174-e464d4a6-afa3-453f-a36e-4289acf5f248.png)

# 🌀 Monsoon
Monsoon is a lightweight overlay solution for your League client that shows 
ARAM balance changes in champion select. Let the winds reveal the unexpected 
surprises before the match begins! :3

# Table of Contents
- [🌀 Monsoon](#-monsoon)
- [Table of Contents](#table-of-contents)
- [Download](#download)
- [Guide](#guide)
  - [Getting started](#getting-started)
- [Limitations](#limitations)
- [FAQ](#faq)
- [License](#license)

# Download
Interested in using Monsoon? [Get it here!]()

# Guide
## Getting started
When launching Monsoon, the application will idle while waiting for an ARAM 
champion select to be created. It is recommended to have Monsoon ready before 
queuing up as the overlay may fail to appear otherwise.

![overlay_example](https://user-images.githubusercontent.com/87099578/193137617-e282a2d2-f5e0-467b-b4e5-f1965aebb51a.png)

Hovering over the information emoji ℹ️ will bring up a tooltip with detailed 
balance changes of a champion if applicable. This emoji will only appear if 
there are any ARAM balance changes to a champion and has other changes made 
(healing/shielding modifiers, mechanic changes, etc). 

This emoji will always appear for bench champions if they have any balance 
changes.

![system_tray](https://user-images.githubusercontent.com/87099578/193139154-faf804c7-ac20-4e51-94c1-692510c91d6d.png)

Monsoon will also leave a icon in your system tray. This icon can be clicked to 
reveal actions you can perform such as exiting Monsoon.

# Limitations
Monsoon was created with the goal of just being an overlay for the League 
client. Therefore, Monsoon will not support the in-game League window/fullscreen.

Due to Monsoon depending on the LoL Fandom for upstream balance changes, said 
balance changes may not be 100% accurate. This may be the most noticable when 
new ARAM balance changes are announced (Wikia editors may update ahead of time) 
or when the upstream may fail to update due to lack of upkeep.

# FAQ
**How was Monsoon made?**

Monsoon was developed using Python in the span of four days. Notable packages 
include:
- PySide6 
(binding of the Qt GUI toolkit)
- willump (League Client connector)
- pywin32 
(makes overlay possible)
- beautifulsoup4 (parsing balance changes).

**Does Monsoon support Mac (or even Linux with Wine)?**

Due to the nature of pywin32, Monsoon cannot currently support Mac or Linux. 
I also do not own an Apple-based computer, so I cannot approve any changes made 
to support said platform.

Support for Linux with Wine will also never be supported as Riot does not 
support the platform with the game anyways.

I am very sorry... :c

# License
Monsoon is licensed under the terms of the GNU GPL v3 license.
