%define _disable_ld_no_undefined 1

Summary:	OpenSubtitles plugin for FatRat
Name:		fatrat-opensubtitles
Version:	1.1.3
Release:	2
License:	GPLv2+
Group:		Networking/File transfer
Url:		https://fatrat.dolezel.info/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	fatrat-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(zlib)
Requires:	fatrat

%description
FatRat is an open source download manager for Linux/Unix systems written
in C++ with the help of the Qt4 library. It is rich in features and is
continuously developed.

%files
%{_libdir}/fatrat/plugins/lib%{name}.so
%{_docdir}/%{name}/TRANSLATIONS

#----------------------------------------------------------------------------

%prep
%setup -q
sed s,lib/fatrat/plugins,%{_lib}/fatrat/plugins,g -i CMakeLists.txt

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build


