%global pypi_name llm_anthropic
%global pkg_name simonw-llm-plugins-anthropic

Name:           python-%{pkg_name}
Version:        0.23
Release:        1%{?dist}
Summary:        LLM plugin to access Anthropic's Claude models

License:        Apache-2.0
URL:            https://github.com/simonw/llm-anthropic
Source0:        %{pypi_source %{pypi_name}}
# Fix PEP 639 license format for older setuptools
Patch0:         fix-license-format-anthropic.patch

BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

%global _description %{expand:
A plugin for the LLM CLI tool and Python library that provides access to
Anthropic's Claude AI models including Claude Opus, Sonnet, and Haiku variants.
Features include image and PDF attachment handling, extended thinking mode for
complex reasoning, web search capabilities, schema-based structured output,
and prompt caching for efficiency.}

%description %_description

%package -n python3-%{pkg_name}
Summary:        %{summary}
Requires:       python(abi) >= 3.10
Requires:       python3dist(llm) >= 0.26
Requires:       python3dist(anthropic) >= 0.75
Requires:       python3dist(json-schema-to-pydantic)

%description -n python3-%{pkg_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -N

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files llm_anthropic

%files -n python3-%{pkg_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Sat Jan 17 2026 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 0.23-1
- Initial packaging for llm-anthropic plugin
