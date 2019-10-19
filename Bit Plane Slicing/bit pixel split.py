from PIL import Image

# Input
imagePath = "test images/BS2.png"
imageName = imagePath.split('/')[-1].split('.')[0]

threshold = 0.1

bits =[1, 2, 4, 8, 16, 32, 64, 128] # 00000001, 00000010,...,10000000

# Step 1: Load the image
img = Image.open(imagePath)

# Step 2: Convert image to GreyScale
imgGS = img.convert('L') # Luminosty

width, height = imgGS.size
totalSize = width*height

uselessBitsIndices= []

pixelData = imgGS.load()

# Step 3: Loop on all bits
for bitIndex in range(len(bits)):
    # Loop on the image
    tempIMG = imgGS.copy()
    tempIMGdata = tempIMG.load()
    counter = 0 # Counter to count set bits
    for i in range(width):
        for j in range(height):
            tempIMGdata[i,j] = 0
            if (pixelData[i,j] & bits[bitIndex]) > 0:
                counter += 1
                tempIMGdata[i,j] = 255
    tempIMG.save("result images/"+imageName+" "+str(bitIndex)+"."+imagePath.split('.')[1])
    print(counter/totalSize)
    if counter / totalSize < threshold: # Check if bit is useless
        uselessBitsIndices.append(bitIndex+1) # one indexed

print(uselessBitsIndices)