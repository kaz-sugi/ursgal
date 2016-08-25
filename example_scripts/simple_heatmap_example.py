#!/usr/bin/env python3.4
# encoding: utf-8

import ursgal
import sys


def main():
    '''
    {
        'heatmap_annotation_field_name' : 'map to uniprot',
        'heatmap_object_field_name'     : 'Protein',
        'heatmap_max_value'             : 4,
        'heatmap_min_value'             : -4,
        'heatmap_color_gradient'        : 'Spectral',
        'heatmap_box_style'             : 'classic'
    }

    '''
    uc = ursgal.UController(
        profile = 'LTQ XL low res',
        params = {
            'heatmap_max_value'  : 3,
            'heatmap_min_value'  : -3,
        }
    )
    uc.visualize(
        input_files      = sys.argv[1],
        engine           = 'plot_pygcluster',
        output_file_name = '{0}_heatmap.svg'.format(sys.argv[1]),
        multi            = False,
    )
    return


if __name__ == '__main__':
    main()
