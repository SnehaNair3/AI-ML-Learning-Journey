from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model
model_name = "gpt2"

model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Evaluation mode
model.eval()


# Responses to evaluate
responses = [
    "The capital of France is Paris",
    "France capital is Paris the"
]


# Function to calculate Perplexity
def compute_ppl(text):

    # Tokenize text
    encodings = tokenizer(text, return_tensors="pt")

    input_ids = encodings["input_ids"]
    attention_mask = encodings["attention_mask"]

    # Calculate loss
    with torch.no_grad():
        outputs = model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            labels=input_ids
        )

        loss = outputs.loss

    # Perplexity = e^loss
    perplexity = torch.exp(loss).item()

    return perplexity


# Calculate PPL for each response
for i, response in enumerate(responses, 1):

    ppl = compute_ppl(response)

    print(f"Response {i}: '{response}'")
    print(f"PPL Score: {ppl:.2f}")
    print()