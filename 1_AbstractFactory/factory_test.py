import unittest

from factories.large_factory import LargeFactory
from factories.medium_factory import MediumFactory
from factories.small_factory import SmallFactory


class FactoryTest(unittest.TestCase):

    def test_large_factory(self):
        large_factory = LargeFactory()
        self.assertEqual(
            str(large_factory.create_button()),
            "<button size = 5 >  </button>")
        self.assertEqual(
            str(large_factory.create_header()),
            "<h size = 5 >  </h>")
        self.assertEqual(
            str(large_factory.create_image()),
            "<image size = 5 >  </image>")
        self.assertEqual(
            str(large_factory.create_text()),
            "<p size = 5 >  </p>")

    def test_medium_factory(self):
        medium_factory = MediumFactory()
        self.assertEqual(
            str(medium_factory.create_button()),
            "<button size = 3 >  </button>")
        self.assertEqual(
            str(medium_factory.create_header()),
            "<h size = 3 >  </h>")
        self.assertEqual(
            str(medium_factory.create_image()),
            "<image size = 3 >  </image>")
        self.assertEqual(
            str(medium_factory.create_text()),
            "<p size = 3 >  </p>")

    def test_small_factory(self):
        small_factory = SmallFactory()
        self.assertEqual(
            str(small_factory.create_button()),
            "<button size = 1 >  </button>")
        self.assertEqual(
            str(small_factory.create_header()),
            "<h size = 1 >  </h>")
        self.assertEqual(
            str(small_factory.create_image()),
            "<image size = 1 >  </image>")
        self.assertEqual(
            str(small_factory.create_text()),
            "<p size = 1 >  </p>")

    def test_factory_is_singleton_instanse(self):
        large_factory = LargeFactory()
        LargeFactory().create_button()
        self.assertEqual(large_factory.instanse, LargeFactory().instanse)

    def test_different_factory_is_singleton_instanse(self):
        large_factory = LargeFactory()
        SmallFactory().create_button()
        self.assertNotEqual(large_factory.instanse, SmallFactory().instanse)


if __name__ == '__main__':
    unittest.main()
