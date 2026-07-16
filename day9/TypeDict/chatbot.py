#AI Chatbot Receiving Mixed Inputs - union, sequence

from typing import Union, Sequence

InputData = Union[str,bytes]

def chatbots(inputs:Sequence[InputData]):
    for item in inputs:
        if isinstance(item,str):
            print("User Text: ",item)
        else:
            print("Image Uploaded: (",len(item), "bytes)") #(4 bytes)

conversation = (
    "Hi",
    "Show me nearby restaurant",
    b'\x89PNG',
    "Explain this image"
)
#b'\xff\xd8\xff' - 3 bytes - jpeg

chatbots(conversation)