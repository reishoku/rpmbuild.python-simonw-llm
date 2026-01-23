%global pypi_name llm_gemini
%global pkg_name simonw-llm-plugins-gemini

Name:           python-%{pkg_name}
Version:        0.28.2
Release:        1%{?dist}
Summary:        LLM plugin to access Google's Gemini family of models

License:        Apache-2.0
URL:            https://github.com/simonw/llm-gemini
Source0:        %{pypi_source %{pypi_name}}
# Fix PEP 639 license format for older setuptools
Patch0:         fix-license-format-gemini.patch

BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

%global _description %{expand:
A plugin for the LLM CLI tool and Python library that provides access to
Google's Gemini family of AI models. Supports multimodal inputs including
images, audio, video, and YouTube URLs. Features include JSON structured
output, code execution, Google Search grounding, and text embeddings.}

%description %_description

%package -n python3-%{pkg_name}
Summary:        %{summary}
Requires:       python(abi) >= 3.10
Requires:       python3dist(llm) >= 0.27
Requires:       python3dist(httpx)
Requires:       python3dist(ijson)

%description -n python3-%{pkg_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -N

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files llm_gemini

%files -n python3-%{pkg_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Sat Jan 17 2026 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 0.28.2-1
- Initial packaging for llm-gemini plugin
