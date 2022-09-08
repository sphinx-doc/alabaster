from invoke import Collection
from invocations import docs, checks
from invocations.packaging import release


ns = Collection(release, docs, checks.blacken)
ns.configure(
    {
        "packaging": {
            "sign": True,
            "wheel": True,
            "changelog_file": "docs/changelog.rst",
        }
    }
)
