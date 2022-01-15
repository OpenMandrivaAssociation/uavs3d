%define major 0
%define libname %mklibname uavs3d %{major}
%define devname %mklibname uavs3d -d
%define snapshot 20220115

Name: uavs3d
Version: 1.1.70
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

# version.sh works only on a git checkout, not a
# release tarball or equivalent.
# So let's force it to say what it says on a git
# checkout...
cat >version.h <<EOF
#ifndef __VERSION_H__
#define __VERSION_H__

#define VER_MAJOR  $(echo %{version} |cut -d. -f1)                // major version number
#define VER_MINOR  $(echo %{version} |cut -d. -f2)                // minor version number
#define VER_BUILD  $(echo %{version} |cut -d. -f3)             // build number

#define VERSION_TYPE "release"
#define VERSION_STR  "%{version}"
#define VERSION_SHA1 "23a42eefbcde8f4d826b71f2e158f948f3e2b3ee"

#endif // __VERSION_H__
EOF
rm version.sh

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
