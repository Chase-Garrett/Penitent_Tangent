from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic
from .forms import BotForm
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import praw
# Create your views here.

class IndexView(generic.FormView):
    template_name = "bot/index.html"
    form_class = BotForm

    def form_valid(self, form):
        try:
            # connect to reddit api with python wrapper
            reddit = praw.Reddit('bot')

            # analyze sentiment of the provided content
            analyzer = SentimentIntensityAnalyzer()

            # get url from form submission
            url = form.cleaned_data['url']
            submission = reddit.submission(url=url)

            # track the total compound score of the thread
            compound_score = 0.0

            # track number of commnets to read from a submission
            MAX_COMMENTS = 1000
            comment_count = 0

            # iterate through submission comment and get the total compound score
            for top_comment in submission.comments.list():
                if comment_count >= MAX_COMMENTS:
                    break
                vs = analyzer.polarity_scores(top_comment.body)
                compound_score += vs["compound"]

                comment_count += 1

                # set sentiment to default to neutral
                sentiment = "Neutral"

            # return positive/negative sentiment to user
            if compound_score > 0.1:
                sentiment = "Positive"
            elif compound_score < -0.1:
                sentiment = "Negative"

            return render(self.request, 'bot/index.html', {'bot_message': sentiment})
        except praw.exceptions.APIException as e:
            error_message = "Reddit API Error: {}".format(str(e))
            return render(self.request, 'bot/index.html', {'bot_message': error_message})
        except Exception as e:
            error_message = "An unexpected error occurred: {}".format(str(e))
            return render(self.request, 'bot/index.html', {'bot_message': error_message})
