---
layout: post
title:  "SNH - Intro and Overview"
date:   2018-5-14 17:50:00
categories: ['SNH']
published: true
Abstract:
defs_used:


---
# Moody's Introduction

The Strong Program in SNA is that it is so important to have friends, it is what makes us - our relational attributes is what makes us. Connections is what makes us us

The promise is that there are connections between us that are invisible or intangible. We can make it visible and do something with us. So how do we make sense of things and make them visible.

There are lots of papers on network and health

We think carefully about our data and draw heavily on graphic imagery.

We want to think about hwo to understand the global contxt of health - We hvae to understand how exposure is structured. We have to make sense of how social position in healthcare research and we need to figure it out. Across a lot of our studies, social behaviors can account for a lot of the variance in outcomes.  "who you are" explains what's going on, and this has to dow ith networks.

The mechanism through which networks matter depends on what the disease outcome you're focused on.

Spillover Effects - We have a doctor, patients and a direct outcome, but we also have indirect outcomes.
# Period
* Society and the Adolescent Self-Image Morris Rosenburg - THinking about how adolescents are in communities and how - too fast but it's in the notes!
* Everrett Rogers - Diffusion of Innovations

* In the 70's they focused more on Homophily - the causal ambiguity of netowrk associations?
* How do we go about identifying the causal effect of networks - if we want to do somethign in the world
* There are both selection and influence efects, so can we have mor eor less impact on one or the other to drive differences  
* Burkman group - How social setting effects health behavior over a long term period - those who had a high level of connections did better health-wise than others.
* There was also a lot around HIV/AIDS that was a real mystery that really tried to focus on what's going on here.
* The idea is that social goods move kind of like diseases - we can rob a lot of the ideas from one and carry it into the other
* John Potter - Seeking the Positivies
* Social Relations and Health - There is one piece social relationships and health

* There is also a lot of Dukehim - With Pescasilido - Social relationshis and mental health within a concrete network setting.
* Data work turns out to be semi-cross sectional because of data constraints - Martina MOrris did work on concurrency? In a lot of countries you find comparable rates of activity at the individual level but wild difference in community rates of disease spreading . What's going on here?  
* Ties overlapping in time is important for understanding cross-country variance.
* Anderson and May - came up with the touchstone text for unerstanding compartmental modles?
* And then peer infleunce - Bauman and Ement - Longitudinal friendship networks - dynamic networks that allows us to collect things longitudinally.
* Valente - Network Models of the Diffusion of Innovations - This took the population curve idea for Rogers and put it in place in actual networks tructures. If you're going to write a paper on network diffusion you should have this. Where does diffusion start.

IN THE 90s
* Add Health - Wave 3 in the field currently, following poeple that were in hs in 94. It's fascinating to have this kind of global network data studies. If you study the whole network
* Now in the developing world we have these whole village netowrks explaining waht's going on.


* Now we are working statistcally - thinking of soething different - NOw we have data to play with
* We want to model things - so now there are different statistical models in networks
* The idea that community structures are built by networks
* Christakis and Fowler - Spread of Obesity - so this piece sparked a movement trying to model contagion.

Moody argues that everyting should be a network!


## What are Social Networks
What is the network research lifecycle like? YOu ahve a series of research questions - then you use or find a dataset then you do some kind of cycle of scoring ad estiamtion cycle. There is a feedback loop . Then you do a model
What are the appraoches -
1. Networks as Variables - we come up with a feature of a network to predict an outcome
2. Network as Structures -

1. Connectionalist approach thinks of netowrks as pipes.
2. Positionalists - Netowrks as Rolse - people are distinct from each other based on their connections - vice presidents for instance put people in the same place.

Then you can think of connectionalist as of these CAUSING (Peer INfluence) or EFFECTING (peer Selection) something. Positional we might think of a burden of popularity as a cause they create constraints on interactions , or a sa result once you occupy in a role you recreate the network by redoing things in the same way.

### The Connectionist Model
The reproductive rate is based on the probability of infection, likelihood of contact, and the duration of contact. So:

Ro = BcD

So we know the risk is different depending on embeddedness maters -

What generates that structure? How do we get connectivity in random graphs. Especially if there is low-degree, and so only some are connected and they are really spindly. We think about

### Positioanl NEtwork

Without seeing a label we can see patterns of a network graph of a family.
We learn the rules of a setting. We can make sense of the system without the labels -

# Data
1. Data on nodes - rows of datasets - classic dataset
2. Data on Edges - their relationships

WE think of the values the data can take - binary or values - ever had sex with is binary indirect.
Bindary directd graph mwhere things cannot be reciprocated

Ties can be valued - have you ever had sex vs how many times. And this can be directed or not.

Relationships can also be antisymmetric, if i'm your boss youc an't be my boss

You can also have multiplex networks - different things at the same time

There can also be data error from asked questions. We also usually don't get a lot of multiplex data.

## Levels of Data

There are multiple levels of analysis.

So you can use jsut best friend dyad for instance. Or you can ahve the ego network (5 friends, or your set of friends), and then you can get friends of friends. What makes it an ego network is that we defined it to a particular ego. A community group is just a group of people.

We can also have partial networks - more than an ego netowrk and less than a global network - it is had to get full coveage. Snowball samples generate partial networks. Global networks have everyone in a bound even if they aren't connected to anyone else.

Modes in networks are the psosibility to exist within/between/ One mode network lets everyone be friends. Logical constraints mediates the difference. So - people and groups. I am connected to you because we're in the groups.

Two mode network is everywhere - you can get it without a survey - You can create ONE MODE PROJECTIONS of TWO MODE NETWORKS. THis is what th ePaul Revere datset has .
* Brier - Duality of People and Gorups - There is somthing interesting going on here

YOu can look at physicains who shares patients for instance - This makes a kind of physician networks - hospitals readmission rates can differ depending on when you get into the different communities.

# From Pictures to Matrices
Adjacency Matrix is a two dimensional array that has numbers for what's where.

And then you can do matrix algebra - BUT it is this thing that's pretty rough. We have really sprase matricies - Then we can move to an adjaacny list - One row for each respondent and a column for each person you're tied to.

Arc List is an edge wise recording of the same htings. But then it's easy to lose your isolates. WE usually have a node dataset

The two mode network si a not-square adjacency matrix
