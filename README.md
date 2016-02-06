# Cusrse_of_Dimensionality
generating the graph for studying curse of dimensionality

Understanding the curse of dimensionality. Consider the following experiment:
generate n data points with dimensionality k. Let each data point be generated using a uniform random
number generator with values between 0 and 1. Now, for a given k, calculate
r(k) = log10(dmax(k) − dmin(k)/dmin(k))

where dmax(k) is the maximum distance between any pair of points and dmin(k) is minimum distance between
any pair of points (you cannot use identical points to obtain the minimum distance of 0). Let k take each
value from {1, 2, . . . , 99, 100}. Repeat each experiment multiple times to get stable values by averaging the
quantities over multiple runs for each k.

Plot r(k) as a function of k for three different values of n; n ∈ {100, 1000, 10000}. Label and
scale each axis properly to be able to make comparisons over different n’s. Embed your final picture(s)
in the file you are submitting for this assignment.
