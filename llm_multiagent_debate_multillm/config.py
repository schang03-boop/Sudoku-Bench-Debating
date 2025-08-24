from constant import *

MODEL_REFERENCES = {
    LLAMA_3: 'meta-llama/Meta-Llama-3.1-8B-Instruct',
    LLAMA_3_PIPELINE: 'meta-llama/Meta-Llama-3.1-8B-Instruct',
    LLAMA_3_NIM: 'meta-llama/Meta-Llama-3.1-8B-Instruct',
    MISTRAL_7B: 'mistralai/Mistral-7B-Instruct-v0.3',
    OPENAI_GPT: 'gpt-3.5-turbo',
    CUSTOM_ENDPOINT: {
        'api_url': 'https://api-inference.huggingface.co/models/',
        'api_key': '',
        'nim_base_url': 'https://huggingface.co/api/integrations/dgx/v1'
    }
}








