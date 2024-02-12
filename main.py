from statemachine import StateMachine, State


class LightBulb(StateMachine):

    # creating states
    offState = State("off", initial=True)
    onState = State("on")

    # transitions of the state
    switchOn = offState.to(onState)
    switchOff = onState.to(offState)


bulb = LightBulb()
print(bulb.current_state)

a = [s.id for s in bulb.states]
print(a)

b = [s.id for s in bulb.transitions]
print(b)
