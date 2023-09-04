import pprint
import google.generativeai as palm
import infra.palm.palm_config as palm_config
from llama_index.llms.palm import PaLM as llama_palm

cfg = palm_config.load_config()
api_key = cfg["api_key"]

palm.configure(api_key=api_key)

models = [
    m for m in palm.list_models() if "generateText" in m.supported_generation_methods
]
model = models[0].name

model = llama_palm(api_key=api_key)
print(model.complete("Hello, tell me a story about your life as an ai."))
