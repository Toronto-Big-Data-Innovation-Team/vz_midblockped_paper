#!/usr/bin/env python
# coding: utf-8

# (section:methods)=
# # Methods

# ## Modelling Procedure
# 
# Our model and operationalization recommendations are based on a network screening and infrastructure prioritization framework developed at the Highway Safety Research Center at the University of North Carolina - Chapel Hill, which is described in Kumfer et al. 2019 {cite}`kumf+2019` and a corresponding National Cooperative Highway Research Program (NCHRP) contractor's report {cite}`thom+2018contract`. Their framework adapts modelling and prioritization techniques typically used for vehicle-vehicle collisions on highways to vehicle-pedestrian ones, and it forms the technical underpinnings of the NCHRP guide on pedestrian network screening best practices {cite}`thom+2018guide`. While this guide covers a number possible approaches to pedestrian collision network screening, Kumfer et al. is particularly interesting to us because they specifically tackle the difficult task of modeling midblock pedestrian crossing collisions, which tend to be rarer.
# 
# Their procedure is:
# 
# 1. Obtain a midblock network - a geospatial table of where each row represents the roadway of a midblock.
# 2. Associate collision location data to the midblocks, as well as a wide range of physical, demographic, traffic volume, and other types of data. The result is that each midblock has an associated population density, traffic volume, etc., that serve as independent variables to the regression, and an associated number of collisions, serving as the dependent variable.
# 3. Perform dimensionality reduction, to reduce the number of independent variables used in the regression to those that are most significantly predictive.
# 4. Perform a negative binomial regression to obtain the final model.
# 
# For more detail, please see [cite}`thom+2018guide` Data and Methodology, and {cite}`thom+2018guide` Section 4.2.
# 
# Our procedure broadly follows these steps. In step 3, Kumfer et al. used a conditional random forest (CRF) to select only variables that have a statistically significant predictive effect for collision frequency, and reduced the number of independent variables from 51 to 35-36 {cite}`thom+2018contract`. We instead perform a simpler dimensionality reduction that focuses on reducing multicollinearity.
# 
# Negative binomial regression is one of the modelling methods in general use for collision frequency modelling. For an overview of alternatives, and our rational for adopting this method, see [](section:appendix:alternate).

# In[ ]:




