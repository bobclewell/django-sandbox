from django.test import TestCase
from django.urls import reverse
from .models import Topic

def stub_topic():
    """Creates a basic topic for use in testing."""
    Topic.objects.create_topic(
        title="How awesome is Bacon?",
        description="Trying to evaluate the level of awesomeness of Bacon."
    )


def stub_comment():
    """Creates a basic comment within the above topic for use in testing."""
    stub_topic()
    topic = Topic.objects.get(pk=1)
    topic.comment_set.create(comment_text="I'd say it's as awesome as bacon covered in bacon!")


class TopicViewTests(TestCase):
    def test_the_creation_of_a_new_topic(self):
        """Confirms the created topic appears in the index view."""
        stub_topic()
        response = self.client.get(reverse('index'))
        self.assertContains(response, "awesome")


class CommentViewTests(TestCase):
    def test_the_creation_of_a_new_comment(self):
        """Confirms the created topic and comment appear in the details view."""
        stub_comment()
        response = self.client.get(reverse('details', kwargs={'topic_id': 1}))
        self.assertContains(response, "How awesome")
        self.assertContains(response, "bacon covered in bacon!")


    def test_a_404_error_if_the_topic_does_not_exist(self):
        """Confirms the user gets a 404 error if they go to an invalid topic ID."""
        stub_comment()
        response = self.client.get(reverse('details', kwargs={'topic_id': 42}))
        self.assertEqual(response.status_code, 404)
