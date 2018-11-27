VALID_EVENTS = {
    'assistant.search': {
        'query': str,
    },
    'assistant.guide_cued': {
        'guide': int,
        'cue': str,
        'org_id': int,
    },
    'assistant.guide_opened': {
        'guide': int,
    },
    'assistant.guide_dismissed': {
        'guide': int,
        'step': int,
    },
    'assistant.guide_finished': {
        'guide': int,
        'useful': bool,
    },
    'assistant.support': {
        'subject': str,
    },
    'command_palette.open': {
    },
    'command_palette.select': {
        'query': str,
    },
    'command_palette.query': {
        'query': str,
    },
    'dateselector.utc_changed': {
        'utc': bool,
    },
    'dateselector.time_changed': {
        'time': str,
        'field_changed': str,
    },
    'discover.query': {
        'org_id': int,
        'projects': list,
        'fields': list,
        'conditions': list,
        'aggregations': list,
        'orderby': str,
        'limit': int,
    },
    'docs.feedback-sent': {
        'useful': int,
    },
    'experiment.installation_instructions': {
        'integration': str,
        'experiment': bool,
    },
    'feature.rate_limits.upgrade_clicked': {
        'org_id': int,
    },
    'feature.data_forwarding.upgrade_clicked': {
        'org_id': int,
    },
    'feature.discard_group.upgrade_clicked': {
        'org_id': int,
    },
    'feature.custom_inbound_filters.upgrade_clicked': {
        'org_id': int,
    },
    'feature.auth_provider.upgrade_clicked': {
        'org_id': int,
        'provider': str,
    },
    'integrations.index_viewed': {
        'org_id': int,
    },
    'integrations.install_modal_opened': {
        'org_id': int,
        'integration': str,
    },
    'integrations.details_viewed': {
        'org_id': int,
        'integration': str,
    },
    'integrations.upgrade_clicked': {
        'integration': str,
        'org_id': int,
        'feature': str,
        'plan': str,
    },
    'install_prompt.banner_viewed': {
        'org_id': int,
        'page': str,
    },
    'install_prompt.banner_clicked': {
        'org_id': int,
        'page': str,
    },
    'issue.search': {
        'query': str,
    },
    'issue_error_banner.viewed': {
        'org_id': int,
        'platform': str,
        'group': str,
        'error_type': list,
        'error_message': list,
    },
    'issue_page.viewed': {
        'group_id': int,
        'org_id': int,
        'project_id': int,
    },
    'membership_limit.upgrade_clicked': {
        'org_id': int,
    },
    'omnisearch.open': {
    },
    'omnisearch.select': {
        'query': str,
    },
    'omnisearch.query': {
        'query': str,
    },
    'onboarding.complete': {
        'project': str,
    },
    'onboarding.wizard_opened': {
        'org_id': int,
    },
    'onboarding.wizard_closed': {
        'org_id': int,
    },
    'onboarding.wizard_clicked': {
        'org_id': int,
        'todo_id': int,
        'todo_title': str,
        'action': str,
    },
    'onboarding.show_instructions': {
        'project': str,
    },
    'orgdash.resources_shown': {
    },
    'orgdash.resource_clicked': {
        'link': str,
        'title': str,
    },
    'platformpicker.search': {
        'query': str,
        'num_results': int,
    },
    'platformpicker.create_project': {
    },
    'platformpicker.select_platform': {
        'platform': str,
    },
    'platformpicker.select_tab': {
        'tab': str,
    },
    'releases.landing_card_clicked': {
        'org_id': int,
        'project_id': int,
        'step_id': int,
        'step_title': str,
    },
    'releases.landing_card_viewed': {
        'org_id': int,
        'project_id': int,
    },
    'releases.progress_bar_viewed': {
        'org_id': int,
        'project_id': int,
        'steps': list,
    },
    'releases.progress_bar_clicked_next': {
        'org_id': int,
        'project_id': int,
        'cta': str,
    },
    'releases.progress_bar_closed': {
        'org_id': int,
        'project_id': int,
        'action': str,
    },
    'releases.tab_viewed': {
        'org_id': int,
        'project_id': int,
    },
    'sample_event.created': {
        'org_id': int,
        'project_id': int,
        'source': str,
    },
    'sample_event.button_viewed': {
        'org_id': int,
        'project_id': int,
        'source': str,
    },
    'sample_event.button_viewed2': {
        'org_id': int,
        'project_slug': str,
        'source': str,
    },
    'settings_search.open': {
    },
    'settings_search.select': {
        'query': str,
    },
    'settings_search.query': {
        'query': str,
    },
    'sidebar_help.open': {
    },
    'sidebar_help.query': {
        'query': str,
    },
    'sourcemap.sourcemap_error': {
        'org_id': int,
        'group': str,
        'error_type': list,
    },
    'trial.banner_clicked': {
        'org_id': int,
    },
}
