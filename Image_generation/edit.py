import openai
import secret
from io import BytesIO
from PIL import Image

# pip3 install Pillow

openai.api_key = secret.API_KEY

def read_rgba_image(path,resize) -> bytes:
    image = Image.open(path)
    if resize is not None:
        image = image .resize(resize)
    image = image.convert('RGBA')
    bytes_stream = BytesIO()
    image.save(bytes_stream, format='PNG')
    return bytes_stream.getvalue()

image_bytes = read_rgba_image("Image_generation/img/image.png",resize=(1024,1024))
mask_bytes = read_rgba_image("Image_generation/img/mask.png",resize=(1024,1024))

my_prompt = "a gold retriever is sitting there"
print(my_prompt)

response = openai.Image.create_edit(
    image=image_bytes,
    mask=mask_bytes,
    prompt=my_prompt,
    n=1,
    size="1024x1024"
)

for i in range(len(response['data'])):
    print("\n url: " + response['data'][i]['url'])
