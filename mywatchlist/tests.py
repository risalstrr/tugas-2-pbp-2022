import datetime
from django.test import TestCase

# Create your tests here.
from mywatchlist.models import MyWatchList


class MywatchlistTestCase(TestCase):
    def setUp(self):
        MyWatchList.objects.create(watched=True, title="Stranger Things", rating=3,
                                   release_date=datetime.date(2022, 7, 6), review="Nice!")

    def test_mywatchlist_name_should_be_exist(self):
        watchlist = MyWatchList.objects.get(watched=True, title="Stranger Things", rating=3,
                                            release_date=datetime.date(2022, 7, 6), review="Nice!")
        self.assertEqual(watchlist.title, "Stranger Things")

    def test_mywatchlist_props_should_be_same(self):
        watchlist = MyWatchList.objects.get(watched=True, title="Stranger Things", rating=3,
                                            release_date=datetime.date(2022, 7, 6), review="Nice!")
        self.assertEqual(watchlist.watched, True)
        self.assertEqual(watchlist.title, "Stranger Things")
        self.assertEqual(watchlist.rating, 3)
        self.assertEqual(watchlist.release_date, datetime.date(2022, 7, 6))
        self.assertEqual(watchlist.review, "Nice!")
