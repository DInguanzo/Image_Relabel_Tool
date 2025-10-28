# Image Relabel Tool

Small python script to make renaming of image file easier.

## Use

This script is supposed to rename image file names according to the date the image was taken and the event name using 
following format: YYYYMMDD_HHMMSS_event-name.ARW

Open up the script and change the event name and root folder path for where your pictures are stored, that's it!

## Dependencies 

Uses the [`PyExifTool`](https://github.com/sylikc/pyexiftool) library which requires the [`ExifTool` by Phil Harvey](https://exiftool.org/) to be installed.
