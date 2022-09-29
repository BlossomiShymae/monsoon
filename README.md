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
to support said platforms. I am very sorry... :c

# License

