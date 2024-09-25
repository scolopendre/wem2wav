# wem2wav
sound converter

This script is just an edit of https://github.com/s-thom/bg3-sounds-converter that I made to convert the wem files in the Voice bank.
It's extremely simple and any other vgstream script would do the same thing, but I'm lazy and would rather repurpose a script I already have LOL.

Here's the actually insane Baldur's Gate 3 audio extraction guide that I wrote this script for: https://docs.google.com/document/d/1v3ClInw6lSAoy51hyJ1TLnPVapJSbe3PIRD2GJr_OB0/edit?usp=sharing

## Requirements (from s-thom)

This script assumes you are on Windows and are comfortable enough in a terminal to run a command or two.

You will need to download/install a few things to make this work.

- [BG3 Modders Multitool](https://github.com/ShinyHobo/BG3-Modders-Multitool)
  - Used to unpack the audio files and metadata from the game.
  - Download the latest release from [the releases page](https://github.com/ShinyHobo/BG3-Modders-Multitool/releases) and extract somewhere.
- [Python 3](https://www.python.org/)
  - Used to run this script.
  - Install how you would normally install Python, The Windows Installer from [the website](https://www.python.org/downloads/) is a good choice if you don't know what to do.
  - Run `python --version` to check that Windows doesn't have the broken alias enabled.
    - If it does, then search Settings for "app execution aliases" and disable the entries for `python.exe` and `python3.exe`.
- [vgmstream](https://github.com/vgmstream/vgmstream)
  - Used to convert the `.wem` files to `.wav` so audio players can play them.
  - Download the latest release from [the builds website](https://vgmstream.org/) and extract the folder somewhere.
  - Double check the release has a bunch of DLLs included.

## Usage (edited from s-thom)

1. Ensure you check this project out in a path with _no spaces_ in the name
   - This project is currently sensitive to this, and having spaces in any paths will mean it doesn't work.
2. Open the Modders Multitool
   - Make sure you have your game path set correctly. This can be confirmed by opening the Configuration dialog from thetop menu.
3. In the top menu, select `Utilities` > `Game File Operations` > `Unpack Game Files`.
4. Select `Voice.pak` and confirm.
5. Wait for the unpacking to complete.
6. Back in this project, change the constants in `categoriser.py`
   - `folder_vgmstream` should be the folder you extracted vgmstream to.
   - `folder_unpacked_data` should be the folder with the audio you want to convert.
   - `folder_audio_converted` should be the folder where you want the converted audio to go. 
7. Run `python wem2wav.py`
   - This will take some time, so go off and enjoy your life while it does its thing.

