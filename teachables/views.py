from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Topic, Lesson, Step

def home(request):
    topics = Topic.objects.all()
    return render(request, 'home.html', {'topics': topics})

def topic(request, pk):
    topics = Topic.objects.all()
    topic = get_object_or_404(Topic, pk=pk)
    lessons = Lesson.objects.filter(pk=pk)
    return render(request, 'topic.html', {'topic': topic, 'lessons': lessons, 'topics': topics})

def lesson(request, topic_pk, lesson_pk):
    topics = Topic.objects.all()
    topic = get_object_or_404(Topic, pk=topic_pk)
    lesson = get_object_or_404(Lesson, pk=lesson_pk)
    steps = Step.objects.filter(lesson=lesson_pk)
    return render(request, 'lesson.html', {'topic': topic, 'lesson': lesson, 'steps': steps, 'topics': topics})