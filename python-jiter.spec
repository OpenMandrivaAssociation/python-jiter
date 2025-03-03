Name:           python-jiter
Version:        0.8.2
Release:        1
Summary:        Fast iterable JSON parser
License:        MIT
URL:            https://github.com/pydantic/jiter/
Source0:        https://files.pythonhosted.org/packages/source/j/jiter/jiter-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  python-maturin
BuildRequires:  python-pip
BuildRequires:  rust-packaging
#BuildSystem: python

%description
This is a standalone version of the JSON parser used in `pydantic-core`. The recommendation is to only use this package directly if you do not use `pydantic`.

%prep
%cargo_prep -v vendor
%autosetup -p1 -n jiter-%{version} -a1

%build
%py_build

%install
%py_install

%files
%doc README.md
%{python_sitearch}/jiter
%{python_sitearch}/jiter-%{version}.dist-info
