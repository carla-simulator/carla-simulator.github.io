---
layout: post
comments: true
title:  "CARLA 0.8.2: Driving Benchmark"
subtitle: ""
author: felipecode
auth_page: https://github.com/felipecode
date:   2018-03-27 08:00:00 +0002
background: '/img/posts/2018-03-27/release-0.8.0-header.jpg'
---

We release the new  **CARLA 0.8.2 Release** presenting a new and redefined **driving benchmark**. We endorse you people try it and attempt [to beat our driving agents](#can-you-beat-our-agents-).


<!-- Get release button -->
<p class="center"><a href="https://github.com/carla-simulator/carla/releases" target="_blank" class="btn btn-primary" title="Go to CARLA releases" style="text-decoration: none;"><i class="fab fa-github fa-lg"></i> Get CARLA 0.8.2</a></p>




[//]: <>(One of the main burdens for one specific science or  technology to evolve is having consistent way to compare what  the scientists propose. Progress seems to happen when there is a clear, well defined and reproducible problem to tackle.)

[//]: <>(In computer vision, for instance, the Image-Net Dataset  helped the unveiling of deep learning and CNNs as  a ground breaking technology. This raised image recognition to unimaginable level when compared to just few years ago.)

For autonomous driving, standard ways to compare methods is scarce, since every company investing real money on this matter seems to have their own data, private simulators and cars. This material, is of course, not accessible to the general public. How could then the autonomous driving community compare their agents ?


**That is one of the reasons why CARLA was designed** . We are working to be a standard way  to compare a autonomous driving algorithms. For now we present the driving benchmark module that allows users to create sets of experiment and access the driving quality of an agent.

[//]: <>(On this release we already provide the driving benchmark for CoRL2017 and show updated results for the Reinforcement Learning Method and the Imitation Learning Method. We also discuss the reproducibility of CARLA results, i.e, how)

The CARLA 0.8.2 release also adds a few fixes: ( NESTOR)


#### Driving benchmark overview


![benchmark diagram](/img/posts/2018-04-02/benchmark_diagram_small.png)

> Figure: Overview of the driving benchmark module, agents and new tasks (experiments) could easily be placed on the driving benchmark.

The driving benchmark serves as a controlled interface to test your agent. The modules provides a simple python interface where you just need to redefine one function to get your agent
running. The interface is agnostic to the type of agent you have: reinforcement learning, imitation learning etc. Also, it provides a way to create new sets of experiments that can be used to challenge your agent.
More information can be found at the [driving benchmark documentation]()


#### Sample results

We compute the driving benchmark using the [CoRL2017](http://proceedings.mlr.press/v78/dosovitskiy17a/dosovitskiy17a.pdf) set of tasks for  reinforcement learning and  imitation learning agents. We show the average success and standard deviation of three runs. By success we define as the percentage of episodes that the agent is able to reach the goal.

###### Percentage of Success, Imitation Learning

Task          | Training Conditions | New Town | New Weather     | New Town & Weather
--------------|:------------------- |:--------:|:---------------:| :----:
Straight      | 95 ± 0.81           | 98 ± 0.00| 95 ± 0.94       | 90 ± 1.69
One Turn      | 89 ± 0.00           | 73 ± 0.81| 88 ± 1.80       | 74 ± 1.69
Navigation    | 83 ± 0.94           | 61 ± 1.69| 76 ± 1.60       | 57 ± 6.59
Nav. Dynamic  | 82 ± 0.94           | 53 ± 2.94| 78 ± 0.00       | 47 ± 3.39

> Table: Average percentage of sucess for imitation learning over three runs, the standard deviation is also shown.

###### Percentage of Success, Reinforcement Learning

Task          | Training Conditions | New Town | New Weather     | New Town & Weather
--------------|:-------------------:|:--------:|:---------------:| :-------------:
Straight      | 91 ±                 | 97       | 96              | 90
One Turn      | 89 ±                 | 65       | 88              | 76
Navigation    | 83 ±                 | 49       | 76              | 66
Nav. Dynamic  | 82 ±                 | 48       | 78              | 52

> Table: Average percentage of success for reinforcement learning over three runs, the standard deviation is also shown.

We also show the average number  of kilometers without making am infraction. Besides the average computed in a single benchmark, we also compute the average and standard deviation between three runs. For all the infractions, only the task with dinamic objects is considered as made in the [CoRL 2017 paper](proceedings.mlr.press/v78/dosovitskiy17a/dosovitskiy17a.pdf).

###### Infractions Imitation Learning

Infractions                | Training Conditions | New Town   | New Weather     | New Town & Weather
--------------             |:-------------------:|:----------:|:---------------:| :----:
Opposite Lane              | 50.0 ± 23.6         | 2.55 ± 0.10| 33.7 ± 0.35     | 3.76 ± 0.36
Sidewalk                   | 15.6 ± 5.16         | 1.21 ± 0.07| 5.62 ± 0.05     | 1.08 ± 0.12
Collision-static           | 2.36 ± 0.52         | 0.60 ± 0.05| 4.07 ± 1.91     | 0.51 ± 0.06
Collision-car              | 2.96 ± 0.71         | 0.59 ± 0.07| 2.24 ± 0.56     | 0.54 ± 0.05
Collision-pedestrian       | 3.34 ± 0.17         | 2.52 ± 0.69| 5.00 ± 0.92     | 1.79 ± 0.36

> Table: Average number of kilometers travelled before infraction. The results shown are again averaged over three runs, the standard deviation is also shown.


###### Infractions Reinforcement Learning

Infractions                | Training Conditions | New Town | New Weather     | New Town & Weather
--------------             |:-------------------:|:--------:|:---------------:| :----:
Opposite Lane              | 91                  | 97       | 96              | 90
Sidewalk                   | 89                  | 65       | 88              | 76
Collision-static           | 83                  | 49       | 76              | 66
Collision-car              | 82                  | 48       | 78              | 52
Collision-pedestrian       | 82                  | 48       | 78              | 52

> Table: Average number of kilometers travelled before infraction. The results shown are again averaged over three runs, the standard deviation is also shown.


To run the driving benchmark for imitation learning go to the [imitation learning repository](https://github.com/carla-simulator/imitation-learning).
To run the driving benchmark for reinforcement learning go to the [reinforcement learning repository](https://github.com/carla-simulator/imitation-learning).

#### About the existent standard deviation

As we can see from the results tables, there is a non-negligible amount of standard deviation on three runs in the benchmark, specially for the new town and weather situation. CARLA has reproducible experiments but not perfectly. Right now, there are a few sources of non-determinsm that can make a simulation with same parameters to be
different:

* **Different load time for textures**: Different machines, or even the same machine, can take different time to load textures.
* **Pedestrians algorithms are non-deterministic** (See  [#258](https://github.com/carla-simulator/carla/issues/258) ).

On the following video we compare the frames of two different runs in the same machine. The pixels in red show when there is a different between the images from the two runs.

<div class="intrinsic-container intrinsic-container-16x9">
  <iframe src="https://www.youtube.com/embed/6uCbRHj3ojo?feature=oembed&vq=hd720" frameborder="0" gesture="media" allowfullscreen="" class="fluidvids-item" data-fluidvids="loaded"></iframe>
</div>

As we can see, until time 0:21 there are no many differences, except in some positions where the texture was loaded in a different time. After, there is a pedestrian crashing into another on 0:20 and this already changes the course of the simulation. These differences can indeed affect the results of machine learning based methods.


#### Can you beat our agents ?


Comment your results for the CoRL2017 here or send your them with documentation or code to carla_driving_benchmark@gmail.com. As soon as we have enough material we promisse another blog post with the best agents on CARLA. It is of our intention, in the future, to promote CARLA AI challenges, so we are very welcome to any feedback about this benchmark.


