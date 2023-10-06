# openai - Python Pip Package

import openai
import secret
import ex5

openai.api_key = secret.API_KEY

my_prompt = ex5.get_a_animal() + " " + ex5.get_a_place()
print("prompt= " + my_prompt)

response = openai.Image.create (
    prompt=my_prompt,
    n=1,
    size="1024x1024"
)

num = len(response['data'])
for i in range(num):
    print("url_: " + response['data'][i]['url'])
