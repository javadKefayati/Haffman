import re
# # def  freq(text):
# #       frequency = {}
# #       numbers = re.findall("\d+",text)
# #       another =  re.findall("\D+",text) 

# #       for num in numbers:
# #            if(not num in frequency)  :
# #                  frequency[num] = 0
# #            frequency[num] +=1  

# #       for ano in another:
# #             for char  in ano:
# #                   if(not char in frequency)  :
# #                         frequency[char] = 0
# #                   frequency[char] +=1
# #       return frequency

# # # print (freq("[123,32]]]aaa{{"))

# str ={"name":"javad","famil":"kefa"}
# for i in str:
#       print(i)
str = "123p=[123,43]"
te = re.findall("(\d+|\W)",str)
print(te)
