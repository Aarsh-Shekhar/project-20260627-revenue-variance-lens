import unittest

from revenue_variance_lens.models import Record
from revenue_variance_lens.scoring import score_record


class DepthCheck29(unittest.TestCase):
    def test_029_reporting_view(self):
        record = Record(id="segment-029", exposure=19157, signal=0.499, urgency=8)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
