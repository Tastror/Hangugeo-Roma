# Hangugeo-Roma

## What for?

A lightweight GUI application that **transliterates Hangul into Roman script**, making learning Korean smoother for beginners.

## How to use?

Download the latest release, open the binary file `hangugeo-UI.exe`, type in the Hangul in the left and you'll see the output in the right.

## Feature

You can change the transliteration rules in [hangugeo.json](hangugeo.json).

## Develop

The binary(exe) file is generated by [pyinstaller](https://pyinstaller.org/en/stable/), by using the commands below.

```shell
pip install pyinstaller wxPython
pyinstaller -F -w hangugeo-UI.py
cp hangugeo.json dist/
```
