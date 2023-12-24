# Exoplanet Detection Algorithm

## Overview
Exoplanets are planets that are not part of the Solar System. They orbit distant stars light-years away. Scientists show great interest in exoplanets as they can provide crucial information about solar systems, planet masses and radii, and extraterrestrial life. They could harbor life, or be a viable place for humans to live in the future. 

One particular telescope that has set out to observe these exoplanets is the Kepler Space Telescope from NASA. Its mission is to survey as many stars as possible in pursuit of exoplanets. The data obtained from Kepler is in the form of lightcurves. These lightcurves are graphs showing the quantity of light from a star that reaches Kepler over time. This data is primarily tailored to the transit method of exoplanet detection. When exoplanets travel between stars and Earth in their orbit, they block some of the star's light, causing a dip in the amount of light that reaches Earth. Seeing a significant pattern of such dips indicates the star might have an exoplanet, hence, the transit method. 

Astrophysics and the objects in space have always intrigued me. In this project, I aim to use machine learning algorithms, with Kepler data as input to detect exoplanets. I used [https://github.com/google-research/exoplanet-ml/](https://github.com/google-research/exoplanet-ml/) as a source for my code.

## Objectives
The objective of my project is to develop a machine learning-based program where a Kepler ID (Kepler's identification of observed stars) is provided as an input, and returns the probability of the star containing an exoplanet as output.

## Methodology
I used a development environment called Conda, which allows easy switching between different versions of TensorFlow. To train the model, data was sourced from the [Kepler DR24](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=q1_q17_dr24_tce) dataset. The neural network that classifies exoplanets uses the TensorFlow framework. Tests were performed on the model, which showed it had a 92.3% accuracy at detecting exoplanets. 

When predicting whether a star has an exoplanet or not, it uses a Threshold Crossing Event (TCE) as input. A TCE is a repeating series of dips found in star lightcurves that is considered significant, and not noise. TCEs are found in the DR24 dataset. They are composed of a KIC (Kepler ID), period, duration, and t0; the period is the duration of the orbit, the duration is the duration of the transit, and t0 is the time in which the dip is first seen by Kepler. The NASA Exoplanet Archive's API was used to find all TCEs for any given KIC, and provides it as input for the machine learning algorithm. Following that, the output of the program was organized so as to show the final results.
In the implemented program, there is a function that uses the NASA Archive's API to retrieve the TCEs of a particular star. The duration and t0 are adjusted to match the neural network's expected input. If multiple TCEs exist for a given star, all those are looped.

## Observation points

In this project, 10 known exoplanets and 5 known non-exoplanets are provided as input, and the output of the program is validated against the expected values.

## Challenges faced and their Resolutions
There were several challenges encountered during this project. One roadblock was function deprecation between Tensorflow 1 and Tensorflow 2. When this major update of Tensorflow occurred, several functions were deprecated, rendering large amounts of the code dysfunctional. In addition, pip3 did not support installing TensorFlow v1. The resolution was using Conda as the development environment, followed by downloading TensorFlow v1. 

Another challenge was KICs that were not present in the lightcurve archive. Several KICs in the DR24 database did not exist in the lightcurve archive. This was resolved when all KICs fewer than 8 digits long were excluded. 

A third issue was when the t0 value was abnormally high, which returned an error as Kepler had not performed any observations of that star at that time. The t0 marks the time relative to the start of Kepler's mission, instead of the beginning of the lightcurve. The resolution to this was passing t0 % period as input to the neural network, as this set the time to the start of Kepler's observation. A final problem was long, messy output. The resolution was switching from os.popen to os.system, and adding a function at the end of each command to reroute all the output to NULL.

## Lessons Learned
- Check the deprecation date of libraries, and avoid using libraries which be deprecated soon.
- Use AI programming tools to accelerate and simplify programming tasks.
- APIs are much more efficient methods of retrieving information than web-scraping.
- Set clear scopes of the project, and critically think about the skill and knowledge level of people that will be performing any given research. 

## Findings
The output of the program successfully identified 10 exoplanets and 5 non-exoplanets using the Kepler ID. 

## Conclusion
This machine-learning based Python project can be used to detect exoplanets using Kepler ID. Machine learning is crucial due to the sheer volume of telescope data in the astrophysics field; the billions of surveyed stars are far too much for human analytical analysis. This necessitates machine learning to analyze these datasets. This project allows amateur astrophysicists and citizen scientists to hunt for exoplanets and explore the universe beyond our Earth. With this, we can potentially find extraterrestrial life, and even a home for us in the future.