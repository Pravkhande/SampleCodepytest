import pytest
#print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

from page.result import DuckDuckGoResultPage
from page.search import DuckDuckGoSearchPage

def test_basic_duckduckgo_search(browser):
  # Set up test case data
  PHRASE = 'panda'

  # Search for the phrase
  search_page = DuckDuckGoSearchPage(browser)
  search_page.load()
  search_page.search(PHRASE)

  # Verify that results appear
  result_page = DuckDuckGoResultPage(browser)
  assert result_page.link_div_count() > 0
  assert result_page.phrase_result_count(PHRASE) > 0
  assert result_page.search_input_value() == PHRASE
