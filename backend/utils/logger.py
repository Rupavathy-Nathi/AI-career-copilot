from loguru import logger
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

logger.add(
    "logs/app.log",
    rotation="1 MB",
    retention="7 days",
    level="INFO"
)

def get_logger():
    return logger
