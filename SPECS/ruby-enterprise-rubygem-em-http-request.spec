%define ruby_dist ruby-enterprise
%define ruby_dist_dash %{ruby_dist}-
%define _prefix /opt/ruby-enterprise
%define _gem %{_prefix}/bin/gem
%define _ruby %{_prefix}/bin/ruby

# Generated from em-http-request-0.3.0.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{_ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{_ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname em-http-request
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}
%define __arch_install_post   /usr/lib/rpm/check-rpaths

Summary: EventMachine based, async HTTP Request client
Name: %{?ruby_dist_dash}rubygem-%{gemname}
Version: 0.3.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/igrigorik/em-http-request
Source0: http://gemcutter.orggems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?ruby_dist_dash}rubygems
Requires: %{?ruby_dist_dash}rubygem(eventmachine) >= 0.12.9
Requires: %{?ruby_dist_dash}rubygem(addressable) >= 2.0.0
Requires: %{?ruby_dist_dash}rubygem(escape_utils) >= 0
BuildRequires: %{?ruby_dist_dash}rubygems
BuildRequires: make
BuildRequires: ruby-enterprise
Provides: %{?ruby_dist_dash}rubygem(%{gemname}) = %{version}

%description
EventMachine based, async HTTP Request client


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
%{_gem} install --local --install-dir %{buildroot}%{gemdir} \
                --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct  3 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 0.3.0-1.hhg
- Rebuild for Ruby Enterprise Edition

* Thu Apr 28 2011 Sergio Rubio <rubiojr@frameos.org> - 0.3.0-1
- Initial package
