from statemachine import StateMachine, State


def _create_q2():
    while True:
        # Wait till the input is received.
        # Once received, store the input in char.
        char = yield

        # depending on what we received as the input,
        # change the current state of the fsm
        if char == "b":
            # on receiving 'b' the state moves to 'q2'
            current_state = q2
        elif char == "c":
            # on receiving 'c' the state moves to 'q3'
            current_state = q3
        else:
            break
