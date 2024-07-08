from PIL import Image

def get_black_pixels_in_portion(image_path, left=0, top=0, right=1, bottom=1):
    # Open an image file
    with Image.open(image_path) as img:
        # Convert the image to RGB mode
        img = img.convert('RGB')
        # Get the pixel data
        pixels = img.load()

        black_pixel_count = 0
        black_pixels = []

        # Iterate through each pixel in the specified portion of the image
        for y in range(top, bottom):
            for x in range(left, right):
                r, g, b = pixels[x, y]
                # Check if the pixel is black
                if r<120 and g<120 and b<120:
                    black_pixel_count += 1
                    black_pixels.append((x, y))

        #print(f'Number of black pixels in the specified portion: {black_pixel_count}')
        return black_pixels

#print(f'Coordinates of black pixels in the specified portion: {black_pixels}')

def GetImageDimensions(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        return width, height
