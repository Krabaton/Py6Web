from logging.config import fileConfig
from sqlalchemy import create_engine
from alembic import context

from src.store.models import db
from src.store.accessor import DBAccessor
from src.settings import config as app_config

config = context.config
fileConfig(config.config_file_name)
target_metadata = db


def run_migrations_online() -> None:
    DBAccessor()

    connectable = create_engine(app_config["postgres"]["database_url"])

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
