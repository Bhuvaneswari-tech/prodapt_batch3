#A company is building AI virtual Assistant
#It has to accept different input format - text, image, audio

from typing import Union

def process_input(data: Union[str, bytes])-> None:
    if isinstance(data,str):
        print("Processing Text: ", data)
    elif isinstance(data, bytes):
        print("Processing Image/Audio Bytes: ", data)

process_input("Artificial Intelligence")

process_input(b'\x89PNG\r\n')

#Union - One variable can accept different data types.
#89 - Non printable byte used to identify PNG image
#PNG - PNG image
#\r - Carriage return
#\n - new line
#isinstance - for checking the input type
    
    