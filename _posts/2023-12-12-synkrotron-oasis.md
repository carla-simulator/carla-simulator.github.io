---
layout: post
comments: true
title:  "OASIS Sim from Synkrotron"
subtitle: "GUI based CARLA simulation management, visual scenario authoring and cloud job management in the OASIS Sim platform"
description: "GUI based CARLA simulation management, visual scenario authoring and cloud job management in the OASIS Sim platform"
author: "@MattRoweEAIF"
image: 'img/carla.jpg'
background: '/img/posts/2023-12-12/sensor_config.png'
---

<br>


**Ever wanted to set up complex CARLA simulations and scenarios without writing a line of code?** - This is the power of Synkrotron’s [__OASIS Simulation Platform__](https://www.synkrotron.ai/sim.html).

<br>

![OASIS logo](/img/posts/2023-12-12/oasis_logo.png){:class="img-fluid rounded mx-auto d-block"}

<br>

 OASIS Sim facilitates the development and execution of complex scenarios through an intuitive, web-based, graphical user interface. The vast configurability of the CARLA simulator is exposed through OASIS Sim’s multiple views for __Scenario Authoring__, __Vehicle Configuration__, __Diagnosis__ and __Cloud Job Management__. The simulation workload can be distributed and __parallelised on the cloud__, leveraging the power of distributed cloud computing such as Amazon Web Services with the latest GPU technology. In the following, we introduce you to OASIS Sim’s principal views to explain how they can help you set up and run your simulations! Please visit the [Synkrotron website](http://www.synkrotron.ai/) and [request a trial](https://synkrotron.ai/contact.html).

{% include youtube.html id="YRI67aar3S0" %}

# Visual scenario authoring

![OASIS scenario authoring](/img/posts/2023-12-12/scenario_authoring.png){:class="img-fluid rounded mx-auto d-block"}

OASIS Sim provides a Scenario Editor GUI that enables users to design and edit traffic scenarios visually and intuitively. Users can specify the environment condition, the driving task of the ego vehicle and the behaviors of other traffic participants. The definition of these elements is compatible with OpenScenario 1.0 and can be imported from external sources or exported. Background traffic can also be managed in this view to add diversity and complexity to each scenario.

# Sensor and vehicle configuration

![OASIS vehicle config](/img/posts/2023-12-12/sensor_config.png){:class="img-fluid rounded mx-auto d-block"}

In the Vehicle Configuration panel users can equip the ego vehicle with pre-defined sensor types, a vehicle dynamics model and an autonomous driving system. This view offers visualizations of sensor placement and fields of view, allowing comprehensive configuration of the sensor suite and behaviors of the ego vehicle.


# Cloud based job management

![OASIS job management](/img/posts/2023-12-12/job_management.png){:class="img-fluid rounded mx-auto d-block"}

OASIS Sim works on the cloud, leveraging the scalability of cloud computing and the latest GPU technology to accelerate your simulation workflow. Each simulation is managed as a cloud processing job in the task management view. For each job you can see progress status and key outcome indicators such as collisions or traffic infractions. Multiple jobs will be parallelised using cloud computing resources to accelerate the R&D workflow. 

# Diagnosis 

![OASIS diagnosis 1](/img/posts/2023-12-12/diagnosis_1.png){:class="img-fluid rounded mx-auto d-block"}

Completed simulations can be analyzed in detail through the Diagnosis view to scrutinize the performance of an autonomous driving system under test both visually and through log data. Sensor feeds such as cameras and LIDAR can be replayed directly, performance logs can be viewed and downloaded and telemetry details such as speed, acceleration and inertial motion can be viewed graphically. The Diagnosis view gives you everything you need to troubleshoot your system through detailed metrics and visual analysis. 

![OASIS diagnosis 2](/img/posts/2023-12-12/diagnosis_2.png){:class="img-fluid rounded mx-auto d-block"}

# Deployment and integration

Both cloud and local deployments of Oasis Sim are available through containers. A comprehensive API exposes OASIS Sim’s features for seamless DevOps integration in your R&D workflow. Please visit the [Synkrotron website](http://www.synkrotron.ai/) and [request a trial](https://synkrotron.ai/contact.html).

<br>

*This is the first of a series of articles covering different tools within the CARLA Ecosystem. CARLA provides integration with numerous tools from the community, partners and sponsors to augment its capabilities and address a wide array of simulation use cases.*
