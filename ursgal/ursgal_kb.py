#!/usr/bin/env python3

CAM_MOD            = 57.0214637206
DIFFERENCE_14N_15N = 0.997035
PROTON             = 1.00727646677

NITROGENS = {
    'A' : 1,
    'C' : 1,
    'D' : 1,
    'E' : 1,
    'F' : 1,
    'G' : 1,
    'H' : 3,
    'I' : 1,
    'K' : 2,
    'L' : 1,
    'M' : 1,
    'N' : 2,
    'P' : 1,
    'Q' : 2,
    'R' : 4,
    'S' : 1,
    'T' : 1,
    'V' : 1,
    'W' : 2,
    'Y' : 1,
}

# mass of all amino acid difference between 15N and 14N
DICT_15N_DIFF = {
    'A' : 0.997035,
    'C' : 0.997035,
    'D' : 0.997035,
    'E' : 0.997035,
    'F' : 0.997035,
    'G' : 0.997035,
    'H' : 2.99110,
    'I' : 0.997035,
    'K' : 1.99407,
    'L' : 0.997035,
    'M' : 0.997035,
    'N' : 1.99407,
    'P' : 0.997035,
    'Q' : 1.99407,
    'R' : 3.98814,
    'S' : 0.997035,
    'T' : 0.997035,
    'V' : 0.997035,
    'W' : 1.99407,
    'Y' : 0.997035
}