[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=ovuruska_deepinfra-python&metric=bugs)](https://sonarcloud.io/summary/new_code?id=ovuruska_deepinfra-python)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=ovuruska_deepinfra-python&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=ovuruska_deepinfra-python)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=ovuruska_deepinfra-python&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=ovuruska_deepinfra-python)
![Build Status](https://github.com/ovuruska/deepinfra-python/actions/workflows/deploy.yaml/badge.svg)
[![PyPI version](https://badge.fury.io/py/deepinfra.svg)](https://pypi.org/project/deepinfra/)
[![Python Version](https://img.shields.io/pypi/pyversions/deepinfra.svg)](https://pypi.org/project/deepinfra/)
[![License](https://img.shields.io/github/license/ovuruska/deepinfra-python.svg)](LICENSE)

# deepinfra

`deepinfra` is a Python library designed to provide a simple interface for interacting with DeepInfra's Inference API, facilitating various AI and machine learning tasks.

## Installation

To install `deepinfra`, run the following command:

```bash
pip install deepinfra
```

## Examples

### Use Automatic Speech Recognition

You can use the Automatic Speech Recognition (ASR) API to transcribe audio files, URLs and buffer objects.
#### Transcribe an audio file

```python
from deepinfra import AutomaticSpeechRecognition

model_name = "openai/whisper-base"
asr = AutomaticSpeechRecognition(model_name)

file_path = "path/to/audio/file" 
body = {
    "audio": file_path
}
transcription = asr.generate(body)
print(transcription["text"])
```

#### Transcribe an audio URL

```python
from deepinfra import AutomaticSpeechRecognition

model_name = "openai/whisper-base"
asr = AutomaticSpeechRecognition(model_name)

url = "https://path/to/audio/file"
body = {
    "audio": url
}
transcription = asr.generate(body)
print(transcription["text"])
```

#### Generate an image using SDXL

```python
from deepinfra import Sdxl
import requests

model = Sdxl()
body = {
    "input":{
        "prompt": "A happy little cloud"
    }
}
resp = model.generate(body)
image = resp["images"][0]
image_url = resp["output"][0]

# Write image_url to image.png
with open("image.png", "wb") as file:
    file.write(requests.get(image_url).content)

```

#### Generate an image using a text-to-image model

```python
from deepinfra import TextToImage
import base64

model_name = "CompVis/stable-diffusion-v1-4"
model = TextToImage(model_name)
body = {
    "prompt": "A happy little cloud"
}
resp = model.generate(body)
image = resp["image"]
image = image.replace("data:image/png;base64,", "")

with open("image.png", "wb") as fp:
    fp.write(base64.b64decode(image))
```

#### Generate text using LLM

```python
from deepinfra import TextGeneration

model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
model = TextGeneration(model_name)
body = {
    "input": "Write a story about a happy little cloud"
}
resp = model.generate(body)
result = resp["results"][0]["generated_text"]
print(result)
```