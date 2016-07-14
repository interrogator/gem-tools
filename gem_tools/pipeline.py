"""A simple function that runs the entire pipeline"""

def process(filename, kernel=(11, 11), iterations=2, outfile=False, **kwargs):
    """
    Run the pipeline

    :param filename: Path to file
    :type filename: `str`

    """

    from gem_tools.generator import (classify,
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

    from gem_tools.gui import the_gui

    import os
    import sys

    PYTHON_VERSION = sys.version_info.major
    INPUTFUNC = input if PYTHON_VERSION == 3 else raw_input

    model = load_model()

    preprocessed_image, input_image, filename, filepath = preprocess(filename)

    contours = detect_roi(image, kernel, iterations)

    sorted_contours = sort_contours(contours)

    classified_contours, contour_types = classify(sorted_contours, image, model)

    if not outfile:
        f, ext = os.path.splitext(filename)
        outfile = '%s-out.%s' % (f, ext)

    # got to pop this up in a PIL window, simple gui or something
    the_gui(filename=outfile)
    #Image(filename=outfile)
    
    false_positives = false_positives(INPUTFUNC())

    updated_contours, updated_contour_types = redraw(image, classified_contours, contour_types, false_positives)

    f, ext = os.path.splitext(outfile)
    updated_out = '%s-updated.%s' % (f, ext)
    
    the_gui(filename=updated_out)
    #Image(filename=updated_out)

    mark = INPUTFUNC()

    if mark == 'y':
        updated_contours, updated_contour_types = draw_roi(image, updated_contours, updated_contour_types)
    else:
        pass

    hires_contours = project(image, original, updated_contours)

    generate_annotation(filename, original, hires_contours, updated_contour_types)

    return

# run from command line using any args passed in
if __name__ == "__main__":
    import sys
    return process(*sys.argv[1:])
