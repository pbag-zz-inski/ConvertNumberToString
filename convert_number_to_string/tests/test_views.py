#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""Klasa testująca widoki."""

from django.test import TestCase
from morelia.decorators import tags


@tags(['unit'])
class NumberToStringJsonViewTest(TestCase):
    u"""Klasa testująca widok number_to_string_json."""

    def test_should_return_string_when_response_is_json(self):
        u"""Test sprawdzający poprawność konwersji z int na string oraz wyświetlenie odpowiedzi w formacie json."""
        pass
