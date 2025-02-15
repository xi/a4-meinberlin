import json

import pytest
from django.urls import reverse

from adhocracy4.dashboard import components
from adhocracy4.test.helpers import assert_template_response
from adhocracy4.test.helpers import redirect_target
from adhocracy4.test.helpers import setup_phase
from meinberlin.apps.maptopicprio.models import MapTopic
from meinberlin.apps.maptopicprio.phases import PrioritizePhase

component = components.modules.get("map_topic_edit")


@pytest.mark.django_db
def test_edit_view(client, phase_factory, maptopic_factory, area_settings_factory):
    phase, module, project, item = setup_phase(
        phase_factory, maptopic_factory, PrioritizePhase
    )
    initiator = module.project.organisation.initiators.first()
    area_settings_factory(module=module)
    url = component.get_base_url(module)
    client.login(username=initiator.email, password="password")
    response = client.get(url)
    assert_template_response(
        response, "meinberlin_maptopicprio/maptopic_dashboard_list.html"
    )


@pytest.mark.django_db
def test_maptopic_create_view(
    client, phase_factory, category_factory, area_settings_factory
):
    phase, module, project, item = setup_phase(phase_factory, None, PrioritizePhase)
    area_settings_factory(module=module)
    initiator = module.project.organisation.initiators.first()
    category = category_factory(module=module)
    url = reverse("a4dashboard:maptopic-create", kwargs={"module_slug": module.slug})
    data = {
        "name": "name",
        "description": "dec",
        "category": category.pk,
        "point": '{ "type":"Feature", "geometry":{ "type":"Point",'
        '"coordinates":[ 13.0, 52.0 ] }, "properties":{}}',
        "point_label": "test",
    }
    client.login(username=initiator.email, password="password")
    response = client.post(url, data)
    assert redirect_target(response) == "maptopic-list"
    topic = MapTopic.objects.get(name=data.get("name"))
    assert topic.description == data.get("description")
    assert topic.category.pk == data.get("category")
    assert topic.point == json.loads(data.get("point"))
    assert topic.point_label == data.get("point_label")


@pytest.mark.django_db
def test_maptopic_update_view(
    client, phase_factory, maptopic_factory, category_factory, area_settings_factory
):
    phase, module, project, item = setup_phase(
        phase_factory, maptopic_factory, PrioritizePhase
    )
    initiator = module.project.organisation.initiators.first()
    area_settings_factory(module=module)
    category = category_factory(module=module)
    url = reverse(
        "a4dashboard:maptopic-update", kwargs={"pk": item.pk, "year": item.created.year}
    )
    data = {
        "name": "name",
        "description": "desc",
        "category": category.pk,
        "point": '{ "type":"Feature", "geometry":{ "type":"Point",'
        '"coordinates":[ 13.0, 52.0 ] }, "properties":{}}',
        "point_label": "test",
    }
    client.login(username=initiator.email, password="password")
    response = client.post(url, data)
    assert redirect_target(response) == "maptopic-list"
    item.refresh_from_db()
    assert item.description == data.get("description")
    assert item.category.pk == data.get("category")
    assert item.point == json.loads(data.get("point"))
    assert item.point_label == data.get("point_label")


@pytest.mark.django_db
def test_maptopic_delete_view(
    client, phase_factory, maptopic_factory, area_settings_factory
):
    phase, module, project, item = setup_phase(
        phase_factory, maptopic_factory, PrioritizePhase
    )
    initiator = module.project.organisation.initiators.first()
    area_settings_factory(module=module)
    url = reverse(
        "a4dashboard:maptopic-delete", kwargs={"pk": item.pk, "year": item.created.year}
    )
    client.login(username=initiator.email, password="password")
    response = client.delete(url)
    assert redirect_target(response) == "maptopic-list"
    assert not MapTopic.objects.exists()
