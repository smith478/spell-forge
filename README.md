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