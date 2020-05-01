class DbRouter:
    """A basic class to route any django_q db operation to its own db."""

    def db_for_read(self, model, **hints):
        return select_db_from_model(model)

    def db_for_write(self, model, **hints):
        return select_db_from_model(model)

    def allow_migrate(self, db, app_label, model_name='', **hints):
        if app_label == 'django_q':
            return db == 'django_q'
        return db == 'default'


def select_db_from_model(model):
    if model._meta.app_label == 'django_q':
        return 'django_q'
    return 'default'
