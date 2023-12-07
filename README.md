<div align="center">

# CheckVersions

[![Run Tests](https://github.com/muhammad-fiaz/checkversions/actions/workflows/python-package.yml/badge.svg)](https://github.com/muhammad-fiaz/checkversions/actions/workflows/python-package.yml)
[![PyPI Version](https://img.shields.io/pypi/v/checkversions)](https://pypi.org/project/checkversions/)
[![Python Versions](https://img.shields.io/pypi/pyversions/checkversions)](https://pypi.org/project/checkversions/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://img.shields.io/pypi/dm/checkversions)](https://pypi.org/project/checkversions/)
[![Last Commit](https://img.shields.io/github/last-commit/muhammad-fiaz/checkversions)](https://github.com/muhammad-fiaz/checkversions)
[![GitHub Issues](https://img.shields.io/github/issues/muhammad-fiaz/checkversions)](https://github.com/muhammad-fiaz/checkversions/issues)
[![GitHub Stars](https://img.shields.io/github/stars/muhammad-fiaz/checkversions)](https://github.com/muhammad-fiaz/checkversions/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/muhammad-fiaz/checkversions)](https://github.com/muhammad-fiaz/checkversions/network)

[![Maintainer](https://img.shields.io/badge/Maintainer-muhammad--fiaz-blue)](https://github.com/muhammad-fiaz)
[![Sponsor on GitHub](https://img.shields.io/badge/Sponsor%20on%20GitHub-Become%20a%20Sponsor-blue)](https://github.com/sponsors/muhammad-fiaz)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Stability](https://img.shields.io/badge/Stability-Stable-green)](https://github.com/muhammad-fiaz/checkversions)

</div>



CheckVersions is a powerful and intuitive version comparison tool designed to simplify the process of discerning the latest and older versions in software development.

## Features

- **Semantic Version Analysis:** Leverage our sophisticated semantic versioning analysis engine to compare versions like "0.0.0-beta" effortlessly.
- **Automated Version Ranking:** Quickly identify the latest, older releases, or pre-releases with our automated version-ranking system.
- **Efficient Version Delta Assessment:** CheckVersions provides a detailed breakdown of the differences between versions, allowing you to make informed decisions about your software.
- **User-Friendly Interface:** Our intuitive user interface ensures that developers can effortlessly compare versions through graphical representations, providing detailed insights into the chronological order of your software iterations.
- **Secure Version Analysis:** Security is paramount. CheckVersions ensures version comparison is performed securely, protecting your intellectual property and facilitating risk-free decision-making in your development process.

## Getting Started

## Installation

```bash
npm install checkversions
```
## Usage
```python3
from checkversions import *

# Example 1: Basic Version Comparison
current_version = "v1.0.0"
latest_version = "v1.0.0-beta"
result = compare_versions(current_version, latest_version)
print(result)
# Output: v1.0.0
```
In this example, we demonstrate a basic version comparison. The compare_versions function is used to compare the current_version (v1.0.0) with the latest_version (v1.0.0-beta). The result is printed, and it shows that the latest version is v1.0.0.

```python3
# Example 2: Comparing Versions with Hyphens and Words
version1 = "2.0.0-beta"
version2 = "2.0.1-alpha"
result = compare_versions(version1, version2)
print(result)
# Output: 2.0.1-alpha

```
In this example, we showcase version comparison with hyphens and additional words. The compare_versions function compares version1 (2.0.0-beta) with version2 (2.0.1-alpha). The result is printed, indicating that the latest version is 2.0.1-alpha.

## Default Hierarchy
```json
{
  "beta": 0,
  "prerelease": 1,
  "alpha": 2,
  "unstable": 3,
  "stable": 4,
  "release": 5
}

```
The default hierarchy is a JSON representation that assigns priority values to version words. For instance, "beta" has a priority of 0, "prerelease" has a priority of 1, and so on.

## Custom Hierarchy

```python3
from checkversions import *

# Example 3: Custom Hierarchy
# Define a custom hierarchy
custom_hierarchy = {"beta": 0, "alpha": 1, "rc": 2, "gamma": 3, "stable": 4}

version1 = "v1.0.0-beta"
version2 = "v1.0.1-alpha"
result = compare_versions(version1, version2, custom_hierarchy)
print(result)
# Output: v1.0.1-alpha

```
In this example, we introduce a custom hierarchy for version comparison. The custom_hierarchy dictionary is defined with version words and their corresponding priority. The compare_versions function uses this custom hierarchy to compare version1 (v1.0.0-beta) with version2 (v1.0.1-alpha). The result is printed, indicating that the latest version is v1.0.1-alpha.

## Contributing
Contributions are welcome! Before contributing, please read our [Contributing Guidelines](CONTRIBUTING.md) to ensure a smooth and collaborative development process.

## Code of Conduct

Please review our [Code of Conduct](CODE_OF_CONDUCT.md) to understand the standards of behavior we expect from contributors and users of this project.

## License
This project is licensed under the [MIT License](). See [LICENSE](LICENSE) for more details.

## Support the Project
<br>
<div align="center">

<h5> <strong> 💰 You can help me improve more by offering a little support on any platform❤️</strong></h5>

[![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/muhammadfiaz) [![Patreon](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://patreon.com/muhammadfiaz) [![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/muhammadfiaz)
[![Sponsor muhammad-fiaz](https://img.shields.io/badge/Sponsor-%231EAEDB.svg?&style=for-the-badge&logo=GitHub-Sponsors&logoColor=white)](https://github.com/sponsors/muhammad-fiaz)
[![Open Collective Backer](https://img.shields.io/badge/Open%20Collective-Backer-%238CC84B?style=for-the-badge&logo=open-collective&logoColor=white)](https://opencollective.com/muhammadfiaz)
</div>



## Happy Coding ❤️
