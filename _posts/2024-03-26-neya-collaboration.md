---
layout: post
comments: true
title:  "CARLA teams up with Neya Systems to upgrade to the Unreal Engine 5"
subtitle: "Upgrading to Unreal Engine 5 brings incredible new graphics capabilities to level up simulation realism in CARLA"
description: "Upgrading to Unreal Engine 5 brings incredible new graphics capabilities to level up simulation realism in CARLA"
author: "@MattRoweEAIF"
image: 'img/carla.jpg'
background: '/img/posts/2024-03-26/carla_ue5_teaser.png'
---

{% include youtube.html id="J4pHRM1Q5nQ" %}

We are thrilled to announce today our collaboration with [__Neya Systems__](www.neyarobotics.com ) and its parent company [__Applied Research Systems (ARA)__](https://www.ara.com/), in which the CARLA team and Neya Systems are working together to __upgrade the CARLA simulator to Unreal Engine 5__. The long awaited upgrade is motivated by ARA's requirements in developing a Virtual Testbed for [__DARPA's Triage Challenge__](https://triagechallenge.darpa.mil/). The DARPA Triage Challenge involves a series of competitive events aimed at promoting innovation for medical triage. Neya Systems leverages the CARLA framework for stress testing the autonomy and control of its off-road vehicles in a virtual environment before moving to field tests.


"*CARLA’s advanced features and flexibility align perfectly with our commitment to pushing the boundaries of innovation in the field of autonomy,*” said __Kurt Bruck, division manager, Neya Systems__. “*In addition, CARLA’s capability to simulate off-road environments allows us to explore and develop autonomous solutions that go beyond conventional paved road scenarios. Updating CARLA to Unreal Engine 5 will be a significant accomplishment for open-source simulation developers everywhere.*" 

## What does this mean for CARLA? 

[__Unreal Engine 5__](https://www.unrealengine.com/en-US/unreal-engine-5) brings a comprehensive suite of upgrades that promise to __dramatically improve modeling, simulation realism and performance in CARLA__. First and foremost, Unreal Engine 5 looks incredible! If you haven't already, check out the teaser video above. More specifically, UE5 brings a number of important innovations that promise to supercharge your autonomy simulations:

### Nanite

Nanite is the new virtualized geometry system at the core of UE5. It allows an __unprecedented level of geometry detail__ and high object counts without compromising performance. Meshes can be used with a far higher level of geometric detail while still achieving real-time performance due to Nanite's intelligent geometry management. Nanite only works on the level of detail that can be perceived, distant objects in the scene are rendered using less polygons while Nanite continuously adjusts the number of polygons used for an object as its distance from the camera changes. Level Of Detail meshes (LODs) are no longer needed, eliminating the artefacts associated with LODs and reducing modelling time. 

![nanite](/img/posts/2024-03-26/nanite_geom.png){:class="img-fluid"}

### Lumen

Lumen is Unreal Engine 5's new global illumination and reflections system that improves the appearance of indirectly illuminated objects. In a real world scene, a lot of the light illuminating an object comes not from a direct light source like the sun or a streetlamp, but from light diffusely reflected from other objects. The objects that reflect the light affect its qualities, such as color and intensity. Lumen models these indirect lighting effects and reflections with stunning realism!

![lumen](/img/posts/2024-03-26/lumen.png){:class="img-fluid"}

### Metahumans

The upgrade to Unreal Engine 5 opens up the possibility to __bring Metahumans into CARLA__! [MetaHumans](https://www.unrealengine.com/en-US/metahuman) is a technology framework that facilitates modeling and animation of hyper-realistic human characters in video games. Alongside the improved rendering of skin, clothes and hair come a suite of tools to help you create Metahumans efficiently in UE5. The MetaHumans framework provides UIs for modeling and animating hyper-realistic depictions of humans. This has big implications for robotic applications of CARLA involving facial recognition, such as security drones or search and rescue applications. 

## Coming soon!

The collaboration plans to release an initial update to CARLA in the summer of 2024, with additional updates to CARLA’s physics capabilities to follow in 2025. __Stay tuned here and on [LinkedIn](https://www.linkedin.com/company/carla-simulator/) for future updates__!


<br>
<br>
<br>
<br>

### About Neya Systems

Neya Systems, a division of Applied Research Associates, is committed to advancing the field of unmanned systems through the development and integration of cutting-edge technologies and expertise in autonomy, computer vision, cybersecurity, and general unmanned systems development and deployment. Our team of experts is dedicated to creating innovative solutions that help our customers meet their mission goals. 

### About ARA

Applied Research Associates, Inc. (ARA) was founded in 1979, in Albuquerque, New Mexico, to offer science and engineering research to solve problems of national importance. ARA delivers leading-edge products and innovative solutions for national defense, energy, homeland security, aerospace, healthcare, transportation, and manufacturing. With over 2,000 employee-owners at locations in the U.S. and Canada, ARA offers a broad range of technical expertise in defense technologies, civil engineering, computer software and simulation, systems analysis, biomedical engineering, environmental technologies, and blast testing and measurement.