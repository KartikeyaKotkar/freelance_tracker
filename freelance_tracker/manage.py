#!/usr/bin/env python
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freelance_tracker.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # If the import fails, it could be because Django is not installed.
        # Make sure it's installed and available in the current environment.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
