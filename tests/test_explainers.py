import pytest
from src import explainers


def test_explain_spike_contains_date():
    txt = explainers.explain_spike('2024-01-03')
    assert '2024-01-03' in txt


def test_explain_idle_contains_fields():
    row = {'resource_id':'r1','service_name':'Storage','region':'us-east','cost_per_day':1.23,'usage_per_day':0.01}
    txt = explainers.explain_idle(row)
    assert 'r1' in txt
    assert 'Storage' in txt
    assert '0.01' in txt
