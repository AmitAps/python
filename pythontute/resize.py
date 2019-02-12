from PIL import Image
from sys import argv

if(argv) != 4:
    exit("Usage: python resize.py n inile outfile")

n = int(argv[1])
infile = argv[2]
outfile = argv[3]

inimage = Image.open(infile)
width, height = inimage.size
outimage = inimage.resize(width * n, height * n)

outimage.save(outfile)
