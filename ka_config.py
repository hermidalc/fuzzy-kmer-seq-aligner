# Karlin-Altschul parameters
# from ncbi-blast-2.9.0+-src/c++/src/algo/blast/core/blast_stat.c
KA_PARAMS = {
    # Nucleotide parameters for (match, mismatch) substitution scores and
    # (gap opening cost, gap extension cost):
    # [Lambda, K, H, Alpha, Beta, Theta]
    'na': {
        (1, -5): {
            (0, 0):  [1.39, 0.747, 1.38, 1.00, 0, 100],
            (3, 3):  [1.39, 0.747, 1.38, 1.00, 0, 100],
        },
        (1, -4): {
            (0, 0):  [1.383, 0.738, 1.360, 1.020,   0, 100],
            (1, 2):  [1.360, 0.670, 1.200, 1.100,   0,  98],
            (0, 2):  [1.260, 0.430, 0.900, 1.400,  -1,  91],
            (2, 1):  [1.350, 0.610, 1.100, 1.200,  -1,  98],
            (1, 1):  [1.220, 0.350, 0.720, 1.700,  -3,  88],
        },
        (2, -7): {
            (0, 0):  [0.690, 0.730, 1.340, 0.515,   0, 100],
            (2, 4):  [0.680, 0.670, 1.200, 0.550,   0,  99],
            (0, 4):  [0.630, 0.430, 0.900, 0.700,  -1,  91],
            (4, 2):  [0.675, 0.620, 1.100, 0.600,  -1,  98],
            (2, 2):  [0.610, 0.350, 0.720, 1.700,  -3,  88],
        },
        (1, -3): {
            (0, 0):  [1.374, 0.711, 1.310, 1.050,   0, 100],
            (2, 2):  [1.370, 0.700, 1.200, 1.100,   0,  99],
            (1, 2):  [1.350, 0.640, 1.100, 1.200,  -1,  98],
            (0, 2):  [1.250, 0.420, 0.830, 1.500,  -2,  91],
            (2, 1):  [1.340, 0.600, 1.100, 1.200,  -1,  97],
            (1, 1):  [1.210, 0.340, 0.710, 1.700,  -2,  88],
        },
        (2, -5): {
            (0, 0):  [0.675, 0.650, 1.100, 0.600,  -1,  99],
            (2, 4):  [0.670, 0.590, 1.100, 0.600,  -1,  98],
            (0, 4):  [0.620, 0.390, 0.780, 0.800,  -2,  91],
            (4, 2):  [0.670, 0.610, 1.000, 0.650,  -2,  98],
            (2, 2):  [0.560, 0.320, 0.590, 0.950,  -4,  82],
        },
        (1, -2): {
            (0, 0):  [1.280, 0.460, 0.850, 1.500,  -2,  96],
            (2, 2):  [1.330, 0.620, 1.100, 1.200,   0,  99],
            (1, 2):  [1.300, 0.520, 0.930, 1.400,  -2,  97],
            (0, 2):  [1.190, 0.340, 0.660, 1.800,  -3,  89],
            (3, 1):  [1.320, 0.570, 1.000, 1.300,  -1,  99],
            (2, 1):  [1.290, 0.490, 0.920, 1.400,  -1,  96],
            (1, 1):  [1.140, 0.260, 0.520, 2.200,  -5,  85],
        },
        (2, -3): {
            (0, 0):  [0.550, 0.210, 0.460, 1.200,  -5,  87],
            (4, 4):  [0.630, 0.420, 0.840, 0.750,  -2,  99],
            (2, 4):  [0.615, 0.370, 0.720, 0.850,  -3,  97],
            (0, 4):  [0.550, 0.210, 0.460, 1.200,  -5,  87],
            (3, 3):  [0.615, 0.370, 0.680, 0.900,  -3,  97],
            (6, 2):  [0.630, 0.420, 0.840, 0.750,  -2,  99],
            (5, 2):  [0.625, 0.410, 0.780, 0.800,  -2,  99],
            (4, 2):  [0.610, 0.350, 0.680, 0.900,  -3,  96],
            (2, 2):  [0.515, 0.140, 0.330, 1.550,  -9,  81],
        },
        (3, -4): {
            (6, 3):  [0.389, 0.250, 0.560, 0.700,  -5,  95],
            (5, 3):  [0.375, 0.210, 0.470, 0.800,  -6,  92],
            (4, 3):  [0.351, 0.140, 0.350, 1.000,  -9,  86],
            (6, 2):  [0.362, 0.160, 0.450, 0.800,  -4,  88],
            (5, 2):  [0.330, 0.092, 0.280, 1.200, -13,  81],
            (4, 2):  [0.281, 0.046, 0.160, 1.800, -23,  69],
        },
        (4, -5): {
            (0, 0):  [0.220, 0.061, 0.220, 1.000, -15,  74],
            (6, 5):  [0.280, 0.210, 0.470, 0.600,  -7,  93],
            (5, 5):  [0.270, 0.170, 0.390, 0.700,  -9,  90],
            (4, 5):  [0.250, 0.100, 0.310, 0.800, -10,  83],
            (3, 5):  [0.230, 0.065, 0.250, 0.900, -11,  76],
        },
        (1, -1): {
            (3, 2):  [1.090, 0.310, 0.550, 2.000,  -2,  99],
            (2, 2):  [1.070, 0.270, 0.490, 2.200,  -3,  97],
            (1, 2):  [1.020, 0.210, 0.360, 2.800,  -6,  92],
            (0, 2):  [0.800, 0.064, 0.170, 4.800, -16,  72],
            (4, 1):  [1.080, 0.280, 0.540, 2.000,  -2,  98],
            (3, 1):  [1.060, 0.250, 0.460, 2.300,  -4,  96],
            (2, 1):  [0.990, 0.170, 0.300, 3.300, -10,  90],
        },
        (3, -2): {
            (5, 5):  [0.208, 0.030, 0.072, 2.900, -47,  77],
        },
        (5, -4): {
            (10, 6): [0.163, 0.068, 0.160, 1.000, -19,  85],
            ( 8, 6): [0.146, 0.039, 0.101, 1.300, -29,  76],
        },
    },
    # Amino acid parameters for substitution matrix and
    # (gap opening cost, gap extension cost):
    # [Lambda, K, H, Alpha, Beta, C, Alpha_V, Sigma]
    'aa': {
        'blosum62': {
            (11, 2): [0.297, 0.082, 0.270, 1.1, -10, 0.641766,  12.673800,  12.757600],
            (10, 2): [0.291, 0.075, 0.230, 1.3, -15, 0.649362,  16.474000,  16.602600],
            ( 9, 2): [0.279, 0.058, 0.190, 1.5, -19, 0.659245,  22.751900,  22.950000],
            ( 8, 2): [0.264, 0.045, 0.150, 1.8, -26, 0.672692,  35.483800,  35.821300],
            ( 7, 2): [0.239, 0.027, 0.100, 2.5, -46, 0.702056,  61.238300,  61.886000],
            ( 6, 2): [0.201, 0.012, 0.061, 3.3, -58, 0.740802, 140.417000, 141.882000],
            (13, 1): [0.292, 0.071, 0.230, 1.2, -11, 0.647715,  19.506300,  19.893100],
            (12, 1): [0.283, 0.059, 0.190, 1.5, -19, 0.656391,  27.856200,  28.469900],
            (11, 1): [0.267, 0.041, 0.140, 1.9, -30, 0.669720,  42.602800,  43.636200],
            (10, 1): [0.243, 0.024, 0.100, 2.5, -44, 0.693267,  83.178700,  85.065600],
            ( 9, 1): [0.206, 0.010, 0.052, 4.0, -87, 0.731887, 210.333000, 214.842000],
        },
        'pam250': {
            (15, 3): [0.205, 0.049, 0.130, 1.6, -23, 0.687656,  34.578400,  34.928000],
            (14, 3): [0.200, 0.043, 0.120, 1.7, -26, 0.689768,  43.353000,  43.443800],
            (13, 3): [0.194, 0.036, 0.100, 1.9, -31, 0.697431,  50.948500,  51.081700],
            (12, 3): [0.186, 0.029, 0.085, 2.2, -41, 0.704565,  69.606500,  69.793600],
            (11, 3): [0.174, 0.020, 0.070, 2.5, -48, 0.722438,  98.653500,  98.927100],
            (17, 2): [0.204, 0.047, 0.120, 1.7, -28, 0.684799,  41.583800,  41.735800],
            (16, 2): [0.198, 0.038, 0.110, 1.8, -29, 0.691098,  51.635200,  51.843900],
            (15, 2): [0.191, 0.031, 0.087, 2.2, -44, 0.699051,  67.256700,  67.558500],
            (14, 2): [0.182, 0.024, 0.073, 2.5, -53, 0.714103,  96.315100,  96.756800],
            (13, 2): [0.171, 0.017, 0.059, 2.9, -64, 0.728738, 135.653000, 136.339000],
            (21, 1): [0.205, 0.045, 0.110, 1.8, -34, 0.683265,  48.728200,  49.218800],
            (20, 1): [0.199, 0.037, 0.100, 1.9, -35, 0.689380,  60.832000,  61.514100],
            (19, 1): [0.192, 0.029, 0.083, 2.3, -52, 0.696344,  84.019700,  84.985600],
            (18, 1): [0.183, 0.021, 0.070, 2.6, -60, 0.710525, 113.829000, 115.184000],
            (17, 1): [0.171, 0.014, 0.052, 3.3, -86, 0.727000, 175.071000, 177.196000],
        },
    }
}

KA_NA_ROUND_DOWN = [(2, -7), (2, -5), (2, -3), (3, -4)]