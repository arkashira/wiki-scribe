import json
from dataclasses import dataclass
from typing import List

@dataclass
class ArticleMetadata:
    title: str
    author: str
    date: str

class WikiScribe:
    def __init__(self, schema):
        self.schema = schema

    def validate_metadata(self, metadata: ArticleMetadata):
        if not isinstance(metadata.title, str) or not metadata.title:
            raise ValueError("Title must be a non-empty string")
        if not isinstance(metadata.author, str) or not metadata.author:
            raise ValueError("Author must be a non-empty string")
        if not isinstance(metadata.date, str) or not metadata.date:
            raise ValueError("Date must be a non-empty string")

    def check_formatting(self, article_text: str):
        if not article_text.startswith("# "):
            raise ValueError("Article text must start with a heading")
        if not article_text.endswith("\n"):
            raise ValueError("Article text must end with a newline")

    def review_article(self, metadata: ArticleMetadata, article_text: str):
        try:
            self.validate_metadata(metadata)
            self.check_formatting(article_text)
            return True
        except ValueError as e:
            return False

    def approve_or_reject(self, metadata: ArticleMetadata, article_text: str):
        if self.review_article(metadata, article_text):
            return "Approved"
        else:
            return "Rejected"
