import unittest
from obscurepy.models.obs_variable import ObsVariable


class ObsVariableTest(unittest.TestCase):

    def setUp(self):
        self.fixture = ObsVariable('new name', 'old name')
