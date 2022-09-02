Feature: DuckDuckGo Instant Answer API

  Scenario Outline: Basic DuckDuckGo API Query
    Given the DuckDuckGo API is queried with "<phrase>"
    Then the response status code is "200"
    And the response contains results for "<phrase>"

    Examples: Distros
      | phrase |
      | ubuntu |
      | arch   |
      | fedora |
