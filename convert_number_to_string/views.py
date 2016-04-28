#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""Widok aplikacji convert_number_to_string."""

import json
import inflect
from django.http import HttpResponse


def convert_number_to_string_json(request, number):
    u"""Widok zwracający liczbę jako tekst w formacie json."""

    items = {}
    convert_engine = inflect.engine()
    items[number] = convert_engine.number_to_words(number)
    return HttpResponse(json.dumps(items), content_type='application/json')
