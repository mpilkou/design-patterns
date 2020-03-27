import unittest
import proxy


class ProxyTest(unittest.TestCase):

    def test_proxy(self):
        proxy_file = proxy.ProxyFileLoader(proxy.File("file"))
        self.assertNotEqual(proxy_file.file_show(), None)

    def test_proxy_1(self):
        proxy_file = proxy.ProxyFileLoader(proxy.File("file"))
        self.assertNotEqual(proxy_file.file_show(), 1)

    def test_proxy_2(self):
        proxy_file = proxy.ProxyFileLoader(proxy.File("file"))
        self.assertEqual(proxy_file.file_show(), 2)


if __name__ == '__main__':
    unittest.main()
