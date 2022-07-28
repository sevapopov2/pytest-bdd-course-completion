Feature: Cucumber Basket
    Scenario: Add cucumbers to a basket
        Given the basket has "2" cucumbers
        When "4" cucumbers are added to the basket
        Then the basket contains "6" cucumbers
