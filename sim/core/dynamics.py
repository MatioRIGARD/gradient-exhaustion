"""Main loop: reinvestment and endogenous entry/exit.

The feedback loop of the model: capture -> revenue -> reinvestment -> better
capture. Agents whose revenue falls below their participation cost leave the
market; entrants appear where profit remains. Human market exit is the observed
variable and must never be forced. See §2.2. Implemented in T3.3.
"""
