from vllm import LLM, SamplingParams

# Initialize the LLM
llm = LLM(model="/hf_models/Qwen-Qwen2.5-7B-Instruct/", tokenizer_mode="slow", trust_remote_code=True, max_model_len=4096, enforce_eager=True, dtype="bfloat16")

# Create sampling parameters
sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=100, skip_special_tokens=False)

# Generate text
prompts = ["Explain quantum physics in 50 words."]
outputs = llm.generate(prompts, sampling_params)

# Print results
for output in outputs:
    print(f"Prompt: {output.prompt}")
    print(f"Generated text: {output.outputs[0].text}\n")