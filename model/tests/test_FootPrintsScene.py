
import os
import unittest
from xml.dom import minidom

from core.model.FootprintsScene import FootprintsScene


# ------------------------------------------------------------------------------
# FootprintsSceneTestCase
#
# python -m unittest discover core/model/tests/
# python -m unittest core.model.tests.test_FootprintsScene
# ------------------------------------------------------------------------------
class FootprintsSceneTestCase(unittest.TestCase):

    # -------------------------------------------------------------------------
    # testFootprintsScene
    # -------------------------------------------------------------------------
    def testFootprintsScene(self):

        sceneGML = None

        GML_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'scene.gml')

        sceneGML = minidom.parse(GML_FILE)
        features = sceneGML.getElementsByTagName('gml:featureMember')[0]
        fps = FootprintsScene(features)

        self.assertEqual(fps.fileName(),
                         '/css/nga/WV01/1B/2015/100/' +
                         'WV01_102001003A7E9A00_X1BS_502788423060_01/' +
                         'WV01_20150410052955_102001003A7E9A00_' +
                         '15APR10052955-P1BS-502788423060_01_P005.ntf')

        self.assertEqual(fps.pairName(),
                         'WV01_20150410_102001003C718E00_102001003A7E9A00')

        self.assertEqual(fps.stripName(),
                         'WV01_102001003A7E9A00_P1BS_502788423060_01')

        # Test retrieving a tag that does not exist.
        with self.assertRaises(RuntimeError):
            fps._getValue('doesNotExist')
