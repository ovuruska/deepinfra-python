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
print(transcription)
```

