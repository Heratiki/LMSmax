# LMSmax - LM Studio Model Settings Optimizer

A tool to optimize model settings for better performance in LM Studio by discovering models and applying optimal settings from Hugging Face.

## Features

- Automatic model discovery via LM Studio API
- Fetches optimal settings from Hugging Face
- Applies settings automatically to LM Studio models
- Logging and error handling
- Configuration via environment variables

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Copy `.env.example` to `.env` and configure your settings:
   - Set your LM Studio API key
   - Set your Hugging Face token
   - Adjust logging settings if needed

## Usage

Run the optimizer:
```bash
python src/main.py
```

## Development

- Run tests: `pytest`
- Format code: `black .`
- Sort imports: `isort .`
- Type checking: `mypy src/`

## Project Structure

```
LMSmax/
├── src/
│   ├── main.py          # Main entry point
│   ├── models.py        # LM Studio API interaction
│   ├── settings.py      # Hugging Face settings fetcher
│   └── utils.py         # Utility functions
├── tests/               # Unit tests
├── docs/               # Documentation
├── examples/           # Usage examples
├── requirements.txt    # Project dependencies
└── .env               # Configuration
```

## License

MIT License