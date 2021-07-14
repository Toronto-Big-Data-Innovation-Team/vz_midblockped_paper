(section:background)=
# Background

From 2010-2019 inclusive in the City of Toronto, pedestrians crossing at
midblocks represent only 16% of all pedestrians involved in a collision, but 28%
of all pedestrians seriously injured in a collision, and 42% of all pedestrian
collision fatalities. More pedestrians are killed or seriously injured in
midblock crossing collisions than any other type of collision in the City's
recent history. Because of this disproportionately high tendency of death or
serious injury, the City of Toronto's Vision Zero 2.0 report {cite}`ts2019`
designated midblock crossings as one of five issues to target road safety
interventions over the next several years. The report identified long distances
between safe crossing locations and the presense of transit stops, retail and
other destinations for foot traffic as drivers of midblock crossings, and road
width and number of lanes, high vehicle speeds, and limited visibility as risk
factors for collisions during crossings.

To address midblock crossing collisions, Vision Zero 2.0 proposes a set of
interventions: - When investigating where to install new traffic signals,
Transportation Services will consider road width, posted speed limits, and other
factors related to midblock crossing collisions - TTC stop consolidation -
removing bus stops along long midblocks to discourage crossings - A review of
pedestrian refuge islands for design improvements or replacement by a pedestrian
crosswalk

To inform the location prioritization for implementing these interventions, the
report calls for a road network-wide safety review, commonly referred to as
network screening.

Perhaps the most straightforward technique for network screening, and one that
has historically be used at the City, is hotspotting: tallying the number of
collisions that have occured at a location over a recent period of time.
Hotspotting is easy to implement, flexible in its ability to disproportionately
weight eg. killed or seriously injured (KSI) collisions, and, given sufficient
data, capable of revealing important patterns within a jurisdiction's crash
history. It is, however, a reactive approach, since one must wait for a history
of collisions to build up before confirming a hotspot. Moreover, it can be
unreliable due to fluctuations in the frequency of collisions (the number of
collisions per unit time) at a given location over time. A hotspot determined
from recent crash history may only exist due to a fluctuation, and therefore may
not reflect the underlying risk at the location (likewise a location with few or
no crashes may only appear relatively safe because of a fluctuation). This issue
is particularly prominent for midblock pedestrian crossings due to their
relative rarity. The United States Federal Highway Administration (FHWA) calls
this phenomenon the "regression to the mean effect" 
{cite}`thom+2018guide,srin+16`, and advocates for network screening approaches
based on predictive modeling as part of their "systemic safety" approach.

Predictive models estimate the relationship between various characteristics of a
location, such as road width, traffic volume, or nearby land usage, and its
**mean** collision frequency, i.e. collision frequency corrected for statistical
issues like regression to the mean. While historical crash data is required to
fit a model, only location characteristics are required to make predictions with
it, making models proactive tools rather than reactive ones. Additionally, a
natural byproduct of the fitting process is the relative contributions of each
location characteristic in setting the mean collision frequency; these can give
clues to the root causes of midblock crossing risk across the road network.

In support of Vision Zero 2.0, we developed a model that predicts the midblock
crossing pedestrian collision frequency on Toronto's arterial and collector
streets. We also constructed a framework for integrating its results into new
and existing City safety infrastructure programs.
