"""A simple function that runs the entire pipeline"""

def process(filename, **kwargs):
    from gem.generator import (classify,
                               describe,
                               detect_roi,
                               draw_roi,
                               extract_bu,
                               false_positives,
                               generate_annotation,
                               generate_graphics,
                               generate_text,
                               preprocess,
                               project,
                               redraw,
                               load_model,
                               sort_contours,
                               tokenize,
                               vlog)
    # do something here :)

    return

