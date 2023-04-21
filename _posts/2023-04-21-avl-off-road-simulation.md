---
layout: post
comments: true
title:  "Let's go off-road!"
subtitle: "AVL has integrated CARLA into their simulation toolchain for autonomous driving use cases in unpaved terrain"
description: "AVL has integrated CARLA into their simulation toolchain for autonomous driving use cases in unpaved terrain"
author: "@MattRoweEAIF"
image: 'img/carla.jpg'
background: '/img/posts/2023-04-21//AVL_headquarters.jpg'
---

{% include youtube.html id="hqpQObbm_j0" %}

CARLA is being widely used for the virtual testing of autonomous road vehicles with realistic
environment simulation. But have you ever tried to use it for off-road applications such as
agriculture, construction, or logistics?

AVL engineers have found a solution to enhance CARLA for simulation in unpaved, rough
terrain. This has been achieved by coupling CARLA with the advanced vehicle dynamics
software AVL VSM<sup>TM</sup>. With the AVL solution, the vehicle dynamics precisely interact with the
surface based on a synchronization of all wheel contact positions. In combination with AVL’s
soft-soil tire model, users can expect realistic driving behavior.

The two simulation tools are coupled using AVLs open co-simulation platform
Model.CONNECT<sup>TM</sup>. With plug & play interfaces it is easy to connect the signal I/O ports of the
tools with each other in a graphical user interface. The powerful co-simulation engine handles
the correct synchronization of all tools and can even handle tools running with different
frequencies.

In the concrete example of the autonomous tractor, the co-simulation setup was extended with
a sensor fusion algorithm that outputs a unified list of detected objects as well as the automated
driving control algorithm. The control loop is closed by updating the new vehicle position in
CARLA and generating new sensor data.

AVL agreed to contribute their CARLA code changes and technical documentation to the
CARLA project. Furthermore, AVL tools are available free of charge via the University
Partnership Program. Stay tuned and contact us if you are interested at [__info@avl.com__](mailto:info@avl.com).

![avl_tractor](/img/posts/2023-04-21/avl_tractor.png){:class="img-fluid rounded mx-auto d-block"}
