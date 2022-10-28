# fmt: off

from typing import Union

VALID_EVENTS = {
    # Core product analytics
    #
    # Generally you will want to categorize your events here.
    #
    # These are for usages of the product that we want to explicitly always
    # track. These events should likely also be tracked in external services
    # such as Amplitude.
    #
    # A good question to ask yourself to decide if a event falls into this
    # category is "would these be part of an event funnel that I would like to
    # understand?"
    "active_release_notification.sent": {
        "organization_id": int,
        "project_id": int,
        "group_id": int,
        "providers": str,
        "release_version": str,
        "recipient_email": str,
        "recipient_username": str,
        "suspect_committer_ids": list,
        "code_owner_ids": list,
        "team_ids": list,
    },
    "alert_details.viewed": {
        "alert_id": int,
        "org_id": int,
    },
    "alert_stream.viewed": {
        "org_id": int,
        "status": str,
    },
    "alert_stream.documentation_clicked": {
        "org_id": int,
        "user_id": int,
    },
    "alert_chooser_flow.select": {
        "org_id": int,
        "type": str,
        "granularity": str,
    },
    "alert_chooser_cards.select": {
        "org_id": int,
        "type": str,
    },
    "alert_builder.filter": {
        "org_id": int,
        "query": str,
    },
    "alert_wizard.option_selected": {
        "org_id": int,
        "alert_type": str,
    },
    "alert_wizard.option_viewed": {
        "org_id": int,
        "alert_type": str,
    },
    "am_beta.learn_more_clicked": {
        "org_id": int,
    },
    "am_beta.viewed": {
        "org_id": int,
    },
    "am_beta_modal.docs_clicked": {
        "org_id": int,
    },
    "assistant.guide_cued": {
        "guide": str,
        "cue": str,
        "org_id": int,
    },
    "assistant.guide_opened": {
        "guide": str,
    },
    "assistant.guide_dismissed": {
        "guide": str,
        "step": int,
        "org_id": int,
    },
    "assistant.guide_finished": {
        "guide": str,
        "useful": bool,
        "org_id": int,
    },
    "business_landing.viewed": {
        "org_id": int,
        "plan": str,
        "source": str,
        "is_modal": bool,
        "is_trial": bool,
        "has_permissions": bool,
        "initial_feature": str,
    },
    "business_landing.clicked": {
        "org_id": int,
        "plan": str,
        "source": str,
        "is_modal": bool,
        "is_trial": bool,
        "type": str,
    },
    "business_landing.closed": {
        "org_id": int,
        "plan": str,
        "source": str,
        "is_modal": bool,
        "is_trial": bool,
        "closing_feature": str,
    },
    "checkout.click_continue": {
        "step_number": int,
        "plan": str,
    },
    "checkout.change_plan": {
        "plan": str,
    },
    "checkout.change_contract": {
        "plan": str,
    },
    "checkout.ondemand_changed": {
        "cents": int,
        "plan": str,
    },
    "checkout.ondemand_budget.turned_off": {
        "org_id": int,
    },
    "checkout.ondemand_budget.update": {
        "org_id": int,
        # current budget
        "strategy": str,
        "total_budget": int,
        "error_budget": int,
        "transaction_budget": int,
        "attachment_budget": int,
        # previous budget
        "previous_strategy": str,
        "previous_total_budget": int,
        "previous_error_budget": int,
        "previous_transaction_budget": int,
        "previous_attachment_budget": int,
    },
    "checkout.step_activated": {
        "org_id": int,
        "step": int,
        "step_name": str,
        "current_plan": str,
        "plan": str,
        "plan_tier": str,
        "ondemand_max_spend": int,
        "session_id": str,
    },
    "checkout.viewed": {
        "org_id": int,
        "current_plan": str,
        "session_id": str,
    },
    "checkout.transactions_upgrade": {
        "org_id": int,
        "transactions": int,
        "previous_transactions": int,
    },
    "checkout.upgrade": {
        "org_id": int,
        "plan": str,
        "errors": int,
        "transactions": int,
        "attachments": int,
        "previous_plan": str,
        "previous_errors": int,
        "previous_transactions": int,
        "previous_attachments": int,
    },
    "command_palette.open": {},
    "dateselector.utc_changed": {
        "utc": bool,
        "path": str,
        "org_id": int,
    },
    "dateselector.time_changed": {
        "time": str,
        "field_changed": str,
        "path": str,
        "org_id": int,
    },
    # Track the redirects from deprecated URLs to newer URLs
    "deprecated_urls.redirect": {
        "feature": str,
        "url": str,  # the URL being redirected from
        "org_id": int
    },
    # Track deprecated features
    "deprecated.feature": {
        "feature": str,
        "url": str,  # optional
        "org_id": int
    },
    "dashboards2.edit.start": {
        "org_id": int,
    },
    "dashboards2.edit.cancel": {
        "org_id": int,
    },
    "dashboards2.edit.complete": {
        "org_id": int,
    },
    "dashboards2.create.start": {
        "org_id": int,
    },
    "dashboards2.create.cancel": {
        "org_id": int,
    },
    "dashboards2.create.complete": {
        "org_id": int,
    },
    "dashboards2.delete": {
        "org_id": int,
        "dashboard_id": str,
    },
    "dashboards2.widget.change_source": {
        "org_id": int,
        "source": str,
    },
    "dashboards2.view": {
        "org_id": int,
        "dashboard_id": str,
    },
    "dashboards2.tablewidget.open_in_discover": {
        "org_id": int,
    },
    "dashboards_manage.change_sort": {
        "org_id": int,
        "sort": str,
    },
    "dashboards_manage.search": {
        "org_id": int,
    },
    "dashboards_manage.paginate": {
        "org_id": int,
    },
    "dashboards_manage.delete": {
        "org_id": int,
        "dashboard_id": str,
    },
    "dashboards_manage.duplicate": {
        "org_id": int,
        "dashboard_id": str,
    },
    "dashboards_manage.create.start": {
        "org_id": int,
    },
    "dashboards_manage.templates.add": {
        "org_id": int,
        "dashboard_id": str,
        "was_previewed": bool,
    },
    "dashboards_manage.templates.toggle": {
        "org_id": int,
        "show_templates": bool,
    },
    "dashboards_manage.templates.preview": {
        "org_id": int,
        "dashboard_id": str,
    },
    "dashboards_views.add_widget_modal.opened": {
        "org_id": int,
    },
    "dashboards_views.add_widget_modal.change": {
        "org_id": int,
        "from": str,
        "field": str,
        "value": str,
        "widget_type": str,
    },
    "dashboards_views.edit_widget_modal.opened": {
        "org_id": int,
    },
    "dashboards_views.add_widget_modal.confirm": {
        "org_id": int,
    },
    "dashboards_views.edit_widget_modal.confirm": {
        "org_id": int,
    },
    "dashboards_views.widget_builder.change": {
        "org_id": int,
        "field": str,
        "from": str,
        "value": str,
        "widget_type": str,
        "new_widget": bool,
    },
    "dashboards_views.widget_builder.opened": {
        "org_id": int,
        "new_widget": bool,
    },
    "dashboards_views.widget_builder.save": {
        "org_id": int,
        "data_set": str,
        "new_widget": bool,
    },
    "dashboards_views.query_selector.opened": {
        "org_id": int,
        "widget_type": str,
    },
    "dashboards_views.query_selector.selected": {
        "org_id": int,
        "widget_type": str,
    },
    "dashboards_views.open_in_discover.opened": {
        "org_id": int,
        "widget_type": str,
    },
    "dashboards_views.widget_library.add": {
        "org_id": int,
        "num_widgets": int,
    },
    "dashboards_views.widget_library.add_widget": {
        "org_id": int,
        "title": str,
    },
    "dashboards_views.widget_library.switch_tab": {
        "org_id": int,
        "to": str,
    },
    "dashboards_views.widget_library.opened": {
        "org_id": int,
    },
    'dashboards_views.widget_viewer.edit': {
        "org_id": int,
        "display_type": str,
        "widget_type": str,
    },
    'dashboards_views.widget_viewer.open': {
        "org_id": int,
        "display_type": str,
        "widget_type": str,
    },
    'dashboards_views.widget_viewer.open_source': {
        "org_id": int,
        "display_type": str,
        "widget_type": str,
    },
    'dashboards_views.widget_viewer.paginate': {
        "org_id": int,
        "display_type": str,
        "widget_type": str,
    },
    'dashboards_views.widget_viewer.select_query': {
        "org_id": int,
        "display_type": str,
        "widget_type": str,
    },
    'dashboards_views.widget_viewer.sort': {
        "org_id": int,
        "display_type": str,
        "widget_type": str,
        "column": str,
        "order": str,
    },
    'dashboards_views.widget_viewer.toggle_legend': {
        "org_id": int,
        "display_type": str,
        "widget_type": str,
    },
    'dashboards_views.widget_viewer.zoom': {
        "org_id": int,
        "display_type": str,
        "widget_type": str,
    },
    "discover_search.failed": {
        "org_id": int,
        "search_type": str,
        "search_source": str,
        "error": str,
    },
    "discover_v2.add_equation": {
        "org_id": int,
    },
    "discover_v2.change_sort": {
        "org_id": int,
        "sort": str,
    },
    "discover_v2.delete_query_failed": {
        "error": str,
        "fields": list,
        "org_id": int,
        "projects": list,
        "query": str,
    },
    "discover_v2.delete_query_request": {
        "fields": list,
        "org_id": int,
        "projects": list,
        "query": str,
    },
    "discover_v2.delete_query_success": {
        "fields": list,
        "org_id": int,
        "projects": list,
        "query": str,
    },
    "discover_v2.prebuilt_query_click": {
        "org_id": int,
        "query_name": str,
    },
    "discover_v2.build_new_query": {
        "org_id": int,
    },
    "discover_v2.update_query_failed": {
        "error": str,
        "fields": list,
        "org_id": int,
        "projects": list,
        "query": str,
    },
    "discover_v2.update_query_request": {
        "fields": list,
        "org_id": int,
        "projects": list,
        "query": str,
    },
    "discover_v2.update_query_success": {
        "fields": list,
        "org_id": int,
        "projects": list,
        "query": str,
    },
    "discover_v2.update_query_name_request": {
        "fields": list,
        "org_id": int,
        "projects": list,
        "query": str,
    },
    "discover_v2.update_query_name_success": {
        "fields": list,
        "org_id": int,
        "projects": list,
        "query": str,
    },
    "discover_v2.saved_query_click": {
        "org_id": int,
    },
    "discover_v2.saved_query.search": {
        "org_id": int,
    },
    "discover_v2.save_new_query_request": {
        "fields": list,
        "org_id": int,
        "projects": list,
        "query": str,
    },
    "discover_v2.save_new_query_success": {
        "fields": list,
        "org_id": int,
        "projects": list,
        "query": str,
    },
    "discover_v2.save_new_query_failed": {
        "fields": list,
        "org_id": int,
        "projects": list,
        "query": str,
        "error": str,
    },
    "discover_v2.results.download_csv": {
        "org_id": int,
    },
    "discover_v2.results.drilldown": {
        "org_id": int,
    },
    "discover_v2.results.cellaction": {
        "org_id": int,
        "action": str,
    },
    "discover_v2.results.toggle_tag_facets": {
        "org_id": int,
    },
    "discover_v2.y_axis_change": {
        "org_id": int,
        "y_axis_value": str,
    },
    "discover_v2.facet_map.clicked": {
        "tag": str,
        "org_id": int,
    },
    "discover_v2.event_details": {
        "event_type": str,
        "org_id": int,
    },
    "discover_v2.opt_out": {
        "org_id": int,
        "user_id": int,
    },
    "discover_v2.opt_in": {
        "org_id": int,
        "user_id": int,
    },
    "discover_v2.column_editor.open": {
        "org_id": int,
    },
    "discover_v2.update_columns": {
        "org_id": int,
    },
    "discover_v2.tour.start": {
        "org_id": int,
    },
    "discover_v2.tour.advance": {
        "org_id": int,
        "step": int,
        "duration": int,
    },
    "discover_v2.tour.close": {
        "org_id": int,
        "step": int,
        "duration": int,
    },
    "discover_views.add_to_dashboard.modal_open": {
        "org_id": int,
        "saved_query": bool,
    },
    "discover_views.add_to_dashboard.confirm": {
        "org_id": int,
    },
    "environmentselector.toggle": {
        "action": str,
        "path": str,
        "org_id": int,
    },
    "environmentselector.update": {
        "count": int,
        "path": str,
        "org_id": int,
    },
    "environmentselector.clear": {
        "path": str,
        "org_id": int,
    },
    "environmentselector.direct_selection": {
        "path": str,
        "org_id": int,
    },
    "event_cause.viewed": {
        "org_id": int,
        "project_id": int,
    },
    "event_cause.docs_clicked": {
        "org_id": int,
        "project_id": int,
    },
    "event_cause.snoozed": {
        "org_id": int,
        "project_id": int,
    },
    "event_cause.dismissed": {
        "org_id": int,
        "project_id": int,
    },
    "experiment.installation_instructions": {
        "integration": str,
        "experiment": bool,
    },
    "feature.discard_group.modal_opened": {
        "org_id": int,
    },
    "feature.auth_provider.upgrade_clicked": {
        "org_id": int,
        "provider": str,
        "plan": str,
    },
    "feature.custom_inbound_filters.upgrade_clicked": {
        "org_id": int,
        "plan": str,
    },
    "feature.data_forwarding.upgrade_clicked": {
        "org_id": int,
        "plan": str,
    },
    "feature.discard_group.upgrade_clicked": {
        "org_id": int,
        "plan": str,
    },
    "feature.rate_limits.upgrade_clicked": {
        "org_id": int,
        "plan": str,
    },
    "feature.auth_provider.upgrade_viewed": {
        "org_id": int,
        "provider": str,
        "plan": str,
    },
    "feature.custom_inbound_filters.trial_viewed": {
        "org_id": int,
        "plan": str,
    },
    "feature.data_forwarding.trial_viewed": {
        "org_id": int,
        "plan": str,
    },
    "feature.discard_group.trial_viewed": {
        "org_id": int,
        "plan": str,
    },
    "feature.rate_limits.trial_viewed": {
        "org_id": int,
        "plan": str,
    },
    "feature.custom_inbound_filters.upgrade_viewed": {
        "org_id": int,
        "plan": str,
    },
    "feature.data_forwarding.upgrade_viewed": {
        "org_id": int,
        "plan": str,
    },
    "feature.discard_group.upgrade_viewed": {
        "org_id": int,
        "plan": str,
    },
    "feature.rate_limits.upgrade_viewed": {
        "org_id": int,
        "plan": str,
    },
    "feature.custom_inbound_filters.learn_more_clicked": {
        "org_id": int,
    },
    "feature.data_forwarding.learn_more_clicked": {
        "org_id": int,
    },
    "feature.discard_group.learn_more_clicked": {
        "org_id": int,
    },
    "feature.rate_limits.learn_more_clicked": {
        "org_id": int,
    },
    "trial_ended_notice.dismissed_understood": {
        "org_id": int,
    },
    "trial_ended_notice.dismissed_upgrade": {
        "org_id": int,
    },
    "grace_period_modal.seen": {
        "org_id": int,
    },
    "integrations.index_viewed": {
        "org_id": int,
        "analytics_session_id": str,
        "integrations_installed": int,
        "view": str,
    },
    "integrations.install_modal_opened": {
        "org_id": int,
        "integration": str,
        "integration_type": str,
        "already_installed": bool,
        "analytics_session_id": str,
        "role": str,
        "view": str,
        "integration_status": str,
    },
    "integrations.integration_viewed": {
        "org_id": int,
        "integration": str,
        "analytics_session_id": str,
        "integration_type": str,
        "role": str,
        "integration_status": str,
    },
    "integrations.details_viewed": {
        "org_id": int,
        "integration": str,
        "analytics_session_id": str,
        "integration_type": str,
        "role": str,
        "integration_status": str,
    },
    "integrations.installation_start": {
        "org_id": int,
        "integration": str,
        "analytics_session_id": str,
        "integration_type": str,
        "role": str,
        "integration_status": str,
    },
    "integrations.installation_complete": {
        "org_id": int,
        "integration": str,
        "analytics_session_id": str,
        "integration_type": str,
        "role": str,
        "integration_status": str,
    },
    "integrations.uninstall_clicked": {
        "org_id": int,
        "integration": str,
        "analytics_session_id": str,
        "integration_type": str,
        "role": str,
        "integration_status": str,
    },
    "integrations.uninstall_completed": {
        "org_id": int,
        "integration": str,
        "analytics_session_id": str,
        "integration_type": str,
        "role": str,
        "integration_status": str,
    },
    "integrations.reauth_start": {
        "org_id": int,
        "integration": str,
        "analytics_session_id": str,
        "integration_type": str,
        "role": str,
        "integration_status": str,
    },
    "integrations.reauth_complete": {
        "org_id": int,
        "integration": str,
        "analytics_session_id": str,
        "integration_type": str,
        "role": str,
        "integration_status": str,
    },
    "integrations.enabled": {
        "org_id": int,
        "integration": str,
        "analytics_session_id": str,
        "integration_type": str,
        "role": str,
        "integration_status": str,
        "view": str,
    },
    "integrations.disabled": {
        "org_id": int,
        "integration": str,
        "analytics_session_id": str,
        "integration_type": str,
        "role": str,
        "integration_status": str,
        "view": str,
    },
    "integrations.config_saved": {
        "org_id": int,
        "integration": str,
        "analytics_session_id": str,
        "integration_type": str,
        "role": str,
        "integration_status": str,
        "view": str,
    },
    "integrations.upgrade_plan_modal_opened": {
        "org_id": int,
        "integration": str,
        "analytics_session_id": str,
        "role": str,
        "integration_tab": str,
        "plan": str,
    },
    "integrations.integration_tab_clicked": {
        "org_id": int,
        "integration": str,
        "analytics_session_id": str,
        "integration_type": str,
        "role": str,
        "integration_status": str,
        "view": str,
    },
    "integrations.plugin_add_to_project_clicked": {
        "org_id": int,
        "integration": str,
        "analytics_session_id": str,
        "integration_type": str,
        "role": str,
        "integration_status": str,
        "view": str,
    },
    "integrations.directory_item_searched": {
        "org_id": int,
        "analytics_session_id": str,
        "role": str,
        "view": str,
        "search_term": str,
        "num_results": int,
    },
    "integrations.directory_category_selected": {
        "org_id": int,
        "analytics_session_id": str,
        "role": str,
        "view": str,
        "category": str,
    },
    "integrations.upgrade_clicked": {
        "integration": str,
        "org_id": int,
        "feature": str,
        "plan": str,
    },
    "integrations.upgrade_viewed": {
        "integration": str,
        "org_id": int,
        "feature": str,
        "plan": str,
    },
    "integrations.trial_viewed": {
        "integration": str,
        "org_id": int,
        "feature": str,
        "plan": str,
    },
    "integrations.stacktrace_link_viewed": {
        "org_id": int,
        "view": str,
        "state": str,
        "project_id": int,
        "platform": str,
    },
    "install_prompt.banner_viewed": {
        "org_id": int, "page": str,
    },
    "install_prompt.banner_clicked": {
        "org_id": int, "page": str,
    },
    "invite_modal.opened": {
        "org_id": int,
        "modal_session": str,
        "can_invite": bool,
        "source": str,
    },
    "invite_modal.requests_sent": {
        "org_id": int,
        "modal_session": str,
    },
    "invite_modal.invites_sent": {
        "org_id": int,
        "modal_session": str,
    },
    "invite_modal.add_more": {
        "org_id": int,
        "modal_session": str,
    },
    "invite_modal.closed": {
        "org_id": int,
        "modal_session": str,
    },
    "invite_request.tab_viewed": {
        "org_id": int,
    },
    "invite_request.tab_clicked": {
        "org_id": int,
    },
    "invite_request.page_viewed": {
        "org_id": int,
    },
    "invite_request.approved": {
        "org_id": int,
        "invite_status": str,
        "member_id": int,
    },
    "invite_request.denied": {
        "org_id": int,
        "invite_status": str,
        "member_id": int,
    },
    "issue_details.action_clicked": {
        "org_id": int,
        "group_id": int,
        "issue_category": str,
        "project_id": int,
        "action_type": str,
        "assigned_suggestion_reason": str,
        "alert_date": str,
        "alert_rule_id": str,
        "alert_type": str,
    },
    "issue_details.event_navigation_clicked": {
        "org_id": int,
        "project_id": int,
        "button": str,
    },
    "issue_details.event_json_clicked": {
        "org_id": int,
        "group_id": int,
    },
    "issue_details.suspect_commits": {
        "org_id": int,
        "group_id": int,
        "issue_category": str,
        "project_id": int,
        "count": int,
    },
    "issue_details.tab_changed": {
        "org_id": int,
        "group_id": int,
        "issue_category": str,
        "tab": str,
        "project_id": int,
        "action_type": str,
        "alert_date": str,
        "alert_rule_id": str,
        "alert_type": str,
    },
    "issue_details.performance.autogrouped_siblings_toggle": {
        "org_id": int,
    },
    "issue_details.performance.hidden_spans_expanded": {
        "org_id": int,
    },
    "issue.search_sidebar_clicked": {
        "org_id": int,
    },
    "issue_search.empty": {
        "org_id": int,
        "search_type": str,
        "search_source": str,
        "query": str,
    },
    "issue_search.failed": {
        "org_id": int,
        "search_type": str,
        "search_source": str,
        "error": str,
    },
    "issue_error_banner.viewed": {
        "org_id": int,
        "platform": str,
        "group": str,
        "error_type": list,
        "error_message": list,
    },
    "issue_page.viewed": {
        "org_id": int,
        "project_id": int,
    },
    "issues_tab.viewed": {
        "org_id": int,
        "num_issues": int,
        "num_perf_issues": int,
        "page": int,
        "query": str,
        "tab": str,
    },
    "inbox_tab.clicked": {
        "org_id": int,
    },
    "inbox_tab.issue_clicked": {
        "org_id": int,
        "group_id": str,
    },
    "issue_alert_rule_details.viewed": {
        "org_id": int,
        "rule_id": int,
    },
    "issue_alert_rule_details.edit_clicked": {
        "org_id": int,
        "rule_id": int,
    },
    "issues_stream.issue_clicked": {
        "org_id": int,
        "group_id": str,
        "tab": str,
        "was_shown_suggestion": bool,
    },
    "issues_stream.issue_assigned": {
        "org_id": int,
        "group_id": str,
        "tab": str,
        "was_shown_suggestion": bool,
        "did_assign_suggestion": bool,
        "assigned_suggestion_reason": str,
        "assigned_type": str,
    },
    "issues_stream.paginate": {
        "direction": str,
    },
    "issues_stream.realtime_clicked": {
        "org_id": int,
        "enabled": bool,
    },
    "issues_stream.sort_changed": {
        "org_id": int,
        "sort": str,
    },
    "join_request.viewed": {
        "org_slug": str,
    },
    "member_limit_modal.seen": {
        "org_id": int,
    },
    "membership_limit.trial_viewed": {
        "org_id": int,
        "plan": str,
    },
    "membership_limit.upgrade_clicked": {
        "org_id": int,
        "plan": str,
    },
    "membership_limit.upgrade_viewed": {
        "org_id": int,
        "plan": str,
    },
    "monitor.mark_failed": {
        "org_id": int,
        "monitor_id": int,
        "project_id": int,
    },
    "monitors.page_viewed": {
        "org_id": int,
    },
    "new_project.visited": {
        "org_id": int,
        "alert_defaults_experiment_variant": str,
    },
    "new_project.alert_rule_selected": {
        "org_id": int,
        "project_id": int,
        "rule_type": str,
    },
    "new_alert_rule.viewed": {
        "org_id": int,
        "project_id": int,
        "alert_type": str,
        "duplicate_rule": str,
        "wizard_v3": str,
        "session_id": str,
    },
    "edit_alert_rule.viewed": {
        "org_id": int,
        "project_id": int,
        "alert_type": str,
    },
    "edit_alert_rule.add_row": {
        "org_id": int,
        "project_id": int,
        "type": str,
        "name": str,
    },
    "alert_rule_details.viewed": {
        "org_id": int,
        "project_id": int,
        "rule_id": int,
        "alert": str,
        "has_chartcuterie": str,
    },
    "omnisearch.open": {},
    "onboarding.wizard_opened": {
        "org_id": int,
    },
    "onboarding.wizard_closed": {
        "org_id": int,
    },
    "onboarding.wizard_clicked": {
        "org_id": int,
        "todo_id": str,
        "todo_title": str,
        "action": str,
    },
    "onboarding_v2.step_compete": {
        "org_id": int,
        "step": str,
    },
    "onboarding_v2.skipped": {
        "org_id": int,
    },
    "onboarding_v2.first_event_recieved": {
        "org_id": int,
        "project": str,
    },
    "onboarding_v2.first_transaction_recieved": {
        "org_id": int,
        "project": str,
    },
    "onboarding_v2.setup_choice_selected": {
        "org_id": int,
        "choice": str,
    },
    "onboarding_v2.user_invited": {
        "org_id": int,
        "project": str,
    },
    "onboarding_v2.full_docs_clicked": {
        "org_id": int,
        "project": str,
        "platform": str,
    },
    "ondemand_budget_modal.ondemand_budget.turned_off": {
        "org_id": int,
    },
    "ondemand_budget_modal.ondemand_budget.update": {
        "org_id": int,
        # current budget
        "strategy": str,
        "total_budget": int,
        "error_budget": int,
        "transaction_budget": int,
        "attachment_budget": int,
        # previous budget
        "previous_strategy": str,
        "previous_total_budget": int,
        "previous_error_budget": int,
        "previous_transaction_budget": int,
        "previous_attachment_budget": int,
    },
    "orgdash.resources_shown": {},
    "orgdash.resource_clicked": {
        "link": str,
        "title": str,
    },
    "page_filters.pin_click": {
        "org_id": int,
        "filter": str,
        "pin": bool,
    },
    "past_due_modal.seen": {
        "org_id": int,
    },
    "performance_views.change_view": {
        "org_id": int,
        "view_name": str,
        "project_platforms": str,
    },
    "performance_views.landingv2.content": {
        "org_id": int,
    },
    "performance_views.landingv2.new_landing": {
        "org_id": int,
    },
    "performance_views.landingv2.display_change": {
        "org_id": int,
        "change_to_display": str,
        "default_display": str,
        "current_display": str,
        "is_default": bool,
    },
    "performance_views.landingv2.display.filter_change": {
        "org_id": int,
        "field": str,
        "min_value": int,
        "max_value": int,
    },
    "performance_views.landingv2.transactions.sort": {
        "org_id": int,
        "field": str,
        "direction": str,
    },
    "performance_views.landingv3.widget.interaction": {
        "org_id": int,
        "widget_type": str,
    },
    "performance_views.landingv3.widget.switch": {
        "org_id": int,
        "from_widget": str,
        "to_widget": str,
        "from_default": bool,
    },
    "performance_views.landingv3.widget.add_to_dashboard": {
        "org_id": int,
        "from_widget": str,
    },
    "performance_views.landingv3.batch_queries": {
        "org_id": int,
        "num_collected": int,
        "num_sent": int,
        "num_saved": int,
    },
    "performance_views.landingv3.display_change": {
        "org_id": int,
        "change_to_display": str,
        "default_display": str,
        "current_display": str,
        "is_default": bool,
    },
    "performance_views.landingv3.table_pagination": {
        "org_id": int,
        "direction": str,
    },
    "performance_views.overview.view": {
        "org_id": int,
        "project_platforms": str,
    },
    "performance_views.overview.sort": {
        "org_id": int,
        "field": str,
    },
    "performance_views.overview.navigate.summary": {
        "org_id": int,
        "project_platforms": str,
    },
    "performance_views.overview.search": {
        "org_id": int,
    },
    "performance_views.overview.change_chart": {
        "org_id": int,
        "metric": str,
    },
    "performance_views.overview.cellaction": {
        "org_id": int,
        "action": str,
    },
    "performance_views.project_transaction_threshold.change": {
        "org_id": int,
        "from": str,
        "to": str,
        "key": str,
    },
    "performance_views.project_transaction_threshold.clear": {
        "org_id": int,
    },
    "performance_views.latency_chart.zoom": {
        "org_id": int,
    },
    "performance_views.summary.view_in_discover": {
        "org_id": int,
    },
    "performance_views.summary.view_details": {
        "org_id": int,
    },
    "performance_views.summary.open_issues": {
        "org_id": int,
    },
    "performance_views.summary.tag_explorer.cell_action": {
        "org_id": int,
    },
    "performance_views.summary.tag_explorer.change_page": {
        "org_id": int,
    },
    "performance_views.summary.tag_explorer.sort": {
        "org_id": int,
        "field": str,
        "direction": str,
    },
    "performance_views.summary.tag_explorer.tag_value": {
        "org_id": int,
    },
    "performance_views.summary.tag_explorer.visit_tag_key": {
        "org_id": int,
    },
    "performance_views.summary.view_in_transaction_events": {
        "org_id": int,
    },
    "performance_views.key_transactions.add": {
        "org_id": int,
    },
    "performance_views.tags.change_tag": {
        "org_id": int,
        "from_tag": str,
        "to_tag": str,
        "is_other_tag": bool
    },
    "performance_views.tags.tags_tab_clicked": {
        "org_id": int,
        "project_platforms": str,
    },
    "performance_views.tags.interaction": {
        "org_id": int,
    },
    "performance_views.tags.jump_to_release": {
        "org_id": int,
    },
    "performance_views.trends.compare_baselines": {
        "org_id": int,
    },
    "performance_views.trends.change_function": {
        "org_id": int,
        "function_name": str,
    },
    "performance_views.trends.change_parameter": {
        "org_id": int,
        "parameter_name": str,
    },
    "performance_views.trends.hide_transaction": {
        "org_id": int,
        "confidence_level": str,
    },
    "performance_views.trends.summary": {
        "org_id": int,
        "confidence_level": str,
    },
    "performance_views.trends.widget_interaction": {
        "org_id": int,
        "widget_type": str,
    },
    "performance_views.trends.widget_pagination": {
        "org_id": int,
        "direction": str,
        "widget_type": str,
    },
    "performance_views.trends.change_duration": {
        "org_id": int,
        "value": str,
        "widget_type": str,
    },
    "performance_views.tour.start": {
        "org_id": int,
    },
    "performance_views.tour.advance": {
        "org_id": int,
        "step": int,
        "duration": int,
    },
    "performance_views.tour.close": {
        "org_id": int,
        "step": int,
        "duration": int,
    },
    "performance_views.key_transaction.toggle": {
        "org_id": int,
        "action": str,
    },
    "performance_views.vitals.vitals_tab_clicked": {
        "org_id": int,
        "project_platforms": str,
    },
    "performance_views.vitals.reset_view": {
        "org_id": int,
    },
    "performance_views.vitals.filter_changed": {
        "org_id": int,
        "value": str,
    },
    "performance_views.vitals.open_in_discover": {
        "org_id": int,
        "vital": str,
    },
    "performance_views.filter_dropdown.selection": {
        "org_id": int,
        "action": str,
    },
    "performance_views.relative_breakdown.selection": {
        "org_id": int,
        "action": str,
    },
    "performance_views.events.events_tab_clicked": {
        "org_id": int,
        "project_platforms": str,
    },
    "performance_views.transactionEvents.cellaction": {
        "org_id": int,
        "action": str,
    },
    "performance_views.transactionEvents.sort": {
        "org_id": int,
        "field": str,
        "direction": str,
    },
    "performance_views.transactionEvents.ops_filter_dropdown.selection": {
        "org_id": int,
        "action": str,
    },
    "performance_views.transactionEvents.display_filter_dropdown.selection": {
        "org_id": int,
        "action": str,
    },
    "performance_views.span_summary.change_chart": {
        "org_id": int,
        "change_to_display": str,
    },
    "performance_views.span_summary.view": {
        "org_id": int,
        "project_platforms": str,
    },
    "performance_views.spans.spans_tab_clicked": {
        "org_id": int,
        "project_platforms": str,
    },
    "performance_views.spans.change_op": {
        "org_id": int,
        "operation_name": str,
    },
    "performance_views.spans.change_sort": {
        "org_id": int,
        "sort_column": str,
    },
    "performance_views.vital_detail.switch_vital": {
        "org_id": int,
        "from_vital": str,
        "to_vital": str,
    },
    "performance_views.vital_detail.view": {
        "org_id": int,
        "project_platforms": str,
    },
    "performance_views.trace_view.view": {
        "org_id": int,
    },
    "performance_views.trace_view.open_in_discover": {
        "org_id": int,
    },
    "performance_views.trace_view.open_transaction_details": {
        "org_id": int,
        "operation": str,
        "transaction": str,
    },
    "performance_views.team_key_transaction.set": {
        "org_id": int,
        "action": str,
    },
    "performance_views.transaction_summary.change_chart_display": {
        "org_id": int,
        "from_chart": str,
        "to_chart": str,
    },
    "performance_views.transaction_summary.status_breakdown_click": {
        "org_id": int,
        "status": str
    },
    "performance_views.all_events.open_in_discover": {
        "org_id": int,
    },
    "performance_views.event_details.filter_by_op": {
        "org_id": int,
        "operation": str,
    },
    "performance_views.event_details.search_query": {
        "org_id": int,
    },
    "performance_views.event_details.open_span_details": {
        "org_id": int,
        "operation": str,
    },
    "performance_views.event_details.anchor_span": {
        "org_id": int,
        "span_id": str,
    },
    "performance_views.event_details.json_button_click": {
        "org_id": int,
    },
    "performance_views.anomalies.anomalies_tab_clicked": {
        "org_id": int,
        "project_platforms": str,
    },
    "span_view.embedded_child.hide": {
        "org_id": int,
    },
    "span_view.embedded_child.show": {
        "org_id": int,
    },
    "platformpicker.create_project": {},
    "platformpicker.select_platform": {
        "platform": str,
    },
    "platformpicker.select_tab": {
        "tab": str,
    },
    "projectselector.bookmark_toggle": {
        "org_id": int,
        "bookmarked": bool,
    },
    "projectselector.toggle": {
        "action": str,
        "path": str,
        "org_id": int,
    },
    "projectselector.update": {
        "count": int,
        "path": str,
        "multi": bool,
        "org_id": int,
    },
    "projectselector.clear": {
        "path": str,
        "org_id": int,
    },
    "projectselector.direct_selection": {
        "path": str,
        "org_id": int,
    },
    "power_icon.clicked": {
        "org_id": int,
        "plan": str,
        "source": str,
    },
    "sales.contact_us_clicked": {
        "org_id": int,
        "source": str,
    },
    "quick_trace.connected_services": {
        "org_id": int,
        "projects": int,
    },
    "quick_trace.dropdown.clicked": {
        "org_id": int,
        "node_key": str,
    },
    "quick_trace.dropdown.clicked_extra": {
        "org_id": int,
        "node_key": str,
    },
    "quick_trace.missing_service.docs": {
        "org_id": int,
        "platform": str,
    },
    "quick_trace.missing_service.dismiss": {
        "org_id": int,
        "platform": str,
    },
    "quick_trace.missing_instrumentation.docs": {
        "org_id": int,
        "project_id": int,
        "platform": str,
    },
    "quick_trace.missing_instrumentation.dismiss": {
        "org_id": int,
        "project_id": int,
        "platform": str,
    },
    "quick_trace.missing_instrumentation.snoozed": {
        "org_id": int,
        "project_id": int,
        "platform": str,
    },
    "quick_trace.node.clicked": {
        "org_id": int,
        "node_key": str,
    },
    "quick_trace.trace_id.clicked": {
        "org_id": int,
        "source": str,
    },
    "releases.landing_card_clicked": {
        "org_id": int,
        "project_id": int,
        "step_id": int,
        "step_title": str,
    },
    "releases.landing_card_viewed": {
        "org_id": int,
        "project_id": int,
    },
    "releases.progress_bar_viewed": {
        "org_id": int,
        "project_id": int,
        "steps": list,
        "cta": str,
    },
    "releases.progress_bar_clicked_next": {
        "org_id": int,
        "project_id": int,
        "cta": str,
    },
    "releases.progress_bar_closed": {
        "org_id": int,
        "project_id": int,
        "action": str,
    },
    "releases.tab_viewed": {
        "org_id": int,
        "project_id": int,
    },
    'sampling.settings.modal.recommended.next.steps_back': {
        "project_id": str,
    },
    'sampling.settings.modal.recommended.next.steps_cancel': {
        "project_id": str,
    },
    'sampling.settings.modal.recommended.next.steps_done': {
        "project_id": str,
    },
    'sampling.settings.modal.recommended.next.steps_read_docs': {
        "project_id": str,
    },
    'sampling.settings.modal.specific.rule.condition_add': {
        "conditions": list,
        "project_id": str,
    },
    'sampling.settings.modal.specify.client.rate_cancel': {
        "project_id": str,
    },
    'sampling.settings.modal.specify.client.rate_next': {
        "project_id": str,
    },
    'sampling.settings.modal.specify.client.rate_read_docs': {
        "project_id": str,
    },
    'sampling.settings.modal.uniform.rate_cancel': {
        "project_id": str,
    },
    'sampling.settings.modal.uniform.rate_done': {
        "project_id": str,
    },
    'sampling.settings.modal.uniform.rate_next': {
        "project_id": str,
    },
    'sampling.settings.modal.uniform.rate_read_docs': {
        "project_id": str,
    },
    'sampling.settings.modal.uniform.rate_switch_current': {
        "project_id": str,
    },
    'sampling.settings.modal.uniform.rate_switch_recommended': {
        "project_id": str,
    },
    'sampling.settings.rule.specific_activate': {
        "conditions": list,
        "conditions_stringified": str,
        "project_id": str,
        "sampling_rate": Union[str, None],
    },
    'sampling.settings.rule.specific_create': {
        "conditions": list,
        "conditions_stringified": str,
        "project_id": str,
        "sampling_rate": Union[str, None],
    },
    'sampling.settings.rule.specific_deactivate': {
        "conditions": list,
        "conditions_stringified": str,
        "project_id": str,
        "sampling_rate": Union[str, None],
    },
    'sampling.settings.rule.specific_delete': {
        "conditions": list,
        "conditions_stringified": str,
        "project_id": str,
        "sampling_rate": Union[str, None],
    },
    'sampling.settings.rule.specific_save': {
        "conditions": list,
        "conditions_stringified": str,
        "project_id": str,
        "sampling_rate": Union[str, None],
    },
    'sampling.settings.rule.specific_update': {
        "conditions": list,
        "conditions_stringified": str,
        "project_id": str,
        "sampling_rate": Union[str, None],
        "old_conditions": list,
        "old_conditions_strified": str,
        "old_sampling_rate": Union[str, None],
    },
    'sampling.settings.rule.uniform_activate': {
        "project_id": str,
        "sampling_rate": Union[str, None],
    },
    'sampling.settings.rule.uniform_create': {
        "old_sampling_rate": Union[str, None],
        "project_id": str,
        "sampling_rate": Union[str, None],
    },
    'sampling.settings.rule.uniform_deactivate': {
        "project_id": str,
        "sampling_rate": Union[str, None],
    },
    'sampling.settings.rule.uniform_update': {
        "old_sampling_rate": Union[str, None],
        "project_id": str,
        "sampling_rate": Union[str, None],
    },
    'sampling.settings.view': {
        "project_id": str
    },
    'sampling.settings.view_get_started': {
        "project_id": str,
    },
    'sampling.settings.view_read_docs': {
        "project_id": str,
    },
    "sample_event.created": {
        "org_id": int,
        "project_id": int,
        "source": str,
    },
    "sample_event.failed": {
        "org_id": int,
        "project_id": int,
    },
    "sample_event.button_viewed": {
        "org_id": int,
        "project_id": int,
        "source": str,
    },
    "sample_event.button_viewed2": {
        "org_id": int,
        "project_slug": str,
        "source": str,
    },
    "sdk_updates.seen": {
        "org_id": int,
    },
    "sdk_updates.snoozed": {
        "org_id": int,
    },
    "sdk_updates.clicked": {
        "org_id": int,
    },
    "settings_search.open": {},
    "sidebar_help.open": {},
    "sourcemap.sourcemap_error": {
        "org_id": int,
        "group": str,
        "error_type": list,
    },
    'subscription_page.usagelog_filter.clicked': {
        "org_id": int,
        "selection": str,
    },
    'suspect_resolution.evaluation': {
        "algo_version": str,
        "resolved_group_id": int,
        "candidate_group_id": int,
        "resolved_group_resolution_type": str,
        "pearson_r_coefficient": float,
        "pearson_r_start_time": str,
        "pearson_r_end_time": str,
        "pearson_r_resolution_time": str,
        "is_commit_correlated": bool,
        "resolved_issue_release_ids": list,
        "candidate_issue_release_ids": list,
    },
    "team_insights.viewed": {
        "org_id": int,
    },
    "trial.start_clicked": {
        "org_id": int,
        "source": str,
        "feature": str,
        "plan": str,
        "integration": str,
    },
    "trial.banner_clicked": {
        "org_id": int,
    },
    "trial.request_another_clicked": {
        "org_id": int,
    },
    "usage_exceeded_modal.seen": {
        "org_id": int,
    },
    "user_feedback.viewed": {
        "org_id": int,
        "projects": list,
    },
    "user_feedback.docs_clicked": {
        "org_id": int,
        "projects": list,
    },
    "user_feedback.dialog_opened": {
        "org_id": int,
        "projects": list,
    },
    "zendesk_link.viewed": {
        "org_id": int,
    },
    "zendesk_link.clicked": {
        "org_id": int,
    },

    # Adhoc events
    #
    # These are events that are NOT bounded events, for example search queries
    # or clicking specific results of a search.
    #
    # A good way to determine if an event falls into this category is to ask
    # yourself the following questions:
    #
    # - Is this event going to be high volume?
    # - Does this event contain unstructured data like search queries
    # - Would you explicitly only write SQL queries / JOINs for this data to
    #   get exact numbers? Or is it enough to exist in a tool such as Amplitude
    #   for simple analytic.
    #
    # Otherwise you group your event above as a product analytics.
    "am_checkout.viewed": {
        "org_id": int,
        "user_id": int,
    },
    "checkout.data_sliders_viewed": {
        "org_id": int,
        "user_id": int,
    },
    "checkout.data_slider_changed": {
        "org_id": int,
        "user_id": int,
        "data_type": str,
        "quantity": int,
    },
    "command_palette.query": {
        "query": str,
    },
    "command_palette.select": {
        "query": str,
        "source_type": str,
        "result_type": str,
    },
    "docs.feedback-sent": {
        "useful": int,
    },
    "docs.cookie_consent": {
        "consent": str,
    },
    "omnisearch.query": {
        "query": str,
    },
    "omnisearch.select": {
        "query": str,
        "source_type": str,
        "result_type": str,
    },
    "search.pin": {
        "org_id": int,
        "search_type": str,  # "issues", "events"
        "action": str,  # "pin" or "unpin"
        "query": str,
    },
    "search.autocompleted": {
        "org_id": int,
        "query": str,
        "search_type": str,  # "issues" or "events"
    },
    "search.display_changed": {
        "org_id": int,
    },
    "search.invalid_field": {
        "org_id": int,
        "search_type": str,  # "issues" or "events"
        "search_source": str,  # "recent_search", "search_builder", "main_search",
        "attempted_field_name": str,
    },
    "search.search_with_invalid": {
        "org_id": int,
        "query": str,
        "search_type": str,  # "issues" or "events"
        "search_source": str,  # "recent_search", "search_builder", "main_search"
    },
    "search.searched": {
        "org_id": int,
        "query": str,
        "search_type": str,  # "issues" or "events"
        "search_source": str,  # "recent_search", "search_builder", "main_search",
    },
    "search.shortcut_used": {
        "org_id": int,
        "query": str,
        "search_type": str,  # "issues" or "events"
        "search_source": str,  # "recent_search", "search_builder", "main_search"
        "shortcut_method": str,  # "click" or "hotkey"
        "shortcut_type": str,  # "previous", "next", "negate", "delete"
    },
    "search.operator_autocompleted": {
        "org_id": int,
        "query": str,
        "search_operator": str,
        "search_type": str,
    },
    "tag.clicked": {
        "is_clickable": bool,  # whether the tag is meant to be clickable or not
    },
    "settings_search.select": {
        "query": str,
        "source_type": str,
        "result_type": str,
    },
    "settings_search.query": {
        "query": str,
    },
    "sidebar_help.query": {
        "query": str,
    },
    "organization_saved_search.selected": {
        "org_id": int,
        "query": str,
        "search_type": str,  # "issues" or "events"
        "id": int,  # saved search id
    },
    "platformpicker.search": {
        "query": str,
        "num_results": int,
    },
    "sidebar.item_clicked": {
        "org_id": int,
        "sidebar_item_id": str,
        "dest": str,  # the URL the click will bring you to
    },
}
