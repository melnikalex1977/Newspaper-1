from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from django.utils.decorators import method_decorator
from django.views import View

from .models import Redactor, Newspaper, Topic
from .forms import (RedactorCreationForm,
                    RedactorLicenseUpdateForm,
                    NewspaperForm, RedactorSearchForm,
                    NewspaperSearchForm,
                    TopicSearchForm
                    )


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "newspaper/topic_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TopicSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Topic.objects.all()
        form = TopicSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newspaper:topic-list")


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    title = Newspaper
    context_object_name = "newspaper_list"
    template_name = "newspaper/newspaper_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = NewspaperSearchForm(
            initial={"title": title}
        )
        return context

    def get_queryset(self):
        queryset = Newspaper.objects.all().select_related("topic")
        form = NewspaperSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(title__icontains=form.cleaned_data["title"])
        return queryset


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("newspaper:newspaper-list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RedactorListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = RedactorSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Redactor.objects.all().prefetch_related("newspapers__topic")
        form = RedactorSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.all().prefetch_related("newspapers__topic")


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm


class RedactorLicenseUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorLicenseUpdateForm
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("newspaper:redactor-list")


@method_decorator(login_required, name='dispatch')
class ToggleAssignToNewspaperView(View):
    def post(self, request, pk):
        redactor = Redactor.objects.post(id=request.user.id)
        if Newspaper.objects.filter(id=pk, redactors=redactor).exists():
            redactor.newspapers.remove(pk)
        else:
            redactor.newspapers.add(pk)
        return HttpResponseRedirect(
            reverse_lazy
            ("newspaper:newspaper-detail", args=[pk])
        )


class Index(View):
    def get(self, request):
        num_redactors = Redactor.objects.count()
        num_newspapers = Newspaper.objects.count()
        num_topics = Topic.objects.count()

        num_visits = request.session.get("num_visits", 0)
        request.session["num_visits"] = num_visits + 1

        context = {
            "num_redactors": num_redactors,
            "num_newspapers": num_newspapers,
            "num_topics": num_topics,
            "num_visits": num_visits + 1,
        }

        return render(request, "newspaper/index.html", context=context)
