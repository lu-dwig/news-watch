import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    def setUp(self):
        self.new_article = Articles("Vox.com","Dylan Matthew","Economic Strand","Have we been thinking about economic growth all wrong?","http//www.vox.com","https://www.vox.com/future-perfect/23048981/economic-growth-productivity-philippon","2022-04-30 T22:41:51Z")

    def instance_test(self):
        self.assertTrue(isinstance(self.new_article,Articles))

if __name__ == "__main__":
    unittest.main()
    