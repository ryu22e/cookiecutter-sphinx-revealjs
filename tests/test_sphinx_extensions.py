from unittest.mock import MagicMock

from sphinx.addnodes import document
from sphinx.application import Sphinx


class TestSphinxBudoux:
    def test_add_wbr_tags_to_titles(self):
        from sphinx_extensions.sphinx_budoux import html_page_context

        app = MagicMock(Sphinx)
        app.config = {
            "budoux_target_tags": ["h1"],
        }
        context = {"body": "<h1>本日は晴天なり</h1>"}

        html_page_context(app, "test", "test", context, MagicMock(document))

        assert "body" in context.keys()
        assert "<wbr>" in context["body"]

    def test_not_add_wbr_tags_to_titles_if_documemt_is_none(self):
        from sphinx_extensions.sphinx_budoux import html_page_context

        app = MagicMock(Sphinx)
        app.config = {
            "budoux_target_tags": ["h1"],
        }
        context = {"body": "<h1>本日は晴天なり</h1>"}
        document = None

        html_page_context(app, "test", "test", context, document)

        assert "body" in context.keys()
        assert context["body"] == "<h1>本日は晴天なり</h1>"
