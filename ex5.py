# Take the followinf code : 'str = "X-DSPAM-Confidence:0.8475"'
# Use find and string slicing to extract the portion of the string after the colon character 
# and then use the float function to convert the extracted string into a floating point number.

str = 'X-DSPAM-Confidence:0.8475'

start = str.find(':')                         # locates ':' in string
data = str[start +1:]                         # slices the string from after the ':'
number = float(data)                          # converts string number to float number
print(number)                                
print(type(number))
