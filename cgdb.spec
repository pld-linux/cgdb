Summary:	A lightweight, but fully functional curses frontend to gdb
Summary(pl):	Lekki, ale w pe³ni funkcjonalny frontend do gdb oparty na ncurses
Name:		cgdb
Version:	0.5.3
Release:	2
License:	GPL
Group:		Development/Debuggers
Source0:	http://dl.sourceforge.net/cgdb/%{name}-%{version}.tar.gz
# Source0-md5:	51adf1db0307adaba24336ef3a18e0c3
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-missing_includes.patch
Patch2:		%{name}-am_no_debug.patch
URL:		http://cgdb.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	readline-devel
Requires:	gdb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGDB is a curses-based interface to the GNU Debugger (GDB). The goal
of CGDB is to be lightweight and responsive; not encumbered with
unnecessary features. The interface is designed to deliver the
familiar GDB text interface, with a split screen showing the source as
it executes. The UI is modeled on the classic Unix text editor, vi.
Those familiar with vi should feel right at home using CGDB.

%description -l pl
CGDB to oparty na curses interfejs do GNU Debuggera (GDB). Celem CGDB
jest bycie lekkim i reaktywnym, nie obci±¿onym niepotrzebnymi
mo¿liwo¶ciami. Interfejs zosta³ tak zaprojektowany, by dostarczyæ
znajomy interfejs tekstowy GDB z podzielonym ekranem pokazuj±cym
¼ród³a wykonywanego kodu. Interfejs u¿ytkownika jest modelowany na
klasyczny uniksowy edytor tekstu - vi. Znaj±cy vi u¿ywaj±c CGDB
powinni czuæ siê jak w domu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CPPFLAGS=" -I/usr/include/ncurses "
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

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
