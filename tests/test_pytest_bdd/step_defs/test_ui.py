import pytest

from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/ui_scenarios.feature')