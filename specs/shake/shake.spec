# $Id$
# Authority: dag

Summary: Userspace filesystem defragmenter
Name: shake
Version: 0.24
Release: 1
License: GPL
Group: System Environment/Base
URL: http://vleu.net/shake/

Source: http://vleu.net/shake/shake-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libattr-devel

%description
 Shake is a defragmenter that runs in userspace, without the need of patching
the kernel and while the systems is used. There is nothing magic in that:
it just works by rewriting fragmented files. But it has some heuristics that
could make it more efficient than other tools, including defrag and, maybe,
xfs_fsr.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -D -m0755 shake %{buildroot}%{_bindir}/shake
%{__install} -D -m0755 unattr %{buildroot}%{_bindir}/unattr
%{__install} -D -m0644 doc/shake.8 %{buildroot}%{_mandir}/man8/shake.8
%{__install} -D -m0644 doc/unattr.8 %{buildroot}%{_mandir}/man8/unattr.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog COPYING
%doc %{_mandir}/man8/shake.8*
%doc %{_mandir}/man8/unattr.8*
%{_bindir}/shake
%{_bindir}/unattr

%changelog
* Sun Aug 20 2006 Dag Wieers <dag@wieers.com> - 0.24-1
- Updated to release 0.24.

* Wed Aug 16 2006 Dag Wieers <dag@wieers.com> - 0.23-1
- Updated to release 0.23.

* Tue Jun 27 2006 Dag Wieers <dag@wieers.com> - 0.22-1
- Updated to release 0.22.

* Mon Jun 12 2006 Dag Wieers <dag@wieers.com> - 0.20-1
- Initial package. (using DAR)
