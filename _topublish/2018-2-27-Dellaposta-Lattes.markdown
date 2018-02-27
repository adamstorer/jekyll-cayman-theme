---
layout: post
title:  "DellaPosta et. al - Why do Liberals Drink Lattes"
date:   2018-2-27 17:50:00
categories: ['DellaPosta','Culture QE','Reading Notes']
published: true
Abstract: "Popular accounts of “lifestyle politics” and “culture wars” suggest that political and ideological divisions extend also to leisure activities, consumption, aesthetic taste, and personal morality. Drawing on a total of 22,572 pairwise correlations from the General Social Survey (1972–2010), the authors provide comprehensive empirical support for the anecdotal accounts. Moreover, most ideological differences in lifestyle cannot be explained by demographic covariates alone. The authors propose a surprisingly simple solution to the puzzle of lifestyle politics. Computational experiments show how the self-reinforcing dynamics of homophily and influence dramatically amplify even very small elective affinities between lifestyle and ideology, producing a stereotypical world of “latte liberals” and “bird-hunting conservatives” much like the one in which we live."
defs_used:


---
Abstract
>Popular accounts of “lifestyle politics” and “culture wars” suggest that political and ideological divisions extend also to leisure activities, consumption, aesthetic taste, and personal morality. Drawing on a total of 22,572 pairwise correlations from the General Social Survey (1972–2010), the authors provide comprehensive empirical support for the anecdotal accounts. Moreover, most ideological differences in lifestyle cannot be explained by demographic covariates alone. The authors propose a surprisingly simple solution to the puzzle of lifestyle politics. Computational experiments show how the self-reinforcing dynamics of homophily and influence dramatically amplify even very small elective affinities between lifestyle and ideology, producing a stereotypical world of “latte liberals” and “bird-hunting conservatives” much like the one in which we live.

## The Puzzle of Lifestyle Politics

We know that people care a lot about lifestyle in weird ways, a grab bag of practices from music choices to others.

>Recent research by Baldassarri and Gelman ð2008Þ provides compelling
evidence from opinion surveys demonstrating strong and increasing political
and ideological alignment on what they call “moral issues.” When
lifestyle choices such as whom to marry, child-rearing responsibilities, and
when and whether to pray or have children come to be widely regarded
as expressions of group membership, they can become divisive. These “hotbutton”
issues—including gay rights, gender roles, school prayer, and
abortion—differ from consumer tastes in focusing on normative rather
than aesthetic preferences and, accordingly, in the level of passion they engender. p.1475

There are cultural enclaves among seemingly unrelated preferences. What's going on? In the GSS there is clustering of belief in astrology, art consumption and leisure activities. They are also correlated with political leanings.

What's going on here?

Our standard approach is to look at some aspects of thought as immovable (political opinion) and some as movable (horoscope reading)

>This explanatory strategy owes much to Weber’s theory of the status
group as a community of individuals with a shared “style of life” ð½1946
1991Þ. While classes are defined in terms of the production of goods, these
status groups and their associated lifestyles stem instead from patterns of
consumption. The link between production and consumption confers an
“elective affinity” between social class and membership in a status group. p.1484

>The common thread among these theories is the argument that demographic
and ideological organizing principles create axes of culture through
the formative experiences, material interests, and moral foundations that
can be statistically captured by indicators of social and cultural background. p.1485

However, ideological alignment and lifestyle variables go farther then one would likely dream of. There is no coherent cultural explanations for drinking lattes.

## A Relational Alternative

The observations are assumed to be independent, but this is a methodological blind spot.
>Without data on the opinions of peers, researchers have
little choice but to search for “within-individual” explanations among other
attributes of the respondent, as if each respondent arrives at an opinion
independently of what others around them are thinking pl. 1486

The parsimionous relational approach is as follows: alignment is an emergent property of a self-organizing cultural landscape. Self reinforcing dynamics of two well documented social processes - homophily and social influence, create similarity.

>We build on
and extend these studies, using a computational model to show how lifestyle
politics can emerge through a path-dependent historical process and
how very small demographic and socioeconomic effects on opinion can be
amplified many orders of magnitude. p.1489

## A computational model of network autocorrelation
>Autocorrelation means that an observation is dependent
on other observations, where this dependence increases with proximity
in temporal, spatial, and network location. p. 1489

>Less technically, spatial autocorrelation refers to the tendency for
individuals to resemble others in their geographic community, colorfully illustrated
by shared preferences for “books, beer, bikes, and Birkenstocks”
among liberal residents of Portland, Oregon p.1489

Temporal autocorrelation is the tendency for individuals to resemvle themselves other over time.

Network autocorrelation is that they tend to look like their network neighbors.

They do a computational model based on some degree of each of these things and find that small sources of influence and homophily can lead to large differences in groups.

THis is actually in some ways a different direction in network studies. I am not sure how it fits into Emirbayer's scheme.

>Random sampling gives investigators the confidence
that each survey respondent is independent of the others, which is necessary
to obtain an unbiased representation of the distribution of individual
traits in the underlying population. However, this independence also carries
an important, if largely neglected, limitation: Unlike the members of
the underlying population, the respondents in a national random sample
are atomized individuals, unaccompanied by friends and family. In the
absence of relational data, there is no way to measure the effects of sorting
and influence in the clustering of opinions. 
