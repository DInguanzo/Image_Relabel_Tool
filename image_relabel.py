import exiftool # Tool for extracting image metadata
import os # Interfacing with OS and file syste
import re # Regular Expression 

"""
This script is supposed to rename image file names according to the date the image was taken using 
following format: YYYYMMDD_HHMMSS_event-name.ARW.

Image date will be grabbed using the exifimage tool.
"""

eventName = "Ren-Fair"
rootFilepath = r"/home/dinguanzo/Pictures/2025/10_Ren-Fair/RAW"

files = os.listdir(rootFilepath) # Gets a list of all files within root file path
pattern = r'(?P<Year>\d{4}):(?P<Month>\d{2}):(?P<Day>\d{2})\s+(?P<Hour>\d{2}):(?P<Minute>\d{2}):(?P<Second>\d{2})' # Pattern to extract info from metadata

for file in files:
    filepath = os.path.join(rootFilepath, file) # add file path to file name

    with exiftool.ExifToolHelper() as et:
        for d in et.get_tags(filepath, tags=["CreateDate"]): # Grab the date the image was created

            for k, v in d.items(): # print out key-value pairs

                if (k == "EXIF:CreateDate"): # If key matches what we're looking for

                    match = re.search(pattern, v) # Extract info with regex
                    if match:
                        year = match[1]
                        month = match[2]
                        day = match[3]
                        hour = match[4]
                        minute = match[5]
                        second = match[6]
                        newFilename = year + month + day + "_" + hour + minute + second + "_" + eventName + ".ARW"
                        os.rename(filepath, os.path.join(rootFilepath, newFilename)) # Rename file 
                

print("Done")