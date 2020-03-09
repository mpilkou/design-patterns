import unittest
import pickle as pic
import warnings

from multiprocessing.pool import ThreadPool as Pool

from factories.large_factory import LargeFactory
from factories.medium_factory import MediumFactory
from factories.small_factory import SmallFactory

# Python 2/3 compatibility
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    try:
        unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual
    except:
        print("Warning")


class FactoryTest(unittest.TestCase):
    """Factory"""

    def test_large_factory(self):
        factory = LargeFactory()
        self.assertEqual(
            factory.createButton().getHtml(),
            "<button size = 5 >  </button>")
        self.assertEqual(
            factory.createHeader().getHtml(),
            "<h size = 5 >  </h>")
        self.assertEqual(
            factory.createImage().getHtml(),
            "<image size = 5 >  </image>")
        self.assertEqual(
            factory.createText().getHtml(),
            "<p size = 5 >  </p>")

    def test_medium_factory(self):
        factory = MediumFactory()
        self.assertEqual(
            factory.createButton().getHtml(),
            "<button size = 3 >  </button>")
        self.assertEqual(
            factory.createHeader().getHtml(),
            "<h size = 3 >  </h>")
        self.assertEqual(
            factory.createImage().getHtml(),
            "<image size = 3 >  </image>")
        self.assertEqual(
            factory.createText().getHtml(),
            "<p size = 3 >  </p>")

    def test_small_factory(self):
        factory = SmallFactory()
        self.assertEqual(
            factory.createButton().getHtml(),
            "<button size = 1 >  </button>")
        self.assertEqual(
            factory.createHeader().getHtml(),
            "<h size = 1 >  </h>")
        self.assertEqual(
            factory.createImage().getHtml(),
            "<image size = 1 >  </image>")
        self.assertEqual(
            factory.createText().getHtml(),
            "<p size = 1 >  </p>")

    def test_factory_is_singleton_instanse(self):
        factory = LargeFactory()
        LargeFactory().createButton()
        self.assertEqual(factory.instanse, LargeFactory().instanse)

    def test_different_factory_is_singleton_instanse(self):
        factory = LargeFactory()
        SmallFactory().createButton()
        self.assertNotEqual(factory.instanse, SmallFactory().instanse)


if __name__ == '__main__':
    unittest.main()
