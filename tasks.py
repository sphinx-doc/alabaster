from invoke import Collection
from invocations.packaging import release


ns = Collection(release)
ns.configure({
    'packaging': {
        'sign': True,
        'wheel': True,
    }
})
