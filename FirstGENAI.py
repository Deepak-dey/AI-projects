from transformers import pipeline

# Load CodeLlama (small instruct model for code generation)
generator = pipeline("text-generation", model="codellama/CodeLlama-7b-Instruct-hf")

prompt = "Write a Python function to remove null values from a pandas dataframe"
result = generator(prompt, max_length=200, do_sample=True)

print(result[0]['generated_text'])
