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
    #create new object from HuffmanCoding class
    h = HuffmanCoding(path)
    #compress file from above path
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
    #give address file for compress
    picture_name = "./" + input("Enter your picture name: ")
    # convert image to 8-bit grayscale
    img = Image.open(picture_name).convert('L')  
    #set width and height from picture
    WIDTH, HEIGHT = img.size
     # convert image data to a list of integers
    data = list(img.getdata())
    
    # convert that to 2D list (list of lists of integers)
    data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]
    #join all character for string file
    str1 = ''.join(str(e) for e in data)
    str1 = re.sub(r"/D"," ",str1)
    #save arr pict to str file
    
    with open("array_string.txt", "w")as txt_file:
        #write all string from arr picture
        txt_file.write(str1)
    path = "./array_string.txt"
     #call compress function for compress this path
    compress(path)
    
elif user_choose == 2:
   #give address file for compress 
    path = "./" + input("Enter your text file name: ")
    #call compress function for compress this path
    compress(path)

elif user_choose ==3:
    # huffman_file_name = "./" + input("Enter huffman file name : ")
    huffman_file_name = "./" + "array_string_text.txt"
    #open huffman file 
    with open(huffman_file_name,'r+') as huffman_file:
        #read all character from this file 
        huffman_str = huffman_file.read()
        #remove all space from huffman_str
        huffman_str = huffman_str.rstrip()
        #make new object from HuffmanCoding class
    h = HuffmanCoding("")
    #init new dict arr
    frequency = {}
    #read all character from this file 
    # frequency_file_name = "./" + input("Enter frequency file name : ")
    frequency_file_name = "./" + "freq.txt"
    with open(frequency_file_name,'r+') as frequency_file:
        #read all character from this file 
        frequency_str = frequency_file.read()
        #remove all space from frequency_str
        frequency_str = frequency_str.rstrip()
        
    frequency = h.createFrequencyArr(frequency_str)
    # size = input("Enter size of arr  forexample 12*20 :")
    size ="256 *256"
    #make array like [21,43]
    tempArr = re.findall("\d+",size)
    #seprate between two index arr
    HEIGHT, WIDTH = int(tempArr[0]), int(tempArr[1])
    print(HEIGHT,WIDTH)
    #decode huffman string with frequency dict
    print(huffman_str)
    print(frequency)
    numbers = h.decompress(huffman_str, frequency)
    # print(numbers)
    #make arr with numbers string forexample: "32 12 0 1" convert to [32,12,0,1]
    numbers = re.findall("\d+", numbers)
    
    array_for_pict = np.array(numbers, np.uint8)[0:len(numbers)-1]
   
    # Reshape the array into a 
    # familiar resoluition
    new_arr_for_pict = np.reshape(array_for_pict, (WIDTH, HEIGHT))
    print(new_arr_for_pict)
    # sys.exit()
    # creating image object of
    # above array
    data = Image.fromarray(new_arr_for_pict)
    # saving the final output 
    # as a PNG file
    data.save('image.png')





    

         
