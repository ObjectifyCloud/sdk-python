from __future__ import annotations
from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from objectify.client import ObjectifyClient


class AccountingResource:
    def __init__(self, client: ObjectifyClient):
        self.accounts = _Accounts(client)
        self.ledger = _Ledger(client)
        self.invoices = _Invoices(client)
        self.payments = _Payments(client)
        self.banking = _Banking(client)
        self.reports = _Reports(client)


class _Accounts:
    def __init__(self, c: ObjectifyClient): self._c = c
    def list(self, **p: Any) -> Any: return self._c.get("/v1/accounting/accounts", params=p or None)
    def get(self, id: str) -> Any: return self._c.get(f"/v1/accounting/accounts/{id}")
    def create(self, **d: Any) -> Any: return self._c.post("/v1/accounting/accounts", json=d)
    def update(self, id: str, **d: Any) -> Any: return self._c.patch(f"/v1/accounting/accounts/{id}", json=d)
    def delete(self, id: str) -> Any: return self._c.delete(f"/v1/accounting/accounts/{id}")


class _Ledger:
    def __init__(self, c: ObjectifyClient): self._c = c
    def list(self, **p: Any) -> Any: return self._c.get("/v1/accounting/journal-entries", params=p or None)
    def get(self, id: str) -> Any: return self._c.get(f"/v1/accounting/journal-entries/{id}")
    def create(self, **d: Any) -> Any: return self._c.post("/v1/accounting/journal-entries", json=d)
    def post(self, id: str) -> Any: return self._c.post(f"/v1/accounting/journal-entries/{id}/post")
    def reverse(self, id: str) -> Any: return self._c.post(f"/v1/accounting/journal-entries/{id}/reverse")


class _Invoices:
    def __init__(self, c: ObjectifyClient): self._c = c
    def list(self, **p: Any) -> Any: return self._c.get("/v1/accounting/invoices", params=p or None)
    def get(self, id: str) -> Any: return self._c.get(f"/v1/accounting/invoices/{id}")
    def create(self, **d: Any) -> Any: return self._c.post("/v1/accounting/invoices", json=d)
    def approve(self, id: str) -> Any: return self._c.post(f"/v1/accounting/invoices/{id}/approve")
    def void(self, id: str) -> Any: return self._c.post(f"/v1/accounting/invoices/{id}/void")


class _Payments:
    def __init__(self, c: ObjectifyClient): self._c = c
    def list(self, **p: Any) -> Any: return self._c.get("/v1/accounting/payments", params=p or None)
    def get(self, id: str) -> Any: return self._c.get(f"/v1/accounting/payments/{id}")
    def create(self, **d: Any) -> Any: return self._c.post("/v1/accounting/payments", json=d)
    def void(self, id: str) -> Any: return self._c.post(f"/v1/accounting/payments/{id}/void")


class _Banking:
    def __init__(self, c: ObjectifyClient): self._c = c
    def list_accounts(self) -> Any: return self._c.get("/v1/accounting/bank-accounts")
    def get_account(self, id: str) -> Any: return self._c.get(f"/v1/accounting/bank-accounts/{id}")
    def create_account(self, **d: Any) -> Any: return self._c.post("/v1/accounting/bank-accounts", json=d)
    def list_transactions(self, account_id: str, **p: Any) -> Any: return self._c.get(f"/v1/accounting/bank-accounts/{account_id}/transactions", params=p or None)
    def reconcile(self, account_id: str, **d: Any) -> Any: return self._c.post(f"/v1/accounting/bank-accounts/{account_id}/reconcile", json=d)


class _Reports:
    def __init__(self, c: ObjectifyClient): self._c = c
    def trial_balance(self, **p: Any) -> Any: return self._c.get("/v1/accounting/reports/trial-balance", params=p or None)
    def balance_sheet(self, **p: Any) -> Any: return self._c.get("/v1/accounting/reports/balance-sheet", params=p or None)
    def profit_and_loss(self, **p: Any) -> Any: return self._c.get("/v1/accounting/reports/profit-and-loss", params=p or None)
    def cash_flow(self, **p: Any) -> Any: return self._c.get("/v1/accounting/reports/cash-flow", params=p or None)
    def aged_receivables(self, **p: Any) -> Any: return self._c.get("/v1/accounting/reports/aged-receivables", params=p or None)
    def aged_payables(self, **p: Any) -> Any: return self._c.get("/v1/accounting/reports/aged-payables", params=p or None)
    def general_ledger(self, **p: Any) -> Any: return self._c.get("/v1/accounting/reports/general-ledger", params=p or None)
