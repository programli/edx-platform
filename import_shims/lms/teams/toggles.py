from import_shims.warn import warn_deprecated_import

warn_deprecated_import('teams.toggles', 'lms.djangoapps.teams.toggles')

from lms.djangoapps.teams.toggles import *
