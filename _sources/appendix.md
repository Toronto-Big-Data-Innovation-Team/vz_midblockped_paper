# Appendix

(section:appendix:alternate)=
## Alternate Modelling Procedures

As showcased in {cite}`thom+2018guide`, a number of cities have built out
systemic and data-drive prioritization schemes for pedestrian safety. Notably,
the Seattle Department of Transportation (SDOT) replaced their hotspot-based
prioritization procedure with a regression-based one similar to Kumfer et al.
(indeed, SDOT partnered with the UNC Highway Research Center for parts of their
program, and helped pave the way for Kumfer et al. and the NCHRP guide). The
California Department of Transportation used an alternative method - dividing
both collisions and road facility types into sub-categories, then tallying the
number of collision events for each collision/facility combination (see
{cite}`thom+2018contract` Case Example 4). This method cannot infer mean
collision frequencies on individual midblocks, and so is not directly applicable
to our current work.

Negative binomial regression is the simplest commonly-used model that accounts
for the overdispersion of collision data, a common statistical property of
observed collision frequency data in which the variance significantly exceeds
the mean {cite}`washkm03`,  More sophisticated regression models (see eg.
{cite}`lordm10,srinb13,ziaky20` for review papers) that can better fit collision
data are often used in traffic safety research, including:

- Random effects and random parameters models (see {cite}`mannsb16` for a review
and {cite}`amohss16` for a comparative case study) that handle "unobserved
heterogeneity" - variations in mean collision frequency due to independent
variables that cannot be measured or have not been included - and 
unaccounted-for spatial and temporal correlation that results from it.
- Multivariate and joint models that can simultaneously model different levels
of collision severity (eg. {cite}`lan+13, mannsb16`).
- Machine learning techniques such as artificial neural networks and deep
learning (eg. {cite}`behb+18, alma+19`) and support vector regression (eg. 
{cite}`li+08`) that can automatically account for complex and non-linear
relationships between dependent and indepdent variables. Due to the complexity
of these models, they are more prone to overfitting (fitting to the noise as
well as the signal of the data), and more difficult to interpret, especially
from a causal inference standpoint.

While not accounting for phenomena like unobserved heterogeneity can be
detrimental to the model {cite}`mannsb16`, we elect to produce a negative
binomial regression because:
- Negative binomial regression is readily available in both frequentist and
Bayesian forms in statistical software. More sophisticated models would need to
be built from scratch and thoroughly tested.
- It is commonly used in other jurisdictions, making it easier to justify its
use {cite}`thom+2018guide`.
- It serves as a baseline to compare more sophisticated models against.
