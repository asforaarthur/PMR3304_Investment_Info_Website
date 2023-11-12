from django.forms import ModelForm
from .models import Investment, Comentario


class InvestmentForm(ModelForm):
    class Meta:
        model = Investment
        fields = [
            "name",
            "categoria",
            "image_url",
            "texto",
        ]
        labels = {
            "name": "Título",
            "categoria": "Categoria de Investimento",
            "image_url": "URL da Imagem",
            "texto": "Texto"
        }


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = [
            "author",
            "text",
        ]
        labels = {
            "author": "Usuário",
            "text": "Comentário",
        }
