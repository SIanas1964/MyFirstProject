from PIL import Image
im = Image.open("example.png")
im_resiz = im.resize((640,480))
im_rotate = im.rotate(90)
im.rotate(180).resize((640,480)).save("example/flipped_and_resized.jpg")
im_resiz.save("example/example_resized.jpg")
im_rotate.save("example/example_rotated.jpeg")