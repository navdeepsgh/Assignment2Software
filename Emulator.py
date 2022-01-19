import random

# Physics Toolbox Android Application is used to generate the sample data for all the sensors

# acceleration is in m/sec2
accelerometer_readings= [0.727, 0.813, 0.739, 0.65, 0.694, 0.907, 0.971, 0.918, 0.803, 0.699, 0.593, 0.48, 0.472, 0.535, 0.694, 0.863, 0.987, 1.093,
1.186, 1.237, 1.308, 1.304, 1.297, 1.251, 1.192, 1.11, 0.996, 0.873, 0.706, 0.52, 0.348, 0.192, 0.124, 0.18, 0.282, 0.358, 0.417,
0.466, 0.54, 0.55, 0.574, 0.545, 0.5, 0.452, 0.407, 0.311, 0.236, 0.168, 0.088, 0.051, 0.028, 0.052, 0.104, 0.139, 0.194, 0.183,
0.214, 0.204, 0.187, 0.174, 0.166, 0.163, 0.179, 0.16, 0.223, 0.986, 0.813, 0.623, 0.453, 0.357, 0.371, 0.386, 0.408, 0.432,
0.431, 0.424, 0.429, 0.489, 0.479, 0.534, 0.576, 0.672, 0.692, 0.743, 0.799, 0.797, 0.775, 0.762, 0.826, 0.849, 0.911, 0.972,
0.995, 0.984, 0.998, 0.923, 0.841, 0.781, 0.679, 0.59, 0.502, 0.508, 0.432, 0.405, 0.413, 0.34, 0.295, 0.292, 0.308, 0.3, 0.276,
0.26, 0.227, 0.259, 0.236, 0.233, 0.199, 0.161, 0.132, 0.092, 0.099, 0.118, 0.174, 0.229, 0.259, 0.287, 0.353, 0.387, 0.409, 0.405,
0.373, 0.319, 0.284, 0.251, 0.237, 0.246, 0.243, 0.303, 0.354, 0.389, 0.345, 0.324, 0.311, 0.272, 0.19, 0.159, 0.077, 0.075,
0.106, 0.142, 0.18, 0.222, 0.258, 0.276, 0.273, 0.282, 0.298, 0.32, 0.33, 0.312, 0.328, 0.342, 0.352, 0.364, 0.36, 0.337, 0.319,
0.304, 0.278, 0.226, 0.216, 0.204, 0.164, 0.153, 0.161, 0.135, 0.12]


# Gyroscope reading is in radian/sec
gyroscope_readings= [(-0.03, -0.02, -0.07), (-0.04, -0.02, -0.08), (-0.06, -0.02, -0.08), (-0.07, -0.01, -0.08), (-0.07, -0.01, -0.08),
(-0.08, -0.01, -0.08), (-0.09, 0, -0.07), (-0.09, 0, -0.07), (-0.09, 0, -0.06), (-0.09, 0, -0.06), (-0.09, -0.01, -0.06),
(-0.09, -0.01, -0.05), (-0.08, -0.02, -0.05), (-0.08, -0.02, -0.05), (-0.07, -0.03, -0.05), (-0.06, -0.04, -0.06),
(-0.05, -0.04, -0.06), (-0.04, -0.04, -0.06), (-0.03, -0.04, -0.07), (-0.02, -0.04, -0.07), (0, -0.04, -0.07),
(0.01, -0.04, -0.08), (0.02, -0.04, -0.08), (0.04, -0.04, -0.08), (0.04, -0.03, -0.08), (0.05, -0.03, -0.08),
(0.06, -0.03, -0.08), (0.07, -0.03, -0.08), (0.07, -0.02, -0.08), (0.08, -0.02, -0.09), (0.07, -0.02, -0.08),
(0.08, -0.02, -0.08), (0.08, -0.02, -0.08), (0.08, -0.02, -0.08), (0.07, -0.02, -0.08), (0.07, -0.03, -0.08),
(0.07, -0.03, -0.08), (0.06, -0.03, -0.08), (0.06, -0.03, -0.08), (0.06, -0.03, -0.07), (0.05, -0.03, -0.07),
(0.05, -0.04, -0.07), (0.04, -0.04, -0.07), (0.04, -0.04, -0.07), (0.03, -0.05, -0.07), (0.03, -0.05, -0.07),
(0.02, -0.05, -0.07), (0.01, -0.05, -0.07)]


