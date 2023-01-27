from .models import Item

class InventoryRouter:
    """Currently Item is the only model in the checkoutcalculator app, so we
    just need to check for the app label. If we want to check for the Item
    model, check isinstance(model, Item) in db_for_read/write methods and
    model_name.lower() == "item" in the 3rd and 4th methods
    """
    route_app_labels = {"checkoutcalculator"}
    # route_models = {"item"}
    inventory_db_str = "inventory"
    default_db_str = "default"

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self.inventory_db_str
        return self.default_db_str

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self.inventory_db_str
        return self.default_db_str

    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label in self.route_app_labels
            and obj2._meta.app_label in self.route_app_labels):
            return True
        return None  # no opinion on other cases

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        relevant_app = app_label in self.route_app_labels
        relevant_db = db == self.inventory_db_str
        if relevant_app or relevant_db:
            return relevant_app and relevant_db
        return None  # no opinion on other cases