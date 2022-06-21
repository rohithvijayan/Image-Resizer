from PIL import Image
filepath = input('enter filepath:')
img = Image.open(filepath)
# img.show()
new_dimensions = []
a = int(input('Enter width:'))
b = int(input('Enter height:'))
new_dimensions.extend([a, b])
img.thumbnail(new_dimensions)
img.save('Resized_Image.png', 'png')
img.show()
