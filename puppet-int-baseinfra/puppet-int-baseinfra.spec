Name:         puppet-int-baseinfra
Version:      0.1.1
Release:      1
Summary:      Basic infrastructure integration
Group:        Applications/System
License:      GPL
Vendor:       MSAT
Source:       %{name}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-root
Requires:     puppet-baseinfra

%description
This Puppet code provides the glue between basic Puppet
modules and the configuration parameters.

The profiles obtain the YAML parameters needed for basic
Puppet classes and execute the Puppet class code in order. 

A role includes a number of profiles. A role must be tested
with the profile to prove that they work together. Or, in
other words: they don't interfere with eachother, i.e. they
must be orthogonal.

%prep
%setup -q -n %{name}

%build
# Empty.

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
cp -R etc usr $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre
# Empty.

%post
# Empty.

%preun
# Empty.

%postun
# Empty.

%files
%defattr(0644,root,root)
/etc/puppet/modules/profiles
/etc/puppet/modules/roles
%doc /usr/share/doc/%{name}

%changelog
* Sat Jun 21 2014 Allard Berends <allard.berends@example.com> - 0.1.1-1.el5
- Initial creation of the RPM
