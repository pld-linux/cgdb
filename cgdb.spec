Summary:	A lightweight, but fully functional curses frontend to gdb
Summary(pl):	Lekki, ale w pe³ni funkcjonalny frontend do gdb oparty na ncurses
Name:		cgdb
Version:	0.6.0
Release:	1
License:	GPL
Group:		Development/Debuggers
Source0:	http://dl.sourceforge.net/cgdb/%{name}-%{version}.tar.gz
# Source0-md5:	61a5c5b6b76de70efd0bf2335b470f99
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-missing_includes.patch
URL:		http://cgdb.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	readline-devel >= 5.1
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

find . -type f -name Makefile.am -exec %{__sed} -i 's@AM_CFLAGS = -g @AM_CFLAGS = @' '{}' ';'

%build
CPPFLAGS=' -I/usr/include/ncurses '
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

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*
