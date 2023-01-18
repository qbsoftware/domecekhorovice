class OldRouter:
    app_label = "old"
    db_name = "old"

    def db_for_read(self, model, **hints):
        if model._meta.app_label == self.app_label:
            return self.db_name

    def db_for_write(self, model, **hints):
        if model._meta.app_label == self.app_label:
            return self.db_name

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label == self.app_label
            or obj2._meta.app_label == self.app_label
        ):
            return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == self.app_label:
            return db == self.db_name
