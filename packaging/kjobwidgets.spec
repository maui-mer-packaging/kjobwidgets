# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kjobwidgets

# >> macros
# << macros

Summary:    KDE Frameworks 5 Tier 2 addon for jobs
Version:    5.3.0
Release:    2
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kjobwidgets.yaml
Source101:  kjobwidgets-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  qt5-qttools-linguist
BuildRequires:  kcoreaddons-devel
BuildRequires:  kwidgetsaddons-devel

%description
KDE Frameworks 5 Tier 2 addon for jobs.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%find_lang kjobwidgets5_qt --with-qt --all-name || :

%files -f kjobwidgets5_qt.lang
%defattr(-,root,root,-)
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5JobWidgets.so.*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/kjobwidgets_version.h
%{_kf5_includedir}/KJobWidgets
%{_kf5_libdir}/libKF5JobWidgets.so
%{_kf5_cmakedir}/KF5JobWidgets
%{_kf5_mkspecsdir}/qt_KJobWidgets.pri
%{_kf5_dbusinterfacesdir}/*
# >> files devel
# << files devel
