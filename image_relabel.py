import exiftool # Tool for extracting image metadata
import os # Interfacing with OS and file syste
import re # Regular Expression 
import argparse # Argument parser for CLI
import pathlib

"""
This script is supposed to rename image file names according to the date the image was taken using 
following format: YYYYMMDD_HHMMSS_event-name.ARW.

Image date will be grabbed using the exifimage tool.
"""
def renameImages(rootFilePath:pathlib.Path, eventName:str):

    files = os.listdir(rootFilePath) # Gets a list of all files within root file path
    pattern = r'(?P<Year>\d{4}):(?P<Month>\d{2}):(?P<Day>\d{2})\s+(?P<Hour>\d{2}):(?P<Minute>\d{2}):(?P<Second>\d{2})' # Pattern to extract info from metadata

    for file in files:
        filepath = os.path.join(rootFilePath, file) # add file path to file name

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
                            newFileName = year + month + day + "_" + hour + minute + second + "_" + eventName + ".ARW"
                            os.rename(filepath, os.path.join(rootFilePath, newFileName)) # Rename file 
    print("Done")
                
def sanitizeEventNames(eventName):
    return (eventName.replace(" ", ""))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Image Relabel Tool',
        description="Rename image file names according to the date  the image was taken using following format: YYYYMMDD_HHMMSS_event-name.ARW."
    )
    
    parser.add_argument("filepath", 
                        type=pathlib.Path, 
                        help="The filepath to the folder that stores the images")
    
    parser.add_argument("eventName", 
                        help="The event the photos are going to be named after")

    args = parser.parse_args()

    eventName = sanitizeEventNames(args.eventName)
    
    renameImages(args.filepath, eventName)