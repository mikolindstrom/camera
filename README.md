# camera neuron for Kalliope

## Synopsis

This neuron use the raspberrypi camera to take pictures (can be modified for taking movies as well)
(Tested on a raspbian)

## Installation

  ```
  kalliope install --git-url https://github.com/bacardi55/kalliope-picamera.git
  ```

## Options

| parameter         | required | default   | choices | comment                                          |
|-------------------|----------|-----------|-----------------------------|------------------------------|
| number_of_picture | no       | 1         | Integer | The number of picture to take                    |
| directory         | no       | /home/pi/ | String  | The directory where to save the picture          |
| timer             | no       | 1         | String  | A number of second to wait between the picture   |

picture file will be named: "pi_" + datetime.datetime.now() + ".jpg"

## Synapses example
```
---
  - name: "Take-pictures"
    signals:
      - order: "Take a picture"
    neurons:
      - camera:
          number_of_picture: 3
          directory: "/home/pi/Desktop/PIctures/"
          timer: 1
```





* [Blog post about this neuron](http://bacardi55.org/2016/12/26/kalliope-raspberrypi-camera-neuron.html)
* [My posts about kalliope](http://bacardi55.org/kalliope.html)
