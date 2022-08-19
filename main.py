import aspose.slides as slides
import aspose.pydrawing as drawing

# Load presentation
pres = slides.Presentation("samplepptx.pptx")

desiredX = 1200
desiredY = 800
scaleX = (float)(1.0 / pres.slide_size.size.width) * desiredX
scaleY = (float)(1.0 / pres.slide_size.size.height) * desiredY

# Loop through slides
for index in range(pres.slides.length):
    # Get reference of slide
    slide = pres.slides[index]

    # Save as JPG
    slide.get_thumbnail(scaleX, scaleY).save("slide_{i}.jpg".format(i = index+1), drawing.imaging.ImageFormat.jpeg)
