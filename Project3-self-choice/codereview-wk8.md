

within my system, i have utilised a dictionary as a data structure in order to represent the typical statistics of an 'entity'.
the reasoning behind this is that, some creatures may not posess every stat, but still require stats for calculations - so, it makes it easier to search for a stat, by its common tag (e.g: int, str, cha, dex) than by itering through a list that may be missing attributes.

in my code review i was shown an alternative to how i am presently storing attacks for an entity. presently i am just using a list; but that presents the issue that i may have multiple instances of the same ability.
Using a 'set' would solve this issue, but it means that i wouldnt be able to reiterate abilities for different weapons. 

due to the improvement of my code, i'm going to implement the set, and find a new solution to finding unique stuff