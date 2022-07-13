"""
outcome_surveys Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import PluginSignals


class OutcomeSurveysConfig(AppConfig):
    """
    Configuration for the outcome_surveys Django application.
    """

    name = 'outcome_surveys'
    label = 'outcome_surveys'
    verbose_name = "Outcome Surveys"
    plugin_app = {
        PluginSignals.CONFIG: {
            'lms.djangoapp': {
                PluginSignals.RECEIVERS: [
                    {
                        PluginSignals.SIGNAL_PATH: 'lms.djangoapps.grades.signals.signals'
                                                   '.SCHEDULE_FOLLOW_UP_SEGMENT_EVENT_FOR_COURSE_PASSED_FIRST_TIME',
                        PluginSignals.RECEIVER_FUNC_NAME: 'handle_segment_event_fired_for_learner_passed_course_first_time',
                    },
                ],
            },
        },
    }
