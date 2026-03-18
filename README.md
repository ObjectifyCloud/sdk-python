# objectify-sdk

Python SDK for the [Objectify](https://objectify.cloud) multi-tenant Objects Platform API.

## Installation

```bash
pip install objectify-sdk
```

## Quick Start

```python
from objectify import ObjectifyClient

client = ObjectifyClient(api_key="your-api-key")

# List object types
types = client.schema.list_types()

# Create an object
obj = client.objects.create("type-id", {"name": "Hello", "email": "hello@example.com"})

# Search
results = client.search.search("type-id", filters=[
    {"property": "status", "operator": "eq", "value": "active"}
])
```

## Async Usage

```python
from objectify import AsyncObjectifyClient

async with AsyncObjectifyClient(api_key="your-key") as client:
    types = await client.get("/schema/types")
```

## Authentication

```python
# API Key
client = ObjectifyClient(api_key="obj_...")

# Owner JWT
client = ObjectifyClient(jwt="eyJ...")

# Admin key
client = ObjectifyClient(admin_key="your-admin-key")
```

## Resources

- `client.schema` — list_types, get_type, create_type, properties CRUD
- `client.objects` — list, get, create, update, delete, batch, trash, restore, versions
- `client.search` — search, aggregate
- `client.files` — get, update, delete, search, signed_url, batch
- `client.auth` — signup, login, logout, refresh, mfa, sessions, passkeys
- `client.admin.tenants` — CRUD, migrate, set_plan, suspend, analytics, sql
- `client.admin.keys` — list, create, revoke, rotate
- `client.admin.users` — CRUD
- `client.admin.webhooks` — CRUD, test
- `client.accounting.*` — accounts, ledger, invoices, payments, banking, reports
- `client.ai` — chat, generate, embeddings, search, moderate, auto_tag, summarise
- `client.owner` — login, signup, profile, mfa, tenants
- `client.reports` — pipeline, timeseries, leaderboard, funnel

## Error Handling

```python
from objectify import ObjectifyError, NotFoundError

try:
    client.objects.get("type-id", "nonexistent")
except NotFoundError:
    print("Object not found")
except ObjectifyError as e:
    print(f"{e.status} {e.code}: {e}")
```

## License

MIT
