#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
%define		rev	475
Summary:	ReplayGain library
Name:		libreplaygain
Version:	0.0.1.r%{rev}
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://files.musepack.net/source/%{name}_r%{rev}.tar.gz
# Source0-md5:	e27b3b1249b7fbae92d656d9e3d26633
Patch0:		%{name}-link.patch
URL:		http://www.musepack.net/
BuildRequires:	cmake >= 2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ReplayGain library.

%package devel
Summary:	Header files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name}.

%package static
Summary:	Static version of the %{name} library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of the %{name} library.

%prep
%setup -q -n libreplaygain_r%{rev}
%patch0 -p1

%build
%cmake

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}
%{__cp} -r include/replaygain $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libreplaygain.so.*.*.*
%ghost %{_libdir}/libreplaygain.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libreplaygain.so
%{_includedir}/replaygain

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libreplaygain.a
%endif
