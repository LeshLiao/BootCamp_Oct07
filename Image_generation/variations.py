# openai - variations

import openai
import secret

openai.api_key = secret.API_KEY

image_file = "Image_generation/img/image.png"
print(image_file)

response = openai.Image.create_variation(
  image=open(image_file, "rb"),
  n=1,
  size="1024x1024"
)

num = len(response['data'])
for i in range(num):
    print("url_: " + response['data'][i]['url'])

