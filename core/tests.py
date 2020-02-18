from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from core.models import Tweet
from core.serializers import TweetSerializer
from rest_framework.views import status


class CountryDataTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        Tweet.objects.create(name="Peter Parker", message="Hello, I'm Spider Man")
        Tweet.objects.create(name="Bruce Banner", message="Hello, I'm Hulk")


    def test_get_all_tweets(self):
        """
            This test retrieve all tweets
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("/")
        )

        expected = Tweet.objects.all()
        serialized = TweetSerializer(expected, many=True)
        self.assertEqual(response.data['data'], serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_tweet(self):
        """
            This test ensures that a countryData is updated when we make a PATCH request to the display_data/:pk endpoint
        """
        tweet = {
            "name": "Tony Stark",
            "message": "Hello, I'm Iron Man",
        }

        # hit the API endpoint
        response = self.client.post(reverse("/"), tweet, format='json')
        # fetch the data from db
        expected = Tweet.objects.filter(name="Tony Stark").last()

        serialized = TweetSerializer(expected, many=False)
        self.assertEqual(response.data['data']['tweet'], serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
