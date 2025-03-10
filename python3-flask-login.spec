#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (one failing)

%define         module  flask-login
Summary:	Flask-Login provides user session management for Flask
Summary(pl.UTF-8):	Obsługa zarządzania sesją użytkownika w aplikacjach Flask
Name:		python3-%{module}
Version:	0.6.3
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/F/Flask-Login/Flask-Login-%{version}.tar.gz
# Source0-md5:	689564b8b7f3782f0db382b7aa85bbc2
URL:		https://github.com/maxcountryman/flask-login/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-flask >= 1.0.4
BuildRequires:	python3-semantic_version
BuildRequires:	python3-werkzeug >= 1.0.1
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flask-Login provides user session management for Flask. It handles the
common tasks of logging in, logging out, and remembering your users'
sessions over extended periods of time.

%description -l pl.UTF-8
Obsługa zarządzania sesją użytkownika w aplikacjach Flask. Wtyczka
obsługuje najpopularniejsze przypadki użycia: logowanie, wylogowanie,
zapamiętywanie sesji użytkowników przez określony czas.

%package apidocs
Summary:	API documentation for Python Flask-Login module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona Flask-Login
Group:		Documentation

%description apidocs
API documentation for Python Flask-Login module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona Flask-Login.

%prep
%setup -q -n Flask-Login-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m unittest discover -s tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C docs html \
	SOURCEDIR=. \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE README.md
%{py3_sitescriptdir}/flask_login
%{py3_sitescriptdir}/Flask_Login-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_modules,_static,*.html,*.js}
%endif
