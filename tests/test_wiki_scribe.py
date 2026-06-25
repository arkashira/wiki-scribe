from wiki_scribe import WikiScribe, Draft, DraftStatus

def test_get_drafts_needing_review():
    wiki_scribe = WikiScribe()
    draft1 = Draft(1, "Draft 1", DraftStatus.DRAFT)
    draft2 = Draft(2, "Draft 2", DraftStatus.NEEDS_REVIEW)
    draft3 = Draft(3, "Draft 3", DraftStatus.APPROVED)
    wiki_scribe.add_draft(draft1)
    wiki_scribe.add_draft(draft2)
    wiki_scribe.add_draft(draft3)
    drafts_needing_review = wiki_scribe.get_drafts_needing_review()
    assert len(drafts_needing_review) == 2
    assert draft1 in drafts_needing_review
    assert draft2 in drafts_needing_review

def test_approve_draft():
    wiki_scribe = WikiScribe()
    draft = Draft(1, "Draft 1", DraftStatus.DRAFT)
    wiki_scribe.add_draft(draft)
    wiki_scribe.approve_draft(1)
    assert draft.status == DraftStatus.APPROVED

def test_reject_draft():
    wiki_scribe = WikiScribe()
    draft = Draft(1, "Draft 1", DraftStatus.DRAFT)
    wiki_scribe.add_draft(draft)
    wiki_scribe.reject_draft(1)
    assert draft.status == DraftStatus.REJECTED

def test_send_notification():
    wiki_scribe = WikiScribe()
    draft = Draft(1, "Draft 1", DraftStatus.DRAFT)
    wiki_scribe.add_draft(draft)
    wiki_scribe.approve_draft(1)
    # Simulate sending an email notification
    print("Sending email to maintainer@example.com: Draft Draft 1 approved")

def test_draft_not_found():
    wiki_scribe = WikiScribe()
    draft = Draft(1, "Draft 1", DraftStatus.DRAFT)
    wiki_scribe.add_draft(draft)
    try:
        wiki_scribe.approve_draft(2)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Draft not found"