# sample locations have latitude and longitude values in degrees.
sample_locations = [(30.84288111, 75.97805589), (30.8428579, 75.97807576), (30.84284723, 75.97807196),
                    (30.84283059, 75.9780701), (30.84281614, 75.97806375), (30.84280593, 75.97806281),
                    (30.84279129, 75.97807386), (30.8427867, 75.97808289), (30.84278557, 75.97809361),
                    (30.84277582, 75.97809658), (30.84277005, 75.97810818), (30.84276389, 75.97811707),
                    (30.84276487, 75.97812824), (30.84277389, 75.97814833), (30.84278813, 75.97817146),
                    (30.84280348, 75.97819182), (30.84281761, 75.97820795), (30.84285123, 75.97821068),
                    (30.84283042, 75.9781948), (30.84281241, 75.97817487), (30.8427985, 75.97815404),
                    (30.84278397, 75.97813549), (30.84277036, 75.97811613), (30.84275817, 75.97809744),
                    (30.84274609, 75.97807804), (30.84273187, 75.97805943), (30.84271513, 75.97803733),
                    (30.84269219, 75.97801091), (30.8426632, 75.97803234), (30.84268538, 75.97806326),
                    (30.84270465, 75.97809515), (30.84272405, 75.97812987), (30.84274683, 75.97815642),
                    (30.84276883, 75.97818224), (30.84278723, 75.97820593), (30.84280215, 75.97822778),
                    (30.84281946, 75.978209), (30.84281786, 75.97817933), (30.84281093, 75.97815305),
                    (30.84280234, 75.97813547), (30.84279568, 75.97812613), (30.84278509, 75.97812644),
                    (30.84277426, 75.97812885), (30.84278304, 75.97812101), (30.84277664, 75.97811049),
                    (30.84278374, 75.97809947), (30.84279583, 75.9780862), (30.8428107, 75.97807419),
                    (30.8428241, 75.97806183), (30.84283398, 75.9780496), (30.84284235, 75.97804232),
                    (30.84284991, 75.97803592), (30.84286421, 75.97802247), (30.84287306, 75.97801158),
                    (30.84287981, 75.97800282), (30.84288714, 75.97799662), (30.84290442, 75.97803256),
                    (30.8428982, 75.97804532), (30.84288976, 75.97805524), (30.84287758, 75.97806264),
                    (30.84286463, 75.97806835), (30.84285377, 75.97807211), (30.84283798, 75.97807532),
                    (30.84283167, 75.97808937), (30.84284022, 75.97811158), (30.84284871, 75.97811669),
                    (30.84285813, 75.97811631), (30.84287291, 75.97811611), (30.84285998, 75.9781271),
                    (30.84284795, 75.97811037), (30.84284921, 75.97809727), (30.84286148, 75.97809115),
                    (30.84287054, 75.97808434), (30.84287583, 75.97807198), (30.84288232, 75.97806411),
                    (30.84288614, 75.97804765), (30.84288547, 75.97803279), (30.84287704, 75.97803653),
                    (30.84287366, 75.97802625), (30.84287005, 75.97801055), (30.84287264, 75.97799518),
                    (30.84289436, 75.97800557), (30.84289079, 75.9780168), (30.84288837, 75.97802872),
                    (30.8429005, 75.97801634), (30.84286099, 75.97805624), (30.8428608, 75.9780381),
                    (30.84286733, 75.9780542), (30.84285505, 75.97807851), (30.84284805, 75.97811251),
                    (30.8428416, 75.97812229), (30.84283153, 75.97812773), (30.84281468, 75.97812866),
                    (30.84280339, 75.97812039), (30.84279076, 75.97812285), (30.84277703, 75.97811684),
                    (30.84277513, 75.97810578), (30.84277332, 75.97809245), (30.84277894, 75.97808082),
                    (30.84278766, 75.97806673), (30.84278379, 75.97807757), (30.84277716, 75.97808478),
                    (30.84276883, 75.97808995), (30.84275569, 75.97808623), (30.84274647, 75.9780859),
                    (30.84275194, 75.97810017), (30.84275123, 75.97811103), (30.84274546, 75.97812114),
                    (30.84274388, 75.97813692), (30.84273729, 75.97815223), (30.84275029, 75.97816019),
                    (30.84276059, 75.97816988), (30.84276715, 75.9781793), (30.84277682, 75.97818928),
                    (30.84279121, 75.97820241), (30.84282266, 75.97819559), (30.84282114, 75.97818349),
                    (30.84281145, 75.97818082), (30.84280079, 75.97817913), (30.84279031, 75.97817349),
                    (30.84277253, 75.97816699), (30.84276086, 75.97815801), (30.84274873, 75.97814882),
                    (30.84273504, 75.97813956), (30.8427267, 75.97813188), (30.84271399, 75.97812039),
                    (30.84270241, 75.97810261), (30.84269792, 75.97809328), (30.84268913, 75.97807679),
                    (30.84268395, 75.9780679), (30.84267304, 75.97805404), (30.84268131, 75.9781266),
                    (30.84269121, 75.97812938), (30.84270112, 75.97813069), (30.8427121, 75.97814193),
                    (30.84272204, 75.97815003), (30.84273282, 75.97814016), (30.84273797, 75.97812147),
                    (30.84274397, 75.97810535), (30.84274578, 75.97808851), (30.84275267, 75.97807248),
                    (30.84276458, 75.97806076)]


# return any random value from acceleration readings as the current value
def current_acceleration():
    current_reading = random.choice(accelerometer_readings)
    return current_reading


# return any random value from gyroscope readings as the current value
def current_gyroscope():
    current_reading = random.choice(gyroscope_readings)
    return current_reading

# return any location coordinates as the current location of the bicycle
def current_location():
    current_location_coordinates = random.choice(sample_locations)
    return current_location_coordinates