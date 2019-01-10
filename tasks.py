from invoke import Collection
from invocations import docs, travis, checks
from invocations.packaging import release


ns = Collection(release, docs, travis, checks.blacken)
ns.configure(
    {
        "packaging": {
            "sign": True,
            "wheel": True,
            "changelog_file": "docs/changelog.rst",
        }
    }
)
