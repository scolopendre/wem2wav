import shutil
import os
import glob
import subprocess

should_convert = True

#folder names must have NO SPACES or the code will not run
#make sure to double backslash the file path.
#for instance: "C:\ModdingTools\vgmstream-win64" -> "C:\\ModdingTools\\vgmstream-win64"

folder_vgmstream = ""
folder_audio_raw = ""
folder_audio_converted = ""


if should_convert:
  cwd = os.getcwd()
  os.chdir(folder_vgmstream)

  wems = glob.glob(f"{folder_audio_raw}\\*.wem")
  for wem in wems:
    _, filename = os.path.split(wem)
    subprocess.call(f'vgmstream-cli -o {folder_audio_converted}\\{filename}.wav {folder_audio_raw}\\{filename}', shell=True)

  os.chdir(cwd)

