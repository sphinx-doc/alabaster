from invoke import Collection
from invocations import docs
from invocations.packaging import release


ns = Collection(release, docs)
ns.configure({
    'packaging': {
        'sign': True,
        'wheel': True,
        'changelog_file': 'docs/changelog.rst',
    }
})
