
import pytest

from hypothesis import assume, settings, given, strategies as st
import radixsort
import bucketsort
import combsort
import countingsort
import heapsort
import insertionsort
import mergesort
import quicksort
import selectstatistic


@settings(max_examples=100)
@given(s=st.lists(st.integers(min_value=0, max_value=1000), min_size=0, max_size=100))
def test_radixsort(s):
    assert sorted(s) == radixsort.radixsort(s)


@settings(max_examples=100)
@given(s=st.lists(st.integers(min_value=-1000, max_value=1000), min_size=0, max_size=100))
def test_bucketsort(s):
    assert sorted(s) == bucketsort.bucketsort(s)


@settings(max_examples=100)
@given(s=st.lists(st.integers(min_value=-1000, max_value=1000), min_size=0, max_size=100))
def test_combsort(s):
    assert sorted(s) == combsort.combsort(s)


@settings(max_examples=100)
@given(s=st.lists(st.integers(min_value=-1000, max_value=1000), min_size=0, max_size=100))
def test_countingsort(s):
    assert sorted(s) == countingsort.countingsort(s)


@settings(max_examples=100)
@given(s=st.lists(st.integers(min_value=-1000, max_value=1000), min_size=0, max_size=100))
def test_insertionsort(s):
    assert sorted(s) == insertionsort.insertionsort(s)


@settings(max_examples=100)
@given(s=st.lists(st.integers(min_value=-1000, max_value=1000), min_size=0, max_size=100))
def test_mergesort(s):
    assert sorted(s) == mergesort.mergesort(s)


@settings(max_examples=100)
@given(s=st.lists(st.integers(min_value=-1000, max_value=1000), min_size=0, max_size=100))
def test_heapsort(s):
    assert sorted(s) == heapsort.heapsort(s)


@settings(max_examples=100)
@given(s=st.lists(st.integers(min_value=-1000, max_value=1000), min_size=0, max_size=100))
def test_quicksort(s):
    assert sorted(s) == quicksort.quicksort(s)


@pytest.mark.xfail(raises=ValueError)
@settings(max_examples=100)
@given(s=st.lists(st.integers(min_value=-1000, max_value=1000), min_size=0, max_size=100),
       stat=st.integers(min_value=1, max_value=10))
def test_selectstat(s, stat):
    assume(stat <= len(s) - 1)
    try:
        selectstatistic.select_statistic(s, stat)
    except ValueError:
        assert True
    if not s:
        assert [] == selectstatistic.select_statistic(s, stat)
    else:
        assert sorted(s)[stat] == selectstatistic.select_statistic(s, stat)
