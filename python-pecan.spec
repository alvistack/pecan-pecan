# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-pecan
Epoch: 100
Version: 1.4.1
Release: 1%{?dist}
BuildArch: noarch
Summary: WSGI object-dispatching web framework
License: BSD-3-Clause
URL: https://github.com/pecan/pecan/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
A WSGI object-dispatching web framework, designed to be lean and fast
with few dependencies.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pecan
Summary: WSGI object-dispatching web framework
Requires: python3
Requires: python3-logutils >= 0.3
Requires: python3-Mako >= 0.4.0
Requires: python3-six
Requires: python3-WebOb >= 1.8
Requires: python3-WebTest >= 1.3.1
Provides: python3-pecan = %{epoch}:%{version}-%{release}
Provides: python3dist(pecan) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pecan = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pecan) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pecan = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pecan) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pecan
A WSGI object-dispatching web framework, designed to be lean and fast
with few dependencies.

%files -n python%{python3_version_nodots}-pecan
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-pecan
Summary: WSGI object-dispatching web framework
Requires: python3
Requires: python3-logutils >= 0.3
Requires: python3-Mako >= 0.4.0
Requires: python3-six
Requires: python3-WebOb >= 1.8
Requires: python3-WebTest >= 1.3.1
Provides: python3-pecan = %{epoch}:%{version}-%{release}
Provides: python3dist(pecan) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pecan = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pecan) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pecan = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pecan) = %{epoch}:%{version}-%{release}

%description -n python3-pecan
A WSGI object-dispatching web framework, designed to be lean and fast
with few dependencies.

%files -n python3-pecan
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-pecan
Summary: WSGI object-dispatching web framework
Requires: python3
Requires: python3-logutils >= 0.3
Requires: python3-mako >= 0.4.0
Requires: python3-six
Requires: python3-webob >= 1.8
Requires: python3-webtest >= 1.3.1
Provides: python3-pecan = %{epoch}:%{version}-%{release}
Provides: python3dist(pecan) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pecan = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pecan) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pecan = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pecan) = %{epoch}:%{version}-%{release}

%description -n python3-pecan
A WSGI object-dispatching web framework, designed to be lean and fast
with few dependencies.

%files -n python3-pecan
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
