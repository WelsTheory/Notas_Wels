from django import forms
from .models import Post, Tag


class PostForm(forms.ModelForm):
    tags_input = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'ej: motivación, negocios, filosofía',
            'class': 'w-full bg-transparent outline-none text-sm text-gray-300 placeholder-gray-600',
        }),
        label='Etiquetas (separadas por comas)',
    )

    class Meta:
        model = Post
        fields = ['text', 'author', 'link', 'source', 'source_custom']
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Pega aquí el texto del post...',
                'rows': 6,
                'class': 'w-full bg-transparent outline-none resize-none text-gray-100 placeholder-gray-600 text-base leading-relaxed',
            }),
            'author': forms.TextInput(attrs={
                'placeholder': 'Nombre del autor',
                'class': 'w-full bg-transparent outline-none text-sm text-gray-300 placeholder-gray-600',
            }),
            'link': forms.URLInput(attrs={
                'placeholder': 'https://enlace-original.com (opcional)',
                'class': 'w-full bg-transparent outline-none text-sm text-gray-300 placeholder-gray-600',
            }),
            'source': forms.Select(attrs={
                'class': 'bg-gray-800 border border-gray-700 text-gray-300 text-sm rounded-lg px-3 py-2 outline-none',
            }),
            'source_custom': forms.TextInput(attrs={
                'placeholder': 'Especifica la fuente',
                'class': 'w-full bg-transparent outline-none text-sm text-gray-300 placeholder-gray-600',
            }),
        }
        labels = {
            'text': 'Texto del post',
            'author': 'Autor',
            'link': 'Enlace original',
            'source': 'Red social / Fuente',
            'source_custom': 'Especificar fuente',
        }

    def save(self, commit=True):
        post = super().save(commit=commit)
        if commit:
            tags_raw = self.cleaned_data.get('tags_input', '')
            post.tags.clear()
            for tag_name in [t.strip().lower() for t in tags_raw.split(',') if t.strip()]:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)
        return post
