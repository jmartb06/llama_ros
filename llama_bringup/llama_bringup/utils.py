# MIT License

# Copyright (c) 2023  Miguel Ángel González Santamarta

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
from ament_index_python.packages import get_package_share_directory
from huggingface_hub import hf_hub_download
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def get_base_launch_path() -> str:
    return os.path.join(
        get_package_share_directory("llama_bringup"),
        "launch",
        "base.launch.py")


def download_model(repo: str, file: str) -> str:

    if repo and file:
        return hf_hub_download(repo_id=repo, filename=file, force_download=False)

    return ""


def get_prompt_path(prompt_file_name: str) -> str:

    if prompt_file_name:

        return os.path.join(
            get_package_share_directory("llama_bringup"),
            "prompts",
            prompt_file_name
        )

    return ""


def create_llama_launch(
    seed: int = -1,
    n_ctx: int = 512,
    n_batch: int = 8,

    n_gpu_layers: int = 0,
    main_gpu: int = 0,
    tensor_split: str = "[0.0]",

    rope_freq_base: float = 0.0,
    rope_freq_scale: float = 0.0,

    mul_mat_q: bool = True,
    f16_kv: bool = True,
    logits_all: bool = False,
    use_mmap: bool = True,
    use_mlock: bool = False,
    embedding: bool = True,

    n_threads: int = 4,
    n_predict: int = 128,
    n_keep: int = -1,

    model_repo: str = "",
    model_filename: str = "",

    lora_base_repo: str = "",
    lora_base_filename: str = "",

    numa: bool = True,

    prefix: str = "",
    suffix: str = "",
    stop: str = "",

    prompt: str = "",
    file: str = "",
    debug: bool = True
) -> IncludeLaunchDescription:

    return IncludeLaunchDescription(
        PythonLaunchDescriptionSource(get_base_launch_path()),
        launch_arguments={
            "seed": str(seed),
            "n_ctx": str(n_ctx),
            "n_batch": str(n_batch),

            "n_gpu_layers": str(n_gpu_layers),
            "main_gpu": str(main_gpu),
            "tensor_split": tensor_split,

            "rope_freq_base": str(rope_freq_base),
            "rope_freq_scale": str(rope_freq_scale),

            "mul_mat_q": str(mul_mat_q),
            "f16_kv": str(f16_kv),
            "logits_all": str(logits_all),
            "use_mmap": str(use_mmap),
            "use_mlock": str(use_mlock),
            "embedding": str(embedding),

            "n_threads": str(n_threads),
            "n_predict": str(n_predict),
            "n_keep": str(n_keep),

            "model": download_model(model_repo, model_filename),
            "lora_base": download_model(lora_base_repo, lora_base_filename),
            "numa": str(numa),

            "prefix": prefix,
            "suffix": suffix,
            "stop": stop,

            "prompt": prompt,
            "file": get_prompt_path(file),
            "debug": str(debug)
        }.items()
    )
