import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from review_conflicts import review
class DomainTests(unittest.TestCase):
 def test_self_review(self):self.assertEqual(review(['a'],[],['a'])['declared_conflicts'],['a'])
 def test_beneficiary_review(self):self.assertEqual(review([],['b'],['b'])['declared_conflicts'],['b'])
 def test_separate(self):self.assertEqual(review(['a'],['b'],['c'])['no_declared_conflict'],['c'])
 def test_no_reviewers(self):
  with self.assertRaises(ValueError):review(['a'],[],[])
 def test_duplicate(self):
  with self.assertRaises(ValueError):review([],[],['a','a'])
