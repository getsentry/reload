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
    'sample_event.created': {
        'org_id': int,
        'project_id': int,
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
    'sso_paywall.upgrade_clicked': {
        'org_id': int,
        'current_plan': str,
        'exposed': int,
    },
    'sso_paywall.viewed': {
        'org_id': int,
        'current_plan': str,
        'exposed': int,
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
}
