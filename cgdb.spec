Summary:	A lightweight, but fully functional curses frontend to gdb
Summary(pl.UTF-8):	Lekki, ale w pełni funkcjonalny frontend do gdb oparty na ncurses
Name:		cgdb
Version:	0.7.0
Release:	1
License:	GPL v2
Group:		Development/Debuggers
Source0:	http://cgdb.me/files/%{name}-%{version}.tar.gz
# Source0-md5:	7bdb1b418db4bcdb16ba004aebd8f3d7
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-info.patch
URL:		http://cgdb.github.io/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel >= 5.1
BuildRequires:	texinfo
Requires:	gdb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGDB is a curses-based interface to the GNU Debugger (GDB). The goal
of CGDB is to be lightweight and responsive; not encumbered with
unnecessary features. The interface is designed to deliver the
familiar GDB text interface, with a split screen showing the source as
it executes. The UI is modeled on the classic Unix text editor, vi.
Those familiar with vi should feel right at home using CGDB.

%description -l pl.UTF-8
CGDB to oparty na curses interfejs do GNU Debuggera (GDB). Celem CGDB
jest bycie lekkim i reaktywnym, nie obciążonym niepotrzebnymi
możliwościami. Interfejs został tak zaprojektowany, by dostarczyć
znajomy interfejs tekstowy GDB z podzielonym ekranem pokazującym
źródła wykonywanego kodu. Interfejs użytkownika jest modelowany na
klasyczny uniksowy edytor tekstu - vi. Znający vi używając CGDB
powinni czuć się jak w domu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
#CPPFLAGS='%{rpmcppflags} -I/usr/include/ncurses '
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

# pass noinst_bindir inside buildroot - don't mess in $TMPDIR/../../..
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	noinst_bindir=/progs

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/cgdb
%{_infodir}/cgdb.info*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/cgdb.txt
