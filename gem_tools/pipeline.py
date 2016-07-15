"""A simple function that runs the entire pipeline"""

from __future__ import print_function

def process(filename, kernel=(11, 11), iterations=2, outfile=False, **kwargs):
    """
    Run the pipeline

    :param filename: Path to file
    :type filename: `str`

    :param kernel: size of kernel
    :type kernel: `tuple` of two `int`s

    """

    import os
    import sys

    # we probably don't need all of these?
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

    # find out our python version so we can set raw_input/input
    PYTHON_VERSION = sys.version_info.major
    INPUTFUNC = input if PYTHON_VERSION == 3 else raw_input

    # make our model: anything customisable here?
    model = load_model()

    # do preprocessing
    image, original, filename, filepath = preprocess(filename)

    # generate an output filename if none specified
    if not outfile:
        n, e = os.path.splitext(filepath)
        outfile = '%s-out%s' % (n, e)

    # don't know what these do, sorry
    contours = detect_roi(image, kernel, iterations)
    sorted_contours = sort_contours(contours)
    classified_contours, contour_types = classify(sorted_contours, image, model, outfile=outfile)

    def process_in_jupyter():
        """loop over a user input, removing false positives"""
        from IPython.display import Image
        Image(filename=outfile)
        false_positives = True
        while false_positives:
            false_positives = INPUTFUNC()
            false_positives = ''.join([i for i in false_positives if i.isnum() or i.isspace()])
            fps = [int(i) for i in false_positives.split()]
            updated_contours, updated_contour_types = redraw(image, classified_contours, contour_types, fps)
        hires_contours = project(image, original, updated_contours)
        generate_annotation(filename, original, hires_contours, updated_contour_types)


    # prefer jupyter, but also allow tkinter app
    # need to specify the error type

    try:
        process_in_jupyter()

    except:
        from gem_tools.gui import the_gui
        the_gui(filepath=outfile,
                image=image,
                classified_contours=classified_contours,
                contour_types=contour_types)

    # need to implement this!
    #if mark == 'y':
    #    
    #else:
    #    pass
        # need updated_contours ... can we return it from gui?
        hires_contours = project(image, original, updated_contours)
        generate_annotation(filename, original, hires_contours, updated_contour_types)
    
    print('\nDone!\n')

    return

# run from command line using any args passed in
if __name__ == "__main__":
    import sys
    process(*sys.argv[1:])
