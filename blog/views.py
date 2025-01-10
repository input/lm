from django.conf import settings
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django_plugin_blog.models import Tag
from django_plugin_blog.views import BlogFeed


class BlogFeedCustom(BlogFeed):
    """Override the default Atom feed created by django-plugin-blog."""
    def item_description(self, item):
        return item.summary_text

    def item_updateddate(self, item):
        return item.created


class BlogTagFeed(Feed):
    """Atom feed of latest blog entries for each tag ('django', 'python', etc.)."""
    feed_type = Atom1Feed

    def get_object(self, request, slug):
        return Tag.objects.get(slug=slug)

    def title(self, obj):
        title = getattr(settings, "DJANGO_PLUGIN_BLOG_FEED_TITLE", None) or obj.get_host()
        return f"{title}: Posts tagged '{obj.name}'"

    def link(self, obj):
        return f"/blog/tag/{obj.slug}/"

    def items(self, obj):
        return obj.entry_set.filter(is_draft=False).order_by("-created")[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summary_text

    def item_link(self, item):
        return f"/blog/{item.created.year}/{item.slug}/"

    def item_author_name(self, item):
        return (
            ", ".join([a.get_full_name() or str(a) for a in item.authors.all()]) or None
        )

    def item_updateddate(self, item):
        return item.created

    def get_feed(self, obj, request):
        feedgen = super().get_feed(obj, request)
        feedgen.content_type = "application/xml; charset=utf-8"
        return feedgen
