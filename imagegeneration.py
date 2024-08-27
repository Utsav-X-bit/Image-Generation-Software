import openai
from PIL import Image
import requests
from io import BytesIO
import os

openai.api_key = open('api_key.txt', 'r').read()

prompt = input("Enter specifications: ")
if prompt.lower() == 'banasthali public school':
    img_BPS = Image.open('images/BPS.jpeg')
    img_BPS.show()
elif prompt.lower() == 'principal' :
    img_principal = Image.open('images/BPS_principal.jpeg')
    img_principal.show()
else :
    size = '1024x1024'
    
    response = openai.Image.create(prompt=prompt, n=1, size=size)
    
    
    image_url = response['data'][0]['url']
    
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    
    img.show()
    
    if not os.path.exists('images'):
        os.makedirs('images')
    
    filename = os.path.join('images', 'image.png')
    img.save(filename)
     variation_ask = input("Do you want variation of this Image ?? : ")
    
    
     def Variation() :
         response_1 = openai.Image.create_variation(
           image=open("images/image.png", "rb"),
           n=1,
           size="1024x1024"
         )
         image_url_1 = response_1['data'][0]['url']
        
         response_1 = requests.get(image_url_1)
         img_1 = Image.open(BytesIO(response_1.content))
    
         img_1.show()
    
         if not os.path.exists('images'):
             os.makedirs('images')
    
         filename_1 = os.path.join('images', 'image_edited.png')
         img.save(filename_1)
    
    
     if variation_ask.lower() == 'no' :
         print("Thank You :)")
     elif variation_ask.lower() == 'yes' :
         Variation()
    
