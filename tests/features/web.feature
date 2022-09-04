Feature: DuckDuckGo Web Browsing

  Background: 
    Given the DuckDuckGo home page is displayed

  Scenario: Basic DuckDuckGo search
    When the user searches for "espeak"
    Then results are shown for "espeak"
