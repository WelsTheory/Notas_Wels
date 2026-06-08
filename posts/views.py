import random
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from .models import Post, Tag
from .forms import PostForm


MOTIVATIONAL_NOTES = [
    "Lo que guardas hoy se convierte en sabiduría mañana.",
    "Cada nota es una semilla. Sigue plantando.",
    "Leer es respirar. Guardar es recordar.",
    "Las mejores ideas merecen un lugar seguro.",
    "Vuelve a leer lo que alguna vez te inspiró.",
    "Tu colección de ideas dice mucho de quién eres.",
    "Un buen texto leído dos veces vale el doble.",
    "Guardar es un acto de intención.",
    "Las palabras de otros pueden iluminar tu propio camino.",
    "Construyes quién eres con lo que decides leer y recordar.",
    "Pequeñas notas, grandes transformaciones.",
    "Lo que te mueve merece no ser olvidado.",
    "Cada autor que guardas es una conversación que continúa.",
    "Tus notas son un mapa de lo que te importa.",
    "El conocimiento guardado es el que realmente se queda.",
]

def dashboard(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PostForm()
    note = random.choice(MOTIVATIONAL_NOTES)
    return render(request, 'posts/dashboard.html', {'motivational_note': note, 'form': form})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})


def random_post(request):
    ids = list(Post.objects.values_list('id', flat=True))
    if not ids:
        return render(request, 'posts/random_post.html', {'post': None})
    post = Post.objects.prefetch_related('tags').get(id=random.choice(ids))
    return render(request, 'posts/random_post.html', {'post': post})


def search(request):
    query = request.GET.get('q', '').strip()
    source_filter = request.GET.get('source', '').strip()
    tag_filter = request.GET.get('tag', '').strip()

    posts = Post.objects.prefetch_related('tags').all()

    if query:
        posts = posts.filter(
            Q(text__icontains=query) |
            Q(author__icontains=query) |
            Q(source_custom__icontains=query)
        )
    if source_filter:
        posts = posts.filter(source=source_filter)
    if tag_filter:
        posts = posts.filter(tags__name__iexact=tag_filter)

    all_tags = Tag.objects.all().order_by('name')
    context = {
        'posts': posts,
        'query': query,
        'source_filter': source_filter,
        'tag_filter': tag_filter,
        'source_choices': Post.SOCIAL_CHOICES,
        'all_tags': all_tags,
        'count': posts.count(),
    }
    return render(request, 'posts/search.html', context)


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('dashboard')
    return render(request, 'posts/confirm_delete.html', {'post': post})
