import logging
import datetime

from kalliope.core.NeuronModule import NeuronModule, MissingParameterException
from picamera import PiCamera
from time import sleep

logging.basicConfig()
logger = logging.getLogger("kalliope")


class Camera(NeuronModule):
    """
    Use the pi camera to take pictures
    """
    def __init__(self, **kwargs):
        #super(Camera, self).__init__(**kwargs)
        super().__init__(**kwargs)

        # get the command
        self.nb_photos = kwargs.get('number_of_picture', 1)
        self.directory = kwargs.get('directory', '/home/pi/')
        self.timer = kwargs.get('timer', 1)

        cam = PiCamera()

        for i in range(self.nb_photos):
            name = "pi_" + str(datetime.datetime.now()) + ".jpg"
            cam.capture(self.directory + name)
            sleep(self.timer)
        cam.close()
