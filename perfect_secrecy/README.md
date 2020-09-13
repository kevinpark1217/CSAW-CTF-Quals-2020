# Perfect Secrecy
Crypto for 50 points:

> Alice sent over a couple of images with sensitive information to Bob,
> encrypted with a pre-shared key. It is the most secure encryption scheme,
> theoretically...

The attached files were:
* `problem/image1.png`
* `problem/image2.png`


# Solution 1
We're given two images of the same size, and we might think to overlay them.
Perhaps combining the black and white pixels will reveal some sort of pattern.
And indeed, they do. Importing both images into GIMP as layers, then dropping
the opacity of the top layer reveals a message, shown in
`solution/overlay_transparant.png`.

> Here's your flag \
> `ZmxhZ3swbjnfdDFtM19QQGQhfQ==`

Putting that into a Base64 decoder gives the flag: `flag{0n9t1m3_P@d!}`.


# Solution 2
The problem text hints that these two images form a one-time-pad. It is indeed
the most secure encryption scheme, theoretically. A common one-time-pad scheme
operating at the bit-level uses exclusive or. Why? Because it's the only
"standard" bitwise operation such that every element (`{0,1}`) has an inverse.
This allows you to, given `Message ^ Pad = Ciphertext`, as well as `Pad` and
`Ciphertext`, solve for `Message` in *all* cases.

Each of the pixels in the problem images are either white or black, presumably
representing bits. Most likely, one of the images is the pad and the other is
the ciphertext. To solve for the message under this scheme, we simply XOR the
pad and the ciphertext. So, we wish to find the XOR of both images.

We could use the method in Solution 1, which computes the XOR by "blending" the
two images. Grey pixels are places where the images differ, and black or white
pixels are where the images are the same. Alternatively, we can write a Python
program to do this for us, as shown in `solution/xor_imgs.py`.

The result is shown in `solution/overlay_xor.png`. From here, it's the same
steps as Solution 1. We read off the image and Base64 decode to get the flag: `flag{0n9t1m3_P@d!}`.
