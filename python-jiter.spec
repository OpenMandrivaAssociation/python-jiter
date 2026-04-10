%undefine _debugsource_template
%define module jiter
%bcond tests 1

Name:		python-jiter
Version:	0.14.0
Release:	1
Summary:	Fast iterable JSON parser
License:	MIT
Group:		Development/Python
URL:		https://github.com/pydantic/jiter
Source0:	https://files.pythonhosted.org/packages/source/j/%{module}/%{module}-%{version}.tar.gz
Source1:	%{name}-%{version}-vendor.tar.xz

BuildSystem: python
BuildRequires:	cargo
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(maturin)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	rust-packaging
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(dirty-equals)
%endif

%description
This is a standalone version of the JSON parser used in `pydantic-core`.

The recommendation is to only use this package directly if you do not
use `pydantic`.

%prep -a
tar xf %{S:1}
%cargo_prep -v vendor

cat >>.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build -p
export RUSTFLAGS="-lpython%{pyver}"
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies


%if %{with tests}
%check
pushd crates/jiter-python/tests
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}"
pytest test_jiter.py
popd
%endif

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
