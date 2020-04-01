import twitter
api = twitter.Api(consumer_key='v1nukJYV0uli0tIszYUp90gui',
                  consumer_secret='yhDGARPiOizRIhZBlvMx0BSdZfDvQc8fxh0pVj3SiPg9kBYa93',
                  access_token_key='2794461276-w2fEKidiEKwEYmcbUIsFSOSvJQNIf1iQPUXpplx',
                  access_token_secret='LSuAybph4tnkVtl0sJByeuFGUTcrLttBCGkkttuPPBDEQ')
statuses = api.GetUserTimeline('eihart123')
print([s.text for s in statuses])
