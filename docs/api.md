# LMSmax API Documentation

## Core Classes

### LMStudioAPI

Handles interactions with the LM Studio API.

#### Methods

- `discover_models() -> List[str]`
  Discovers available models in LM Studio.
  Returns a list of model names.

- `apply_settings(model_name: str, settings: Dict[str, str]) -> None`
  Applies provided settings to a specific model.

### HuggingFaceSettingsFetcher

Fetches optimal settings from Hugging Face for models.

#### Methods

- `fetch_settings(model_name: str) -> Dict[str, str]`
  Retrieves optimal settings for a given model from Hugging Face.
  Returns a dictionary of settings.

### Utility Functions

#### Logger Setup

- `setup_logger(name: str) -> logging.Logger`
  Creates and configures a logger with the specified name.
  Returns a configured Logger instance.

#### Configuration

- `validate_config(config: Any) -> bool`
  Validates the configuration data.
  Returns True if configuration is valid.

## Environment Variables

- `LM_STUDIO_API_URL`: URL of the LM Studio API
- `LM_STUDIO_API_KEY`: API key for LM Studio
- `HF_TOKEN`: Hugging Face API token
- `LOG_LEVEL`: Logging level (default: INFO)
- `LOG_FILE`: Log file path (default: lmsmax.log)