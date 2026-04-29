# optimizely-platform

A Python package providing modules needed to build add-ons that run natively in the Optimizely platform.

## Releasing

1. Merge your changes to `master`.
2. [Create a GitHub Release](../../releases/new) with a tag in the format `vX.Y.Z` (e.g. `v1.2.3`).

The `publish.yaml` workflow builds and publishes to Google Artifact Registry. It will reject tags that aren't strict semver, lack a GitHub Release, or aren't on `master`.
