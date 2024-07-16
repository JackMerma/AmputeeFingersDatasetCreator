from src.process.filter import *
from src.process.utils import *


def process(src_type, file_path):

    # Validating source type
    validate_source_type(src_type)

    # Validating file path
    validate_file_path(file_path)

    
    if src_type == "video":
        # TODO: Implement processing video logic
        pass
    elif src_type == "img":
        image = read_image(file_path)
        show_image(image)
        filtered_image = mask(image, DEFAULT_MIN_RANGE, DEFAULT_MAX_RANGE)
        show_image(filtered_image)
