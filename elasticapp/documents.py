from elasticapp.models import Post
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

@registry.register_document
class PostDocument(Document):
    class Index:
        name = 'post'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Post
        fields = [
            'title',
            'description',
            'image',
            'body',
            'order',
        ]


