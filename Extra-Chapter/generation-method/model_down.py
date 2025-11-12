from modelscope import snapshot_download

model_dir = snapshot_download('kmno4zx/happy-llm-215M-sft', cache_dir='your/cache/dir', revision='master')