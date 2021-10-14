# Changelog

## [1.1.0](https://www.github.com/googleapis/python-security-private-ca/compare/v1.0.6...v1.1.0) (2021-10-08)


### Features

* add context manager support in client ([#131](https://www.github.com/googleapis/python-security-private-ca/issues/131)) ([eb9fc8b](https://www.github.com/googleapis/python-security-private-ca/commit/eb9fc8b1a324505418ece9636e91d844e11845de))

### [1.0.6](https://www.github.com/googleapis/python-security-private-ca/compare/v1.0.5...v1.0.6) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([f86ec89](https://www.github.com/googleapis/python-security-private-ca/commit/f86ec89f3c4537556188064606be005ee7feb056))

### [1.0.5](https://www.github.com/googleapis/python-security-private-ca/compare/v1.0.4...v1.0.5) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([49b5c9a](https://www.github.com/googleapis/python-security-private-ca/commit/49b5c9ae54c594abf1a8158506e2a1ddb6dce67d))

### [1.0.4](https://www.github.com/googleapis/python-security-private-ca/compare/v1.0.3...v1.0.4) (2021-08-10)


### Documentation

* **samples:** add local generation for crypto keys ([#98](https://www.github.com/googleapis/python-security-private-ca/issues/98)) ([0668ffd](https://www.github.com/googleapis/python-security-private-ca/commit/0668ffde892bec99a4cd574bbc257fcc2de6c1c7))


### Miscellaneous Chores

* release as 1.0.4 ([#100](https://www.github.com/googleapis/python-security-private-ca/issues/100)) ([47fb407](https://www.github.com/googleapis/python-security-private-ca/commit/47fb4075db02e5c3eaf4f25f3d032a6c2514afce))

### [1.0.3](https://www.github.com/googleapis/python-security-private-ca/compare/v1.0.2...v1.0.3) (2021-07-29)


### Bug Fixes

* enable self signed jwt for grpc ([#91](https://www.github.com/googleapis/python-security-private-ca/issues/91)) ([674dd85](https://www.github.com/googleapis/python-security-private-ca/commit/674dd8595b9165fec92097d5bb168357ac7ab1ee))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#84](https://www.github.com/googleapis/python-security-private-ca/issues/84)) ([305dc83](https://www.github.com/googleapis/python-security-private-ca/commit/305dc83eec5215fd84a63e5786d8c93b03c468b8))
* **samples:** private CA python samples ([d753667](https://www.github.com/googleapis/python-security-private-ca/commit/d753667bc3a193931893260cec33d0c68ab621d5))


### Miscellaneous Chores

* release as 1.0.3 ([#92](https://www.github.com/googleapis/python-security-private-ca/issues/92)) ([6026929](https://www.github.com/googleapis/python-security-private-ca/commit/6026929efe36ecec40afbc442f09df609b7c42a8))

### [1.0.2](https://www.github.com/googleapis/python-security-private-ca/compare/v1.0.1...v1.0.2) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#83](https://www.github.com/googleapis/python-security-private-ca/issues/83)) ([cd5390c](https://www.github.com/googleapis/python-security-private-ca/commit/cd5390cf5fff50419b000c71431d8ede0de35833))

### [1.0.1](https://www.github.com/googleapis/python-security-private-ca/compare/v1.0.0...v1.0.1) (2021-07-16)


### Bug Fixes

* correct response type of DeleteCaPool ([13e54bf](https://www.github.com/googleapis/python-security-private-ca/commit/13e54bf5ad66f85f1e2165b2cf67604af50ccd0c))
* make allow_config_based_issuance bool optional ([#80](https://www.github.com/googleapis/python-security-private-ca/issues/80)) ([13e54bf](https://www.github.com/googleapis/python-security-private-ca/commit/13e54bf5ad66f85f1e2165b2cf67604af50ccd0c))
* make allow_csr_based_issuance bool optional ([13e54bf](https://www.github.com/googleapis/python-security-private-ca/commit/13e54bf5ad66f85f1e2165b2cf67604af50ccd0c))
* make publish_ca_cert bool optional ([13e54bf](https://www.github.com/googleapis/python-security-private-ca/commit/13e54bf5ad66f85f1e2165b2cf67604af50ccd0c))
* make publish_crl bool optional ([13e54bf](https://www.github.com/googleapis/python-security-private-ca/commit/13e54bf5ad66f85f1e2165b2cf67604af50ccd0c))

## [1.0.0](https://www.github.com/googleapis/python-security-private-ca/compare/v0.4.0...v1.0.0) (2021-07-12)


### Features

* bump release level to production/stable ([#60](https://www.github.com/googleapis/python-security-private-ca/issues/60)) ([170f9be](https://www.github.com/googleapis/python-security-private-ca/commit/170f9be92448278064fd58f2a9302ca2f8c43b04))


### Documentation

* correct links to product documentation ([#77](https://www.github.com/googleapis/python-security-private-ca/issues/77)) ([97821d7](https://www.github.com/googleapis/python-security-private-ca/commit/97821d774f6f3ff0c889e0ad16ef627549e8e28e))

## [0.4.0](https://www.github.com/googleapis/python-security-private-ca/compare/v0.3.0...v0.4.0) (2021-06-30)


### Features

* add always_use_jwt_access ([#70](https://www.github.com/googleapis/python-security-private-ca/issues/70)) ([9b3584d](https://www.github.com/googleapis/python-security-private-ca/commit/9b3584dcf00f50ceab9529f758da3e4ddd5a602c))


### Bug Fixes

* disable always_use_jwt_access ([#74](https://www.github.com/googleapis/python-security-private-ca/issues/74)) ([5cda9ac](https://www.github.com/googleapis/python-security-private-ca/commit/5cda9acc4f7b1aa83bc73700f9cef4f84cc2306a))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-security-private-ca/issues/1127)) ([#65](https://www.github.com/googleapis/python-security-private-ca/issues/65)) ([a82b1ab](https://www.github.com/googleapis/python-security-private-ca/commit/a82b1abdaf8d55f6b6cbf71d6fb7a416e3307888)), closes [#1126](https://www.github.com/googleapis/python-security-private-ca/issues/1126)

## [0.3.0](https://www.github.com/googleapis/python-security-private-ca/compare/v0.2.0...v0.3.0) (2021-05-17)


### Features

* Import v1 by default instead of v1beta1 ([c4c8624](https://www.github.com/googleapis/python-security-private-ca/commit/c4c862426fb5b7b931dd0de4d26d1ac27ce05f1a))
* Make CertificateTemplate bools optional to indicate unset values ([#54](https://www.github.com/googleapis/python-security-private-ca/issues/54)) ([c4c8624](https://www.github.com/googleapis/python-security-private-ca/commit/c4c862426fb5b7b931dd0de4d26d1ac27ce05f1a))
* support self-signed JWT flow for service accounts ([c4c8624](https://www.github.com/googleapis/python-security-private-ca/commit/c4c862426fb5b7b931dd0de4d26d1ac27ce05f1a))


### Bug Fixes

* add async client to %name_%version/init.py ([c4c8624](https://www.github.com/googleapis/python-security-private-ca/commit/c4c862426fb5b7b931dd0de4d26d1ac27ce05f1a))
* **deps:** add packaging requirement ([#56](https://www.github.com/googleapis/python-security-private-ca/issues/56)) ([5877dda](https://www.github.com/googleapis/python-security-private-ca/commit/5877dda559311e87de8f9f06f8174a0e1d4c62bc))

### [0.1.1](https://www.github.com/googleapis/python-security-private-ca/compare/v0.1.0...v0.1.1) (2020-10-02)


### Documentation

* don't treat warnings as errors ([ca0837a](https://www.github.com/googleapis/python-security-private-ca/commit/ca0837a9798d0bf6f3c93dcc003aa38f86eddd5c))

## 0.1.0 (2020-10-02)


### Features

* generate v1beta1 ([9cd5bfa](https://www.github.com/googleapis/python-security-private-ca/commit/9cd5bfaee208396ca5b27590bf09c05ad372d953))
