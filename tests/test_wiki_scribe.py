from wiki_scribe import WikiScribe, ArticleMetadata

def test_validate_metadata():
    scribe = WikiScribe({})
    metadata = ArticleMetadata("Test Article", "John Doe", "2022-01-01")
    scribe.validate_metadata(metadata)

def test_validate_metadata_empty_title():
    scribe = WikiScribe({})
    metadata = ArticleMetadata("", "John Doe", "2022-01-01")
    try:
        scribe.validate_metadata(metadata)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Title must be a non-empty string"

def test_check_formatting():
    scribe = WikiScribe({})
    article_text = "# Test Article\n"
    scribe.check_formatting(article_text)

def test_check_formatting_no_heading():
    scribe = WikiScribe({})
    article_text = "Test Article\n"
    try:
        scribe.check_formatting(article_text)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Article text must start with a heading"

def test_review_article():
    scribe = WikiScribe({})
    metadata = ArticleMetadata("Test Article", "John Doe", "2022-01-01")
    article_text = "# Test Article\n"
    assert scribe.review_article(metadata, article_text)

def test_review_article_invalid_metadata():
    scribe = WikiScribe({})
    metadata = ArticleMetadata("", "John Doe", "2022-01-01")
    article_text = "# Test Article\n"
    assert not scribe.review_article(metadata, article_text)

def test_approve_or_reject():
    scribe = WikiScribe({})
    metadata = ArticleMetadata("Test Article", "John Doe", "2022-01-01")
    article_text = "# Test Article\n"
    assert scribe.approve_or_reject(metadata, article_text) == "Approved"

def test_approve_or_reject_invalid_metadata():
    scribe = WikiScribe({})
    metadata = ArticleMetadata("", "John Doe", "2022-01-01")
    article_text = "# Test Article\n"
    assert scribe.approve_or_reject(metadata, article_text) == "Rejected"
