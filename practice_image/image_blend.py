from PIL import Image
 # Take two images for blending them together
image1 = Image.open("data2/coins1.jpg")
image2 = Image.open("data2/coins2.jpg")
 # Make sure images got an alpha channel
image5 = image1.convert("RGBA")
image6 = image2.convert("RGBA")
 # alpha-blend the images with varying values of alpha
alphaBlended1 = Image.blend(image5, image6, alpha=.2)
alphaBlended2 = Image.blend(image5, image6, alpha=.8)
 # Display the alpha-blended images
alphaBlended1.show()
alphaBlended2.show()