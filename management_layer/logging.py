import logging

# Set up logging before other imports
logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname} {name}:{lineno} {message}",
    datefmt="%Y-%m-%dT%H:%M:%S", style="{"
)
