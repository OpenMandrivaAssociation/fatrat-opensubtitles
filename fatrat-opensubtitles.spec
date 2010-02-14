%define name fatrat-opensubtitles
%define oname fatrat
%define version 1.1.2
%define release %mkrel 1

Summary: OpenSubtitles plugin for FatRat
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: GPLv2
Group: Networking/File transfer
Url:   http://fatrat.dolezel.info/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: zlib-devel
BuildRequires: cmake 

Requires: fatrat = %{version}
Requires: zlib
%description
FatRat is an open source download manager for Linux/Unix systems written in C++ with the help of the Trolltech Qt 4 library. It is rich in features and is continuously developed.

%prep
%setup -q

%build
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}

%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_libdir}/%{oname}/plugins/lib%{name}.so
%{_docdir}/%{name}/TRANSLATIONS

