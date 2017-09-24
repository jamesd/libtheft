%global debug_package %{nil}
%global repo theft

Name:           libtheft
Version:        0.4.3
Release:        1%{?dist}
Summary:        theft is a C library for property-based testing

License:        ISC
URL:            https://github.com/silentbicycle/%{repo}
Source0:        https://github.com/silentbicycle/%{repo}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
Requires:	pkgconfig

%description
theft is a C library for property-based testing. Where example-based
testing checks test results for specific input, theft tests assert
general properties ("for any possible input, [some condition] should
hold"), generate input, and search for counter-examples that make the
test fail. If theft finds any failures, it also knows how to generate
and test simpler variants of the input, and then report the simplest
counter-example found.


%prep
%autosetup -n %{repo}-%{version}


%build
%make_build


%install
%make_install PREFIX=%{buildroot}/%{_exec_prefix}
%if "%{?_lib}" == "lib64"
mv %{buildroot}%{_exec_prefix}/lib %{buildroot}%{_libdir}
sed -i -e 's,${prefix}/lib,${prefix}/%{_lib},' %{buildroot}%{_datarootdir}/pkgconfig/libtheft.pc
%endif
mv %{buildroot}%{_datarootdir}/pkgconfig %{buildroot}%{_libdir}


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md CHANGELOG.md
%{_libdir}/*.a
%{_includedir}/*.h
%{_libdir}/pkgconfig/libtheft.pc


%changelog
* Wed Sep 20 2017 James Davidson <james@greycastle.net> - 0.4.3-1
- Initial packaging
