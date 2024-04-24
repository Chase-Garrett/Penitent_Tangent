#!/usr/bin/env python3

from django import forms

class BotForm(forms.Form):
    url = forms.CharField()
