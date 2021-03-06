import re
from tempfile import tempdir
import matplotlib.pyplot as plt
import numpy as np
import heapq
import os
import sys

# from test import freq

class HuffmanCoding:
	def __init__(self, path):
		self.path = path
		self.heap = []
		self.codes = {}
		self.reverse_mapping = {}
		self.frequency = ""

	class HeapNode:
		# frequency
		def __init__(self, char, freq):
			self.char = char
			self.freq = freq
			self.left = None
			self.right = None

		# defining comparators less_than and equals
		def __lt__(self, other):
			return self.freq < other.freq

		def __eq__(self, other):
			if(other == None):
				return False
			if(not isinstance(other, HeapNode)):
				return False
			return self.freq == other.freq

	# functions for compression:
	#[324,222,743]

	# def make_frequency_dict(self, text):

	# 	frequency = {}
		

      	# another = re.findall("\D+", text)

      	# for num in numbers:
	      # if(not num in frequency):
	      #       frequency[num] = 0
      	#       frequency[num] += 1

      	# for ano in another:
	      #  for char in ano:
	      #        if(not char in frequency):
	      #              frequency[char] = 0
      	#              frequency[char] += 1
      	# return frequency

	

	def  make_frequency_dict(self, text):
		frequency={}
		numbers = re.findall("\d+", text)
		# another = re.findall("\D+", text)

		for num in numbers:
			if (not num in frequency):
				frequency[num] = 0
			frequency[num]+=1
		# for ano in another:
		# 	for char in ano:
		# 		if (not char in frequency):
		# 			frequency[char] = 0
		# 		frequency[char] += 1
		print(frequency)
		return frequency


	def make_heap(self, frequency):
		for key in frequency:
			node = self.HeapNode(key, frequency[key])
			heapq.heappush(self.heap, node)

	def merge_nodes(self):
		while(len(self.heap) > 1):
			node1 = heapq.heappop(self.heap)
			node2 = heapq.heappop(self.heap)

			merged = self.HeapNode(None, node1.freq + node2.freq)
			merged.left = node1
			merged.right = node2

			heapq.heappush(self.heap, merged)

	def make_codes_helper(self, root, current_code):
		if(root == None):
			return

		if(root.char != None):
			self.codes[root.char] = current_code
			self.reverse_mapping[current_code] = root.char
			return

		self.make_codes_helper(root.left, current_code + "0")
		self.make_codes_helper(root.right, current_code + "1")

	def make_codes(self):
		root = heapq.heappop(self.heap)
		current_code = ""
		self.make_codes_helper(root, current_code)

	def get_encoded_text(self, text):
		encoded_text = ""
		te = re.findall("\d+",text)
		print("size of input :"+str(len(te)*8))
		print(self.codes)
		for character in te:
			encoded_text += self.codes[character]
		print("size of  output :"+str(len(encoded_text)))
		print("size of  diffrent :"+str((len(te)*8-len(encoded_text))))
		return encoded_text

	def pad_encoded_text(self, encoded_text):
		extra_padding = 8 - len(encoded_text) % 8
		for i in range(extra_padding):
			encoded_text += "0"

		padded_info = "{0:08b}".format(extra_padding)
		encoded_text = padded_info + encoded_text
		return encoded_text

	def get_byte_array(self, padded_encoded_text):
		if(len(padded_encoded_text) % 8 != 0):
			print("Encoded text not padded properly")
			exit(0)

		b = bytearray()
		for i in range(0, len(padded_encoded_text), 8):
			byte = padded_encoded_text[i:i+8]
			b.append(int(byte, 2))
		return b

	def compress(self ):
		filename, file_extension = os.path.splitext(self.path)
		output_path = filename + ".bin"
		output_text_path = filename + "_text.txt"

		with open(self.path, 'r+') as file, open(output_path, 'wb') as output, open(output_text_path, 'w') as output_txt:
			text = file.read()
			text = text.rstrip()

			self.frequency = self.make_frequency_dict(text)
			# sys.exit()
			self.make_heap(self.frequency)
			self.merge_nodes()
			self.make_codes()
			# print(text)
			encoded_text = self.get_encoded_text(text)
			padded_encoded_text = self.pad_encoded_text(encoded_text)
			b = self.get_byte_array(padded_encoded_text)
			output_txt.write(encoded_text)

			output.write(bytes(b))

		print("Compressed")
		return output_path

	""" functions for convert huffman str to picture: """

	def createFrequencyArr(self, frequency_str):
		#init new dict arr
		frequency={}
		#cut all numbers from this string : for example: 32=>44 ,55=>143 convert to [32,44,55,143]
		numbers = re.findall("\d+", frequency_str)
		#make dict from numbers list
		for i in range(0, len(numbers)-1,2):
			frequency[numbers[i]]=numbers[i+1]

		return frequency
		


	def decompress(self, huffman_str , frequency ):
		numbers =""
		temp = ""
		# make string same => 12 232 13 453
		for char in huffman_str:
			temp += char
			for i in frequency:
				if frequency[i] == temp:
					numbers += i+" "
					temp=""
					continue
		return numbers



				


