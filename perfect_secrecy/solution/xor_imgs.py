import sys
from PIL import Image


# Check that the right arguments were provided
if len(sys.argv) != 4:
    print("Usage: xor_imgs.py file1 file2 output")
    exit(1)


# Open the images in the arguments
file1 = sys.argv[1]
file2 = sys.argv[2]
outfile = sys.argv[3]
img1 = Image.open(file1)
img2 = Image.open(file2)

# Assert that the images are in fact the same size
if img1.size != img2.size:
    print("Images must be the same size")
    exit(2)


# Create the output image
# It is only black or white, and has the same size as the inputs
out = Image.new('1', img1.size)

# Write to the output
for x in range(out.width):
    for y in range(out.height):
        # Get pixels off the input images
        p1 = img1.getpixel( (x,y) )
        p2 = img2.getpixel( (x,y) )
        # Check that the pixels are greyscale
        if type(p1) == tuple or type(p2) == tuple:
            print("Input images must be greyscale")
        # Output the XOR
        out.putpixel( (x,y), p1^p2)

# Save the output
out.save(outfile)
