"""
Results for Kim-Nelson (1989) model testing

Author: Valery Likhosherstov
License: Simplified-BSD

References
----------

Datasets produced using GAUSS code described in Kim and Nelson (1989) and found
at http://econ.korea.ac.kr/~cjkim/MARKOV/programs/tvp.opt
Accessed 2016-07-15
Code was run using OxGauss 6.

Kim, Chang-Jin, and Charles R. Nelson. 1999.
"State-Space Models with Regime Switching:
Classical and Gibbs-Sampling Approaches with Applications".
MIT Press Books. The MIT Press.
"""

"""
Kim and Nelson's (1989) time-varying-parameter model for modelling changing
conditional variance of uncertainty in the U.S. monetary growth.

See http://econ.korea.ac.kr/~cjkim/MARKOV/prgmlist.htm#chapter4

Gauss Code: TVP.OPT
Dataset: TVP.PRN
"""
tvp = {
    'data': {
        'm1': [
            0.751356, -0.869262, -0.259896, -0.165737, 0.943401, -0.046962,
            0.538708, 0.767892, 0.600882, 0.940261, 0.637094, 0.700645,
            -0.112678, 0.56212, 1.02611, 0.949756, 1.00614, 0.953003, 0.687438,
            0.704003, 1.62365, 1.28846, 0.740592, 0.592627, 1.15468, 1.81623,
            1.70609, 1.06374, -0.28899, 0.269746, 1.01466, 1.39968, 2.19217,
            1.58603, 1.34737, 1.69855, 1.92865, 2.11143, 1.78681, 0.807717,
            0.425952, 0.765415, 1.04899, 0.735771, 1.34549, 1.77658, 1.7152,
            2.10344, 1.70995, 0.945527, 1.93568, 1.63384, 2.04653, 2.46058,
            1.9965, 1.17128, 1.18329, 1.24525, 1.66556, 0.890214, 0.894558,
            1.20052, 0.70867, 1.54397, 1.83342, 0.806734, 1.33404, 1.62897,
            1.06408, 1.94351, 2.29821, 1.71822, 1.6892, 2.09215, 1.9218, 2.1932,
            2.02392, 1.77144, 1.2216, 1.82728, 3.40151, 1.12003, 1.0822,
            -1.49428, 4.78721, 2.67028, 0.430245, 1.64798, 1.65203, 1.23086,
            1.80714, 0.417009, 2.13212, 3.9369, 2.53423, 2.79038, 2.73398,
            1.61283, 1.53723, 1.58167, 1.07116, 1.05981, 2.66302, 2.57107,
            3.49415, 2.67452
        ],
        'dint': [
            0.226667, 0.54, 0.69, -0.356667, -0.88, -0.633333, -0.053333,
            0.043333, -0.046667, 0.0, 0.156667, 0.263333, -0.01, 0.126667,
            -0.026667, 0.093333, 0.03, 0.356667, 0.203333, 0.033333, -0.053333,
            0.02, 0.186667, 0.206667, -0.016667, -0.006667, 0.3, 0.443333,
            -0.023333, 0.456667, 0.166667, -0.696667, -0.853333, 0.64, 0.453333,
            0.296667, 0.47, -0.323333, 0.39, 0.506667, 0.103333, 0.826667, 0.33,
            -0.143333, -0.533333, -0.346667, -0.976667, -1.51333, 0.41, 0.76,
            -0.78, -0.793333, 0.333333, 0.45, 0.643333, 0.836667, 0.903333,
            1.72, -0.823333, 0.116667, 0.536667, 0.036667, -0.83, -1.61,
            -0.356667, 0.936667, -0.703333, -0.71, 0.24, -0.006667, -0.476667,
            -0.043333, 0.21, 0.656667, 0.613333, 0.283333, 0.083333, 0.836667,
            1.25667, 0.813333, -0.006667, 0.296667, 2.17, 1.51, -3.73667,
            -0.463333, 4.46, 0.776667, 0.516667, 0.146666, -3.30333, 1.06333,
            -0.393333, -3.10333, -1.41, 0.2, 0.29, 0.743333, -0.34, 0.37,
            0.626667, 0.523333, -1.51667, -0.62, -0.723333, -0.353333
        ],
        'inf': [
            0.191755, 0.496848, 0.608136, 0.113615, 0.603775, 0.037615,
            0.637303, 0.223964, -0.037292, 0.409455, 0.111379, 0.407333,
            0.368868, 0.257401, 0.256739, 0.329128, 0.182382, 0.581397,
            0.289436, 0.432589, 0.143781, 0.179437, 0.500716, 0.32057, 0.638074,
            0.282287, 0.527149, 0.941922, 0.898727, 0.856609, 0.815499,
            0.337838, 0.538179, 1.03455, 0.958213, 1.07932, 0.971196, 1.28042,
            1.23283, 1.21781, 1.50934, 1.45678, 1.43586, 1.62031, 1.39294,
            1.11765, 1.38675, 0.839635, 0.943139, 1.01636, 0.653775, 0.892018,
            0.590286, 0.878951, 1.00265, 1.51123, 2.02234, 2.03193, 2.45291,
            2.93682, 2.60117, 2.86993, 3.04949, 2.05311, 1.22029, 1.98764,
            1.84833, 1.14058, 0.832182, 1.54678, 1.42749, 1.84084, 1.77061,
            1.37604, 1.44721, 1.69179, 2.28691, 2.26953, 2.31812, 2.4588,
            3.19749, 3.14371, 3.12107, 3.86071, 3.32302, 1.83516, 2.79517,
            2.69385, 2.06684, 2.75129, 1.61516, 0.897925, 1.40156, 1.73617,
            0.318655, 0.102209, 1.15112, 0.993698, 0.950915, 1.2902, 0.994496,
            0.888801, 0.817542, 0.821403, 1.11593, 0.579113
        ],
        'surpl': [
            0.103, 0.044, 0.058, 0.188, 0.126, 0.087, 0.096, -0.004, -0.043,
            -0.034, -0.059, -0.201, -0.169, -0.145, -0.122, -0.07, 0.029,
            -0.045, -0.076, -0.225, -0.337, -0.22, -0.151, -0.051, -0.105,
            -0.348, -0.441, -0.397, -0.352, -0.492, -0.547, -0.715, -0.707,
            -0.749, -0.709, -0.641, -0.763, -0.52, -0.389, -0.147, -0.096,
            -0.184, -0.136, -0.124, -0.331, -0.38, -0.369, -0.421, -0.474,
            -0.444, -0.354, -0.213, -0.448, -0.242, -0.614, -0.421, -0.393,
            -0.234, -0.238, -0.21, -0.253, -0.062, -0.199, -0.328, -1.242,
            -0.643, -0.68, -0.567, -0.469, -0.528, -0.561, -0.331, -0.441,
            -0.682, -0.601, -0.572, -0.44, -0.429, -0.417, -0.223, -0.123,
            -0.306, -0.335, -0.435, -0.454, -0.458, -0.398, -0.226, -0.169,
            -0.274, -0.44, -0.351, -0.311, -0.63, -0.917, -0.838, -0.803,
            -0.966, -1.0, -1.044, -1.21, -1.295, -1.419, -1.217, -1.675, -1.619
        ],
        'm1lag': [
            0.828304, 0.751356, -0.869262, -0.259896, -0.165737, 0.943401,
            -0.046962, 0.538708, 0.767892, 0.600882, 0.940261, 0.637094,
            0.700645, -0.112678, 0.56212, 1.02611, 0.949756, 1.00614, 0.953003,
            0.687438, 0.704003, 1.62365, 1.28846, 0.740592, 0.592627, 1.15468,
            1.81623, 1.70609, 1.06374, -0.28899, 0.269746, 1.01466, 1.39968,
            2.19217, 1.58603, 1.34737, 1.69855, 1.92865, 2.11143, 1.78681,
            0.807717, 0.425952, 0.765415, 1.04899, 0.735771, 1.34549, 1.77658,
            1.7152, 2.10344, 1.70995, 0.945527, 1.93568, 1.63384, 2.04653,
            2.46058, 1.9965, 1.17128, 1.18329, 1.24525, 1.66556, 0.890214,
            0.894558, 1.20052, 0.70867, 1.54397, 1.83342, 0.806734, 1.33404,
            1.62897, 1.06408, 1.94351, 2.29821, 1.71822, 1.6892, 2.09215,
            1.9218, 2.1932, 2.02392, 1.77144, 1.2216, 1.82728, 3.40151,
            1.12003, 1.0822, -1.49428, 4.78721, 2.67028, 0.430245, 1.64798,
            1.65203, 1.23086, 1.80714, 0.417009, 2.13212, 3.9369, 2.53423,
            2.79038, 2.73398, 1.61283, 1.53723, 1.58167, 1.07116, 1.05981,
            2.66302, 2.57107, 3.49415
        ]
    },
    'start' : 10,
    'untransformed_start_parameters': [
        0.5, 0.1, 0.1, 0.1, 0.1, 0.1
    ],
    'parameters': [
        0.371245817 * 0.371245817, 0.111236539 * 0.111236539,
        0.017119149 * 0.017119149, 0.272032325 * 0.272032325,
        0.037753247 * 0.037753247, 0.022415721 * 0.022415721
    ],
    'loglike': -97.0924,
    'f_cast': [
        0.055, -0.4941, -1.0564, 0.1769, 0.5331, 0.402, 0.3915, 0.0727, -0.1214,
        -0.199, 0.9478, 0.1647, -0.2886, -0.1428, 0.3868, 0.5192, 0.0805,
        -0.519, -1.6316, -0.0112, 0.4008, -0.67, 0.6585, 0.3274, -0.0534,
        0.4985, 0.214, 0.3807, 0.1551, -0.4986, -0.3752, 0.4447, 0.2581,
        -0.4287, 0.1101, 0.2722, -0.2052, 0.0287, 0.0085, -0.5129, 0.4696,
        -0.0212, 0.4474, 0.9845, -0.6296, -0.5882, 0.4222, 0.573, -0.1197,
        -0.5277, 0.0704, 0.4851, -0.8572, 0.0763, -0.8895, -0.1087, 0.1632,
        -0.0449, -0.4548, 1.0565, 0.3059, -0.2779, -0.0058, 0.3485, -0.0644,
        0.1793, -0.221, -0.0257, -0.3794, 0.6681, 1.2958, -2.4384, 0.4145,
        -2.8845, 4.2997, 0.7437, 0.236, -0.5419, -0.0644, -0.7855, -1.5748,
        -0.2646, 1.2507, 0.89, 0.005, 1.1121, 0.3698, -0.9335, -1.0237, -0.0204,
        -0.6478, -0.4655, 0.3819, 0.588, 0.9706, -0.2644
    ],
    'ss': [
        0.2207, 0.4035, 0.2429, 0.2798, 0.1977, 0.2496, 0.2338, 0.3613, 0.1983,
        0.2847, 0.3201, 0.237, 0.2834, 0.2228, 0.3205, 0.2466, 0.3165, 0.4372,
        0.3185, 0.4137, 0.2802, 0.3901, 0.2887, 0.5511, 0.3016, 0.3416, 0.2973,
        0.5015, 0.3788, 0.3834, 0.5081, 0.4314, 0.3949, 0.4841, 0.3921, 0.3231,
        0.4366, 0.3119, 0.3903, 0.3427, 0.2764, 0.3293, 0.2643, 0.3208, 0.3715,
        0.5973, 0.7453, 0.5919, 0.9341, 0.9719, 0.7644, 0.9097, 0.9983, 0.5757,
        0.5798, 0.7473, 0.5392, 0.3377, 0.3056, 0.5499, 0.4121, 0.5837, 0.4882,
        0.3801, 0.405, 0.494, 0.765, 0.6547, 0.6724, 0.7401, 1.16, 1.0853,
        1.1974, 1.4793, 1.7189, 1.1194, 1.5127, 0.9117, 0.5642, 0.9264, 0.5458,
        0.3991, 0.446, 0.6515, 0.4408, 0.2726, 0.5304, 0.3199, 0.3114, 0.4131,
        0.3016, 0.2919, 0.3085, 0.3038, 0.3944, 0.291
    ],
    'beta_tl': [
        [0.4965, -0.658, 0.5813, -3.2549, -0.0724],
        [0.5126, -0.6555, 0.5719, -3.3179, -0.0709],
        [0.4389, -0.5831, 0.4181, -2.1186, -0.0189],
        [0.3019, -0.3959, 0.1196, -0.7239, 0.0207],
        [0.3727, -0.4049, 0.058, -0.9298, -0.0335],
        [0.4829, -0.439, 0.161, -1.0697, -0.0215],
        [0.5108, -0.3993, 0.4471, -0.6918, 0.0572],
        [0.6079, -0.3483, 0.4996, -0.187, 0.0972],
        [0.6023, -0.341, 0.5741, -0.1433, 0.1038],
        [0.5729, -0.3442, 0.5667, -0.122, 0.1003],
        [0.5521, -0.3105, 0.4848, 0.1181, 0.1097],
        [0.7521, -0.4232, 0.0775, -1.1218, 0.0736],
        [0.7626, -0.4281, 0.0718, -1.1584, 0.1052],
        [0.757, -0.4325, -0.1868, -1.2219, 0.0883],
        [0.7035, -0.4465, -0.2159, -1.3017, 0.098],
        [0.7138, -0.4792, 0.1306, -1.2976, 0.0794],
        [0.7741, -0.5153, 0.1357, -1.7173, 0.0976],
        [0.7618, -0.5138, 0.1794, -1.7576, 0.1067],
        [0.8309, -0.5206, -0.2358, -1.7412, 0.0927],
        [0.7468, -0.3393, -1.2197, -1.5994, 0.1837],
        [0.7451, -0.3401, -1.223, -1.5955, 0.1856],
        [0.7666, -0.3655, -1.0822, -1.7327, 0.1726],
        [0.7155, -0.2192, -0.944, -1.2904, 0.1621],
        [0.6831, -0.3288, -0.7068, -1.4245, 0.2053],
        [0.6554, -0.2914, -0.5176, -1.4186, 0.2319],
        [0.6518, -0.2933, -0.5437, -1.4185, 0.2322],
        [0.6797, -0.31, -0.2444, -1.3599, 0.224],
        [0.6891, -0.3016, -0.1704, -1.3899, 0.2279],
        [0.6832, -0.3461, 0.0626, -1.2895, 0.2391],
        [0.704, -0.3385, 0.1256, -1.2539, 0.2443],
        [0.605, -0.3543, -0.0651, -1.4003, 0.2434],
        [0.5992, -0.3375, -0.2575, -1.424, 0.2665],
        [0.6359, -0.3069, -0.0895, -1.4528, 0.2445],
        [0.6479, -0.3149, 0.0208, -1.4431, 0.2468],
        [0.6738, -0.2881, -0.1767, -1.4472, 0.2379],
        [0.679, -0.2942, -0.1342, -1.4632, 0.2359],
        [0.7273, -0.2934, -0.0569, -1.4789, 0.2475],
        [0.7441, -0.2804, -0.1501, -1.4776, 0.2392],
        [0.7523, -0.2836, -0.1486, -1.4775, 0.2402],
        [0.7538, -0.2824, -0.146, -1.4781, 0.2406],
        [0.6948, -0.3274, -0.3619, -1.4639, 0.2477],
        [0.8999, -0.363, -0.305, -1.4275, 0.2248],
        [0.8989, -0.3619, -0.3151, -1.4319, 0.2236],
        [1.0628, -0.3234, -0.311, -1.4815, 0.2314],
        [1.0959, -0.2846, 0.2317, -1.3609, 0.2623],
        [1.2113, -0.2943, -0.1348, -1.1898, 0.249],
        [1.3005, -0.2927, -0.5252, -1.1919, 0.2722],
        [1.2629, -0.2966, -0.3244, -1.1993, 0.2518],
        [1.2894, -0.2782, -0.1285, -1.1538, 0.2469],
        [1.2988, -0.2701, -0.1707, -1.1522, 0.2462],
        [1.3264, -0.2744, -0.331, -1.1545, 0.2403],
        [1.3314, -0.2734, -0.3105, -1.1558, 0.2387],
        [1.3363, -0.2779, -0.1683, -1.132, 0.239],
        [1.3662, -0.2609, -0.411, -1.0999, 0.2321],
        [1.3796, -0.2636, -0.3915, -1.1038, 0.2307],
        [1.3209, -0.277, -0.5148, -0.7347, 0.2208],
        [1.3205, -0.2821, -0.5581, -0.7462, 0.2182],
        [1.3302, -0.288, -0.4981, -0.7492, 0.2119],
        [1.3132, -0.2871, -0.5063, -0.7533, 0.2103],
        [1.1144, -0.3065, -0.5572, -0.8137, 0.1905],
        [1.0196, -0.3003, 0.0227, -0.84, 0.1677],
        [1.0078, -0.3079, 0.1474, -0.8392, 0.1853],
        [1.0269, -0.3099, 0.0285, -0.858, 0.1771],
        [1.0267, -0.31, 0.0262, -0.8578, 0.1772],
        [1.0764, -0.2997, 0.1328, -0.8925, 0.1745],
        [1.0736, -0.3001, 0.1081, -0.8929, 0.1726],
        [1.0678, -0.3024, 0.1891, -0.8931, 0.1719],
        [1.0911, -0.3, 0.0994, -0.8979, 0.1711],
        [1.0908, -0.3005, 0.0906, -0.8981, 0.1713],
        [1.0801, -0.3069, -0.0355, -0.8981, 0.1765],
        [1.1085, -0.3117, 0.185, -0.8749, 0.162],
        [0.9984, -0.3376, 0.5659, -0.8696, 0.1808],
        [1.1165, -0.3357, -0.0249, -0.835, 0.0692],
        [1.1387, -0.3214, 0.0824, -0.8444, 0.0475],
        [1.2924, -0.2922, -0.6439, -0.7666, 0.0701],
        [1.5698, -0.5257, 0.1098, -0.8641, -0.1011],
        [1.6453, -0.5272, 0.2241, -0.8317, -0.0215],
        [1.6441, -0.5139, 0.2853, -0.831, -0.0269],
        [1.5947, -0.5017, 0.126, -0.8471, -0.0137],
        [1.5838, -0.5013, 0.108, -0.8505, -0.0145],
        [1.6726, -0.4944, -0.1613, -0.8227, -0.0206],
        [1.2829, -0.4045, -0.4496, -0.763, -0.0195],
        [1.1279, -0.4203, -0.4611, -0.7772, -0.0174],
        [1.2281, -0.4152, 0.1011, -0.7625, -0.0589],
        [1.0691, -0.4452, 0.4701, -0.839, -0.0221],
        [1.0707, -0.4453, 0.4689, -0.8399, -0.0217],
        [1.6109, -0.4191, 0.2096, -0.9584, -0.0488],
        [1.6012, -0.4095, 0.4301, -0.9771, -0.0446],
        [1.5902, -0.4308, 0.035, -0.8648, -0.0457],
        [1.4448, -0.4179, -0.3688, -0.7584, -0.0026],
        [1.445, -0.418, -0.3791, -0.7575, -0.0023],
        [1.406, -0.4274, -0.5805, -0.6579, 0.0065],
        [1.3527, -0.4308, -0.7075, -0.5849, 0.0222],
        [1.3832, -0.4496, -0.6074, -0.6392, 0.0158],
        [1.4081, -0.4536, -0.3465, -0.611, 0.0586],
        [1.2291, -0.4531, 0.1552, -0.7252, 0.0818]
    ]
}
