# Predicting the impact of a stimulation on deep sleep, for Dreem

Description of the challenge:
Rythm is a neurotechnology company that was founded in July 2014. It combines neuroscience research and advanced technologies. Rythm employs 70 people in both San Francisco and Paris, and has numerous international partners (CNRS, IRBA, Stanford Center for Sleep Sciences and Medicine). Rythm’s goal is to develop consumer electronic products that improve people’ wellbeing and performance, and hence their daily lives.

The first product, Dreem (dreem.com), is a novel solution that improves sleep; it allows you to fall asleep more easily, impacts the quality of your deep sleep, and wakes you up at the best possible moment.

In this challenge, we focus on the deep sleep enhancement feature of the Dreem headband.

Deep sleep or slow-wave sleep is the most restorative stage of sleep. It can only be monitored with brain activity and is involved in the process of healing, rejuvenation, memory consolidation. Unfortunately, deep sleep can be shallowed with aging, stress or sleep related issues. However, deep sleep stimulation thanks to synchronized sound stimulations enhance deep sleep quality. Dreem headband is able to realize such a synchronized closed loop stimulation. More on the science can be found here original publication and here dreem first publication.

On this challenge, we focus on the few seconds before a stimulation and we want to determine whether or not it is a good moment for a stimulation. To answer that multiple informations are given on those few seconds before a stimulation, including EEG signal and Accelerometer signal. The impact of the stimulation is computed by comparing delta-wave energy after and before the stim. We want to predict this impact of stimulation to be able to stimulate at the best moment.
