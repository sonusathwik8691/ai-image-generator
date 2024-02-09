import openai

openai.api_key = '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'  

def generate_image(prompt):
    response = openai.Completion.create(
        engine="image-alpha-001", 
        prompt=prompt,
        max_tokens=100,
        n=1,
    )
    return response['choices'][0]['text']

prompt_text = "A serene sunset over a mountain lake."
generated_image = generate_image(prompt_text)
print(generated_image)






