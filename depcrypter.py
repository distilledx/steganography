from PIL import Image

key = input('Enter key')

im = Image.open("output.png", 'r')
pixels = list(im.getdata())

key_list = key.split(sep='-')

ords = []

def taker(tup: tuple):
	return str(tup[0])[-1]+str(tup[1])[-1]+str(tup[2])[-1]

for i in key_list[:-1]:
	for j in range(0,6):
		ords.append(taker(pixels[int(i)-j]))

chars = [chr(int(i)) for i in ords]
final = "".join(chars)[:-(6-int((key_list[-1][0])))] #cutting off unnecessary characters
print(final)
