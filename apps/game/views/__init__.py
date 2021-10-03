from django.views.generic import TemplateView


class GameIndexView(TemplateView):
    template_name = "game/index.html"
