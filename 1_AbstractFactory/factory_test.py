import unittest

from factories.large_factory import LargeFactory
from factories.medium_factory import MediumFactory
from factories.small_factory import SmallFactory


class FactoryTest(unittest.TestCase):
    """Factory"""

    def test_large_factory(self):
        factory = LargeFactory()
        self.assertEqual(
            factory.create_button().get_html(),
            "<button size = 5 >  </button>")
        self.assertEqual(
            factory.create_header().get_html(),
            "<h size = 5 >  </h>")
        self.assertEqual(
            factory.create_image().get_html(),
            "<image size = 5 >  </image>")
        self.assertEqual(
            factory.create_text().get_html(),
            "<p size = 5 >  </p>")

    def test_medium_factory(self):
        factory = MediumFactory()
        self.assertEqual(
            factory.create_button().get_html(),
            "<button size = 3 >  </button>")
        self.assertEqual(
            factory.create_header().get_html(),
            "<h size = 3 >  </h>")
        self.assertEqual(
            factory.create_image().get_html(),
            "<image size = 3 >  </image>")
        self.assertEqual(
            factory.create_text().get_html(),
            "<p size = 3 >  </p>")

    def test_small_factory(self):
        factory = SmallFactory()
        self.assertEqual(
            factory.create_button().get_html(),
            "<button size = 1 >  </button>")
        self.assertEqual(
            factory.create_header().get_html(),
            "<h size = 1 >  </h>")
        self.assertEqual(
            factory.create_image().get_html(),
            "<image size = 1 >  </image>")
        self.assertEqual(
            factory.create_text().get_html(),
            "<p size = 1 >  </p>")

    def test_factory_is_singleton_instanse(self):
        factory = LargeFactory()
        LargeFactory().create_button()
        self.assertEqual(factory.instanse, LargeFactory().instanse)

    def test_different_factory_is_singleton_instanse(self):
        factory = LargeFactory()
        SmallFactory().create_button()
        self.assertNotEqual(factory.instanse, SmallFactory().instanse)


if __name__ == '__main__':
    unittest.main()
