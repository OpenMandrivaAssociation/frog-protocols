Name:           frog-protocols
Version:        0.01
Release:        1
Summary:        Faster moving Wayland protocols
Group:          Development/Libraries
License:        MIT
URL:            https://github.com/misyltoad/frog-protocols
Source0:        https://github.com/misyltoad/frog-protocols/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  meson

BuildArch:      noarch

Provides:       %{name}-devel = %{EVRD}

%description
Wayland Protocols has long had a problem with new protocols sitting for months, to years at a time for even basic functionality.
This is hugely problematic when some protocols implement very primitive and basic functionality such as frog-fifo-v1, 
which is needed for VSync to not cause GPU starvation under Wayland and also fix the dreaded application freezing when windows are occluded with FIFO/VSync enabled.
We need to get protocols into end-users hands quicker! 
The main reason many users are still using X11 is because of missing functionality that we can be shipping today, but is blocked for one reason or another.

%prep
%autosetup -p1

%build
%meson
%meson_build


%install
%meson_install

%files
%license LICENSE.md
%doc README.md
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/
