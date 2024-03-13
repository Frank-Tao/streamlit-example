from huggingface_hub import InferenceClient

client = InferenceClient(
    "mistralai/Mistral-7B-Instruct-v0.1"
)

prompt = """<s>[INST] What is AI?  [/INST]</s>
"""

res = client.text_generation(prompt, max_new_tokens=95)
print(res)