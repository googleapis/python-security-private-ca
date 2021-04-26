# Changelog

## [1.0.0](https://www.github.com/googleapis/python-security-private-ca/compare/v0.1.1...v1.0.0) (2021-04-26)


### ⚠ BREAKING CHANGES

* The NamedCurve enum is replaced by the EcKeyType message
* Update the default version of the client to `v1`
* Refactored Elliptic Key curves to provide additional options (#35)
* rename sign hash algorithms; remove CreateCertificateRevocationList, CreateReusableConfig, DeleteReusableConfig, UpdateReusableConfig (#8)

### Features

* Refactored Elliptic Key curves to provide additional options ([#35](https://www.github.com/googleapis/python-security-private-ca/issues/35)) ([00fdf73](https://www.github.com/googleapis/python-security-private-ca/commit/00fdf733e93014975b1afee738623e419de5e433))
* rename sign hash algorithms; remove CreateCertificateRevocationList, CreateReusableConfig, DeleteReusableConfig, UpdateReusableConfig ([#8](https://www.github.com/googleapis/python-security-private-ca/issues/8)) ([c984a78](https://www.github.com/googleapis/python-security-private-ca/commit/c984a7868b5a990d7ef02fd3894aa94ca913a308))
* The NamedCurve enum is replaced by the EcKeyType message ([00fdf73](https://www.github.com/googleapis/python-security-private-ca/commit/00fdf733e93014975b1afee738623e419de5e433))
* Update the default version of the client to `v1` ([00fdf73](https://www.github.com/googleapis/python-security-private-ca/commit/00fdf733e93014975b1afee738623e419de5e433))


### Bug Fixes

* remove client recv msg limit fix: add enums to `types/__init__.py` ([#10](https://www.github.com/googleapis/python-security-private-ca/issues/10)) ([65875b5](https://www.github.com/googleapis/python-security-private-ca/commit/65875b5cf12a6e1c46e53048f7395dea4297c05a))

### [0.1.1](https://www.github.com/googleapis/python-security-private-ca/compare/v0.1.0...v0.1.1) (2020-10-02)


### Documentation

* don't treat warnings as errors ([ca0837a](https://www.github.com/googleapis/python-security-private-ca/commit/ca0837a9798d0bf6f3c93dcc003aa38f86eddd5c))

## 0.1.0 (2020-10-02)


### Features

* generate v1beta1 ([9cd5bfa](https://www.github.com/googleapis/python-security-private-ca/commit/9cd5bfaee208396ca5b27590bf09c05ad372d953))
