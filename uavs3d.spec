%define major 0
%define libname %mklibname uavs3d %{major}
%define devname %mklibname uavs3d -d
%define snapshot 20220115

Name: uavs3d
Version: 1.0.1
Release: %{?snapshot:0.%{snapshot}.}1
Source0: https://github.com/uavs3/uavs3d/archive/%{?snapshot:refs/heads/master}%{!?snapshot:%{version}/%{name}-%{version}}.tar.gz
Patch0: uavs3d-compile.patch
Patch1: uavs3d-buildsystem.patch
Summary: Library for decoding AVS3-P2 format videos
URL: https://github.com/uavs3/uavs3d
License: 4-clause BSD
Group: System/Libraries
BuildRequires: cmake ninja

%description
Library for decoding AVS3-P2 format videos

AVS3 is a Chinese standard for video encoding.

%package -n %{libname}
Summary: Library for decoding AVS3-P2 format videos
Group: System/Libraries

%description -n %{libname}
Library for decoding AVS3-P2 format videos

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%{name} is a library for decoding AVS3-P2 format videos.

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:%{version}}
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
