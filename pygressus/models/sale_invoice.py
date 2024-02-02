from dataclasses import dataclass
from typing import Optional

@dataclass()
class SaleInvoice:
    invoice_source: str
    items: list[object]

    id: Optional[int]
    uuid: Optional[str]
    entity_id: Optional[int]
    entity : Optional[object]
    invoice_date: Optional[str]
    invoice_type: Optional[str]
    delivery_method: Optional[str]
    invoice_send_date_time: Optional[str]
    invoice_due_date: Optional[str]
    invoice_reminded_date_time: Optional[str]
    invoice_num_reminders_send: Optional[int]
    invoice_next_due_date: Optional[str]
    invoice_status: Optional[str]
    invoice_reference: Optional[str]
    invoice_number: Optional[str]
    member_id: Optional[int]
    collection_id: Optional[int]
    contribution_start: Optional[str]
    contribution_end: Optional[str]
    use_direct_debit: Optional[bool]
    invoice_workflow_id: Optional[int]
    addressee: Optional[str]
    addressee_attention: Optional[str]
    email: Optional[str]
    address: Optional[list[object]]
    payments: Optional[list[object]]
    price_inclusive_vat: Optional[object]
    price_exclusive_vat: Optional[object]
    vat: Optional[object]
    price_paid: Optional[object]
    price_unpaid: Optional[object]
    currency: Optional[object]
    created: Optional[str]
    modified: Optional[str]
