%global pypi_name simonw-llm

Name:           python-%{pypi_name}
Version:        0.28
Release:        1%{?dist}
Summary:        CLI utility and Python library for interacting with Large Language Models

License:        Apache-2.0
URL:            https://github.com/simonw/llm
Source0:        %{pypi_source llm}
# Fix PEP 639 license format for older setuptools
Patch0:         fix-license-format.patch

BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

%global _description %{expand:
A CLI utility and Python library for interacting with Large Language Models
from organizations like OpenAI, Anthropic and Gemini plus local models
installed on your own machine. Supports prompt execution, SQLite logging,
embeddings, structured data extraction, and tool integration.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
Requires:       python(abi) >= 3.10
Requires:       python3dist(click)
Requires:       python3dist(click-default-group) >= 1.2.3
Requires:       python3dist(condense-json) >= 0.1.3
Requires:       python3dist(openai) >= 1.55.3
Requires:       python3dist(pip)
Requires:       python3dist(pluggy)
Requires:       python3dist(puremagic)
Requires:       python3dist(pydantic) >= 2
Requires:       python3dist(python-ulid)
Requires:       python3dist(pyyaml)
Requires:       python3dist(setuptools)
Requires:       python3dist(sqlite-migrate) >= 0.1~a2
Requires:       python3dist(sqlite-utils) >= 3.37

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n llm-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -N

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files llm

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/llm

%changelog
* Sat Jan 17 2026 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 0.28-1
- Initial packaging for simonw/llm
