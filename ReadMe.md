# ml_hack_0 project

Recreational Hack #0: Something involving ML and vision

## Installation

```
git clone git@github.com:geekscape/ml_hack_0.git
cd ml_hack_0
python -m venv venv       # Once only, preferably python 3.12.7
source venv/bin/activate  # Each terminal session
pip install -U pip        # Install latest pip
pip install -e .          # Install ml_hack_0 for development
```

## Usage

Start an Aiko Services Pipeline that displays web camera video.

Position mouse pointer over the "video window" and
press "x" to exit the Pipeline ...

```
aiko_pipeline create src/ml_hack_0/webcam_pipeline.json -s 1
```

Set logging level to debug ...

```
aiko_pipeline create src/ml_hack_0/webcam_pipeline.json -s 1 -ll debug
```

## Development

vi src/ml_hack_0/webcam_pipeline.json  # PipelineDefinition
vi src/ml_hack_0/elements.py           # PipelineElements source code
