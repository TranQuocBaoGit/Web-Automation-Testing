from PIL import Image

def crop_and_replace_image(image_path, start_width, start_height, percent_width, percent_height):
    # Open the image
    original_image = Image.open(image_path)

    # Get the dimensions of the original image
    og_width, og_height = original_image.size

    # Calculate the cropping coordinates
    left = og_width * start_width
    upper = og_height * start_height
    right = og_width * percent_width
    lower = og_height * percent_height

    # Crop new image
    new_image = original_image.crop((left, upper, right, lower))

    # Save the top half back to the same file, replacing the original image
    new_image.save(image_path)

