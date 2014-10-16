Summary:	C Configuration File Library
Name:		libconfig
Version:	1.4.9
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.hyperrealm.com/libconfig/%{name}-%{version}.tar.gz
# Source0-md5:	b6ee0ce2b3ef844bad7cac2803a90634
URL:		http://www.hyperrealm.com/main.php?s=libconfig
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libconfig is a simple library for manipulating structured
configuration files.

%package devel
Summary:	Header files for libconfig library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libconfig library.

%package c++
Summary:	C++ Configuration File Library
Group:		Libraries
# doesn't require base, common code included in library

%description c++
libconfig++ is the C++ binding for libconfig library.

%package c++-devel
Summary:	Header files for libconfig++ library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libconfig++
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
Header files for libconfig++ library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_infodir}/dir
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%post	devel -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p/usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	c++ -p /usr/sbin/ldconfig
%postun	c++ -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %ghost %{_libdir}/libconfig.so.?
%attr(755,root,root) %{_libdir}/libconfig.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libconfig.so
%{_includedir}/libconfig.h
%{_pkgconfigdir}/libconfig.pc
%{_infodir}/libconfig.info*

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libconfig++.so.?
%attr(755,root,root) %{_libdir}/libconfig++.so.*.*.*

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libconfig++.so
%{_includedir}/libconfig.h++
%{_pkgconfigdir}/libconfig++.pc

