from PIL import Image
import random

sample = input('Enter string to be encrypted')

im = Image.open("input.png", 'r')
pixels = list(im.getdata())

sample_list = [str(ord(x)) for x in sample]

for i in sample_list:
	#converting all ascii ordinate values to 3 digit
	if len(i) == 1:
		f = '00' + i
		sample_list[sample_list.index(i)] = f
	elif len(i) == 2:
		f = '0' + i
		sample_list[sample_list.index(i)] = f

block_len = len(sample)//6 + 1

used = []
key = ''
count = 0

def checker(a: int):
	#making sure repeated numbers or numbers above 255 dont exist
	for i in range(a-6, a+1):
		if (a in used) or (255 in pixels[a]) or (254 in pixels[a]) or (253 in pixels[a]) or (252 in pixels[a]) or (251 in pixels[a]) or (250 in pixels[a]):
			return False
	return True

#plotting which pixels to convert and generating key
for _ in range(block_len):
	x = random.randint(6, len(pixels))
	while checker(x) == False:
		x = random.randint(6, len(pixels))
		checker(x)
	key += f'{x}-'
	for i in range(7,1,-1):
		count += 1
		if count > len(sample_list):
			key += f'{len(sample_list) - ((len(sample_list)//6)*6)}04'
			break
		used.append(pixels[x-(i-1)])

key_list = key.split(sep='-')

def replacer(tup: tuple, num: str):
	#implementing encrypting logic 
	tup = list(tup)

	for i in tup:
		tup[tup.index(i)] = str(i)

	tup[0] = tup[0][:-1]+num[0]
	tup[1] = tup[1][:-1]+num[1]
	tup[2] = tup[2][:-1]+num[2]

	for i in tup:
		tup[tup.index(i)] = int(i)

	tup = tuple(tup)
	return tup

pix = sample_list.copy()

for i in key_list[:-1]:
	#encrypting
	for j in range(int(i), int(i)-6, -1):
		try:
			pixels[j] = replacer(pixels[j], pix[0])
			del pix[0]
		except:
			pass

image_out = Image.new(im.mode,im.size)
image_out.putdata(pixels)
print(key) #you will want to save this somewhere
image_out.save("output.png")
