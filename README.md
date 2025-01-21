# Spell Forge
Experimentation with vLLM

Here we will experiment with [vLLM](https://github.com/vllm-project/vllm), the high throughput LLM serving library/tool.

## vLLM installation
We will be using linux OS as recommended, and we will use docker to install and run vLLM. One prerequisite is to install Docker and NVIDIA Container Toolkit since our docker image will use the GPU.

Pull the latest docker image:
```bash
export VLLM_COMMIT=f9ecbb18bf03338a4272c933a49a87021363b048 # use full commit hash from the main github branch
docker pull public.ecr.aws/q9t5s3a7/vllm-ci-postmerge-repo:${VLLM_COMMIT}
```

Run the docker image:
```bash
sudo docker run --gpus all --name spell-forge -it --rm -p 8888:8888 -p 8501:8501 -p 8000:8000 -p 80:80 --entrypoint /bin/bash -w /spell-forge -v $(pwd):/spell-forge -v ~/huggingface_models:/hf_models spell-forge:1.0
```

Note: to use newer models you may have to run `pip install --upgrade transformers` in the docker image. In which case `docker commit` can be used to save a new image.
```bash
docker commit a4f306f4f9d2 spell-forge:1.0
```

## Minimal example
A minimal example can be found in `vllm_minimal_example.py`, however some debugging is required, currently it says `LLM` has no attribute `llm_engine`. It may be the version of vLLM needs to be updated.

## Resources
- [llama 3.2 1B](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct)
- [vLLM example](https://christiangrech.medium.com/unlock-faster-llm-serving-with-vllm-a-step-by-step-guide-331afc2f5bf5)
- [Google blog post](https://developers.googleblog.com/en/inference-with-gemma-using-dataflow-and-vllm/)