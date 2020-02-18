from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.utils import json
from rest_framework.response import Response

from core.models import Tweet
from core.serializers import TweetSerializer


class TweetView(APIView):
    """
       API endpoint to manage Tweets
    """

    @staticmethod
    def get_object(pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            return None

    def get(self, request, pk=None):
        """
        Retrieve tweets searching all or by id
        """
        response = dict()
        response['status_code'] = status.HTTP_200_OK
        response['status'] = 'success'

        if pk:
            tweet_obj = self.get_object(pk)
            if tweet_obj:
                response['data'] = TweetSerializer(tweet_obj).data
                return Response(response)
            else:
                response['status_code'] = status.HTTP_404_NOT_FOUND
                response['status'] = 'failed'
                response['data'] = []
                response['message'] = 'Data not found'
                return Response(response)

        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)

        if not serializer:
            response['data'] = []
            return Response(response)

        response['data'] = serializer.data

        return Response(response)

    def post(self, request):
        tweet = json.loads(request.body.decode('utf-8'))
        response = dict()

        if tweet is None:
            return Response(status.HTTP_400_BAD_REQUEST)

        serializer = TweetSerializer(data=tweet)
        if serializer.is_valid(raise_exception=True):
            tweet_saved = serializer.save()
            response['status_code'] = status.HTTP_201_CREATED
            response['status'] = 'success'
            response['data'] = {'tweet': TweetSerializer(tweet_saved).data}
        return Response(response)

