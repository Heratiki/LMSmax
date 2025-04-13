"""
Basic example of using LMSmax to optimize a single model's settings.
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models import LMStudioAPI
from src.settings import HuggingFaceSettingsFetcher
from src.utils import setup_logger

def optimize_single_model(model_name: str):
    """Optimize settings for a single model."""
    logger = setup_logger("example")
    
    # Initialize APIs
    lm_studio = LMStudioAPI()
    hf_fetcher = HuggingFaceSettingsFetcher()
    
    # Fetch and apply settings
    logger.info(f"Fetching settings for model: {model_name}")
    settings = hf_fetcher.fetch_settings(model_name)
    
    logger.info(f"Applying settings to model: {model_name}")
    lm_studio.apply_settings(model_name, settings)
    
    logger.info("Settings optimization complete!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python basic_usage.py <model_name>")
        sys.exit(1)
        
    optimize_single_model(sys.argv[1])