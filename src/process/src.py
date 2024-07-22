from src.process.utils import *


def process(src_type, file_path, m_aoi=True, bb_aoi=True):

    # Validating source type
    validate_source_type(src_type)

    # Validating file path
    validate_file_path(file_path)

    
    if src_type == "video":
        # TODO: Implement processing video logic
        pass
    elif src_type == "img":
        # Loading image
        image = read_image(file_path)

        # Labeling
        label(image, file_path, m_aoi=m_aoi, bb_aoi=bb_aoi)
