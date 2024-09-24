import shutil
import os
import glob
import subprocess

should_convert = True

folder_vgmstream = "C:\\BG3mods\\bg3-sounds-converter-main\\vgmstream-win64"
folder_audio_raw = "c:\\BG3mods\\bg3-modders-multitool\\UnpackedData\\bhaal-audio"
folder_audio_converted = "c:\\BG3mods\\durge-audio\\bhaal-audio"


if should_convert:
  cwd = os.getcwd()
  os.chdir(folder_vgmstream)

  wems = glob.glob(f"{folder_audio_raw}\\*.wem")
  for wem in wems:
    _, filename = os.path.split(wem)
    subprocess.call(f'vgmstream-cli -o {folder_audio_converted}\\{filename}.wav {folder_audio_raw}\\{filename}', shell=True)

  os.chdir(cwd)

