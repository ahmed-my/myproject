from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.http import JsonResponse
from django.utils.timezone import now
from .models import Fitness, Image, Lesson, Course, Home, Article, Tip, Quote, Tool, ToolClick
from django.views.decorators.csrf import csrf_exempt
from posts.models import Post


def fitness_home(request):
    fitness = Fitness.objects.all()
    articles = Article.objects.all().order_by('-published_date')
    tips = Tip.objects.all().order_by('order')
    quotes = Quote.objects.all()

    context = {
        'fitness': fitness,
        'articles': articles,
        'tips': tips,
        'quotes': quotes,
    }
    return render(request, 'fitness/fitness_home.html', context)

# New article_detail view
def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    context = {
        'article': article,
    }
    return render(request, 'fitness/article_detail.html', context)

def search(request):
    query = request.GET.get('q')
    if query:
        fitness_results = Fitness.objects.filter(name__icontains=query)
        article_results = Article.objects.filter(title__icontains=query)
        tip_results = Tip.objects.filter(title__icontains=query)
        quote_results = Quote.objects.filter(content__icontains=query)
    else:
        fitness_results = Fitness.objects.none()
        article_results = Article.objects.filter()
        tip_results = Tip.objects.filter()
        quote_results = Quote.objects.filter()

    context = {
        'query': query,
        'fitness': fitness_results,
        'articles': article_results,
        'tips': tip_results,
        'Quotes': quote_results,
    }
    return render(request, 'fitness/search_results.html', context)

def lesson_page(request, param):
    posts = Post.objects.all()
    lessons = Lesson.objects.all()
    courses = Course.objects.all()
    lesson = get_object_or_404(Lesson, slug=param)
    context = {
        'posts': posts,
        'lessons': lessons,
        'courses': courses,
        'lesson': lesson
    }
    return render(request, 'fitness/lesson_page.html', context)

def course_page(request, param):
    posts = Post.objects.all()
    courses = Course.objects.all()
    lessons = Lesson.objects.all()
    course = get_object_or_404(Course, slug=param)
    context = {
        'posts': posts,
        'courses': courses,
        'lessons': lessons,
        'course': course
    }
    return render(request, 'fitness/course_page.html', context)

def tools_view(request):
    tools = Tool.objects.all()
    context = {
        'tools': tools
    }
    return render(request, 'fitness/tools.html', context)


@csrf_exempt
def ajax_track_tool_click(request):
    if request.method == 'POST':
        tool_name = request.POST.get('tool_name')
        ip = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT')

        ToolClick.objects.create(
            tool_name=tool_name,
            ip_address=ip,
            user_agent=user_agent
        )
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)


def tools_click_stats(request):
    # Aggregate click counts for each tool
    data = ToolClick.objects.values('tool_name').annotate(total=Count('id')).order_by('-total')[:5]
    labels = [entry['tool_name'] for entry in data]
    counts = [entry['total'] for entry in data]
    return JsonResponse({
        'labels': labels,
        'counts': counts
    })