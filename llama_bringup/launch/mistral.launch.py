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


from launch import LaunchDescription
from llama_bringup.utils import create_llama_launch


def generate_launch_description():

    return LaunchDescription([
        create_llama_launch(
            n_ctx=512,
            n_batch=8,
            n_gpu_layers=0,
            n_threads=4,
            n_predict=512,

            model_repo="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
            model_filename="mistral-7b-instruct-v0.1.Q4_K_M.gguf",

            prefix="\n\n[INST] ",
            suffix="\n\n[/INST] ",
            stop="[INST] ",

            file="mistral.txt"
        )
    ])
