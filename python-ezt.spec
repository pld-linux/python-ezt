%bcond_without	tests
Summary:	EZT is a very clean and simple module for templating in Python
Name:		python-ezt
# 0.svnrevision
Version:	0.22
Release:	2
License:	LGPL
Group:		Libraries/Python
# http://ezt.googlecode.com/svn/trunk/ ezt
Source0:	ezt-20080701.tar.gz
# Source0-md5:	82b3eb1fefd547e543d0c1ee5be051b9
URL:		http://code.google.com/p/ezt/
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EZT is a very clean and simple module for templating in Python.

%prep
%setup -q -n ezt

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

install ezt.py $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_comp $RPM_BUILD_ROOT
%py_ocomp $RPM_BUILD_ROOT
%py_postclean

%{?with_tests:cd tests; %{__python} ezt_test.py}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[co]
