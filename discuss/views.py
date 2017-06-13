from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Topic

def index(request):
    """ Lists all topics by title. """
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'discuss/index.html', context)


def details(request, topic_id):
    """Presents the description and comments
    for a selected topic.
    """
    try:
        topic = Topic.objects.get(pk=topic_id)
        comments = topic.comment_set.all()
    except Topic.DoesNotExist:
        raise Http404("The topic does not exist")
    return render(request, 'discuss/details.html', {
        'topic': topic,
        'comments': comments
    })


def new_topic(request):
    """Called via a POST on the index page
    to add a new topic.
    """
    title = request.POST['title']
    description = request.POST['description']

    Topic.objects.create_topic(title, description)
    return HttpResponseRedirect(reverse('index'))


def new_comment(request, topic_id):
    """Called via a POST on the details page
    to add a new comment.
    """
    topic = get_object_or_404(Topic, pk=topic_id)
    comment_text = request.POST['comment_text']

    topic.comment_set.create(comment_text=comment_text)
    return HttpResponseRedirect(reverse('details', kwargs={'topic_id': topic.id}))
