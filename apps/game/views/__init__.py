from django.views.generic import TemplateView


class GameIndex(TemplateView):
    template_name = "game/index.html"
