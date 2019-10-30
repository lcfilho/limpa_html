import unittest
import tagcleaner
import os
import filecmp

class Test_tag(unittest.TestCase):
    
    def test_cleaner(self):
        path= "/home/luisfilho/semantix/teste_takeshi/TESTE_TAGS_HTML/html.txt"
        self.assertTrue(os.path.exists(path))
   
    def test_cleaner_2(self):
        self.assertFalse(filecmp.cmp("/home/luisfilho/semantix/teste_takeshi/TESTE_TAGS_HTML/html.txt", "/home/luisfilho/semantix/teste_takeshi/TESTE_TAGS_HTML/mock01.txt"))

if __name__ == "__main__":
    unittest.main()
  
    
    
