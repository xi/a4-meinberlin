import json

import pytest
from django.conf import settings

from adhocracy4.exports import unescape_and_strip_html
from meinberlin.apps.plans.exports import DashboardPlanExportView


@pytest.mark.django_db
def test_reply_to_mixin(plan_factory, project_factory,
                        administrative_district):
    export = DashboardPlanExportView()
    virtual = export.get_virtual_fields({})
    # ItemExportWithReferenceNumberMixin and ItemExportWithLinkMixin
    assert 'reference_number' in virtual
    assert 'link' in virtual
    # ExportModelFieldsMixin, set in fields
    assert 'title' in virtual
    assert 'description' in virtual
    assert 'contact' in virtual
    assert 'district' in virtual
    assert 'topics' in virtual
    assert 'cost' in virtual
    assert 'duration' in virtual
    assert 'status' in virtual
    assert 'participation' in virtual
    assert 'organisation' in virtual
    # ItemExportWithLocationMixin
    assert 'location_lon' in virtual
    assert 'location_lat' in virtual
    assert 'location_label' in virtual
    # defined directly in DashboardPlanExportView
    assert 'projects' in virtual
    assert 'projects_links' in virtual
    assert 'created' in virtual
    assert 'modified' in virtual

    plan = plan_factory(point='')

    # ItemExportWithReferenceNumberMixin and ItemExportWithLinkMixin
    assert plan.reference_number == export.get_reference_number_data(plan)
    # ItemExportWithLinkMixin cannot be tested easily (needs a request)
    # and should be tested in a4 anyway

    # ExportModelFieldsMixin, set in fields
    assert str(plan.title) == export.get_field_data(plan, 'title')
    assert plan.topics == export.get_field_data(plan, 'topics')
    assert plan.cost == export.get_field_data(plan, 'cost')
    duration = plan.duration
    if duration is None:
        duration = ''
    assert str(duration) == export.get_field_data(plan, 'duration')
    # get_..._data methods overwritten in DashboardPlanExportView
    assert unescape_and_strip_html(plan.description) \
        == export.get_description_data(plan)
    assert unescape_and_strip_html(plan.contact) \
        == export.get_contact_data(plan)
    district = plan.district.name if plan.district else str('City wide')
    assert district == export.get_district_data(plan)
    assert plan.get_status_display() == export.get_status_data(plan)
    assert plan.get_participation_display() \
        == export.get_participation_data(plan)
    assert plan.organisation.name == export.get_organisation_data(plan)
    # ItemExportWithLocationMixin
    assert '' == export.get_location_lon_data(plan)
    assert '' == export.get_location_lat_data(plan)
    assert plan.point_label == export.get_location_label_data(plan)
    # defined directly in DashboardPlanExportView
    projects = ''
    if plan.projects.all():
        projects = ', \n'.join(
            [project.name for project in plan.projects.all()]
        )
    assert projects == export.get_projects_data(plan)

    assert plan.created.strftime('%X %x') == export.get_created_data(plan)
    assert plan.modified.strftime('%X %x') == export.get_modified_data(plan)

    choices = settings.A4_PROJECT_TOPICS
    project_1 = project_factory()
    project_2 = project_factory()
    plan = plan_factory(
        contact='<i>me@example.com</i>',
        description='this is a description<br>with a newline',
        topics=choices[0][0],
        status=0,
        participation=2,
        duration='1 month',
        projects=[project_1, project_2],
        district=administrative_district,
        point=json.loads('{"type":"Feature","properties":{},'
                         '"geometry":{"type":"Point",'
                         '"coordinates":[13.382721,52.512121]}}')
    )

    # ItemExportWithReferenceNumberMixin and ItemExportWithLinkMixin
    assert plan.reference_number == export.get_reference_number_data(plan)
    # ItemExportWithLinkMixin cannot be tested easily (needs a request)
    # and should be tested in a4 anyway

    # ExportModelFieldsMixin, set in fields
    assert str(plan.title) == export.get_field_data(plan, 'title')
    assert plan.topics == export.get_field_data(plan, 'topics')
    assert plan.cost == export.get_field_data(plan, 'cost')
    duration = plan.duration
    if duration is None:
        duration = ''
    assert str(duration) == export.get_field_data(plan, 'duration')
    # get_..._data methods overwritten in DashboardPlanExportView
    assert unescape_and_strip_html(plan.description) \
        == export.get_description_data(plan)
    assert unescape_and_strip_html(plan.contact) \
        == export.get_contact_data(plan)
    district = plan.district.name if plan.district else str('City wide')
    assert district == export.get_district_data(plan)
    assert plan.get_status_display() == export.get_status_data(plan)
    assert plan.get_participation_display() \
        == export.get_participation_data(plan)
    assert plan.organisation.name == export.get_organisation_data(plan)
    # ItemExportWithLocationMixin
    assert 13.382721 == export.get_location_lon_data(plan)
    assert 52.512121 == export.get_location_lat_data(plan)
    assert plan.point_label == export.get_location_label_data(plan)
    # defined directly in DashboardPlanExportView
    projects = ''
    if plan.projects.all():
        projects = ', \n'.join(
            [project.name for project in plan.projects.all()]
        )
    assert projects == export.get_projects_data(plan)

    assert plan.created.strftime('%X %x') == export.get_created_data(plan)
    assert plan.modified.strftime('%X %x') == export.get_modified_data(plan)
