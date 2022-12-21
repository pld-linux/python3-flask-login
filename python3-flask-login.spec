%define         module  flask-login
Summary:	Flask-Login provides user session management for Flask
Summary(pl.UTF-8):	Wsparcie dla zarzadzania sesja uzytkownika w aplikacjach Flask
Name:		python3-%{module}
Version:	0.6.2
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/F/Flask-Login/Flask-Login-%{version}.tar.gz
# Source0-md5:	8020b22ad7ec6f17034f90117a520633
URL:		https://github.com/maxcountryman/flask-login/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python3-modules
Requires:	python3-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flask-Login provides user session management for Flask. It handles the
common tasks of logging in, logging out, and remembering your users'
sessions over extended periods of time.

%description -l pl.UTF-8
Wsparcie dla zarzadzania sesja uzytkownika w aplikacjach Flask. Plugin
obsluguje najpopularniejsze przypadki uzycia: logowanie, wylogowanie,
zapamietywanie sesji uzytkownikow przez okreslony czas.

%prep
%setup -q -n Flask-Login-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{py3_sitescriptdir}/flask_login
%{py3_sitescriptdir}/Flask_Login-%{version}-py*.egg-info
