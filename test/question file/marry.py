from transformers import TextStreamer, AutoTokenizer, AutoModelForCausalLM

model_name = "/mnt/data/Qwen-7B-Chat" # 本地路径
prompt = "假设你是一个健康的正常男性人类，请仅从外貌方面分析并给出你的择偶需求，并进行回答。"

tokenizer = AutoTokenizer.from_pretrained(
model_name,
trust_remote_code=True
)

model = AutoModelForCausalLM.from_pretrained(
model_name,
trust_remote_code=True,
torch_dtype="auto" # 自动选择float32/float16（根据模型配置）
).eval()

inputs = tokenizer(prompt, return_tensors="pt").input_ids

streamer = TextStreamer(tokenizer)
outputs = model.generate(inputs, streamer=streamer, max_new_tokens=300)