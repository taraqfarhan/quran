# Quran CLI & Wallpaper Generator for macOS

A suite of command-line utilities for macOS to display English Quran verses in the terminal, extract verse data, and set dynamically generated Quran verse wallpapers on your desktop.

---

## Features

1. **CLI Verse Viewer (`quran`)**
   - Displays specific verses by Surah and Ayah number, or outputs a random verse when arguments are omitted.
2. **Dynamic Desktop Wallpaper Generator (`quran_wallpaper`)**
   - Renders formatted English Quran verses onto clean wallpaper images and applies them to your macOS desktop.
   - Manages a persistent macOS `launchd` background daemon to automatically change wallpapers at set intervals and start at login.
3. **Data Extractor (`extract_data.py`)**
   - Fetches English Quran translations (by default Saheeh International) from the Al-Quran Cloud API and exports them to a CSV file.

---

## File and Directory Structure

All runtime data, configuration files, and generated wallpapers are stored in the `~/.quran` directory:

```
~/.quran/
├── config.json              # Configuration file (interval, font, resolution)
├── data/
│   └── quran_en.csv         # English Quran dataset (6,236 verses)
└── <surah>_<ayah>.jpg       # Generated wallpaper images
```

---

## Requirements

- **macOS**
- **Python 3.9+**
- **Python Packages**: `pandas`, `pillow`, `requests`
- **System Permissions**: macOS will prompt for automation permissions to allow `osascript` (System Events) to update desktop wallpapers.

---

## Installation

Follow these steps to set up the programs on macOS with minimal effort:

### 1. Clone or Download the Repository

```bash
cd ~/Library && git clone https://github.com/taraqfarhan/quran.git && cd quran
```

_**Note: You shouldn't delete or move the directory afterwards (so choose the path where you clone this repository carefully)**_

I would recommend cloning/downloading the repository into (`~/Library`) directory. `~/Library` directory is hidden by default. To see the hidden folder, you can use `Cmd + Shift + .` in Finder.
But if you want to choose other directory, as long as you don't delete or move the directory afterwards,
you can clone/download it anywhere else.

### 2. Run install.sh

```bash
bash install.sh
```

This script will automatically install the required Python packages, set up the `~/.quran` directory, and download the English Quran dataset.

---

## Usage Instructions

### 1. `quran`

Prints Quran verses in English directly to your terminal.

```bash
quran  # Print a Random Verse

quran 2 255  # Print a Specific Verse
# Pass the Surah number and Verse number as arguments
# If either argument is missing or invalid, a random verse will be printed instead
```

### 2. `quran_wallpaper`

Generates wallpaper images with Quranic verses and updates your desktop wallpaper on macOS.

#### Daemon & Control Commands

```bash
quran_wallpaper start # Start Background Daemon (Runs at login & survives reboot)
# Registers and loads a macOS launchctl daemon (`com.user.quran-wallpaper.plist`)

quran_wallpaper status # Check Daemon Status

quran_wallpaper stop # Stop Background Daemon

quran_wallpaper run # Run Interactively in Foreground

quran_wallpaper download # Download or Update Verse Dataset
```

#### Configuration (`set` command)

Settings are stored in `~/.quran/config.json`. You can modify them using:

```bash
quran_wallpaper set <key> <value>
```

| Key          | Description                        | Default Value Usage                              |
| :----------- | :--------------------------------- | :----------------------------------------------- |
| `interval`   | Refresh interval in seconds        | `3600`                                           |
| `resolution` | Screen resolution (`WidthxHeight`) | `2560x1600`                                      |
| `font`       | Absolute path to font              | `/System/Library/Fonts/Supplemental/Georgia.ttf` |

#### Interval

- Interval is the time in seconds between wallpaper updates. The default is 3600 seconds (1 hour). You can set it to any positive integer value.

For example

```bash
quran_wallpaper set interval 1800   # to set the interval to 30 minutes (30 * 60 = 1800 seconds)
quran_wallpaper set interval 7200   # to set the interval to 2 hours (2 * 60 * 60 = 7200 seconds)
quran_wallpaper set interval 86400  # to set the interval to 1 day (24 hours) (24 * 60 * 60 = 86400 seconds)
quran_wallpaper set interval 172800 # to set the interval to 2 days (2 * 24 * 60 * 60 = 172800 seconds)
quran_wallpaper set interval 604800 # to set the interval to 1 week (7 days) (7 * 24 * 60 * 60 = 604800 seconds)
```

#### Resolution

- Resolution is the size of the wallpaper image in pixels. The default is `2560x1600`. You can set it to any valid resolution supported by your display.
- Find your display's native resolution in Settings > Displays, or use the `system_profiler SPDisplaysDataType` command in Terminal to list all supported resolutions.

For example

```bash
system_profiler SPDisplaysDataType | grep Resolution   # to list all supported resolutions

quran_wallpaper set resolution 1920x1080   # to set the resolution to 1920x1080 (Full HD)
quran_wallpaper set resolution 3840x2160   # to set the resolution to 3840x2160 (4K UHD)
quran_wallpaper set resolution 5120x2880   # to set the resolution to 5120x2880 (5K Retina)
quran_wallpaper set resolution 7680x4320   # to set the resolution to 7680x4320 (8K UHD)
```

#### Fonts

Standard macOS system fonts are located in:

- `/System/Library/Fonts/`
- `/System/Library/Fonts/Supplemental/`

_Note_: These folders are hidden by default. To see the hidden folders in Finder, you can use `Cmd + Shift + .` in Finder.

For example

```bash
quran_wallpaper set font /System/Library/Fonts/Supplemental/Chalkduster.ttf   # set a system font for the wallpaper text

# Custom TrueType (`.ttf`) or OpenType (`.otf`) fonts can also be used
quran_wallpaper set font "/path/to/custom_font.ttf"   # set a custom font for the wallpaper text
```

---

### 3. `extract_data.py`

This is a bonus script. This script fetches the English translation of all 114 Surahs from the Al-Quran Cloud API and outputs them to a CSV file.
You can edit the script to download a different translation or modify the output format.
By default it fetches all 114 Surahs in English (Saheeh International translation) from Al-Quran Cloud API (`quran.com` source data) and outputs `quran_en.csv`.
Open the script and follow the instructions in the comments to modify the translation or output format.

```bash
open -e extract_data.py    # to open the script in TextEdit for editing
python3 extract_data.py    # to run the script and download the dataset
```

---
