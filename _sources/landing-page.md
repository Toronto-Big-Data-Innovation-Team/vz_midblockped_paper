# Introduction

Of the pedestrian collisions from the last decade in Toronto, those that involve
a pedestrian crossing at a midblock are particularly dangerous, accounting for
the majority of pedestrian fatalities and a plurality of serious injuries. The
City's Vision Zero 2.0 Road Safety Plan calls for the proactive deployment of
safety infrastructure to address the risks associated with pedestrian midblock
crossings, prioritized through a systemic and data-driven review of all
midblocks across the City.

To enable the systemic review, our data science team in Policy & Innovation at
the City of Toronto Transportation Services constructed a new network screening
process based on pioneering work from the Highway Safety Research Center at the
University of North Carolina, Chapel Hill. The process is built around a
regression model that fits for the relationships between midblock collision
frequency and various explanatory variables such as local demographics,adjacent
land use, and traffic volume.

This white paper documents our methods, initial results, and recommendations for
using the results for safety infrastructure prioritization. It is a living
document, and will be updated periodically as our modelling and
operationalization techniques are further refined. In [](section:methods), we
provide a background on collision frequency
predictive modelling, and detail our input data, data processing, and modelling
steps.

