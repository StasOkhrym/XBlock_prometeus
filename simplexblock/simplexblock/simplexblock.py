"""Simple collapsible XBlock with editable fields and counter"""

import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioEditableXBlockMixin


class SimpleXBlock(StudioEditableXBlockMixin, XBlock):
    title = String(
        default="Title",
    )
    content = String(
        default="Content",
        scope=Scope.content,
    )
    count = Integer(
        default=0,
        scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )
    editable_fields = ("title", "content")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        The primary view of the SimpleXBlock, shown to students
        when viewing courses.
        """
        context = {
            "title": self.title,
            "content": self.content,
            "count": self.count,
        }

        loader = ResourceLoader(__name__)
        html = loader.render_django_template(
            "static/html/simplexblock.html", context=context
        )

        frag = Fragment(html)
        frag.add_css(self.resource_string("static/css/simplexblock.css"))
        frag.add_javascript(
            self.resource_string("static/js/src/simplexblock.js")
        )
        frag.initialize_js("SimpleXBlock")

        return frag

    @XBlock.json_handler
    def increment_count(self, data, suffix=""):
        """
        An example handler, which increments the data.
        """
        assert data["hello"] == "world"

        self.count += 1
        return {"count": self.count}

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            (
                "SimpleXBlock",
                """<simplexblock/>
             """,
            ),
            (
                "Multiple SimpleXBlock",
                """<vertical_demo>
                <simplexblock/>
                <simplexblock/>
                <simplexblock/>
                </vertical_demo>
             """,
            ),
        ]
