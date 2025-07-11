import logging

# Configure basic logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO  # Change to DEBUG for more verbosity
)

logger = logging.getLogger(__name__)
