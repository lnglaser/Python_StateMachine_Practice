from statemachine import StateMachine, State


class CampaignMachine(StateMachine):
    draft = State("Draft", initial=True, value=1)
    producing = State("Being produced", value=2)
    closed = State("Closed", final=True)

    add_job = draft.to.itself() | producing.to.itself() | closed.to(producing)
    produce = draft.to(producing)
    deliver = producing.to(closed)
