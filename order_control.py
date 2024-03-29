from statemachine import StateMachine, State


class OrderControl(StateMachine):
    waiting_for_payment = State(initial=True)
    processing = State()
    shipping = State()
    completed = State(final=True)

    add_to_order = waiting_for_payment.to(waiting_for_payment)
    receive_payment = waiting_for_payment.to(
        processing, cond="payments_enough"
    ) | waiting_for_payment.to(waiting_for_payment, unless="payments_enough")
    process_order = processing.to(shipping, cond="payment_received")
    ship_order = shipping.to(completed)

    def __init__(self):
        self.order_total = 0
        self.payments = []
        self.payment_received = False
        super(OrderControl, self).__init__()

    def payments_enough(self, amount):
        return sum(self.payments) + amount >= self.order_total

    def before_add_to_order(self, amount):
        self.order_total += amount
        return self.order_total

    def before_receive_payment(self, amount):
        self.payments.append(amount)
        return self.payments

    def after_receive_payment(self):
        self.payment_received = True

    def on_enter_waiting_for_payment(self):
        self.payment_received = False


control = OrderControl()
control.add_to_order(3)
control.add_to_order(7)
control.receive_payment(4)
control.receive_payment(6)
print(control.current_state.name)
print(control.current_state.id)
print(control.order_total)
print(control.payments)
print(control.process_order())
print(control.ship_order())
print(control.payment_received)
print(control.order_total)
