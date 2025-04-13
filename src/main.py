"""
Project Title: LMSmax - LM Studio Model Settings Optimizer
Description: A tool to optimize model settings for better performance.

Optimizes settings for current models in LM Studio, 
Intent is to improve performance and usability.
Should discover models via LM Studio API, check huggingface for
settings, and then apply those settings to the models in LM Studio
based on the model name.
"""

from utils import setup_logger
from models import LMStudioAPI
from settings import HuggingFaceSettingsFetcher

# Initialize logger
logger = setup_logger("LMSmax")

# Main function
if __name__ == "__main__":
    lm_studio_api = LMStudioAPI()
    hf_fetcher = HuggingFaceSettingsFetcher()

    # Discover models
    logger.info("Discovering models in LM Studio...")
    models = lm_studio_api.discover_models()

    # Fetch and apply settings for each model
    for model in models:
        logger.info(f"Fetching settings for model: {model}")
        settings = hf_fetcher.fetch_settings(model)
        logger.info(f"Applying settings to model: {model}")
        lm_studio_api.apply_settings(model, settings)

    logger.info("Model settings optimization complete!")
