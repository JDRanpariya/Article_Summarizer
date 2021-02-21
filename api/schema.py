import graphene
from graphene_django import DjangoObjectType

from .models import Article


class articleType(DjangoObjectType):
    class Meta:
        model = Article


class Query(graphene.ObjectType):
    recentArticles = graphene.List(articleType)
    allarticles = graphene.List(articleType)

    def resolve_recentArticles(self, info, **kwargs):
        return Article.objects.all().order_by('-id')[:3]

    def resolve_allarticles(self, info, **kwargs):
        return Article.objects.all().order_by('-id')


class CreateSummary(graphene.Mutation):
    article = graphene.Field(articleType)

    class Arguments:
        content = graphene.String()

    def mutate(self, info, content):
        article = Article(content=content)
        article.save()

        return CreateSummary(article=article)

class ScrapeSummary(graphene.Mutation):
    article = graphene.Field(articleType)

    class Arguments:
        url = graphene.String()

    def mutate(self, info, url):
        article = Article(url=url)
        article.scrapeSave()

        return ScrapeSummary(article=article)


class Mutation(graphene.ObjectType):
    create_summary = CreateSummary.Field()
    scrape_summary = ScrapeSummary.Field()