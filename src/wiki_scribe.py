import json
from dataclasses import dataclass
from enum import Enum
from typing import List

class DraftStatus(str, Enum):
    DRAFT = "draft"
    NEEDS_REVIEW = "needs review"
    APPROVED = "approved"
    REJECTED = "rejected"

@dataclass
class Draft:
    id: int
    title: str
    status: DraftStatus

class WikiScribe:
    def __init__(self):
        self.drafts = []
        self.maintainer_email = "maintainer@example.com"

    def add_draft(self, draft: Draft):
        self.drafts.append(draft)

    def get_drafts_needing_review(self) -> List[Draft]:
        return [draft for draft in self.drafts if draft.status in (DraftStatus.DRAFT, DraftStatus.NEEDS_REVIEW)]

    def approve_draft(self, draft_id: int):
        for draft in self.drafts:
            if draft.id == draft_id:
                draft.status = DraftStatus.APPROVED
                self.send_notification(f"Draft {draft.title} approved")
                return
        raise ValueError("Draft not found")

    def reject_draft(self, draft_id: int):
        for draft in self.drafts:
            if draft.id == draft_id:
                draft.status = DraftStatus.REJECTED
                self.send_notification(f"Draft {draft.title} rejected")
                return
        raise ValueError("Draft not found")

    def send_notification(self, message: str):
        # Simulate sending an email notification
        print(f"Sending email to {self.maintainer_email}: {message}")

def main():
    wiki_scribe = WikiScribe()
    draft1 = Draft(1, "Draft 1", DraftStatus.DRAFT)
    draft2 = Draft(2, "Draft 2", DraftStatus.NEEDS_REVIEW)
    wiki_scribe.add_draft(draft1)
    wiki_scribe.add_draft(draft2)
    print(wiki_scribe.get_drafts_needing_review())
    wiki_scribe.approve_draft(1)
    wiki_scribe.reject_draft(2)

if __name__ == "__main__":
    main()
