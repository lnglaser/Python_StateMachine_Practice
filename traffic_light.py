import random
from statemachine import StateMachine, State


class TrafficLightMachine(StateMachine):
    green = State(initial=True)
    yellow = State()
    red = State()

    cycle = green.to(yellow) | yellow.to(red) | red.to(green)


def before_cycle(self, event: str, source: State, target: State, message: str = ""):
    message = ". " + message if message else ""
    return f"Running {event} from {source.id} to {target.id}{message}"


def on_enter_red(self):
    print("Don't move.")


def on_exit_red(self):
    print("Go ahead.")


sm = TrafficLightMachine()
randomizer = random.randint(1, 3)

print(sm.send("cycle", message="Fart sound"))

for i in range(randomizer):
    sm.send("cycle")
    print(sm.current_state.id)


if sm.current_state.id == "green":
    on_exit_red(self=any)
elif sm.current_state.id == "red":
    on_enter_red(self=any)
