import os
import random
import requests
from PIL import Image, ImageDraw, ImageFont
import textwrap
import shutil

# Constants for the font path, font size and text width
FONT_PATH = '/path/to/font'
FONT_SIZE = 50
TEXT_WIDTH = 2000

def get_inspirational_quote():
    """Returns a random inspirational quote and its author from an API."""
    # Make a GET request to the API and handle any exceptions
    try:
        response = requests.get('https://api.quotable.io/random?tags=inspirational')
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        return None, None
    
    # Parse the JSON data and extract the quote and author
    data = response.json()
    quote = data['content']
    author = data['author']
    return quote, author

def draw_quote_on_image(image_path, quote, author):
    """Draws a quote and its author on a given image and saves it."""
    # Open the image and create a copy
    image = Image.open(image_path)
    new_image = image.copy()

    # Set the font and size for the text
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    # Format the text with f-strings
    text = f'{quote}\n\n- {author}'

    # Create an ImageDraw object and set the font
    draw = ImageDraw.Draw(new_image)

    # Wrap the text to fit within the specified width
    lines = textwrap.wrap(text, width=int(TEXT_WIDTH / (FONT_SIZE * 0.6)))

    # Calculate the height of the text
    text_height = sum([font.getsize(line)[1] for line in lines])

    # Calculate a random position for the text
    x = random.randint(0, new_image.width - TEXT_WIDTH)
    y = random.randint(0, new_image.height - text_height)

    # Draw each line of text on the image
    for line in lines:
        draw.text((x, y), line, font=font)
        y += font.getsize(line)[1]

    # Save the new image
    new_image.save(image_path)

def main():
    """The main function that runs the script."""
    # Set the path to the original image
    original_image_path = '/path/to/original/image'

    # Set the path to the duplicated image
    duplicated_image_path = '/path/to/duplicated/image' # it's the path that the new image will be saved to

    # Copy the original image to the duplicated image path using shutil module
    shutil.copy(original_image_path, duplicated_image_path)

    # Get a random inspirational quote and its author from an API
    quote, author = get_inspirational_quote()

    # If the quote and author are not None, draw them on the duplicated image
    if quote and author:
        draw_quote_on_image(duplicated_image_path, quote, author)
    
if __name__ == '__main__':
    main()
