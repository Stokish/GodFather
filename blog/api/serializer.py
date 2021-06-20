from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from blog.models import Post


class PostSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='post-api-detail', lookup_field='pk' )
    author = SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def get_author(self, obj):
        return str(obj.author.username)


class PostDetailSerializer(ModelSerializer):
    delete_url = HyperlinkedIdentityField(view_name='post-api-delete', lookup_field='pk')
    update_url = HyperlinkedIdentityField(view_name='post-api-update', lookup_field='pk')
    author = SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def get_author(self, obj):
        return str(obj.author.username)


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        exclude = ('likes', 'author', 'date_posted',)