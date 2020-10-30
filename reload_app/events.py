# fmt: off
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
    },
    "business_landing.clicked": {
        "org_id": int,
        "plan": str,
        "source": str,
        "is_modal": bool,
        "is_trial": bool,
        "type": str,
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
    "discover.query": {
        "org_id": int,
        "projects": list,
        "fields": list,
        "conditions": list,
        "aggregations": list,
        "orderby": str,
        "limit": int,
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
    "issue.search_sidebar_clicked": {
        "org_id": int,
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
    "orgdash.resources_shown": {},
    "orgdash.resource_clicked": {
        "link": str,
        "title": str,
    },
    "past_due_modal.seen": {
        "org_id": int,
    },
    "performance_views.change_view": {
        "org_id": int,
        "view_name": str,
    },
    "performance_views.overview.view": {
        "org_id": int,
    },
    "performance_views.overview.sort": {
        "org_id": int,
        "field": str,
    },
    "performance_views.overview.navigate.summary": {
        "org_id": int,
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
    "performance_views.key_transactions.add": {
        "org_id": int,
    },
    "performance_views.trends.compare_baselines": {
        "org_id": int,
    },
    "performance_views.trends.change_function": {
        "org_id": int,
        "function_name": str,
    },
    "performance_views.trends.change_confidence": {
        "org_id": int,
        "confidence_level": str,
    },
    "performance_views.trends.hide_transaction": {
        "org_id": int,
        "confidence_level": str,
    },
    "performance_views.trends.summary": {
        "org_id": int,
        "confidence_level": str,
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
    "settings_search.open": {},
    "sidebar_help.open": {},
    "sourcemap.sourcemap_error": {
        "org_id": int,
        "group": str,
        "error_type": list,
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
    "search.searched": {
        "org_id": int,
        "query": str,
        "search_type": str,  # "issues" or "events"
        "search_source": str,  # "recent_search", "search_builder", "main_search",
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
