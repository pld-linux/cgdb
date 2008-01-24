Summary:	A lightweight, but fully functional curses frontend to gdb
Summary(pl.UTF-8):	Lekki, ale w pełni funkcjonalny frontend do gdb oparty na ncurses
Name:		cgdb
Version:	0.6.4
Release:	0.1
License:	GPL
Group:		Development/Debuggers
Source0:	http://dl.sourceforge.net/cgdb/%{name}-%{version}.tar.gz
# Source0-md5:	bddcaaee7b20ab2c17f1f4e197db74c0
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-missing_includes.patch
Patch2:		%{name}-info.patch
URL:		http://cgdb.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
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
%patch2 -p1

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

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*.info*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/cgdb.txt
