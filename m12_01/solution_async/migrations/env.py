from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from src.settings import config as our_config
from src.models import Base

config = context.config

fileConfig(config.config_file_name)

target_metadata = Base.metadata

user = our_config['postgres']['user']
password = our_config['postgres']['password']
host = our_config['postgres']['host']
database = our_config['postgres']['database']

config.set_main_option('sqlalchemy.url', f'postgresql://{user}:{password}@{host}/{database}')


def run_migrations_online() -> None:

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
