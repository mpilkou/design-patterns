import unittest
from composite import Picture, Line, Squere, Text



class CompositeTest(unittest.TestCase):
    def test_composite(self):
        p1 = Picture()
        self.assertListEqual(p1.draw(), [[' ',' ',' '],[' ',' ',' '],[' ',' ',' '],])
    
    def test_leaf(self):
        p1 = Squere()
        self.assertListEqual(p1.draw(), [['+','-','+'],['|',' ','|'],['+','-','+'],])

    def test_composite_in_action_2_items(self):
        p1 = Picture()
        p1.add(Squere())
        p1.add(Text())
        p1.add(Line())
        self.assertListEqual(p1.draw(), [['+','-','/'],['T','/','T'],['/','-','+'],])
        

if __name__ == '__main__':
    unittest.main()
