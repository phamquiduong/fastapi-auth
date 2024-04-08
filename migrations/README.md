# Generic single-database configuration.

### Create a Migration Script
```
alembic revision -m "migration_name"
```

### Running our First Migration
```
alembic upgrade head
```

### Downgrading
```
alembic downgrade migration_name
```
