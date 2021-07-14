# Introduction

Over the last decade in the City of Toronto, pedestrians crossing at a midblock
represent around 15% of all pedestrians involved in a collision, but nearly 30%
of all pedestrians seriously injured in a collision, and over 40% of all
pedestrians killed. Because of this disproportionately high likelihood of death
or serious injury, the City of Toronto's Vision Zero 2.0 report {cite}`ts2019`
designated midblock crossings as one of five issues to focus on over the coming
years. The report cites land usage (such as shopping and retail), wide roads,
high travel speeds and long distances between safe crossing locations as major
factors to increasing the frequency of midblock crossing collisions. It proposes
proactive deployment of road safety infrastructure, such as new traffic signals,
to address them.

To optimize the deployment of infrastructure, Vision Zero 2.0 advocates for a
data-driven review of Toronto's road network that leverages the City's
longstanding collision data collection program and rich ecosystem of geospatial
data. Location-based prioritization is often done using recent crash history,
with locations that have seen more collisions more highly prioritized. The
number of collisions at a location, however, can vary greatly from year to year,
and the crash history alone cannot account for this variation. Moreover, using
crash history is an inherently reactive approach, since collisions need to
happen for a crash history to develop.

Instead of using crash history alone, we can utilize predictive models. These
estimate the underlying risk - the collision frequency with the year-to-year
variations smoothed out - using the characteristics of a location, such as road
width, features of the road, traffic volume, or nearby land usage. They not only
account for statistical issues like regression to the mean, but also give clues
to the root causes of collision risk at a location, and can also be used to
predict collision frequency at a location without any historical crash data.

In support of Vision Zero 2.0, we develop a model that predicts the midblock
crossing pedestrian collision frequency on Toronto's arterial and collector
streets. Our model is based on one developed at the Highway Safety Research
Center at the University of North Carolina - Chapel Hill, which is described in
{cite}`kumf+2019,thom+2018guide,thom+2018contract`, and will be referred to
throughout this report as the HSRC model.

{cite}`ts2019`
<!-- 


articular the use of predictive analytics for safety
intervention prioritization

The Vision Zero 2.0 report also emphasizes the importance of data-driven
decision making, in particular the use of predictive analytics for safety
intervention prioritization. Historically, location priority for implementing
safety infrastructure has often been done by request (eg. by City councilors) or
by finding hotspots, locations with a history of frequent and/or severe crashes.
While the latter can be used for network screening - a safety examination of the
City's road network as a whole - it is not only a reactive method (since one
must wait for collisions to occur first) but is also unreliable due to
year-to-year fluctuations in the frequency of collisions at a given location. A
hotspot determined from recent crash history may only exist due to a
fluctuation, and therefore may not reflect the underlying risk at the location.
The United States Federal Highway Administration (FHWA) calls this phenomenon
the "regression to the mean effect" {cite}`thom+2018guide,fhwa2015`, and advocate for
alternative network screening methods based on predictive models as part of
their systemic safety approach. These models determine the relationship between
various characteristics of a location, such as geometric features of the road,
road user volume, or nearby land usage, and its mean collision frequency. They
can account for statistical issues like regression to the mean, and can also be
used to predict collision frequency at a location without any historical crash
data {cite}`thom+2018guide`. -->
