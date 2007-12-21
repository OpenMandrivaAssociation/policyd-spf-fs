Summary:	This is a policy daemon for checking SPF records in postfix
Name:		policyd-spf-fs
Version:	23
Release:	%mkrel 1
License:	LGPL
Group:		System/Servers
URL:		http://www.freestone.net/ftp/policyd-spf-fs/
Source0:	http://www.freestone.net/ftp/policyd-spf-fs/%{name}_%{version}.tar.gz
Source1:	http://www.freestone.net/ftp/policyd-spf-fs/%{name}_%{version}.tar.gz.sig
Patch0:		policyd-spf-fs-no_nameser.h.diff
Patch1:		policyd-spf-fs-optflags.diff
BuildRequires:	libspf-devel >= 1.2.5
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is a policy daemon for checking SPF records in postfix. It is based on
the spfquery command line tool from libspf2.

%prep

%setup -q -n %{name}_%{version}
%patch0 -p0
%patch1 -p0

%build

%make

%install 
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 %{name} %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc CHANGES COPYING README TODO
%attr(0755,root,root) %{_bindir}/%{name}
