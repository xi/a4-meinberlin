import rules

from adhocracy4.modules import predicates as module_predicates

rules.add_perm(
    'meinberlin_offlineevents.view_offlineevent',
    module_predicates.is_allowed_view_item
)

rules.add_perm(
    'meinberlin_offlineevents.add_offlineevent',
    module_predicates.is_project_admin
)

rules.add_perm(
    'meinberlin_offlineevents.change_offlineevent',
    module_predicates.is_project_admin
)


rules.add_perm(
    'meinberlin_offlineevents.delete_offlineevent',
    module_predicates.is_project_admin
)
