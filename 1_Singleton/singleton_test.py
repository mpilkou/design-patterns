import unittest
import pickle as pic
import os

from multiprocessing.pool import ThreadPool as Pool
from singleton import Singleton, ChildSingleton


def help_threat_get_singleton():
    """Help fun"""
    return Singleton()


def help_threat_read_singleton():
    with open("singleton", "rb") as f:
        return pic.load(f)


class SingletonTest(unittest.TestCase):
    """Singleton"""

    def test_is_singleton(self):
        singleton_1 = Singleton()
        self.assertEqual(singleton_1.__class__.__name__, "Singleton")

    def test_is_same_singleton(self):
        singleton_1 = Singleton()
        singleton_2 = Singleton()
        self.assertEqual(
            singleton_1.get_instanse() is singleton_2.get_instanse(), True)

    def test_thread_save(self):
        pool1 = Pool(processes=1)
        pool2 = Pool(processes=1)
        self.assertEqual(
            pool1.apply_async(help_threat_get_singleton).get().get_instanse(),
            pool2.apply_async(help_threat_get_singleton).get().get_instanse())

    """Inheritanse"""
    def test_is_different_singleton_inheritanse(self):
        singleton_1 = Singleton()
        singleton_2 = ChildSingleton()
        self.assertFalse(
            singleton_1.get_instanse() is singleton_2.get_instanse())

    def test_is_same_singleton_child_inheritanse(self):
        singleton_1 = ChildSingleton()
        singleton_2 = ChildSingleton()
        self.assertTrue(
            singleton_1.get_instanse() is singleton_2.get_instanse())

    """Serialisation"""
    def test_is_serialize(self):

        with open("singleton", "wb") as f:
            pic.dump(Singleton(), f)

        pool1 = Pool(processes=1)
        pool2 = Pool(processes=1)
        self.assertEqual(
            pool1.apply_async(help_threat_read_singleton).get().get_instanse(),
            pool2.apply_async(help_threat_read_singleton).get().get_instanse())

        try:
            os.remove("singleton")
        except OSError:
            print("Error in remove")


if __name__ == '__main__':
    unittest.main()
