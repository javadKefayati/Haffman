from huffman import HuffmanCoding
import sys
import matplotlib.pyplot as plt
import numpy as np
import re
from PIL import Image

path = ""

def separateKeyAndValue(arr):
    keys = []
    values=[]
    for i in arr:
          keys.append(i)
          values.append(arr[i])
    return keys,values

def compress(path):

    h = HuffmanCoding(path)
    output_path = h.compress()

    #show nemodar
    keys , values = separateKeyAndValue(h.frequency)
    x = np.array(keys)
    y = np.array(values)
    plt.bar(x,y)
    plt.show()
    # end show nemodar

    print("Compressed file path: " + output_path)


user_choose = int(input("Choose between input:\n\
1-Your input is picture \n2-Your input is array\n3-Your input is huffman for convert ot picture\n"))

if user_choose == 1:
    picture_name = "./" + input("Enter your picture name: ")
    img = Image.open(picture_name).convert('L')  # convert image to 8-bit grayscale
    
    WIDTH, HEIGHT = img.size
    data = list(img.getdata()) # convert image data to a list of integers
   

    # convert that to 2D list (list of lists of integers)
    data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]
    str1 = ''.join(str(e) for e in data)
    str1 = re.sub("([|])","",str1)
    print(str1)
    sys.exit()
    # print("data is: ", data)
    #save arr pict to str file
    
    with open("array_string.txt", "w") as txt_file:
        txt_file.write(str1)
    path = "./array_string.txt"
    compress(path)
    
elif user_choose == 2:
    path = "./" + input("Enter your text file name: ")
    compress(path)
    


