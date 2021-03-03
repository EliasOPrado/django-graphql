from django.urls import path, include
# from django.conf.urls import urls, include
from graphene_django.views import GraphQLView

urlpatterns = [
    # Conexcao com graphql
    path('graphql', GraphQLView.as_view(graphiql=True))
]