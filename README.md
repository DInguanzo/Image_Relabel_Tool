# Image Relabel Tool

Small python script to make renaming of image file easier.

## Use

This script is supposed to rename image file names according to the date the image was taken and the event name using
following format: YYYYMMDD_HHMMSS_event-name.ARW

Call the script in the following format:

```console
python image_relabel.py -h
```

Or

```console
python image_relabel.py /path/to/images/folder "event name"
```

The `eventName` positional argument is able to tolerate whitespace in the name as long as it is entered using quotation marks. (The whitespace will be removed i.e. "event name" -> eventname)

## Dependencies

Uses the [`PyExifTool`](https://github.com/sylikc/pyexiftool) library which requires the [`ExifTool` by Phil Harvey](https://exiftool.org/) to be installed.
