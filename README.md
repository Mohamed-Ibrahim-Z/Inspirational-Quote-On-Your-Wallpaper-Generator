# Inspirational-Quote-On-Your-Wallpaper-Generator
A Python script that randomly selects an inspirational quote from an API and draws it on your chosen wallpaper image. The script runs every time you open Linux and changes your desktop background with the new image.

# Requirements
Python 3  
Requests library  
Pillow library  
Shutil module  
# Usage
1. Clone or download this repo
2. Set the path to the font (line 9)
3. Set the path to the original image in the main function (line 65)
4. Set the path to the duplicated image in the main function (line 68) (this should be the path of the current background image so it can be overwritten)
5. Try the script, If it runs correctly make the script run on the start up of your linux system
6. Enjoy your new inspirational wallpaper!

# Example
My original wallpaper:
![BackgroundBefore](/assets/Before.png)
My wallpaper after running the script:
![BackgroundAfter](/assets/After.png)

# API
The script uses the API from https://api.quotable.io/random?tags=inspirational to get a random quote. The API is free to use and doesn't require a key. The API returns a random quote in JSON format.


# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
