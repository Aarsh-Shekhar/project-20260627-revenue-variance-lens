import unittest

from revenue_variance_lens.models import Record
from revenue_variance_lens.scoring import score_record


class DepthCheck41(unittest.TestCase):
    def test_041_edge_case_review(self):
        record = Record(id="segment-041", exposure=61927, signal=0.216, urgency=2)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
