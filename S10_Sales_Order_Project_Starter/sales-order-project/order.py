"""One sales order's data and related behavior."""

from pricing import calculate_final_total, classify_order


class SalesOrder:
    """Represent one order, not the whole list of orders."""

    def __init__(self, order_id, unit_price, quantity, discount_pct, tax_pct):
        # TODO 1: Save all five arguments as attributes of this instance.
        # Use self so two SalesOrder objects keep their own values.
        raise NotImplementedError("Complete SalesOrder.__init__ in order.py")

    def final_total(self):
        # TODO 2: Return the result of calculate_final_total using this
        # object's four numeric attributes. Do not copy the formula here.
        raise NotImplementedError("Complete SalesOrder.final_total in order.py")

    def band(self):
        # TODO 3: Return classify_order applied to this object's final total.
        raise NotImplementedError("Complete SalesOrder.band in order.py")
