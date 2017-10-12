from django.utils.translation import ugettext_lazy as _
from django.views import generic

from adhocracy4.categories import filters as category_filters
from adhocracy4.filters import filters as a4_filters
from adhocracy4.rules import mixins as rules_mixins
from meinberlin.apps.contrib import filters
from meinberlin.apps.exports import views as export_views
from meinberlin.apps.ideas import views as idea_views

from . import forms
from . import models


def get_ordering_choices(request):
    choices = (('-created', _('Most recent')),)
    if request.module.has_feature('rate', models.Proposal):
        choices += ('-positive_rating_count', _('Most popular')),
    choices += ('-comment_count', _('Most commented')),
    return choices


class ProposalFilterSet(a4_filters.DefaultsFilterSet):
    defaults = {
        'ordering': '-created'
    }
    category = category_filters.CategoryFilter()
    ordering = filters.OrderingFilter(
        choices=get_ordering_choices
    )

    class Meta:
        model = models.Proposal
        fields = ['category']


class ProposalExportView(export_views.ItemExportView,
                         export_views.ItemExportWithRatesMixin,
                         export_views.ItemExportWithCommentCountMixin,
                         export_views.ItemExportWithCommentsMixin,
                         export_views.ItemExportWithLocationMixin):
    model = models.Proposal
    fields = ['name', 'description', 'creator', 'created', 'budget',
              'creator_contribution']

    def get_queryset(self):
        return super().get_queryset() \
            .filter(module=self.module)\
            .annotate_comment_count()\
            .annotate_positive_rating_count()\
            .annotate_negative_rating_count()


class ProposalListView(idea_views.AbstractIdeaListView):
    model = models.Proposal
    filter_set = ProposalFilterSet
    exports = [(_('Proposals with comments'), ProposalExportView)]

    def dispatch(self, request, **kwargs):
        self.mode = request.GET.get('mode', 'map')
        if self.mode == 'map':
            self.paginate_by = 0
        return super().dispatch(request, **kwargs)

    def get_queryset(self):
        return super().get_queryset() \
            .filter(module=self.module) \
            .annotate_positive_rating_count() \
            .annotate_negative_rating_count() \
            .annotate_comment_count()


class ProposalDetailView(idea_views.AbstractIdeaDetailView):
    model = models.Proposal
    queryset = models.Proposal.objects.annotate_positive_rating_count()\
        .annotate_negative_rating_count()
    permission_required = 'meinberlin_kiezkasse.view_proposal'


class ProposalCreateView(idea_views.AbstractIdeaCreateView):
    model = models.Proposal
    form_class = forms.ProposalForm
    permission_required = 'meinberlin_kiezkasse.add_proposal'
    template_name = 'meinberlin_kiezkasse/proposal_create_form.html'


class ProposalUpdateView(idea_views.AbstractIdeaUpdateView):
    model = models.Proposal
    form_class = forms.ProposalForm
    permission_required = 'meinberlin_kiezkasse.change_proposal'
    template_name = 'meinberlin_kiezkasse/proposal_update_form.html'


class ProposalDeleteView(idea_views.AbstractIdeaDeleteView):
    model = models.Proposal
    success_message = _('Your budget request has been deleted')
    permission_required = 'meinberlin_kiezkasse.change_proposal'
    template_name = 'meinberlin_kiezkasse/proposal_confirm_delete.html'


class ProposalModerateView(rules_mixins.PermissionRequiredMixin,
                           generic.UpdateView):
    model = models.Proposal
    form_class = forms.ProposalModerateForm
    permission_required = 'meinberlin_kiezkasse.moderate_proposal'
    template_name = 'meinberlin_kiezkasse/proposal_moderate_form.html'

    def get_success_url(self):
        return self.get_object().get_absolute_url()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['item'] = self.object
        kwargs['creator'] = self.request.user
        return kwargs
